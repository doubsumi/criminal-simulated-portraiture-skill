#!/usr/bin/env python3
"""Review an image-derived FacialProfile and render an evidence-bound report.

This module does not perform computer vision. A host with declared vision
capability must produce observations before this review can describe a face.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from validate_schemas import validate_profile

ROOT = Path(__file__).resolve().parents[1]
COMPONENT_NAMES = [
    ("F01", "皮肤", "Skin"), ("F02", "面部/头部轮廓", "Face/Head Outline"),
    ("F03", "面部/头部构成", "Face/Head Composition"), ("F04", "头发", "Hair"),
    ("F05", "前额", "Forehead"), ("F06", "眉毛", "Eyebrows"),
    ("F07", "眼睛", "Eyes"), ("F08", "面颊", "Cheeks"),
    ("F09", "鼻子", "Nose"), ("F10", "耳朵", "Ears"),
    ("F11", "嘴部", "Mouth"), ("F12", "下巴/下颌线", "Chin/Jawline"),
    ("F13", "颈部", "Neck"), ("F14", "面部毛发", "Facial Hair"),
    ("F15", "面部纹路", "Facial Lines"), ("F16", "疤痕", "Scars"),
    ("F17", "面部标记", "Facial Marks"), ("F18", "人为改变", "Alterations"),
    ("F19", "其他", "Other"),
]
VISIBLE = {"clear", "partial"}
KNOWN_VIEWS = {"frontal", "left_oblique", "right_oblique", "left_profile", "right_profile"}
STATUS_ZH = {
    "clear": "清晰", "partial": "部分可见", "obscured": "被遮挡",
    "not_visible": "不可见", "not_applicable": "不适用", "uncertain": "不确定",
}


def registered_sources() -> set[str]:
    manifest = (ROOT / "knowledge/source_manifest.yaml").read_text(encoding="utf-8")
    return set(re.findall(r"(?m)^  - id: ((?:S|CN)\d+)$", manifest))


def feature_index() -> set[str]:
    ontology = (ROOT / "knowledge/ontology/facial-components.yaml").read_text(encoding="utf-8")
    return set(re.findall(r"(?m)^      - id: (F\d{2}\.C\d{2})$", ontology))


def assess(profile: dict, *, vision_attested: bool = False, image_authorized: bool = False) -> dict:
    validate_profile(profile)
    if profile["task_mode"] != "image_to_description":
        raise ValueError("Phase 4 requires task_mode=image_to_description")
    image = profile.get("image_context")
    quality = profile.get("image_quality_report")
    issues: list[str] = []
    if not vision_attested:
        issues.append("未确认宿主已执行视觉分析；不能声称已分析图像。")
    if not image_authorized:
        issues.append("未确认图像使用授权及分析范围；不能输出人物特征。")
    if not image or not image.get("asset_ids"):
        issues.append("缺少图像资产登记；不能声称已分析图像。")
    if not quality:
        issues.append("缺少图像质量报告；不能进行细节描述。")
    if image and not any(v in KNOWN_VIEWS for v in image.get("viewpoints", [])):
        issues.append("视角未知；不能推断未见角度的结构。")
    if quality and quality["overall_status"] in {"not_suitable", "unknown"}:
        issues.append("图像质量不适合可靠细节观察。")
    if quality and quality["overall_status"] not in {"not_suitable", "unknown"}:
        major = [name for name, factor in quality["factors"].items() if factor["status"] == "major_issue"]
        if major:
            issues.append(f"图像质量报告存在严重因素但仍标为适用：{', '.join(major)}。")

    sources = registered_sources()
    features = feature_index()
    asset_ids = set(image.get("asset_ids", [])) if image else set()
    seen_ids: set[str] = set()
    observed_values: dict[tuple[str, str, str, str], object] = {}
    accepted: list[dict] = []
    excluded: list[dict] = []
    for item in profile["features"]:
        oid = item["observation_id"]
        if oid in seen_ids:
            issues.append(f"{oid}: 重复观察 ID。")
        seen_ids.add(oid)
        if item["feature_id"] not in features or not item["feature_id"].startswith(item["component_id"] + "."):
            issues.append(f"{oid}: 特征 ID 未登记于所属组件。")
        if not set(item["knowledge_refs"]) <= sources:
            issues.append(f"{oid}: 存在未登记知识来源。")
        if not image or item["viewpoint"] not in image.get("viewpoints", []):
            issues.append(f"{oid}: 观察视角未登记于图像上下文。")
        for ref in item["evidence_refs"]:
            if ref["evidence_type"].startswith("image_") and ref["asset_id"] not in asset_ids:
                issues.append(f"{oid}: 图像证据未登记于图像上下文。")
        if item["laterality"]["reference_frame"] == "anatomical" and image and image["mirror_status"] == "unknown":
            issues.append(f"{oid}: 图像镜像状态未知，不能使用解剖学左右。")
        if item["confidence"]["value"] is not None and not item["confidence"]["calibrated"]:
            issues.append(f"{oid}: 未校准置信度不得填写数值。")
        if item["visibility"] in {"partial", "obscured"} and not item["limitations"]:
            issues.append(f"{oid}: 部分可见或遮挡必须记录限制。")
        key = (item["feature_id"], item["dimension_id"], item["viewpoint"], item["laterality"]["reference_frame"], item["laterality"]["side"])
        value = item["observation"]["value"]
        if item["visibility"] in VISIBLE and value not in (None, "unknown", "not_observable", "not_applicable", ""):
            if key in observed_values and observed_values[key] != value:
                issues.append(f"{oid}: 同一特征、视角和侧别存在冲突值。")
            observed_values[key] = value

        reason = None
        if item["confirmation_status"] == "rejected_by_user":
            reason = "已被用户拒绝"
        elif item["source_type"] != "direct_visual_observation":
            reason = "非直接图像观察"
        elif item["visibility"] not in VISIBLE:
            reason = "不可可靠观察"
        elif item["observation"]["value"] in (None, "unknown", "not_observable", "not_applicable", ""):
            reason = "无确定观察值"
        elif not item["evidence_refs"]:
            reason = "缺少个案证据"
        elif not any(ref["evidence_type"] in {"image_region", "image_frame"} for ref in item["evidence_refs"]):
            reason = "缺少图像区域或图像帧证据"
        elif not item["knowledge_refs"]:
            reason = "缺少知识依据"
        if reason:
            excluded.append({"id": oid, "reason": reason})
        else:
            accepted.append(item)

    for relation in profile["spatial_relations"]:
        if relation["subject_feature_id"] not in features or relation["reference_feature_id"] not in features:
            issues.append(f"{relation['relation_id']}: 空间关系指向未登记特征。")
        if not relation["evidence_refs"]:
            issues.append(f"{relation['relation_id']}: 空间关系缺少证据。")
    for asym in profile["asymmetries"]:
        if asym["left_feature_id"] not in features or asym["right_feature_id"] not in features:
            issues.append(f"{asym['asymmetry_id']}: 不对称项指向未登记特征。")
        if not asym["evidence_refs"]:
            issues.append(f"{asym['asymmetry_id']}: 不对称项缺少证据。")
    if profile["asymmetries"] and image and image["mirror_status"] == "unknown":
        issues.append("镜像状态未知；不对称项的左右必须限定为图像坐标系。")

    by_component = {component_id: [] for component_id, _, _ in COMPONENT_NAMES}
    for item in accepted:
        by_component[item["component_id"]].append(item)
    can_describe = bool(image and quality and quality["overall_status"] not in {"not_suitable", "unknown"} and not issues)
    accepted_ids = {item["feature_id"] for item in accepted}
    readiness_missing: list[str] = []
    if "F02.C02" not in accepted_ids:
        readiness_missing.append("face_outline")
    if "F03.C01" not in accepted_ids:
        readiness_missing.append("feature_layout")
    if not any(item["component_id"] == "F11" for item in accepted):
        readiness_missing.append("mouth_region")
    if not any(item["component_id"] in {"F06", "F07"} for item in accepted):
        readiness_missing.append("brow_eye_region")
    if not can_describe:
        accepted = []
        by_component = {component_id: [] for component_id, _, _ in COMPONENT_NAMES}
    return {
        "profile_id": profile["profile_id"], "can_describe": can_describe,
        "quality_status": quality["overall_status"] if quality else "missing",
        "viewpoints": image.get("viewpoints", []) if image else [],
        "issues": issues, "accepted": accepted, "excluded": excluded,
        "by_component": by_component,
        "likeness_prompt_readiness": {
            "ready": can_describe and not readiness_missing,
            "missing_anchors": readiness_missing,
            "note": "This is a completeness gate for prompt preparation, not a likeness score.",
        },
    }


def render(profile: dict, result: dict) -> str:
    lines = [f"# 图像逆向描述报告：{result['profile_id']}", "", "## 图像质量与范围", ""]
    lines.append(f"- 质量状态：{result['quality_status']}")
    lines.append(f"- 已登记视角：{', '.join(result['viewpoints']) or '未知'}")
    lines.append(f"- 可生成特征描述：{'是' if result['can_describe'] else '否'}")
    readiness = result["likeness_prompt_readiness"]
    lines.append(f"- 相似度提示词准备状态：{'充分' if readiness['ready'] else '缺少关键锚点'}")
    if readiness["missing_anchors"]:
        lines.append(f"- 缺少锚点：{', '.join(readiness['missing_anchors'])}")
    quality = profile.get("image_quality_report")
    if quality:
        for name, factor in quality["factors"].items():
            lines.append(f"- {name}：{factor['status']}{'；' + factor['notes'] if factor['notes'] else ''}")
        for limitation in quality["limitations"]:
            lines.append(f"- 图像质量限制：{limitation}")
    for issue in result["issues"]:
        lines.append(f"- 限制/冲突：{issue}")
    lines.extend(["", "## 整体结构", ""])
    overall = [x for x in result["accepted"] if x["component_id"] in {"F02", "F03"}]
    lines.append("；".join(x["observation"]["display_zh"] for x in overall) if overall else "无足够证据形成整体结构描述。")
    lines.extend(["", "## 19 组件观察", ""])
    for component_id, zh, en in COMPONENT_NAMES:
        items = result["by_component"][component_id]
        text = "；".join(
            f"{x['feature_name_zh']}：{x['observation']['display_zh']}（{STATUS_ZH[x['visibility']]}，{x['confidence']['level']}，{x['laterality']['reference_frame']} {x['laterality']['side']}；依据 {', '.join(x['knowledge_refs'])}；证据 {', '.join(r['evidence_id'] for r in x['evidence_refs'])}；限制 {'、'.join(x['limitations']) or '无'}）"
            for x in items
        ) if items else "未取得可用于描述的观察；不补全。"
        lines.append(f"- {component_id} {zh} / {en}：{text}")
    lines.extend(["", "## 空间关系与不对称", ""])
    if result["can_describe"]:
        for relation in profile["spatial_relations"]:
            lines.append(f"- 空间关系 {relation['relation_id']}：{relation['relation_type']}，{relation['subject_feature_id']} 对 {relation['reference_feature_id']}，{relation['value']}。")
        for asym in profile["asymmetries"]:
            lines.append(f"- 不对称 {asym['asymmetry_id']}：{asym['difference']['display_zh']}。")
    if not result["can_describe"] or not (profile["spatial_relations"] or profile["asymmetries"]):
        lines.append("无可报告的空间关系或不对称观察。")
    lines.extend(["", "## 绘画师简报", ""])
    lines.append("；".join(x["observation"]["display_zh"] for x in result["accepted"]) if result["accepted"] else "证据不足，暂不生成具体面部结构简报。")
    lines.extend(["", "## 未采纳观察", ""])
    lines.extend(f"- {x['id']}：{x['reason']}" for x in result["excluded"])
    if not result["excluded"]:
        lines.append("无。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path, help="Existing FacialProfile JSON")
    parser.add_argument("--out", type=Path, help="Report path; stdout when omitted")
    parser.add_argument("--vision-attested", action="store_true", help="Host explicitly confirms visual observations were performed")
    parser.add_argument("--image-authorized", action="store_true", help="Operator confirms image use and analysis scope were authorized")
    args = parser.parse_args()
    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    report = render(profile, assess(profile, vision_attested=args.vision_attested, image_authorized=args.image_authorized))
    if args.out:
        args.out.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
