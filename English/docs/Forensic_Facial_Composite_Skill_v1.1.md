# Forensic Facial Composite Skill

# 刑事摹拟画像与结构化面部描述 Agent Skill

完整设计与工程实施规范 · Codex 开发交付版 · V1.1

| 文档属性     | 内容                                           |
| ------------ | ---------------------------------------------- |
| 项目名称     | Forensic Facial Composite Skill                |
| 中文名称     | 刑事摹拟画像与结构化面部描述 Skill             |
| Skill ID     | `forensic-facial-composite`                    |
| 文档版本     | 1.1                                            |
| 文档状态     | V1.1 修订工程基线；仍须专业评审与实验验证，不构成法证认证或结论依据 |
| 目标实现环境 | 支持 Agent Skills 标准的 Agent                 |
| 主要实现语言 | Markdown、JSON、YAML、Python                   |
| 核心使用场景 | 人脸图片逆向描述、记忆认知访谈、画像提示词生成 |
| 主要实施者   | Codex                                          |
| 设计原则     | 科学严谨、结构化、可追溯、可验证、可扩展       |

> **V1.1 修订说明：** 本文保留 V1.0 的完整设计主体，并以第 32 章补充规范性修正。发生冲突时，第 32 章优先。该版本仍需专业人员复核与实验验证。

# 目录

1. 项目概述与目标定义
2. 专业概念、方法边界与科学依据
3. 系统总体架构
4. 专业面部特征知识库总体设计
5. 面部特征分类体系与详细词典
6. 面部特征词汇与描述语言规范
7. 面部空间关系与整体结构知识库
8. 左右不对称性知识库
9. 图像质量、可观察性与不确定性体系
10. 面部特征稳定性与时间变化
11. 图片逆向描述完整工作流
12. 认知访谈与记忆画像工作流
13. 统一面部数据模型
14. JSON Schema 与数据验证规范
15. 知识库文件组织与索引策略
16. AI 图像生成提示词系统
17. 专业资料来源与知识库构建规范
18. Codex 资料获取与知识库构建任务
19. 相似度与质量评测体系
20. 隐私、伦理与法律边界
21. Skill 文件规范与运行协议
22. Codex 分阶段开发任务
23. 自动化测试用例
24. 最终工程交付物
25. 项目验收标准
26. 版本维护与知识更新
27. 开发过程中的阻塞处理机制
28. 项目开发优先级与范围控制
29. 最终给 Codex 的完整开发指令
30. 项目参考资料快速索引
31. 最终设计结论
32. V1.1 修订条款（规范性补充与冲突优先级）

# 1. 项目概述与目标定义

## 1.1 项目背景

刑事摹拟画像（Forensic Facial Composite）是一类利用目击者、受害者或其他知情人员对目标人物的记忆，通过专业访谈、面部特征分析和绘画/图像构建技术，形成目标人物外观画像的辅助方法。

传统刑事摹拟画像主要依赖专业画像师的经验、认知访谈能力以及绘画工具。近年来，视觉语言模型和图像生成模型的发展，使得其中部分工作可以被 Agent 自动化或辅助完成。

但这并不意味着只要让大语言模型观察一张脸，再输出一段绘画提示词，就能够实现专业画像。

一个可靠的系统至少需要处理以下问题：

1. 如何建立科学、系统、完整的面部特征分类体系？
2. 如何准确描述面部各组成部分的形态？
3. 如何记录不同五官之间的空间关系？
4. 如何区分真实面部特征和拍摄条件造成的视觉差异？
5. 如何从用户的记忆中提取面部信息，同时避免诱导和记忆污染？
6. 如何将专业描述转换成绘画师和图像生成模型能够理解的语言？
7. 如何衡量生成结果与目标面部之间的相似程度？
8. 如何保证整个分析过程可解释、可追溯、可复核？

本项目的核心不是开发一个简单的人脸描述 Prompt，而是构建一套具有专业知识体系、标准化分析流程和可验证输出能力的 Agent Skill。

## 1.2 项目定位

本项目定位为：

基于面部形态学知识、图像观察规范和认知访谈方法的专业面部描述与合成画像辅助 Skill。

它不是：

- 人脸身份识别系统。
- 犯罪嫌疑人自动识别系统。
- 法庭认可的独立法证鉴定系统。
- 能够仅凭面部外观推断人物身份、性格或犯罪倾向的系统。
- 能够保证任何图像生成模型达到固定相似度的系统。

Skill 的主要价值在于将原本依赖专业人员经验的部分工作，转化为具有明确分类、规范流程、结构化数据和质量检查机制的可复用能力。

## 1.3 两项核心功能

### 功能 A：图片逆向描述（Image-to-Description）

用户提供一张或多张人脸图片。

Agent 通过专业知识库和结构化分析流程，对图像中可观察的面部特征进行系统描述。

预期输出：

1. 图像质量评估报告。
2. 面部整体结构描述。
3. 19 类面部组成部分的详细分析。
4. 五官相对位置和比例关系。
5. 左右面部不对称性。
6. 具有辨识价值的可见细节。
7. 每项观察的可见性和置信度。
8. 完整的结构化面部特征档案。
9. 面向人工绘画师的详细描述。
10. 面向 AI 图像生成模型的结构化提示词。

该功能的目标是最大程度保留原图中可观察到的面部特征，使第三方能够依据输出描述重建尽可能接近的面部外观。

重要限制： 单张照片只提供有限的二维观察信息。不能从单张正面照片确定完整三维结构，也不能推断未展示的侧面、耳后、被遮挡区域等信息。

### 功能 B：认知访谈生成画像（Memory-to-Composite）

用户希望根据自己对某个人物的记忆生成面部画像。

Agent 不应直接让用户填写一份简单的五官问卷，而应使用认知访谈方法，通过分阶段、非诱导性的对话逐步获取记忆信息。

预期输出：

1. 访谈记录。
2. 用户自由回忆内容。
3. 结构化面部特征档案。
4. 每项特征的记忆来源与主观置信度。
5. 未知和不确定特征列表。
6. 人工画像师工作简报。
7. 通用 AI 图像生成提示词。
8. 模型适配版本。
9. 用户反馈后的迭代修订结果。

此功能的重点不是让 Agent 尽可能多地询问问题，而是在不污染用户原始记忆的前提下，尽可能有效地提取有价值的面部信息。

## 1.4 项目核心成功标准

项目成功不能仅以 Skill 是否能够运行、是否生成一张图作为判断标准。

建议将成功标准分为四个层级。

| 层级             | 成功标准                                 | 验收方式                 |
| ---------------- | ---------------------------------------- | ------------------------ |
| L1：知识完整性   | 建立专业、结构化、可追溯的面部特征知识库 | 专业知识覆盖检查         |
| L2：分析可靠性   | 能够对可见面部特征进行系统、准确的描述   | 专家标注对照             |
| L3：访谈有效性   | 能够通过非诱导访谈获得结构化面部记忆     | 访谈实验与盲评           |
| L4：画像复现能力 | 依据描述生成具有较高目标相似度的面部图像 | 独立盲评与特征一致性评估 |

最终希望实现：

- 对高质量输入图像，能够系统提取主要面部特征。
- 不会因为追求描述完整性而编造不可观察信息。
- 能够保留具有辨识价值的局部特征及左右差异。
- 能够通过认知访谈收集结构化面部记忆。
- 能够将结构化描述稳定地转换为图像生成提示词。
- 能够对生成结果进行针对性修订，而不是每次都重新随机生成一张脸。
- 所有主要输出都能够追溯其来源、依据和不确定性。

## 1.5 关于 90% 相似度目标

项目提出了一个理想目标：

> 根据图片逆向分析得到的面部描述，或通过认知访谈得到的面部描述，能够让人类绘画师或图像生成工具重建出与目标面部相似度达到 90% 以上的结果。

这一目标值得保留，但必须进行科学定义。

目前不存在一个能够适用于所有图像、所有人类绘画师和所有图像生成模型的统一“人脸重建相似度 90%”指标。

至少需要区分：

1. 人类主观感知相似度。
2. 专业画像师对结构特征的复现程度。
3. 19 类面部组件的特征一致性。
4. 自动人脸特征向量的相似度。
5. 目标人物被独立观察者正确辨认的比例。

这些指标并不等价。

因此，本项目将 90% 设定为长期研发目标和条件化实验验收目标，而不是对每次生成结果的保证。

具体评测标准将在第 16 章定义。

# 2. 专业概念、方法边界与科学依据

## 2.1 专业知识来源优先级

本项目应优先采用以下资料：

| 优先级 | 资料类型                | 主要作用                           |
| ------ | ----------------------- | ---------------------------------- |
| P0     | FISWG 正式规范与指南    | 面部形态特征、图像质量、特征稳定性 |
| P0     | IAI 法证艺术专业指南    | 刑事摹拟画像与专业实践             |
| P0     | Agent Skills 官方规范   | Skill 工程结构与运行约定           |
| P1     | 同行评审的面部画像研究  | 认知访谈、画像构建、识别效果       |
| P1     | 解剖学专业教材与论文    | 面部解剖结构与术语                 |
| P1     | NIST / OSAC / IFSA 资料 | 法证质量控制与记录要求             |
| P2     | 图像生成研究与工程资料  | 提示词转换、模型适配与生成评估     |

特别强调：

- 正式标准是规范性依据。
- 同行评审论文是研究证据。
- 教材和专业词典是知识解释依据。
- 本项目自行制定的 JSON 字段、工作流、提示词策略和评测门槛属于工程设计建议。

不得将四者混为一谈。

## 2.2 FISWG 的作用与使用边界

FISWG 全称：

Facial Identification Scientific Working Group。

官方资料：

- 官方网站：[https://fiswg.org/](https://fiswg.org/)
- 官方文档目录：[https://www.fiswg.org/documents/](https://www.fiswg.org/documents/)

FISWG 是本项目面部形态学知识体系的首要参考来源。

其中最重要的资料是：

Facial Image Comparison Feature List for Morphological Analysis v2.0

官方 PDF：

[https://www.fiswg.org/FISWG_Morph_Analysis_Feature_List_v2.0_20180911.pdf](https://www.fiswg.org/FISWG_Morph_Analysis_Feature_List_v2.0_20180911.pdf)

该文档提供：

- 19 个面部组成部分。
- 组件下属特征。
- 形态描述术语。
- 面部结构观察维度。
- 特征相对位置描述方式。

但是，必须注意：

该文件主要提供面部形态特征清单，并不是一个完整的刑事摹拟画像访谈手册，也不是一个能够直接生成 AI 图像的提示词规范。

本项目应将其作为面部特征知识本体的基础，再结合认知访谈研究、解剖学资料和图像生成工程，建立完整的 Skill。

## 2.3 FISWG 面部比较方法与本项目的区别

FISWG 的：

Facial Comparison Overview and Methodology Guidelines v2.1

官方 PDF：

[https://fiswg.org/fiswg_facial_comparison_overview_and_methodology_guidelines_V2.1_2026026.pdf](https://fiswg.org/fiswg_facial_comparison_overview_and_methodology_guidelines_V2.1_2026026.pdf)

主要讨论面部图像比较的方法学。

其中包括：

- Analysis。
- Comparison。
- Evaluation。
- Verification。
- 形态学分析。
- 图像叠加的使用限制。
- 图像质量和方法适用性。

需要特别注意：

FISWG 的面部比较方法主要面向不同面部图像之间的比较分析，而本项目的两个主要任务是：

1. 从单张图像提取可见面部特征。
2. 从用户记忆收集面部特征并生成合成画像。

两者并不相同。

因此：

- 可以借鉴 FISWG 的形态学特征分类。
- 可以借鉴其图像质量评估原则。
- 可以借鉴其分析记录和不确定性处理方式。
- 不得声称本 Skill 实现了 FISWG 完整面部比较程序。
- 不得声称本 Skill 具有法证身份确认能力。

## 2.4 IAI 法证艺术指南

IAI 全称：

International Association for Identification。

官方资料：

[https://theiai.org/](https://theiai.org/)

已发现的相关资料：

Standards and Guidelines for Forensic Art and Facial Identification

资料入口：

[https://theiai.org/docs/ForensicArtGuidelinesSGFAFI1stEd.pdf](https://theiai.org/docs/ForensicArtGuidelinesSGFAFI1stEd.pdf)

该资料可用于研究：

- 法证艺术的专业职责。
- 刑事摹拟画像的实践流程。
- 画像师与目击者之间的协作。
- 认知访谈。
- 画像构建。
- 画像结果的专业使用限制。

需要注意其版本年代。Codex 应核实是否存在更新版本，不能直接假设早期版本代表当前最新的全部行业要求。

## 2.5 认知访谈的科学依据

认知访谈（Cognitive Interview，CI）是一种旨在改善目击者回忆信息获取的访谈方法。

它并不是通过提供更多选项来帮助用户猜出细节，而是通过合理的记忆提取策略，让受访者尽可能自主回忆。

本项目应重点研究：

- 自由回忆。
- 情境重建。
- 不同回忆线索。
- 开放式提问。
- 非诱导式澄清。
- 记忆来源区分。
- 记忆污染防护。

推荐研究：

Fodarella et al. (2015)

Forensic procedures for facial-composite construction

DOI：

[https://doi.org/10.1108/JFP-10-2014-0033](https://doi.org/10.1108/JFP-10-2014-0033)

另一个重要方向：

Constructing identifiable composite faces: The importance of cognitive alignment of interview and construction procedure

PubMed：

[https://pubmed.ncbi.nlm.nih.gov/31763863/](https://pubmed.ncbi.nlm.nih.gov/31763863/)

该研究方向提示：访谈过程与后续画像构建方式之间的认知匹配可能影响最终画像效果。

因此，本项目不应只设计一套固定问卷，而应允许 Agent 根据用户回忆特点，调整访谈方式。

## 2.6 解剖学资料

推荐基础资料：

NCBI Bookshelf：

Anatomy, Head and Neck: Face

[https://www.ncbi.nlm.nih.gov/sites/books/NBK551530/](https://www.ncbi.nlm.nih.gov/sites/books/NBK551530/)

用于补充：

- 面部区域划分。
- 面部骨骼与软组织。
- 面部肌肉。
- 眼眶、鼻、口周、面颊和下颌结构。
- 面部解剖术语。

本项目必须区分：

| 结构层次 | 例子                       | 主要描述内容       |
| -------- | -------------------------- | ------------------ |
| 骨性结构 | 额骨、颧骨、上颌骨、下颌骨 | 外部轮廓与支撑形态 |
| 软组织   | 脂肪垫、面颊软组织         | 饱满度、凹陷、轮廓 |
| 表面结构 | 皮肤、皱纹、疤痕           | 纹理、色调、标记   |
| 动态结构 | 面部肌肉活动               | 表情与动态变化     |
| 附属结构 | 毛发、眉毛、睫毛           | 分布、密度、形态   |

特别注意：从一张静态照片观察到的表情状态，不应被误认为一个人的固定面部结构。

## 2.7 图像质量与观察可靠性

推荐资料：

FISWG Image Factors to Consider in Facial Image Comparison v1.0

官方 PDF：

[https://fiswg.org/fiswg_image_factors_to_consider_in_facial_img_comparison_v1.0_2021.05.28.pdf](https://fiswg.org/fiswg_image_factors_to_consider_in_facial_img_comparison_v1.0_2021.05.28.pdf)

该文件强调图像质量会影响面部特征的可见性和观察可靠性。

本项目应将以下因素纳入质量门控：

- 图像分辨率。
- 清晰度。
- 光照。
- 噪声。
- 图像压缩。
- 遮挡。
- 头部姿态。
- 镜头畸变。
- 图像伪影。
- 近红外成像。
- 过曝和欠曝。
- 美颜、磨皮和其他图像处理。

不能只依据图片像素数量判断图像质量。增加像素或进行插值，并不等于恢复了原本不存在的真实细节。

## 2.8 面部特征稳定性

推荐资料：

FISWG Physical Stability of Facial Features of Adults v2.0

官方 PDF：

[https://fiswg.org/fiswg_physical_stability_of_facial_features_of_adults_v2.0_2021.05.28.pdf](https://fiswg.org/fiswg_physical_stability_of_facial_features_of_adults_v2.0_2021.05.28.pdf)

该资料讨论成年人的面部特征如何受到以下因素影响：

- 年龄变化。
- 表情。
- 明显体重变化。
- 健康状态变化。
- 创伤。
- 有意改变。
- 毛发、化妆等外观变化。

本项目应当区分：

1. 相对稳定的结构特征。
2. 容易变化的外观特征。
3. 暂时性特征。
4. 人为改变的特征。

例如：

一个人当前的胡须、发型、化妆、皮肤状态，不应自动被认为是永久面部特征。

# 3. 系统总体架构

## 3.1 总体设计

本项目采用模块化 Agent Skill 设计。

Skill 本身不负责训练或部署视觉模型，也不绑定某一个特定 LLM。它负责组织专业知识、定义分析流程、约束模型行为、生成结构化结果，并调用宿主 Agent 所提供的视觉和图像生成能力。

系统由以下模块组成：

```
                  User
                   |
                   v
            Skill Entry Point
                   |
                   v
            Task Mode Router
                   |
          +--------+--------+
          |                 |
          v                 v
  Image-to-Description  Memory-to-Composite
          |                 |
          v                 v
   Image Quality Gate   Cognitive Interview
          |                 |
          v                 v
   Facial Observation   Memory Extraction
          |                 |
          +--------+--------+
                   |
                   v
          Facial Profile Builder
                   |
                   v
         Structured Feature Profile
                   |
          +--------+--------+
          |                 |
          v                 v
    Artist Brief       Prompt Compiler
          |                 |
          v                 v
    Human Review      Image Generation Model
                            |
                            v
                     User Feedback
                            |
                            v
                    Iterative Refinement
```

## 3.2 核心模块职责

| 模块                   | 职责                             |
| ---------------------- | -------------------------------- |
| Skill Entry Point      | 识别用户请求并启动工作流         |
| Task Mode Router       | 判断使用图片逆向描述还是记忆访谈 |
| Knowledge Loader       | 按任务加载专业知识               |
| Image Quality Gate     | 评估图像质量和可观察性           |
| Facial Observation     | 提取面部结构特征                 |
| Cognitive Interview    | 分阶段收集用户记忆               |
| Profile Builder        | 构建统一面部特征档案             |
| Prompt Compiler        | 将结构化数据转为绘画提示词       |
| Artist Brief Generator | 输出人类画像师可使用的工作简报   |
| Quality Validator      | 检查完整性、冲突和不确定性       |
| Iterative Refinement   | 根据用户反馈进行局部修订         |

## 3.3 设计约束

### 3.3.1 模型无关

Skill 不应绑定 OpenAI、Anthropic、Google 或其他单一模型。

视觉观察和文本分析由宿主 Agent 的能力完成。

如果宿主 Agent 不支持图像输入，Skill 必须明确告知用户当前无法执行图像逆向分析，而不是伪造观察结果。

### 3.3.2 知识与执行逻辑分离

专业知识放在 `references/` 和 `knowledge/` 中。

运行流程放在 `SKILL.md` 和相关流程文件中。

结构化数据放在 `schemas/` 中。

测试和验证逻辑放在 `scripts/` 和 `tests/` 中。

不得把所有内容写进一个庞大的 `SKILL.md`。

### 3.3.3 渐进式知识加载

每次任务只加载必要知识：

- 图片分析：加载图像质量、面部形态学、特征关系和稳定性知识。
- 认知访谈：加载 CI/H-CI、非诱导问题、记忆来源与污染控制知识。
- 提示词生成：加载提示词编译规则、模型适配器和质量验证规则。

这样可以降低上下文占用，并使知识库更容易维护。

### 3.3.4 统一数据模型

两个工作模式必须最终生成同一种 `Facial Profile` 数据结构。

但必须保留不同的信息来源：

- 图片直接观察。
- 用户自由回忆。
- 用户提示后回忆。
- 用户确认。
- Agent 建议。
- 外部参考资料。

不能因为最终输出结构相同，就把不同来源的信息混为一谈。

## 3.4 推荐 Skill 目录结构

```
forensic-facial-composite/
│
├── SKILL.md
├── README.md
├── LICENSE
├── CHANGELOG.md
│
├── references/
│   ├── 00-scope-and-ethics.md
│   ├── 01-professional-standards.md
│   ├── 02-facial-anatomy.md
│   ├── 03-fiswg-feature-taxonomy.md
│   ├── 04-facial-morphology-lexicon.md
│   ├── 05-facial-spatial-relations.md
│   ├── 06-facial-asymmetry.md
│   ├── 07-image-quality.md
│   ├── 08-feature-stability.md
│   ├── 09-cognitive-interview.md
│   ├── 10-memory-contamination.md
│   ├── 11-image-analysis-workflow.md
│   ├── 12-memory-interview-workflow.md
│   ├── 13-prompt-engineering.md
│   ├── 14-quality-assurance.md
│   └── 15-source-register.md
│
├── knowledge/
│   ├── ontology/
│   │   ├── facial_components.yaml
│   │   ├── facial_features.yaml
│   │   ├── descriptors_zh_en.yaml
│   │   ├── spatial_relations.yaml
│   │   ├── asymmetry_patterns.yaml
│   │   └── feature_stability.yaml
│   │
│   ├── interview/
│   │   ├── interview_stages.yaml
│   │   ├── question_bank.yaml
│   │   ├── nonleading_question_rules.yaml
│   │   └── memory_source_types.yaml
│   │
│   └── sources/
│       ├── source_manifest.yaml
│       └── source_history.yaml
│
├── schemas/
│   ├── facial_profile.schema.json
│   ├── feature_observation.schema.json
│   ├── image_quality.schema.json
│   ├── interview_record.schema.json
│   ├── prompt_output.schema.json
│   └── source_metadata.schema.json
│
├── templates/
│   ├── image_analysis_report.md
│   ├── facial_profile_report.md
│   ├── artist_brief.md
│   ├── interview_summary.md
│   ├── prompt_output.md
│   └── quality_review.md
│
├── prompt_adapters/
│   ├── generic.md
│   ├── midjourney.md
│   ├── stable-diffusion.md
│   ├── flux.md
│   └── other-models.md
│
├── scripts/
│   ├── fetch_sources.py
│   ├── extract_pdf_text.py
│   ├── build_knowledge_index.py
│   ├── validate_knowledge_base.py
│   ├── validate_profile.py
│   └── run_evaluation.py
│
└── tests/
    ├── test_feature_coverage.py
    ├── test_visibility_handling.py
    ├── test_uncertainty.py
    ├── test_left_right_consistency.py
    ├── test_memory_contamination.py
    ├── test_prompt_consistency.py
    └── fixtures/
```

## 3.5 目录设计要求

1. `SKILL.md` 必须符合 Agent Skills 开放规范。
2. 所有知识文件必须可以独立阅读。
3. YAML 文件用于存储可查询的结构化知识。
4. Markdown 文件用于解释专业概念、方法和工作流程。
5. JSON Schema 用于约束运行时输出。
6. 每个知识条目必须有来源或明确标记为项目自定义。
7. 不得将未经授权的论文全文复制到知识库。
8. 不得将未经许可的人脸照片作为项目内置训练或测试资源。
9. 原始标准文件与项目提炼的知识摘要必须分开存储。
10. 标准更新时保留历史版本，不能静默覆盖。

第一部分结束。

下一部分从第 4 章开始，进入最重要的专业知识库设计：包括 19 个面部组件的完整子特征分类、各特征的解剖学含义、描述维度、中英文术语、可观察条件和知识库数据条目规范。请保留本部分原文，后续章节会直接引用这里定义的架构和术语。

# 第二部分：专业面部特征知识库设计

# 4. 专业面部特征知识库总体设计

本章是整个 Skill 最重要的基础章节之一。

后续的图片逆向分析、认知访谈和提示词生成，都必须依赖这里定义的面部特征知识体系。

知识库不能只是一份面部特征名词表，而应当是一套能够支持 Agent 进行观察、分类、记录、关联、检索和表达的结构化专业知识系统。

## 4.1 知识库的核心目标

知识库需要解决五个问题：

1. 知道观察什么： 建立完整的面部组成部分及其下属特征分类。
2. 知道如何描述： 为每个特征提供标准化的中英文术语和描述维度。
3. 知道如何观察： 明确不同视角、图像质量和遮挡条件下，哪些特征可以被可靠观察。
4. 知道如何关联： 记录不同特征之间的空间关系、左右差异和整体结构关系。
5. 知道如何使用： 将专业特征转化为适用于访谈、绘画简报和 AI 提示词的表达。

## 4.2 知识库的分层结构

建议采用以下七层结构：

| 层级 | 名称                      | 内容                         |
| ---- | ------------------------- | ---------------------------- |
| L1   | Facial Components         | 19 个面部组成部分            |
| L2   | Facial Features           | 各组成部分下的具体特征       |
| L3   | Descriptor Dimensions     | 特征描述维度                 |
| L4   | Descriptor Vocabulary     | 中英文形态描述词             |
| L5   | Spatial Relations         | 特征之间的相对空间关系       |
| L6   | Observability & Stability | 可观察性和稳定性条件         |
| L7   | Prompt Rendering          | 特征向绘画语言及提示词的映射 |

举例：

```
Eyes
 ├── Eye Shape
 │    ├── Almond-shaped
 │    ├── Round
 │    ├── Narrow
 │    └── Other / Uncertain
 │
 ├── Eye Position
 │    ├── Wide-set
 │    ├── Close-set
 │    └── Neutral
 │
 ├── Eye Corners
 │    ├── Inner Canthus
 │    ├── Outer Canthus
 │    └── Canthal Tilt
 │
 ├── Eyelids
 │    ├── Upper Eyelid
 │    ├── Lower Eyelid
 │    ├── Eyelid Crease
 │    └── Hooding
 │
 └── Asymmetry
      ├── Left-right size difference
      ├── Left-right shape difference
      └── Left-right eyelid difference
```

上述树形结构是项目设计的知识组织方式，并非 FISWG 原文的目录结构。

## 4.3 19 个面部组成部分的完整覆盖要求

知识库必须完整包含以下 19 类：

| ID   | 英文名称              | 中文名称      | 必须支持的观察方向       |
| ---- | --------------------- | ------------- | ------------------------ |
| F01  | Skin                  | 皮肤          | 正面、斜面、局部         |
| F02  | Face/Head Outline     | 面部/头部轮廓 | 正面、侧面               |
| F03  | Face/Head Composition | 面部/头部构成 | 正面、斜面               |
| F04  | Hair                  | 头发          | 正面、侧面、顶部可见部分 |
| F05  | Forehead              | 额头          | 正面、侧面               |
| F06  | Eyebrows              | 眉毛          | 正面、斜面               |
| F07  | Eyes                  | 眼睛          | 正面、斜面、侧面可见部分 |
| F08  | Cheeks                | 面颊          | 正面、斜面、侧面         |
| F09  | Nose                  | 鼻子          | 正面、侧面、斜面         |
| F10  | Ears                  | 耳朵          | 正面、侧面、斜面         |
| F11  | Mouth                 | 嘴部          | 正面、斜面               |
| F12  | Chin/Jawline          | 下巴/下颌线   | 正面、侧面、斜面         |
| F13  | Neck                  | 颈部          | 正面、侧面               |
| F14  | Facial Hair           | 面部毛发      | 正面、侧面、局部         |
| F15  | Facial Lines          | 面部纹路      | 正面、斜面、局部         |
| F16  | Scars                 | 疤痕          | 局部、正面、斜面         |
| F17  | Facial Marks          | 面部标记      | 局部、正面、斜面         |
| F18  | Alterations           | 人为修饰      | 正面、侧面、局部         |
| F19  | Other                 | 其他          | 根据具体特征决定         |

注意：观察方向表示有助于观察该特征的图像视角，并不意味着必须获得全部视角才能完成描述。

## 4.4 特征描述的统一维度

每个具体特征应尽可能映射到以下通用维度。

| 维度     | 英文            | 说明                           |
| -------- | --------------- | ------------------------------ |
| 形状     | Shape           | 特征整体形态                   |
| 大小     | Size            | 相对于相邻结构或整体面部的大小 |
| 长度     | Length          | 特征的相对长度                 |
| 宽度     | Width           | 特征的相对宽度                 |
| 高度     | Height          | 特征的相对高度                 |
| 位置     | Position        | 在面部中的位置                 |
| 间距     | Spacing         | 与其他特征的相对距离           |
| 角度     | Angle           | 倾斜或朝向                     |
| 突出程度 | Prominence      | 相对于周边结构的突出程度       |
| 深度     | Depth           | 可见凹陷或凸起程度             |
| 对称性   | Symmetry        | 左右差异                       |
| 纹理     | Texture         | 表面结构                       |
| 色调     | Tone            | 图像中呈现的明暗或颜色         |
| 密度     | Density         | 毛发或标记的分布密度           |
| 边界     | Edge Definition | 特征边缘清晰程度               |
| 方向     | Orientation     | 结构的方向性                   |
| 分布     | Distribution    | 特征在区域内的分布情况         |

并非所有维度都适用于所有特征。

例如：

- 痣需要位置、形状、大小、可见色调和突出程度。
- 眉毛需要形状、长度、宽度、密度、方向和左右差异。
- 鼻梁需要宽度、轮廓、方向、突出程度及视角信息。
- 皱纹需要位置、方向、数量、长度和可见深度。

禁止为了填满字段而编造观察值。

# 5. 面部特征分类体系与详细词典

本章以 FISWG 19 个组件为主框架，补充解剖学术语和工程化描述维度。

Codex 必须将本章内容转化为结构化知识文件，而不是仅将本章作为一段自然语言说明保存在 `references/` 中。

## 5.1 F01 — Skin（皮肤）


9

### 5.1.1 观察目标

皮肤组件主要描述面部可见皮肤的整体外观、表面纹理、色调以及明显的局部状态。

必须区分：

- 整体皮肤外观。
- 局部皮肤纹理。
- 局部色素或颜色差异。
- 暂时性皮肤状态。
- 光照和图像处理造成的视觉效果。

### 5.1.2 特征维度

| 特征 ID | 特征名称             | 描述内容             |
| ------- | -------------------- | -------------------- |
| F01-01  | Overall Texture      | 整体皮肤纹理         |
| F01-02  | Visible Pore Pattern | 可见毛孔情况         |
| F01-03  | Overall Tone         | 图像中呈现的整体色调 |
| F01-04  | Tone Variation       | 局部色调差异         |
| F01-05  | Surface Smoothness   | 表面平滑程度         |
| F01-06  | Surface Irregularity | 可见表面不规则       |
| F01-07  | Local Skin Condition | 局部皮肤状态         |
| F01-08  | Skin Reflectance     | 皮肤表面反光情况     |

### 5.1.3 术语

| 英文            | 中文       | 用法               |
| --------------- | ---------- | ------------------ |
| Smooth          | 平滑       | 可见纹理较少       |
| Fine-textured   | 纹理细腻   | 表面细节较细       |
| Coarse-textured | 纹理较粗   | 表面纹理较明显     |
| Visible pores   | 毛孔可见   | 可观察到毛孔       |
| Uneven texture  | 纹理不均匀 | 局部表面差异       |
| Dry appearance  | 干燥外观   | 仅描述图像可见状态 |
| Oily appearance | 油润外观   | 仅描述图像可见状态 |
| Reflective      | 反光明显   | 可能受光照影响     |
| Matte           | 哑光       | 表面反射较弱       |
| Uneven tone     | 色调不均   | 局部颜色或明暗差异 |

### 5.1.4 观察限制

1. 不根据照片色调直接推断人物真实肤色。
2. 不根据皮肤外观推断健康状态。
3. 不根据皮肤状态推断年龄，除非用户明确要求描述视觉年龄印象；本 Skill 默认不进行年龄推断。
4. 不把图像磨皮造成的光滑效果认定为真实皮肤纹理。
5. 光照、曝光、白平衡和滤镜可能改变皮肤呈现。

### 5.1.5 提示词映射

将结构化观察转换为绘画语言，例如：

- `fine_textured` → naturally fine skin texture
- `visible_pores` → subtle visible skin pores
- `uneven_tone` → naturally uneven visible skin tone
- `localized_texture_irregularity` → localized natural skin texture variation

禁止自动生成“完美无瑕皮肤”等美化描述，除非用户明确要求艺术化处理。

## 5.2 F02 — Face/Head Outline（面部/头部轮廓）


6

### 5.2.1 观察目标

该组件用于描述头部外轮廓及面部轮廓。

必须区分：

- 头颅外轮廓。
- 面部软组织外轮廓。
- 额部轮廓。
- 颧部轮廓。
- 下颌轮廓。
- 下巴轮廓。

不能仅用一个“脸型”标签替代完整轮廓描述。

### 5.2.2 特征维度

| 特征 ID | 特征名称           | 描述内容     |
| ------- | ------------------ | ------------ |
| F02-01  | Head Top Outline   | 头部顶部轮廓 |
| F02-02  | Upper Face Outline | 上部面部轮廓 |
| F02-03  | Midface Outline    | 中部面部轮廓 |
| F02-04  | Cheek Width        | 颧部相对宽度 |
| F02-05  | Lower Face Outline | 下部面部轮廓 |
| F02-06  | Jawline Shape      | 下颌线形态   |
| F02-07  | Chin Contour       | 下巴外轮廓   |
| F02-08  | Overall Face Shape | 整体面部形态 |
| F02-09  | Profile Contour    | 侧面轮廓     |
| F02-10  | Outline Asymmetry  | 轮廓左右差异 |

### 5.2.3 常用整体轮廓描述词

| 英文              | 中文         |
| ----------------- | ------------ |
| Oval              | 椭圆形       |
| Round             | 圆形         |
| Square            | 方形         |
| Rectangular       | 长方形       |
| Oblong            | 偏长形       |
| Heart-shaped      | 心形         |
| Inverted-triangle | 倒三角形     |
| Triangular        | 三角形       |
| Diamond-shaped    | 菱形         |
| Broad             | 宽阔         |
| Narrow            | 窄           |
| Tapered           | 逐渐收窄     |
| Angular           | 棱角明显     |
| Soft-contoured    | 轮廓柔和     |
| Elongated         | 纵向较长     |
| Broad lower face  | 下部面部较宽 |
| Narrow lower face | 下部面部较窄 |

以上词汇用于视觉描述，不构成互斥的科学脸型分类。

### 5.2.4 推荐组合描述

不要只输出：

> Oval face.

应优先输出更具体的结构描述：

> The face has a relatively broad upper and middle region, with the lower face gradually narrowing toward a softly rounded chin.

中文：

> 面部上部与中部相对较宽，下部逐渐向下收窄，下巴轮廓较为圆钝。

这样可以保留更多形态信息。

### 5.2.5 观察限制

- 正面照片适合观察整体正面轮廓。
- 侧面照片有助于观察额部、鼻部、唇部和下巴的前后关系。
- 三分之四视角可能造成左右宽度视觉差异。
- 广角近距离拍摄可能改变面部中央和边缘的相对视觉大小。
- 头发遮挡不能被当作真实面部轮廓。

## 5.3 F03 — Face/Head Composition（面部整体构成）


8

### 5.3.1 观察目标

该组件是整个面部知识库的关键部分。

它描述不同面部组成部分之间的相对位置、大小、间距和整体组织方式。

面部相似性不只来自眼睛、鼻子、嘴巴各自的形状，也来自它们组合在一起形成的整体结构。

因此，系统必须独立记录：

- 五官之间的相对距离。
- 五官相对于整体脸部的位置。
- 不同面部区域之间的相对宽度。
- 面部上下区域的视觉比例。
- 五官整体排列是否偏集中或偏分散。

### 5.3.2 特征维度

| 特征 ID | 特征名称                          | 描述内容                 |
| ------- | --------------------------------- | ------------------------ |
| F03-01  | Eye Spacing                       | 两眼间距                 |
| F03-02  | Eye-to-Face Position              | 眼睛相对于面部的位置     |
| F03-03  | Nose-to-Eye Relationship          | 鼻部与眼睛的相对关系     |
| F03-04  | Nose-to-Mouth Relationship        | 鼻部与嘴部的相对关系     |
| F03-05  | Mouth-to-Eye Relationship         | 嘴部与眼睛的相对关系     |
| F03-06  | Upper-Mid-Lower Face Relationship | 面部上、中、下区域关系   |
| F03-07  | Cheek-to-Jaw Width Relationship   | 颧部与下颌宽度关系       |
| F03-08  | Ear Position Relationship         | 耳朵相对于其他结构的位置 |
| F03-09  | Feature Concentration             | 五官整体集中程度         |
| F03-10  | Overall Feature Arrangement       | 整体五官布局             |

### 5.3.3 上、中、下面部区域

作为工程化描述方法，可以将面部划分为：

- Upper Face：上部面部区域。
- Midface：中部面部区域。
- Lower Face：下部面部区域。

其边界和解剖学定义应参考解剖学资料及所采用的标志点定义，不得把示意性分区当作所有面部均适用的精确测量标准。

### 5.3.4 相对关系描述

| 关系                | 描述示例                                                     |
| ------------------- | ------------------------------------------------------------ |
| Eye Spacing         | Eyes appear relatively wide-set.                             |
| Eye Position        | Eyes appear relatively high within the visible face.         |
| Nose Width          | Nose appears relatively broad compared with the visible interocular spacing. |
| Mouth Width         | Mouth appears relatively narrow compared with the nose.      |
| Midface             | The midface appears relatively long.                         |
| Lower Face          | The lower face appears relatively short.                     |
| Cheek/Jaw           | The cheek region appears broader than the jaw region.        |
| Feature Arrangement | Facial features appear relatively concentrated in the central region. |

这些描述应当基于图像视角和质量条件，不得直接转换为未经校准的真实人体尺寸。

### 5.3.5 重要限制

FISWG 的特征清单使用相对特征关系，并不意味着可以将普通二维照片直接当作精准人体测量数据。

本 Skill：

- 可以描述视觉上的相对比例。
- 可以描述某个特征相对于另一个特征更宽、更窄、更高或更低。
- 不应直接输出精确毫米数。
- 不应使用未经验证的黄金比例作为面部正常标准。
- 不应强迫真实面部符合对称或理想化比例。

## 5.4 F04 — Hair（头发）


7

### 5.4.1 观察目标

头发组件描述头部可见毛发的形态、分布、纹理、密度和发际线。

需要区分：

- 头发本身。
- 发际线。
- 发型造成的视觉轮廓。
- 头发对面部其他结构的遮挡。

### 5.4.2 特征维度

| 特征 ID | 特征名称              | 描述内容           |
| ------- | --------------------- | ------------------ |
| F04-01  | Hair Length           | 长度               |
| F04-02  | Hair Shape            | 整体发型轮廓       |
| F04-03  | Hair Texture          | 直、波浪、卷曲等   |
| F04-04  | Hair Density          | 可见密度           |
| F04-05  | Hair Distribution     | 分布情况           |
| F04-06  | Hair Color Appearance | 图像中可见的发色   |
| F04-07  | Hair Parting          | 分缝               |
| F04-08  | Hairline Shape        | 发际线形状         |
| F04-09  | Temporal Hairline     | 两侧额角发际线     |
| F04-10  | Widow's Peak          | 美人尖             |
| F04-11  | Hair Whorl            | 发旋（仅在可见时） |
| F04-12  | Hair Asymmetry        | 左右分布差异       |

### 5.4.3 常用术语

| 英文              | 中文           |
| ----------------- | -------------- |
| Straight          | 直发           |
| Wavy              | 波浪发         |
| Curly             | 卷发           |
| Coiled            | 紧密卷曲       |
| Fine              | 纤细           |
| Coarse            | 较粗           |
| Dense             | 浓密           |
| Sparse            | 稀疏           |
| Receding hairline | 发际线后移外观 |
| Widow's peak      | 美人尖         |
| Center part       | 中分           |
| Side part         | 侧分           |
| Uneven hairline   | 发际线不规则   |
| Temple recession  | 额角后移外观   |

### 5.4.4 观察限制

- 发型属于可改变的外观特征。
- 发色可能受光照、染发、滤镜影响。
- 发际线可能被刘海或帽子遮挡。
- 不应根据当前发型推断人物长期发型。
- 不应将头发遮挡造成的额头轮廓误认为头骨轮廓。

## 5.5 F05 — Forehead（额头）


9

### 5.5.1 观察目标

描述额头的可见高度、宽度、轮廓、倾斜程度，以及眉弓区域的形态。

### 5.5.2 特征维度

| 特征 ID | 特征名称              | 描述内容     |
| ------- | --------------------- | ------------ |
| F05-01  | Forehead Height       | 相对高度     |
| F05-02  | Forehead Width        | 相对宽度     |
| F05-03  | Forehead Shape        | 正面形状     |
| F05-04  | Forehead Slope        | 侧面倾斜     |
| F05-05  | Forehead Contour      | 额部轮廓     |
| F05-06  | Brow Ridge Prominence | 眉弓突出程度 |
| F05-07  | Brow Ridge Continuity | 眉弓连续性   |
| F05-08  | Forehead Asymmetry    | 左右差异     |

### 5.5.3 常用术语

- High forehead：相对较高的额头。
- Low forehead：相对较低的额头。
- Broad forehead：相对宽阔的额头。
- Narrow forehead：相对狭窄的额头。
- Sloping forehead：侧面轮廓呈倾斜状。
- Rounded forehead：轮廓较圆。
- Flat forehead contour：轮廓较平。
- Prominent brow ridge：眉弓突出较明显。

### 5.5.4 观察限制

额头的可见高度会受到发际线、发型和头部姿态影响。

眉弓突出程度需要谨慎描述，不能仅凭阴影推断骨性结构。

## 5.6 F06 — Eyebrows（眉毛）


9

### 5.6.1 观察目标

描述左右眉毛的形状、长度、宽度、密度、方向、位置及相互差异。

必须分别记录左右眉毛，不能只记录一个笼统的眉形。

### 5.6.2 特征维度

| 特征 ID | 特征名称            | 描述内容     |
| ------- | ------------------- | ------------ |
| F06-01  | Overall Brow Shape  | 整体眉形     |
| F06-02  | Brow Length         | 长度         |
| F06-03  | Brow Width          | 宽度         |
| F06-04  | Brow Thickness      | 粗细         |
| F06-05  | Brow Density        | 毛发密度     |
| F06-06  | Brow Arch           | 眉峰与弧度   |
| F06-07  | Brow Head Position  | 眉头位置     |
| F06-08  | Brow Tail Position  | 眉尾位置     |
| F06-09  | Brow Tilt           | 倾斜程度     |
| F06-10  | Brow-Eye Distance   | 眉眼间距     |
| F06-11  | Brow Hair Direction | 毛发生长方向 |
| F06-12  | Brow Asymmetry      | 左右差异     |

### 5.6.3 常用眉形术语

| 英文          | 中文           |
| ------------- | -------------- |
| Straight      | 平直眉         |
| Arched        | 弧形眉         |
| Angular       | 棱角明显的眉形 |
| Gently curved | 轻微弯曲       |
| Rounded arch  | 圆弧形眉峰     |
| High arch     | 高眉峰         |
| Low arch      | 低眉峰         |
| Thick         | 浓眉           |
| Thin          | 细眉           |
| Sparse        | 稀疏           |
| Dense         | 浓密           |
| Tapered tail  | 眉尾逐渐变细   |
| Uneven        | 不规则         |
| Asymmetric    | 左右不对称     |

### 5.6.4 重要描述规则

应分别描述：

- 左眉整体形状。
- 右眉整体形状。
- 左眉眉峰位置。
- 右眉眉峰位置。
- 两眉的密度差异。
- 两眉与眼睛之间的距离。

例如：

> The left eyebrow has a more pronounced arch, while the right eyebrow appears relatively straighter.

中文：

> 左侧眉毛的眉峰更明显，右侧眉毛整体相对平直。

### 5.6.5 观察限制

- 化妆和修眉会改变眉形。
- 表情会改变眉毛的高度和弧度。
- 阴影可能造成眉毛密度或眉弓突出程度的误判。
- 眉毛被刘海遮挡时，应标记为部分可见或不可见。

## 5.7 F07 — Eyes（眼睛）


5

眼睛是面部描述中需要重点处理的组件之一。

仅仅描述“大眼睛”“小眼睛”“杏仁眼”远远不够。

眼睛区域包含多个相互关联的解剖和表面结构，且具有明显的左右差异。

### 5.7.1 眼睛整体形态

| 特征 ID | 特征名称                 | 描述内容           |
| ------- | ------------------------ | ------------------ |
| F07-01  | Overall Eye Shape        | 整体眼形           |
| F07-02  | Palpebral Fissure Length | 眼裂相对长度       |
| F07-03  | Palpebral Fissure Height | 眼裂相对高度       |
| F07-04  | Eye Width                | 眼睛相对宽度       |
| F07-05  | Eye Height               | 眼睛相对高度       |
| F07-06  | Eye Prominence           | 眼球突出程度       |
| F07-07  | Eye Depth Appearance     | 眼窝深浅的视觉表现 |
| F07-08  | Eye Spacing              | 两眼间距           |
| F07-09  | Eye Position             | 眼睛相对面部的位置 |
| F07-10  | Eye Asymmetry            | 左右眼差异         |

### 5.7.2 眼角结构

| 特征 ID | 特征名称            | 描述内容             |
| ------- | ------------------- | -------------------- |
| F07-11  | Inner Canthus       | 内眼角               |
| F07-12  | Outer Canthus       | 外眼角               |
| F07-13  | Canthal Tilt        | 内外眼角相对高度关系 |
| F07-14  | Inner Canthal Shape | 内眼角形态           |
| F07-15  | Outer Canthal Shape | 外眼角形态           |
| F07-16  | Epicanthic Fold     | 内眦赘皮等可见形态   |
| F07-17  | Canthal Asymmetry   | 左右眼角差异         |

### 5.7.3 眼睑结构

| 特征 ID | 特征名称             | 描述内容       |
| ------- | -------------------- | -------------- |
| F07-18  | Upper Eyelid Shape   | 上眼睑形态     |
| F07-19  | Lower Eyelid Shape   | 下眼睑形态     |
| F07-20  | Upper Eyelid Crease  | 上眼睑褶皱     |
| F07-21  | Eyelid Hooding       | 上眼睑覆盖情况 |
| F07-22  | Lower Eyelid Contour | 下眼睑轮廓     |
| F07-23  | Eyelid Prominence    | 眼睑突出程度   |
| F07-24  | Eyelid Asymmetry     | 左右眼睑差异   |

### 5.7.4 眼球可见结构

| 特征 ID | 特征名称          | 描述内容     |
| ------- | ----------------- | ------------ |
| F07-25  | Iris Visibility   | 虹膜可见程度 |
| F07-26  | Pupil Visibility  | 瞳孔可见程度 |
| F07-27  | Sclera Visibility | 巩膜可见程度 |
| F07-28  | Iris Appearance   | 虹膜图像表现 |
| F07-29  | Pupil Appearance  | 瞳孔图像表现 |

瞳孔大小会受到光照和生理状态影响，不应把单张图中的瞳孔大小直接当作稳定面部特征。

### 5.7.5 睫毛

| 特征 ID | 特征名称          | 描述内容 |
| ------- | ----------------- | -------- |
| F07-30  | Upper Eyelashes   | 上睫毛   |
| F07-31  | Lower Eyelashes   | 下睫毛   |
| F07-32  | Eyelash Length    | 长度     |
| F07-33  | Eyelash Density   | 密度     |
| F07-34  | Eyelash Direction | 方向     |
| F07-35  | Eyelash Asymmetry | 左右差异 |

### 5.7.6 常用眼形术语

| 英文                 | 中文             |
| -------------------- | ---------------- |
| Almond-shaped        | 杏仁形           |
| Round                | 圆形             |
| Narrow               | 细长             |
| Wide                 | 较宽             |
| Hooded               | 上眼睑覆盖较明显 |
| Deep-set             | 眼窝视觉上较深   |
| Prominent            | 眼球视觉上较突出 |
| Downturned           | 外眼角相对偏低   |
| Upturned             | 外眼角相对偏高   |
| Neutral tilt         | 近水平           |
| Wide-set             | 两眼间距相对较宽 |
| Close-set            | 两眼间距相对较窄 |
| Monolid appearance   | 单眼皮外观       |
| Double eyelid crease | 可见双眼皮褶皱   |

### 5.7.7 眼部描述示例

不推荐：

> Large beautiful almond eyes.

推荐：

> The eyes are moderately elongated, with a visible upper eyelid crease. The outer corners appear slightly higher than the inner corners. The left eye appears marginally narrower than the right.

中文：

> 眼睛整体呈中等偏长的形态，上眼睑褶皱可见。外眼角相对于内眼角略高。左眼视觉上比右眼稍窄。

### 5.7.8 重要限制

1. 不要将眼睛大小与瞳孔大小混为一谈。
2. 不要将上眼睑褶皱和眼球突出程度混为一谈。
3. 不要仅凭阴影判断眼窝深度。
4. 不要根据眼形推断族裔或其他身份属性。
5. 不要根据眼睛外观推断性格、情绪倾向或心理状态。
6. 表情和视线方向可能改变眼睑形态。
7. 低分辨率图像不能可靠描述虹膜和睫毛的微小细节。

第二部分到此结束。

本部分已经定义了知识库结构，并详细展开了 F01–F07。下一部分继续 F08–F19，尤其会详细处理鼻部、耳部、口部、下颌、面部标记和特殊特征；随后建立统一的中英描述词典与特征关系体系。

# 第三部分：F08–F19 面部特征知识库

## 5.8 F08 — Cheeks（面颊）

### 5.8.1 观察目标

面颊组件用于描述颧部、面颊软组织以及脸颊区域的外观形态。

需要区分：

- 颧骨区域的外部轮廓。
- 面颊软组织的饱满程度。
- 面颊凹陷。
- 面颊表面可见的酒窝、纹路及其他局部特征。

不能将面颊看起来饱满或凹陷，直接等同于骨骼结构的确定结论。

### 5.8.2 特征维度

| 特征 ID | 特征名称             | 描述内容         |
| ------- | -------------------- | ---------------- |
| F08-01  | Cheek Width          | 面颊区域相对宽度 |
| F08-02  | Cheek Fullness       | 面颊饱满程度     |
| F08-03  | Cheek Hollowing      | 面颊凹陷程度     |
| F08-04  | Zygomatic Prominence | 颧部突出程度     |
| F08-05  | Cheek Contour        | 面颊整体轮廓     |
| F08-06  | Cheek Soft Tissue    | 面颊软组织形态   |
| F08-07  | Cheek Dimple         | 酒窝             |
| F08-08  | Cheek Asymmetry      | 左右面颊差异     |

### 5.8.3 常用术语

| 英文                      | 中文               |
| ------------------------- | ------------------ |
| Full cheeks               | 饱满的面颊         |
| Hollow cheeks             | 凹陷的面颊         |
| Prominent cheekbones      | 颧部较突出         |
| Flat cheek contour        | 面颊轮廓较平       |
| Rounded cheeks            | 圆润的面颊         |
| Angular cheek contour     | 面颊轮廓较明显     |
| High cheekbone appearance | 颧部位置视觉上较高 |
| Cheek dimple              | 酒窝               |
| Asymmetric cheeks         | 左右面颊不对称     |

### 5.8.4 观察限制

- 面部表情可能改变面颊轮廓。
- 体重变化可能改变面颊软组织。
- 光照和阴影可能造成凹陷或突出感。
- 三分之四视角下左右面颊的视觉宽度不能直接比较。
- 不应仅凭照片阴影判断颧骨的真实骨性突出程度。

## 5.9 F09 — Nose（鼻子）

鼻部是面部中心区域的重要组成部分，也是需要进行多视角分析的组件。

鼻子不能只用“高鼻梁”“塌鼻子”“大鼻子”描述。

需要分别观察鼻根、鼻梁、鼻体、鼻尖、鼻翼、鼻孔和鼻小柱等结构，并记录它们之间的关系。

### 5.9.1 鼻部整体结构

| 特征 ID | 特征名称           | 描述内容         |
| ------- | ------------------ | ---------------- |
| F09-01  | Overall Nose Shape | 鼻部整体形态     |
| F09-02  | Nose Length        | 鼻部相对长度     |
| F09-03  | Nose Width         | 鼻部相对宽度     |
| F09-04  | Nose Projection    | 鼻部侧面突出程度 |
| F09-05  | Nose Axis          | 鼻部整体轴线     |
| F09-06  | Nose Symmetry      | 鼻部左右对称性   |

### 5.9.2 鼻根与鼻梁

| 特征 ID | 特征名称                 | 描述内容           |
| ------- | ------------------------ | ------------------ |
| F09-07  | Nasal Root               | 鼻根形态           |
| F09-08  | Nasal Bridge             | 鼻梁形态           |
| F09-09  | Bridge Width             | 鼻梁宽度           |
| F09-10  | Bridge Height Appearance | 鼻梁高度的视觉表现 |
| F09-11  | Bridge Profile           | 鼻梁侧面轮廓       |
| F09-12  | Bridge Straightness      | 鼻梁是否呈直线轮廓 |
| F09-13  | Bridge Curvature         | 鼻梁曲线           |
| F09-14  | Bridge Asymmetry         | 鼻梁左右或轴线差异 |

### 5.9.3 鼻尖

| 特征 ID | 特征名称             | 描述内容         |
| ------- | -------------------- | ---------------- |
| F09-15  | Nasal Tip Shape      | 鼻尖形态         |
| F09-16  | Nasal Tip Size       | 鼻尖相对大小     |
| F09-17  | Nasal Tip Projection | 鼻尖突出程度     |
| F09-18  | Nasal Tip Rotation   | 鼻尖朝向         |
| F09-19  | Nasal Tip Definition | 鼻尖轮廓清晰程度 |
| F09-20  | Nasal Tip Asymmetry  | 鼻尖左右差异     |

### 5.9.4 鼻翼与鼻孔

| 特征 ID | 特征名称            | 描述内容           |
| ------- | ------------------- | ------------------ |
| F09-21  | Alar Shape          | 鼻翼形态           |
| F09-22  | Alar Width          | 鼻翼宽度           |
| F09-23  | Alar Thickness      | 鼻翼厚度的视觉表现 |
| F09-24  | Alar Flare          | 鼻翼外扩程度       |
| F09-25  | Nostril Shape       | 鼻孔形状           |
| F09-26  | Nostril Size        | 鼻孔大小           |
| F09-27  | Nostril Orientation | 鼻孔朝向           |
| F09-28  | Nostril Asymmetry   | 左右鼻孔差异       |

### 5.9.5 鼻底与鼻小柱

| 特征 ID | 特征名称             | 描述内容     |
| ------- | -------------------- | ------------ |
| F09-29  | Nasal Base           | 鼻底整体形态 |
| F09-30  | Columella            | 鼻小柱       |
| F09-31  | Columella Width      | 鼻小柱宽度   |
| F09-32  | Columella Length     | 鼻小柱长度   |
| F09-33  | Columella Position   | 鼻小柱位置   |
| F09-34  | Nasal Base Asymmetry | 鼻底左右差异 |

### 5.9.6 常用术语

| 英文                | 中文             |
| ------------------- | ---------------- |
| Straight bridge     | 鼻梁较直         |
| Convex bridge       | 鼻梁侧面轮廓略凸 |
| Concave bridge      | 鼻梁侧面轮廓略凹 |
| Broad bridge        | 鼻梁较宽         |
| Narrow bridge       | 鼻梁较窄         |
| Rounded tip         | 圆钝鼻尖         |
| Bulbous tip         | 较饱满的鼻尖     |
| Pointed tip         | 较尖的鼻尖       |
| Upturned tip        | 鼻尖略上翘       |
| Downturned tip      | 鼻尖略下垂       |
| Broad alae          | 鼻翼较宽         |
| Narrow alae         | 鼻翼较窄         |
| Flared nostrils     | 鼻翼外扩         |
| Asymmetric nostrils | 左右鼻孔不对称   |

### 5.9.7 鼻部观察视角

| 视角     | 主要观察内容                               |
| -------- | ------------------------------------------ |
| 正面     | 鼻梁宽度、鼻翼宽度、鼻孔左右差异、鼻轴偏斜 |
| 侧面     | 鼻梁侧面轮廓、鼻尖突出程度、鼻尖旋转方向   |
| 三分之四 | 鼻部整体立体外观、鼻翼与鼻尖关系           |
| 低角度   | 鼻底、鼻孔和鼻小柱可见情况                 |

### 5.9.8 重要限制

1. 正面照片不能可靠确定鼻梁侧面曲线。
2. 侧面照片不能完整展示左右鼻翼对称性。
3. 广角镜头可能使鼻部视觉上变大。
4. 近距离拍摄会改变鼻部相对于耳部和面颊的视觉比例。
5. 不应从阴影推断鼻梁真实高度。
6. 不应使用未经校准的照片测量推断真实鼻部尺寸。

## 5.10 F10 — Ears（耳朵）

### 5.10.1 观察目标

耳部包含多个具有不同形态的结构。系统应尽可能在耳朵清晰可见时进行细节描述。

### 5.10.2 整体特征

| 特征 ID | 特征名称         | 描述内容       |
| ------- | ---------------- | -------------- |
| F10-01  | Overall Ear Size | 耳朵相对大小   |
| F10-02  | Ear Shape        | 整体耳形       |
| F10-03  | Ear Position     | 耳朵位置       |
| F10-04  | Ear Angle        | 耳朵方向和角度 |
| F10-05  | Ear Prominence   | 耳朵突出程度   |
| F10-06  | Ear Length       | 相对长度       |
| F10-07  | Ear Width        | 相对宽度       |
| F10-08  | Ear Asymmetry    | 左右耳差异     |

### 5.10.3 耳部解剖结构

| 特征 ID | 英文名称          | 中文名称   |
| ------- | ----------------- | ---------- |
| F10-09  | Helix             | 耳轮       |
| F10-10  | Antihelix         | 对耳轮     |
| F10-11  | Tragus            | 耳屏       |
| F10-12  | Antitragus        | 对耳屏     |
| F10-13  | Earlobe           | 耳垂       |
| F10-14  | Concha            | 耳甲腔     |
| F10-15  | Triangular Fossa  | 三角窝     |
| F10-16  | Scapha            | 舟状窝     |
| F10-17  | Intertragic Notch | 耳屏间切迹 |

### 5.10.4 耳垂特征

| 特征 ID | 特征名称          | 描述内容       |
| ------- | ----------------- | -------------- |
| F10-18  | Attached Earlobe  | 附着型耳垂外观 |
| F10-19  | Free Earlobe      | 游离型耳垂外观 |
| F10-20  | Earlobe Size      | 耳垂大小       |
| F10-21  | Earlobe Shape     | 耳垂形状       |
| F10-22  | Earlobe Asymmetry | 左右耳垂差异   |

### 5.10.5 常用术语

| 英文              | 中文             |
| ----------------- | ---------------- |
| Protruding ears   | 耳朵较突出       |
| Close-set ears    | 耳朵相对贴近头部 |
| Attached earlobes | 附着型耳垂       |
| Free earlobes     | 游离型耳垂       |
| Large earlobes    | 耳垂较大         |
| Small earlobes    | 耳垂较小         |
| Rounded ears      | 耳朵轮廓较圆     |
| Angular ears      | 耳部轮廓较明显   |
| Asymmetric ears   | 左右耳不对称     |

### 5.10.6 观察限制

- 长发可能遮挡耳朵。
- 耳朵可能只在侧面或三分之四视角中清晰可见。
- 佩戴耳饰可能遮挡耳垂。
- 耳朵被头发遮挡时不能补全耳部结构。
- 左右耳不可见程度不同，应分别记录。

## 5.11 F11 — Mouth（嘴部）

嘴部包含上唇、下唇、唇红缘、唇峰、人中、口角和牙齿等结构。

本组件必须区分嘴唇的自然形态、表情造成的动态变化，以及化妆带来的视觉改变。

### 5.11.1 整体口部

| 特征 ID | 特征名称                 | 描述内容     |
| ------- | ------------------------ | ------------ |
| F11-01  | Overall Mouth Shape      | 整体嘴形     |
| F11-02  | Mouth Width              | 嘴部宽度     |
| F11-03  | Mouth Position           | 嘴部相对位置 |
| F11-04  | Mouth Symmetry           | 左右对称性   |
| F11-05  | Mouth Corner Position    | 嘴角位置     |
| F11-06  | Mouth Corner Orientation | 嘴角方向     |
| F11-07  | Lip Closure              | 嘴唇闭合状态 |

### 5.11.2 上唇与下唇

| 特征 ID | 特征名称             | 描述内容     |
| ------- | -------------------- | ------------ |
| F11-08  | Upper Lip Shape      | 上唇形态     |
| F11-09  | Lower Lip Shape      | 下唇形态     |
| F11-10  | Upper Lip Fullness   | 上唇丰满程度 |
| F11-11  | Lower Lip Fullness   | 下唇丰满程度 |
| F11-12  | Upper Lip Projection | 上唇突出程度 |
| F11-13  | Lower Lip Projection | 下唇突出程度 |
| F11-14  | Vermilion Border     | 唇红缘       |
| F11-15  | Cupid's Bow          | 唇峰         |
| F11-16  | Lip Asymmetry        | 左右唇形差异 |
| F11-17  | Lip Surface          | 唇部表面状态 |

### 5.11.3 人中结构

| 特征 ID | 特征名称          | 描述内容     |
| ------- | ----------------- | ------------ |
| F11-18  | Philtrum Length   | 人中相对长度 |
| F11-19  | Philtrum Width    | 人中宽度     |
| F11-20  | Philtrum Columns  | 人中嵴       |
| F11-21  | Philtrum Groove   | 人中沟       |
| F11-22  | Philtrum Symmetry | 人中对称性   |

### 5.11.4 牙齿

| 特征 ID | 特征名称                | 描述内容           |
| ------- | ----------------------- | ------------------ |
| F11-23  | Dental Visibility       | 牙齿可见程度       |
| F11-24  | Tooth Shape             | 可见牙齿形状       |
| F11-25  | Tooth Size              | 可见牙齿相对大小   |
| F11-26  | Tooth Alignment         | 牙齿排列           |
| F11-27  | Dental Spacing          | 可见牙缝           |
| F11-28  | Missing Teeth           | 可见缺牙情况       |
| F11-29  | Dental Color Appearance | 图像中牙齿颜色表现 |
| F11-30  | Dental Asymmetry        | 可见牙齿排列差异   |

### 5.11.5 常用术语

| 英文                       | 中文             |
| -------------------------- | ---------------- |
| Full upper lip             | 上唇丰满         |
| Full lower lip             | 下唇丰满         |
| Thin upper lip             | 上唇较薄         |
| Thin lower lip             | 下唇较薄         |
| Defined cupid's bow        | 唇峰明显         |
| Flat upper lip contour     | 上唇轮廓较平     |
| Wide mouth                 | 嘴较宽           |
| Narrow mouth               | 嘴较窄           |
| Downturned corners         | 嘴角向下         |
| Upturned corners           | 嘴角向上         |
| Asymmetric lips            | 左右唇形不对称   |
| Visible dental gap         | 可见牙缝         |
| Irregular dental alignment | 可见牙齿排列不齐 |

### 5.11.6 重要限制

- 张嘴、微笑、说话会改变口部形态。
- 化妆可能改变唇形边界。
- 牙齿只有在可见时才能描述。
- 不能根据闭合嘴唇推断牙齿形态。
- 不应根据嘴角方向推断人物情绪或人格。
- 如果图像存在唇部修饰或滤镜，应明确记录。

## 5.12 F12 — Chin/Jawline（下巴/下颌线）

### 5.12.1 观察目标

描述下巴、下颌线和下颌角的形态，以及它们与面颊和颈部的相对关系。

### 5.12.2 下巴特征

| 特征 ID | 特征名称        | 描述内容         |
| ------- | --------------- | ---------------- |
| F12-01  | Chin Shape      | 下巴形状         |
| F12-02  | Chin Width      | 下巴相对宽度     |
| F12-03  | Chin Height     | 下巴相对高度     |
| F12-04  | Chin Projection | 下巴侧面突出程度 |
| F12-05  | Chin Position   | 下巴位置         |
| F12-06  | Chin Symmetry   | 下巴对称性       |
| F12-07  | Chin Cleft      | 颏裂             |
| F12-08  | Chin Dimple     | 颏窝             |
| F12-09  | Chin Groove     | 颏部沟纹         |
| F12-10  | Chin Contour    | 下巴轮廓         |

### 5.12.3 下颌线特征

| 特征 ID | 特征名称             | 描述内容       |
| ------- | -------------------- | -------------- |
| F12-11  | Jawline Shape        | 下颌线整体形态 |
| F12-12  | Jawline Definition   | 下颌线清晰程度 |
| F12-13  | Jaw Width            | 下颌相对宽度   |
| F12-14  | Jaw Angle            | 下颌角形态     |
| F12-15  | Jaw Angle Definition | 下颌角清晰程度 |
| F12-16  | Jawline Asymmetry    | 左右下颌线差异 |
| F12-17  | Lower Face Contour   | 下部面部轮廓   |
| F12-18  | Submental Contour    | 颏下区域轮廓   |

### 5.12.4 常用术语

| 英文            | 中文         |
| --------------- | ------------ |
| Rounded chin    | 圆钝下巴     |
| Square chin     | 方形下巴     |
| Pointed chin    | 尖下巴       |
| Broad chin      | 宽下巴       |
| Narrow chin     | 窄下巴       |
| Prominent chin  | 下巴突出     |
| Receding chin   | 下巴后缩外观 |
| Cleft chin      | 颏裂         |
| Dimpled chin    | 有颏窝       |
| Defined jawline | 下颌线清晰   |
| Soft jawline    | 下颌线柔和   |
| Angular jaw     | 下颌角明显   |
| Broad jaw       | 下颌较宽     |
| Narrow jaw      | 下颌较窄     |

### 5.12.5 观察限制

- 侧面视角对于下巴前后突出程度很重要。
- 正面视角更适合观察下巴宽度和左右差异。
- 体重变化会影响下颌和颏下软组织外观。
- 胡须可能遮挡下颌线。
- 头部俯仰会改变下颌轮廓。
- 阴影不能直接证明骨骼结构。

## 5.13 F13 — Neck（颈部）

### 5.13.1 特征维度

| 特征 ID | 特征名称               | 描述内容     |
| ------- | ---------------------- | ------------ |
| F13-01  | Neck Width             | 颈部相对宽度 |
| F13-02  | Neck Length Appearance | 可见颈部长度 |
| F13-03  | Neck Contour           | 颈部轮廓     |
| F13-04  | Neck Muscle Visibility | 可见肌肉轮廓 |
| F13-05  | Neck Skin Folds        | 颈部皮肤褶皱 |
| F13-06  | Neck Vein Visibility   | 可见血管     |
| F13-07  | Laryngeal Prominence   | 喉部突出外观 |
| F13-08  | Neck Asymmetry         | 左右差异     |

### 5.13.2 观察限制

- 衣物可能遮挡颈部。
- 头部姿态可能改变颈部可见长度。
- 肌肉紧张和姿势会改变表面轮廓。
- 不应将短暂的肌肉状态当作永久特征。
- 不应从喉部外观推断身份或敏感属性。

## 5.14 F14 — Facial Hair（面部毛发）

### 5.14.1 观察目标

描述胡须、胡茬、唇须和其他面部毛发的形状、分布、密度、长度及边缘。

### 5.14.2 特征维度

| 特征 ID | 特征名称               | 描述内容               |
| ------- | ---------------------- | ---------------------- |
| F14-01  | Moustache              | 唇须                   |
| F14-02  | Chin Beard             | 下巴胡须               |
| F14-03  | Cheek Beard            | 面颊胡须               |
| F14-04  | Jaw Beard              | 下颌胡须               |
| F14-05  | Neck Beard             | 颈部胡须               |
| F14-06  | Stubble                | 胡茬                   |
| F14-07  | Beard Length           | 胡须长度               |
| F14-08  | Beard Density          | 胡须密度               |
| F14-09  | Beard Distribution     | 胡须分布               |
| F14-10  | Beard Texture          | 胡须纹理               |
| F14-11  | Beard Color Appearance | 图像中可见色调         |
| F14-12  | Beard Edge Shape       | 胡须边缘形状           |
| F14-13  | Beard Connection       | 不同胡须区域的连接情况 |
| F14-14  | Beard Asymmetry        | 左右差异               |

### 5.14.3 常用术语

- Clean-shaven：无明显胡须。
- Light stubble：轻微胡茬。
- Heavy stubble：明显胡茬。
- Full beard：较完整的胡须。
- Short beard：短胡须。
- Long beard：长胡须。
- Goatee：山羊胡。
- Moustache：唇须。
- Sideburns：鬓角毛发。
- Patchy beard：分布不均的胡须。
- Dense beard：浓密胡须。
- Sparse beard：稀疏胡须。

### 5.14.4 观察限制

面部毛发属于高度可改变的外观特征。

不得仅凭当前照片判断人物长期是否留胡须。

胡须可能遮挡嘴角、下巴、下颌线和皮肤标记，必须同时记录遮挡情况。

## 5.15 F15 — Facial Lines（面部纹路）

### 5.15.1 观察目标

记录面部可见的皱纹、沟纹、褶皱和线状结构。

需要区分：

- 自然形成的皮肤纹路。
- 表情引起的动态纹路。
- 长期可见的皱纹。
- 疤痕或其他线状标记。

### 5.15.2 特征维度

| 特征 ID | 特征名称           | 描述内容     |
| ------- | ------------------ | ------------ |
| F15-01  | Forehead Lines     | 额纹         |
| F15-02  | Glabellar Lines    | 眉间纹       |
| F15-03  | Periorbital Lines  | 眼周纹       |
| F15-04  | Crow's Feet        | 鱼尾纹       |
| F15-05  | Infraorbital Lines | 眶下纹       |
| F15-06  | Nasal Lines        | 鼻部周围纹路 |
| F15-07  | Nasolabial Folds   | 鼻唇沟       |
| F15-08  | Perioral Lines     | 口周纹       |
| F15-09  | Marionette Lines   | 木偶纹       |
| F15-10  | Mental Crease      | 颏唇沟       |
| F15-11  | Cheek Lines        | 面颊纹路     |
| F15-12  | Neck Lines         | 颈纹         |
| F15-13  | Other Facial Lines | 其他面部纹路 |

### 5.15.3 每条纹路需要记录的属性

- 位置。
- 数量。
- 长度。
- 方向。
- 深度的视觉表现。
- 是否连续。
- 是否对称。
- 是否可能由表情造成。
- 可见程度。
- 观察置信度。

### 5.15.4 观察限制

不能根据静态照片判断某条纹路一定是永久性皱纹。

例如，皱眉时出现的眉间纹可能主要由当前表情造成。

应使用“图像中可见的纹路”作为描述基准。

## 5.16 F16 — Scars（疤痕）

### 5.16.1 特征维度

| 特征 ID | 特征名称              | 描述内容           |
| ------- | --------------------- | ------------------ |
| F16-01  | Scar Location         | 位置               |
| F16-02  | Scar Shape            | 形状               |
| F16-03  | Scar Size             | 相对大小           |
| F16-04  | Scar Length           | 长度               |
| F16-05  | Scar Width            | 宽度               |
| F16-06  | Scar Orientation      | 方向               |
| F16-07  | Scar Color Appearance | 图像中可见色调     |
| F16-08  | Scar Depth Appearance | 凹凸程度的视觉表现 |
| F16-09  | Scar Edge             | 边缘形态           |
| F16-10  | Scar Distribution     | 分布               |
| F16-11  | Scar Visibility       | 可见程度           |

### 5.16.2 常用术语

- Linear scar：线状疤痕。
- Curved scar：弧形疤痕。
- Irregular scar：不规则疤痕。
- Depressed scar：凹陷性外观。
- Raised scar：隆起性外观。
- Hypopigmented appearance：色素较浅的外观。
- Hyperpigmented appearance：色素较深的外观。

### 5.16.3 观察限制

仅根据图像不应推断疤痕形成原因、受伤时间或医学性质。

不能把所有局部色差都认定为疤痕。

如果无法区分痣、色斑、阴影或疤痕，应标记为不确定的局部标记。

## 5.17 F17 — Facial Marks（面部标记）

### 5.17.1 观察目标

描述不属于普通皮肤整体纹理、但具有局部特征的可见面部标记。

### 5.17.2 特征分类

| 特征 ID | 特征名称                     | 描述内容           |
| ------- | ---------------------------- | ------------------ |
| F17-01  | Mole                         | 痣                 |
| F17-02  | Freckles                     | 雀斑               |
| F17-03  | Acne Marks                   | 痘印               |
| F17-04  | Acne Lesions                 | 可见痤疮样局部标记 |
| F17-05  | Birthmark                    | 胎记外观           |
| F17-06  | Pigmentation Patch           | 色素斑             |
| F17-07  | Redness Patch                | 局部发红           |
| F17-08  | Bruise Appearance            | 瘀斑外观           |
| F17-09  | Abrasion Appearance          | 擦伤外观           |
| F17-10  | Vitiligo-like Depigmentation | 可见色素减退区域   |
| F17-11  | Rosacea-like Redness         | 可见局部红斑       |
| F17-12  | Other Marks                  | 其他局部标记       |

这里的 `-like` 表示视觉外观相似，不代表医学诊断。

### 5.17.3 每个标记需要记录的属性

- 所属区域。
- 具体位置。
- 左侧或右侧。
- 形状。
- 大小。
- 数量。
- 可见色调。
- 边界清晰程度。
- 是否突出。
- 是否被遮挡。
- 是否与其他标记形成特殊排列。

### 5.17.4 特殊位置描述

为了提高复现能力，不能只写“脸上有一颗痣”。

应该尽可能写成：

> A small, dark, round mark is visible on the image-left cheek, below and lateral to the outer corner of the left eye.

中文：

> 图像左侧面颊可见一处较小的深色圆形标记，位于眼外角下方并偏外侧。

注意：若图片存在镜像风险，必须使用“图像左侧/右侧”，不能擅自转换成人物解剖学左右侧。

## 5.18 F18 — Alterations（人为修饰）

### 5.18.1 观察目标

记录通过人为行为形成、改变或装饰面部外观的可见特征。

### 5.18.2 特征分类

| 特征 ID | 特征名称                    | 描述内容        |
| ------- | --------------------------- | --------------- |
| F18-01  | Piercing                    | 穿孔            |
| F18-02  | Tattoo                      | 纹身            |
| F18-03  | Cosmetic Makeup             | 化妆            |
| F18-04  | Permanent Makeup            | 半永久/纹绣外观 |
| F18-05  | Eyebrow Modification        | 眉部修饰        |
| F18-06  | Eyelash Modification        | 睫毛修饰        |
| F18-07  | Lip Modification Appearance | 唇部修饰外观    |
| F18-08  | Other Alterations           | 其他人为修饰    |

### 5.18.3 穿孔描述

记录：

- 位置。
- 数量。
- 饰品形状。
- 饰品大小。
- 饰品颜色。
- 左右侧。
- 是否可能遮挡其他结构。

### 5.18.4 纹身描述

记录：

- 所在区域。
- 图案形状。
- 图案方向。
- 大小。
- 可见颜色。
- 线条粗细。
- 图案与周围结构的相对位置。

### 5.18.5 观察限制

不能仅凭照片判断某个标记是纹身、贴纸、化妆还是其他临时装饰。

如果来源无法确定，应描述其可见外观，而不是推断形成方式。

## 5.19 F19 — Other（其他特征）

该组件用于记录无法归入前述 18 个类别、但对面部外观描述有价值的可见特征。

### 5.19.1 使用原则

只有在确实无法归入现有类别时才使用 `F19`。

不能因为 Agent 不知道某个特征的专业名称，就直接将它归类为 Other。

如果某个特征实际上属于眼部、鼻部、耳部或其他已定义组件，应先尝试查找正确的特征类别。

### 5.19.2 数据要求

每条 Other 特征必须记录：

- 描述。
- 位置。
- 形态。
- 可见程度。
- 观察来源。
- 置信度。
- 无法归类的原因。
- 是否需要专业人员进一步确认。

# 6. 面部特征词汇与描述语言规范

## 6.1 词汇库的设计目标

仅有英文专业术语还不够。

Agent 必须能够将观察结果转换为：

1. 专业英文描述。
2. 专业中文描述。
3. 人类绘画师能够理解的自然语言。
4. AI 图像模型能够理解的提示词。

因此，应将词汇库拆分为三种表达层。

| 表达层                        | 主要用途           |
| ----------------------------- | ------------------ |
| Anatomical Vocabulary         | 解剖学和专业术语   |
| Morphological Vocabulary      | 面部形态描述       |
| Artistic Rendering Vocabulary | 绘画和图像生成表达 |

例如：

| 专业术语             | 形态描述     | 绘画表达                     |
| -------------------- | ------------ | ---------------------------- |
| Palpebral fissure    | 眼裂偏长     | elongated eye opening        |
| Nasal alae           | 鼻翼较宽     | relatively broad nasal wings |
| Zygomatic prominence | 颧部突出     | prominent cheek contour      |
| Chin projection      | 下巴突出程度 | more forward-projecting chin |
| Vermilion border     | 唇红缘       | clearly defined lip border   |

绘画表达不得改变专业观察的含义。

## 6.2 词汇数据结构

每个词汇条目建议包含：

```
descriptor_id: eye_shape_almond
canonical_name_en: almond-shaped
canonical_name_zh: 杏仁形
category: shape
applicable_components:
  - F07
definition_en: >
  An eye shape with an elongated opening and relatively tapered
  inner and outer regions.
definition_zh: >
  眼裂整体偏长，内外侧轮廓相对收窄的视觉形态。
usage_notes:
  - Must be based on visible eye contour.
  - Do not infer identity or ethnicity.
prompt_expression:
  generic: almond-shaped eyes
synonyms:
  - almond eye shape
related_descriptors:
  - narrow
  - elongated
source_refs:
  - S01
status: project_curated
```

这里的定义是项目词汇库的初始编写规范，Codex 应对照专业来源检查术语含义，不应把示例文本当作标准原文。

## 6.3 词汇使用规则

1. 一个特征可以同时使用多个描述词。
2. 不能把所有形态强行归类为固定类别。
3. 不确定时允许使用宽泛描述。
4. 不允许根据面部特征进行身份或敏感属性推断。
5. 形态词汇必须与实际可见特征一致。
6. 描述词不能替代原始观察记录。
7. 英文和中文描述应保持相同语义。
8. 不能为了让 Prompt 更流畅而删除左右差异。
9. 不得自动把不规则特征修正为对称或标准形态。
10. 对存在多种解释的特征，应保留原始描述并标注不确定性。

## 6.4 禁止使用的模糊表达

以下词语不能单独作为专业面部特征：

- 好看。
- 普通。
- 有气质。
- 凶狠。
- 温柔。
- 聪明。
- 精明。
- 狡猾。
- 善良。
- 像某种人。
- 犯罪相。
- 有攻击性。

这些词要么是主观审美判断，要么是人格、道德或行为推断，不能代替面部形态描述。

如果用户使用了这些词，Agent 可以询问其具体指向的可见外观特征，但不得自行将其解释成确定的解剖特征。

例如，用户说“看起来很凶”，Agent 可以询问：

> 你记得的是眉眼、眼睑、嘴角还是其他哪一部分的外观？如果只是整体印象，也可以保留为主观印象，不必强行转换成某个具体面部特征。

第三部分结束。

下一部分将进入第 7 章至第 9 章：面部空间关系、左右不对称性、图像质量与特征稳定性，以及图片逆向描述的完整执行流程。这部分会把前面定义的 19 类特征连接起来，解决“逐个五官都描述了，但组合出来却不像原图”的关键问题。

# 第四部分：面部空间关系、图像质量与逆向分析流程

# 7. 面部空间关系与整体结构知识库

## 7.1 为什么必须独立建立空间关系知识库

面部特征的识别价值并不只取决于单个组成部分。

例如，两张脸可能都具有：

- 杏仁形眼睛。
- 较宽的鼻翼。
- 较薄的上唇。
- 圆钝的下巴。

但它们仍然可能存在明显差异，因为：

- 两眼之间的距离不同。
- 眼睛在面部中的位置不同。
- 鼻部与嘴部之间的距离不同。
- 颧部和下颌的宽度关系不同。
- 上、中、下面部的相对比例不同。
- 五官的整体分布不同。

因此，系统必须建立一个独立于 19 个组件的 `Spatial Relations` 知识库。

19 个组件描述“有什么特征”，空间关系知识库描述“这些特征如何组合”。

## 7.2 空间关系的基本类型

建议将面部空间关系分为八类：

| 类型     | 英文                      | 内容                       |
| -------- | ------------------------- | -------------------------- |
| 距离关系 | Distance Relationship     | 两个结构之间的相对间距     |
| 宽度关系 | Width Relationship        | 两个结构的相对宽度         |
| 高度关系 | Height Relationship       | 两个结构的相对高度         |
| 位置关系 | Positional Relationship   | 结构相对于另一个结构的位置 |
| 角度关系 | Angular Relationship      | 结构之间的方向和角度       |
| 比例关系 | Proportional Relationship | 多个结构的相对大小关系     |
| 对齐关系 | Alignment Relationship    | 结构是否在视觉上对齐       |
| 对称关系 | Symmetry Relationship     | 左右结构的对应程度         |

## 7.3 必须建立的核心关系

### 7.3.1 眼部关系

| 关系 ID | 名称                      | 描述内容               |
| ------- | ------------------------- | ---------------------- |
| R01     | Interocular Spacing       | 两眼之间的间距         |
| R02     | Eye-to-Nose Position      | 眼睛与鼻部的相对位置   |
| R03     | Brow-to-Eye Distance      | 眉毛与眼睛的距离       |
| R04     | Eye-to-Face Position      | 眼睛在整体面部中的位置 |
| R05     | Left-Right Eye Difference | 左右眼差异             |
| R06     | Eye-to-Cheek Relationship | 眼睛与颧部的相对关系   |

### 7.3.2 鼻部关系

| 关系 ID | 名称                   | 描述内容                 |
| ------- | ---------------------- | ------------------------ |
| R07     | Nose-to-Eye Width      | 鼻宽与眼部间距的关系     |
| R08     | Nose-to-Mouth Distance | 鼻底与嘴部的相对距离     |
| R09     | Nose-to-Mouth Width    | 鼻宽与嘴宽的关系         |
| R10     | Nose-to-Face Width     | 鼻宽与整体面部宽度的关系 |
| R11     | Nose Axis Alignment    | 鼻部轴线与面部中线的关系 |

### 7.3.3 嘴部关系

| 关系 ID | 名称                         | 描述内容             |
| ------- | ---------------------------- | -------------------- |
| R12     | Mouth-to-Eye Width           | 嘴宽与眼部间距的关系 |
| R13     | Mouth-to-Chin Distance       | 嘴部与下巴的相对距离 |
| R14     | Upper-Lower Lip Relationship | 上下唇之间的比例关系 |
| R15     | Mouth Corner Alignment       | 左右嘴角的位置关系   |

### 7.3.4 面部区域关系

| 关系 ID | 名称                              | 描述内容                 |
| ------- | --------------------------------- | ------------------------ |
| R16     | Upper-Midface Relationship        | 上部与中部面部的相对关系 |
| R17     | Mid-Lower Face Relationship       | 中部与下部面部的相对关系 |
| R18     | Cheek-Jaw Width Relationship      | 颧部与下颌宽度关系       |
| R19     | Forehead-Cheek Width Relationship | 额部与颧部宽度关系       |
| R20     | Face Height-Width Relationship    | 面部纵横向视觉关系       |
| R21     | Ear-Eye Position                  | 耳朵与眼睛的位置关系     |
| R22     | Ear-Nose Position                 | 耳朵与鼻部的位置关系     |
| R23     | Nose-Chin Alignment               | 鼻部与下巴的相对轴线关系 |

## 7.4 关系描述语言

建议采用以下定性描述：

- relatively wider than：相对更宽。
- relatively narrower than：相对更窄。
- positioned higher than：位置相对更高。
- positioned lower than：位置相对更低。
- closer to：相对更接近。
- farther from：相对更远。
- more centrally positioned：位置更靠近中央。
- more laterally positioned：位置更偏向侧面。
- relatively elongated：相对较长。
- relatively compressed：相对较紧凑。
- more concentrated：五官相对集中。
- more widely distributed：五官分布相对分散。

这些词汇应优先用于相对关系，而不是输出未经校准的绝对数值。

## 7.5 空间关系数据结构

```
relation_id: R07
relation_name_en: Nose-to-Eye Width
relation_name_zh: 鼻宽与眼部间距关系

subject_feature: F09
reference_feature: F07

relation_type: width_relationship

allowed_values:
  - relatively_narrower
  - approximately_similar
  - relatively_wider
  - uncertain

observation_requirements:
  preferred_view:
    - frontal
  minimum_visibility:
    - nose_visible
    - both_eyes_visible

limitations:
  - Perspective distortion may affect apparent proportions.
  - Oblique views are not suitable for direct frontal width comparison.
  - No calibrated anatomical measurements should be inferred.

prompt_rendering:
  relatively_narrower: >
    The nose appears relatively narrow compared with the
    interocular spacing.
```

## 7.6 关系冲突检查

系统必须检查不同特征之间是否出现明显矛盾。

例如：

- 面部被描述为下部明显收窄，但同时被描述为下颌非常宽。
- 两眼被描述为明显宽间距，但另一条描述又认为两眼非常接近。
- 鼻部被描述为明显偏斜，但面部中线关系又被描述为完全居中。

但是，冲突检查不能简单地把不同描述当作错误。

真实人脸可能存在复杂的不对称结构。

因此，冲突检测应分为：

1. 逻辑冲突： 两条描述在相同视角、相同参照下无法同时成立。
2. 视角差异： 正面和侧面观察产生不同视觉结果。
3. 来源差异： 用户回忆与图片观察不同。
4. 时间差异： 不同时间拍摄的照片显示不同外观。
5. 不确定性差异： 某项观察本身不够可靠。

只有逻辑冲突才应要求用户进一步核实。

# 8. 左右不对称性知识库

## 8.1 设计目标

面部并非完全对称。

如果 Agent 为了让图像更美观而自动将左右面部结构标准化，就可能破坏真实人物最有价值的特征。

因此，左右不对称性必须作为独立知识模块。

## 8.2 左右标记规范

统一采用：

- `left`
- `right`
- `bilateral`
- `midline`
- `unknown`

必须额外区分：

- `anatomical_left`
- `anatomical_right`
- `image_left`
- `image_right`

因为部分照片可能经过镜像处理。

在镜像状态未知时，系统只能可靠地说“图像左侧”，不能自动认定为人物的解剖学左侧。

## 8.3 不对称性分类

### 眼眉区域

- 左右眉峰高度不同。
- 左右眉毛长度不同。
- 左右眉毛密度不同。
- 左右眼裂大小不同。
- 左右眼裂形态不同。
- 左右眼角倾斜程度不同。
- 左右眼睑褶皱不同。
- 左右眼睛突出程度不同。

### 鼻部

- 鼻轴偏向。
- 鼻尖偏向。
- 左右鼻翼形态不同。
- 左右鼻孔大小不同。
- 左右鼻孔形态不同。
- 鼻小柱位置偏移。

### 嘴部

- 左右嘴角高度不同。
- 左右嘴唇丰满程度不同。
- 左右唇红缘形态不同。
- 人中相对于嘴部中心偏移。
- 嘴部整体中线偏移。

### 面颊与下颌

- 左右颧部突出程度不同。
- 左右脸颊饱满程度不同。
- 左右下颌轮廓不同。
- 下巴中心偏移。
- 左右下颌角形态不同。

### 耳部

- 左右耳高度不同。
- 左右耳大小不同。
- 左右耳突出程度不同。
- 左右耳垂形态不同。

## 8.4 不对称性记录结构

```
{
  "asymmetry_id": "ASYM-001",
  "component_id": "F07",
  "feature": "eye_width",
  "side_a": "image_left",
  "side_b": "image_right",
  "difference_type": "relative_size_difference",
  "description": "The image-left eye appears slightly narrower.",
  "visibility": "clear",
  "confidence": "medium",
  "evidence_source": "direct_visual_observation",
  "mirror_status": "unknown",
  "limitations": [
    "Perspective may influence apparent width."
  ]
}
```

## 8.5 不对称性在提示词中的优先级

当用户明确确认某项不对称性时，提示词必须保留它。

例如：

```
Preserve the natural left-right asymmetry:
the image-left eye is slightly narrower than the image-right eye,
and the left eyebrow has a more pronounced arch.
Do not symmetrize these features.
```

禁止使用会让模型自动对称化的描述替代用户确认的结构差异。

# 9. 图像质量、可观察性与不确定性体系

## 9.1 设计目标

图片逆向描述的首要任务不是尽可能多地输出特征，而是判断哪些特征真正能够从图像中观察到。

本项目必须建立独立的 Image Quality Gate。

它应当在正式面部特征分析之前运行。

推荐核心资料：

FISWG Image Factors to Consider in Facial Image Comparison v1.0

[https://fiswg.org/fiswg_image_factors_to_consider_in_facial_img_comparison_v1.0_2021.05.28.pdf](https://fiswg.org/fiswg_image_factors_to_consider_in_facial_img_comparison_v1.0_2021.05.28.pdf)

## 9.2 图像质量检查项目

| ID   | 检查项目  | 英文           | 主要风险                   |
| ---- | --------- | -------------- | -------------------------- |
| IQ01 | 分辨率    | Resolution     | 细节不足                   |
| IQ02 | 清晰度    | Sharpness      | 轮廓模糊                   |
| IQ03 | 光照      | Lighting       | 细节被阴影或高光覆盖       |
| IQ04 | 噪声      | Noise          | 产生伪细节                 |
| IQ05 | 压缩      | Compression    | 细节损失和块状伪影         |
| IQ06 | 遮挡      | Obstructions   | 特征不可见                 |
| IQ07 | 姿态      | Pose           | 特征比例和位置发生视觉变化 |
| IQ08 | 畸变      | Distortion     | 面部形状失真               |
| IQ09 | 图像伪影  | Artifacts      | 产生错误细节               |
| IQ10 | 颜色偏差  | Color Shift    | 颜色描述不可靠             |
| IQ11 | 运动模糊  | Motion Blur    | 边缘和局部细节丢失         |
| IQ12 | 过曝/欠曝 | Exposure       | 细节丢失                   |
| IQ13 | 图像滤镜  | Filters        | 真实外观被改变             |
| IQ14 | 镜像状态  | Mirroring      | 左右侧标记可能错误         |
| IQ15 | 表情状态  | Expression     | 动态结构改变               |
| IQ16 | 景深      | Depth of Field | 局部区域失焦               |

## 9.3 头部姿态

必须识别：

- Yaw：偏航。
- Pitch：俯仰。
- Roll：侧倾。

定义：

| 姿态                | 含义         |
| ------------------- | ------------ |
| Frontal             | 正面         |
| Near-frontal        | 接近正面     |
| Three-quarter left  | 左侧三分之四 |
| Three-quarter right | 右侧三分之四 |
| Profile left        | 左侧面       |
| Profile right       | 右侧面       |
| Upward tilted       | 头部上仰     |
| Downward tilted     | 头部下俯     |
| Rolled left/right   | 头部侧倾     |

如果视觉模型无法可靠估计角度，系统应使用定性描述，而不是编造精确角度。

例如：

正确：

> The face is shown in a slight three-quarter view.

不正确：

> The face is rotated exactly 17.4 degrees.

除非使用经过校准的姿态估计工具并且该数值确实来自工具输出。

## 9.4 分辨率与细节可见性

必须区分：

- 图像像素数量。
- 人脸区域像素数量。
- 实际可分辨的细节。

不能因为原图分辨率很高，就认为眼部细节一定清晰。

例如：

一张高分辨率照片可能存在严重运动模糊；另一张尺寸较小的正面照片反而能够清楚显示五官轮廓。

系统必须以实际可观察细节为准。

## 9.5 遮挡检查

常见遮挡：

- 眼镜。
- 墨镜。
- 口罩。
- 刘海。
- 长发。
- 帽子。
- 手。
- 其他物体。
- 阴影。
- 饰品。

每个面部组件都应单独记录遮挡情况。

例如：

```
{
  "component_id": "F07",
  "visibility": "partial",
  "occlusion": {
    "present": true,
    "type": "eyeglasses",
    "affected_region": "upper_eye_region"
  }
}
```

## 9.6 图像失真

重点关注：

### 广角透视失真

近距离广角拍摄可能使鼻部等中央结构视觉上更大，同时使外围结构看起来更小。

### 长焦与远距离拍摄

拍摄距离和焦距会影响面部透视关系。

### 图像纵横比改变

图像被横向拉伸或纵向压缩，可能使面部整体变宽或变窄。

### 数字美颜与生成式修图

可能改变：

- 眼睛大小。
- 鼻梁高度。
- 下巴形状。
- 皮肤纹理。
- 脸部轮廓。
- 左右对称性。

系统不能默认图像完全忠实地记录原始面部外观。

## 9.7 图像质量等级

建议使用四级质量状态：

| 状态                    | 定义               | 行为                 |
| ----------------------- | ------------------ | -------------------- |
| High Utility            | 主要特征清晰       | 可以进行较完整描述   |
| Usable with Limitations | 部分特征受影响     | 输出描述并标记限制   |
| Low Utility             | 大量关键特征不可靠 | 只描述明确可见部分   |
| Unsuitable              | 无法可靠分析       | 拒绝进行精细特征分析 |

注意：这是本项目的工程质量分级，不是 FISWG 官方统一评分等级。

## 9.8 单项特征的可观察性

每个特征独立记录：

| 状态           | 含义                     |
| -------------- | ------------------------ |
| Clear          | 清晰可见                 |
| Partial        | 部分可见                 |
| Obscured       | 被遮挡                   |
| Not Visible    | 图像中不可见             |
| Uncertain      | 是否存在或具体形态不确定 |
| Not Applicable | 不适用                   |

举例：

一张正面照片可能：

- 眼睛：Clear。
- 鼻梁正面宽度：Clear。
- 鼻梁侧面曲线：Not Visible。
- 耳部：Partial。
- 后脑轮廓：Not Visible。

即使图像整体质量很好，也不意味着每个特征都可观察。

## 9.9 置信度规则

建议采用：

- High。
- Medium。
- Low。
- Unknown。

但必须明确：

模型自评置信度不是经过统计校准的真实概率。

在没有专家标注数据集和校准实验之前，不得向用户显示“92% 确定”等看似精确的数字。

可以使用以下初始工程规则：

| 置信度  | 建议条件                               |
| ------- | -------------------------------------- |
| High    | 特征清晰、视角合适、没有明显遮挡和失真 |
| Medium  | 特征基本可见，但存在部分观察限制       |
| Low     | 细节不清楚，存在明显视角或图像质量影响 |
| Unknown | 无法判断或没有足够信息                 |

## 9.10 未知信息处理规则

任何无法观察的特征都必须进入 `unknowns`。

例如：

```
{
  "feature_id": "F09-11",
  "feature_name": "Nasal Bridge Profile",
  "status": "not_visible",
  "reason": "No suitable side view is available.",
  "must_not_infer": true
}
```

提示词编译器必须遵守：

- 不得把未知特征转换为默认的标准脸特征。
- 不得为了完整性自动补全。
- 不得将 Agent 建议写成用户确认信息。
- 不得将正面观察推断成可靠的侧面结构。

# 10. 面部特征稳定性与时间变化

## 10.1 设计目标

同一个人在不同时间可能具有不同的外观。

本项目必须区分：

- 相对稳定的面部结构。
- 短期变化的外观。
- 随年龄变化的特征。
- 可能被人为改变的特征。
- 因健康、创伤或其他状态变化而改变的特征。

主要参考：

FISWG Physical Stability of Facial Features of Adults v2.0

[https://fiswg.org/fiswg_physical_stability_of_facial_features_of_adults_v2.0_2021.05.28.pdf](https://fiswg.org/fiswg_physical_stability_of_facial_features_of_adults_v2.0_2021.05.28.pdf)

## 10.2 变化因素

| 因素     | 英文                   | 影响                       |
| -------- | ---------------------- | -------------------------- |
| 表情     | Expression             | 改变眼睑、嘴角、面颊和纹路 |
| 年龄     | Aging                  | 改变皮肤、软组织、毛发等   |
| 体重变化 | Weight Change          | 改变面颊和下颌软组织       |
| 健康状态 | Health Change          | 可能改变皮肤、组织及外观   |
| 创伤     | Injury                 | 可能产生瘢痕和组织变化     |
| 人为改变 | Intentional Alteration | 可能改变毛发、妆容、穿孔等 |
| 牙科变化 | Dental Changes         | 可能改变可见牙齿和口部外观 |
| 手术     | Surgery                | 可能改变面部结构和软组织   |

## 10.3 稳定性属性

建议为特征增加：

```
stability_profile:
  short_term_stability: high
  long_term_stability: medium
  expression_sensitivity: low
  aging_sensitivity: medium
  weight_change_sensitivity: medium
  health_change_sensitivity: unknown
  intentional_alteration_sensitivity: medium
```

以上数值仅为字段示例，不代表具体特征已经被认定为相应稳定等级。

Codex 必须依据 FISWG 原始资料逐项填充，不得用模型常识代替标准内容。

## 10.4 稳定性知识的使用场景

### 图片逆向描述

只描述当前图像中的外观，同时标记易变特征。

### 记忆访谈

如果用户记得的是较久以前的人物外观，Agent 应避免将当前发型、胡须、皮肤状态等默认当作永久特征。

### 提示词生成

如果目标是复现某个特定时间点的外观，应明确提示词对应的时间状态。

例如：

> Reconstruct the visible facial appearance as remembered from that specific period, including the hairstyle and facial hair described by the witness.

# 11. 图片逆向描述完整工作流

## 11.1 工作流总览

```
Input Image
    |
    v
Permission & Scope Check
    |
    v
Image Quality Gate
    |
    v
Viewpoint Assessment
    |
    v
Overall Facial Structure
    |
    v
19 Component Analysis
    |
    v
Spatial Relationship Analysis
    |
    v
Asymmetry Analysis
    |
    v
Visibility & Confidence Review
    |
    v
Consistency Validation
    |
    v
Structured Facial Profile
    |
    +--------------------+
    |                    |
    v                    v
Artist Brief       AI Prompt Compiler
    |                    |
    +----------+---------+
               |
               v
        User Review
               |
               v
       Iterative Revision
```

## 11.2 Step 1：输入检查

Agent 首先确认：

- 用户是否提供了图像。
- 用户是否有权使用该图像。
- 用户希望进行哪种分析。
- 是否需要生成可用于绘画的描述。
- 是否存在真实刑事案件用途。

如果涉及真实案件，应说明该工具是辅助性工具，不能代替专业法证人员。

## 11.3 Step 2：图像质量门控

必须先执行第 9 章定义的检查。

输出：

```
Image Quality Assessment

Overall Utility:
Viewpoint:
Head Pose:
Expression:
Resolution:
Sharpness:
Lighting:
Occlusion:
Distortion Risk:
Mirroring Status:
Possible Editing:
Main Limitations:
```

如果图像不适合进行精细描述，应先告知用户，而不是直接生成一份看似完整的报告。

## 11.4 Step 3：整体面部结构分析

先观察整体，不立即拆分五官。

记录：

- 头部轮廓。
- 面部整体形态。
- 面部上、中、下区域关系。
- 颧部和下颌宽度关系。
- 五官集中程度。
- 整体视觉重心。
- 可见的不对称性。

整体观察不能代替后续 19 组件分析。

## 11.5 Step 4：19 组件逐项分析

按照 F01–F19 顺序检查。

每个组件必须至少给出：

- 是否可见。
- 可观察的特征。
- 左右侧信息。
- 特征描述。
- 观察置信度。
- 图像质量限制。
- 是否存在特殊标记。
- 是否需要用户进一步确认。

对于没有可用信息的组件，明确标记未知，不要留空后让下游模型自动补全。

## 11.6 Step 5：空间关系分析

在完成单个组件观察后，再分析特征之间的关系。

例如：

- 眼间距相对于单眼宽度。
- 鼻宽相对于眼间距。
- 嘴宽相对于鼻宽。
- 鼻底到上唇的相对距离。
- 颧部与下颌宽度关系。
- 眼睛在面部中的位置。

必须考虑图像姿态和透视畸变。

## 11.7 Step 6：不对称性分析

对左右结构进行独立比较。

优先检查：

- 眉毛。
- 眼睛。
- 鼻翼。
- 嘴角。
- 面颊。
- 下颌。
- 耳朵。

对于无法确定左右身份的镜像图片，使用图像左/右标记。

## 11.8 Step 7：跨特征一致性检查

检查：

1. 特征描述是否相互矛盾。
2. 特征是否受到同一遮挡影响。
3. 不同视角的信息是否被错误混合。
4. 是否把表情当成固定结构。
5. 是否把光照当成皮肤或骨骼特征。
6. 是否把镜像方向标错。
7. 是否将未知特征错误填充。
8. 是否将推断标记为直接观察。

## 11.9 Step 8：构建结构化档案

所有有效观察必须进入统一 `Facial Profile`。

结构化档案是最终报告、绘画简报和 Prompt 的唯一事实来源。

不得在 Prompt 阶段凭空添加新的面部特征。

## 11.10 Step 9：生成多层输出

最终必须生成以下五个部分：

### A. 图像质量报告

简述图像质量和限制。

### B. 整体面部描述

用自然语言概括整体结构。

### C. 19 组件分析报告

逐项展示面部特征、可见性、左右差异和置信度。

### D. 绘画师简报

提供可供专业绘画师使用的完整描述。

### E. AI 生图提示词

生成结构化 Prompt、Negative Prompt 和未确认信息清单。

## 11.11 Step 10：用户复核与局部修订

用户可以指出：

- 哪项描述错误。
- 哪项特征遗漏。
- 哪项特征需要更详细描述。
- 哪项特征不应进入最终 Prompt。
- 哪项特征需要保留特殊不对称。

系统必须只修改相关字段，并重新运行一致性检查。

第四部分结束。

下一部分将进入第 12 章和第 13 章：认知访谈完整流程、详细问题库、记忆污染控制，以及统一 JSON 数据结构和 Schema 设计。这部分是第二条核心工作流，也是整个 Skill 能否真正具备专业画像能力的关键。

# 第五部分：认知访谈与统一数据模型

# 12. 认知访谈与记忆画像工作流

## 12.1 设计目标

记忆画像模式的目标不是让用户通过选择题拼出一张脸，而是尽可能科学地提取、组织和复核用户对目标人物面部外观的记忆。

Agent 应扮演经过专业方法约束的访谈辅助者，而不是替用户决定目标人物长什么样。

本项目采用分阶段认知访谈设计，并结合整体面部印象与局部特征回忆。

主要参考：

- Fodarella et al. (2015), Forensic procedures for facial-composite construction。
- Constructing identifiable composite faces: The importance of cognitive alignment of interview and construction procedure。
- IAI《Standards and Guidelines for Forensic Art and Facial Identification》。

这些研究可支持访谈方法设计，但本项目的具体问题顺序、状态机和数据字段属于工程设计，需要通过实际实验验证。

## 12.2 认知访谈的核心原则

### 原则一：自由回忆优先

用户首先应该有机会自行描述目标人物，而不是在 Agent 提供的选项中寻找答案。

### 原则二：整体与局部结合

先收集整体面部印象，再逐步提取局部结构，最后重新检查整体组合。

### 原则三：开放式提问

优先使用：

> 你记得这个人的眼睛有什么特点吗？

避免：

> 这个人的眼睛是不是很大？

### 原则四：允许不确定

用户可以回答：

- 不记得。
- 不确定。
- 没有注意。
- 只能记得大概。
- 只记得某个局部。

不得强迫用户选择一个特征。

### 原则五：严格区分信息来源

必须区分：

- 用户主动回忆。
- Agent 提问后用户回忆。
- Agent 提供候选信息。
- 用户确认候选信息。
- 用户拒绝候选信息。
- 用户无法判断。

### 原则六：不把 AI 建议当成记忆

Agent 提出的任何候选描述，都不能自动成为用户的回忆。

即使用户在看到 AI 生成图后觉得“好像就是这样”，也不能把这种事后确认与最初自由回忆混为一谈。

## 12.3 访谈状态机

建议将访谈设计为状态机，而不是一次性输出完整问卷。

```
START
  |
  v
CONSENT_AND_SCOPE
  |
  v
MEMORY_CONTAMINATION_CHECK
  |
  v
FREE_RECALL
  |
  v
CONTEXT_REINSTATEMENT
  |
  v
HOLISTIC_FACE_RECALL
  |
  v
FEATURE_RECALL
  |
  v
DISTINCTIVE_FEATURE_RECALL
  |
  v
RELATIONSHIP_RECALL
  |
  v
CONFIDENCE_REVIEW
  |
  v
SUMMARY_CONFIRMATION
  |
  v
PROFILE_FINALIZATION
  |
  v
ARTIST_BRIEF_AND_PROMPT
  |
  v
ITERATIVE_REFINEMENT
  |
  v
END
```

每个阶段都必须允许：

- 正常完成。
- 暂时跳过。
- 回到前一阶段。
- 用户主动结束。
- 用户修改之前的回答。

不能因为用户不愿回答某个问题，就阻止其完成整个流程。

## 12.4 阶段 0：访谈说明与授权

Agent 首先说明：

1. 访谈目的是整理用户对面部外观的记忆。
2. 不需要猜测或填满所有特征。
3. 用户可以随时表示不确定。
4. 系统会区分原始回忆和 Agent 提供的建议。
5. 访谈结果属于辅助性画像材料，不是身份确认或司法鉴定。

如果用户说明涉及真实案件，必须明确系统不能代替正式证人访谈或专业法证画像师。

### 需要确认的基本信息

建议使用自然对话逐项询问：

- 你是亲眼见过这个人，还是希望创作一个想象中的人物？
- 你是否希望尽可能还原真实记忆？
- 你是否已经看过这个人的照片、视频或其他画像？
- 你是否接受通过分阶段对话逐步回忆？

如果用户只是创作虚构角色，则不需要把整个流程包装成目击者访谈，应切换到普通角色设计模式。

## 12.5 阶段 1：记忆污染检查

该阶段的目标是了解用户的记忆来源。

建议问题：

1. 你最初是通过什么方式看到这个人的？
2. 你最后一次看到这个人距离现在有多久？
3. 你是否看过其他人对这个人的描述？
4. 你是否看过基于这个人的照片制作的画像？
5. 是否有人向你提出过关于这个人五官的描述？
6. 你现在对这个人的印象，是否受到这些信息的影响？

这些问题不是用来评价用户记忆是否真实，而是帮助系统区分信息来源。

需要记录：

```
{
  "memory_contamination": {
    "previous_photographs_seen": false,
    "previous_composites_seen": false,
    "external_descriptions_received": false,
    "possible_suggestion_exposure": "unknown",
    "notes": ""
  }
}
```

不能仅凭用户看过一张照片，就认定其记忆已经被污染。

## 12.6 阶段 2：自由回忆

这是最重要的访谈阶段。

Agent 应先提出一个开放问题：

> 请你尽可能自由地描述这张脸。暂时不需要按照眼睛、鼻子、嘴巴的顺序，也不用担心描述是否准确。可以从最先浮现的整体印象开始。

用户回答期间：

- 不要频繁打断。
- 不要主动补充形态。
- 不要将用户的词汇自动转换成精确的解剖学判断。
- 尽量保留用户原始表达。

完成后可以进行有限的开放式追问：

- 还有没有其他特征是你特别记得的？
- 有没有某个局部特别容易在脑海中浮现？
- 有没有一些细节你很确定，而另一些细节完全想不起来？

记录原始回答，不要覆盖。

## 12.7 阶段 3：观察情境重建

该阶段用于帮助用户回忆观察条件。

建议问题：

- 当时你是在什么环境下看到这个人的？
- 你距离这个人大概有多远？
- 你看到的是正面、侧面还是斜侧面？
- 当时光线如何？
- 你观察了多长时间？
- 这个人是否移动或转头？
- 你是否能清楚看到整个面部？
- 当时有没有物体、头发或其他因素遮挡？

注意：如果用户已经无法回忆这些信息，应允许跳过。

情境重建是辅助记忆的方法，不意味着 Agent 能根据情境自动推断出目标人物的面部结构。

## 12.8 阶段 4：整体面部回忆

先不逐个拆分五官，而是帮助用户描述整体结构。

建议问题：

1. 你记得这张脸整体偏宽还是偏长吗？
2. 脸部上部、中部和下部有什么明显区别？
3. 面部轮廓更偏圆润还是棱角分明？
4. 下半脸是否明显收窄？
5. 五官整体看起来比较集中还是分散？
6. 有没有特别明显的左右不对称？
7. 整体面部轮廓中，哪个部分最容易被你记住？

必须允许回答：

- 记不清。
- 不确定。
- 没有注意。
- 无法比较。

### 整体印象与特征描述的区别

用户可能会说：

> 这张脸给我的感觉比较瘦长。

Agent 可以追问：

> 你记得的是整个脸部轮廓比较长，还是脸颊和下颌比较窄？如果无法区分，也可以保留为整体印象。

不要直接将“瘦长”转换为确定的骨骼结构。

## 12.9 阶段 5：头发与额头

建议问题：

- 你记得头发大概是什么长度吗？
- 整体轮廓偏直、偏卷还是有波浪？
- 头发是否有明显分缝？
- 发际线是否有特别明显的形状？
- 额头在整体面部中显得偏高还是偏低？
- 是否记得额角或发际线的特殊形态？

如果用户没有注意头发，不应反复追问。

头发属于容易改变的外观特征，应与面部结构分开记录。

## 12.10 阶段 6：眉眼区域

先进行整体回忆：

> 你对这个人的眉眼区域还有什么印象？

然后根据用户已有回答，选择适当的细化问题。

### 眉毛

- 你记得眉毛整体偏浓还是偏淡吗？
- 眉毛更接近平直还是有明显弧度？
- 是否记得眉峰的位置？
- 左右眉毛有没有明显不同？

### 眼睛

- 你记得眼睛整体偏圆还是偏长吗？
- 眼睛在整张脸中的位置大概如何？
- 两眼之间的距离有什么印象？
- 眼角是否有明显倾斜？
- 上眼睑是否有明显褶皱？
- 左右眼是否存在差异？
- 你是否记得虹膜颜色，还是当时并没有注意？

不应连续询问所有问题。

Agent 应根据用户已有记忆动态选择下一问题。

## 12.11 阶段 7：鼻部

建议问题：

- 你对鼻子的整体形状有什么印象？
- 从正面看，鼻梁显得宽还是窄？
- 鼻尖是圆润、较尖，还是其他形态？
- 鼻翼是否明显？
- 鼻子在整张脸中显得突出还是相对平缓？
- 你是否记得鼻子有明显偏斜？
- 你是从正面看到鼻子，还是有侧面观察？

特别注意：

用户没有侧面观察时，不要逼迫其描述鼻梁的侧面曲线。

## 12.12 阶段 8：嘴部与下半脸

### 嘴部

- 你记得嘴部整体偏宽还是偏窄吗？
- 上唇和下唇分别是什么形态？
- 嘴角有什么特别印象？
- 是否记得明显唇峰？
- 是否能回忆起牙齿形态？
- 嘴部是否存在左右差异？

### 下巴与下颌

- 下巴更偏圆、方还是尖？
- 下颌线是否清晰？
- 面部下部是否明显收窄？
- 从侧面看，下巴是否有明显突出或后缩？
- 是否记得下巴有特殊凹陷或沟纹？

不要把用户对下半脸的整体印象强行拆成精确解剖学结论。

## 12.13 阶段 9：面颊、耳朵与特殊标记

建议问题：

- 面颊看起来饱满还是比较凹陷？
- 是否记得颧部轮廓明显？
- 耳朵是否清楚可见？
- 是否记得某处有痣、疤痕、雀斑或其他特殊标记？
- 特殊标记大概位于哪个区域？
- 你能确定它位于图像或人物的哪一侧吗？

对于特殊标记，位置往往比形容词更有价值。

如果用户只能记得：

> 左脸上好像有一颗痣。

应继续确认：

- 是面颊上部还是下部？
- 靠近鼻子还是耳朵？
- 大致靠近眼睛还是嘴角？
- 你是否确定是痣，而不是其他颜色差异？

如果用户无法回答，应保留模糊描述。

## 12.14 阶段 10：记忆置信度复核

Agent 应对每项特征单独询问用户的记忆确定程度。

推荐采用：

| 级别    | 用户理解                     |
| ------- | ---------------------------- |
| High    | 我非常确定自己记得这个特征   |
| Medium  | 我大致记得，但细节不完全确定 |
| Low     | 只是模糊印象                 |
| Unknown | 我无法判断                   |

注意：这是用户对自身记忆的主观报告，不是记忆准确性的客观概率。

每项特征必须独立评估，不能把用户对整体脸型的高置信度扩展到所有五官。

## 12.15 阶段 11：复述核对

Agent 应将目前收集的信息整理成结构化摘要。

例如：

```
目前记录的整体特征：

1. 整体脸型：
   你记得面部偏长，下半脸相对收窄。
   记忆置信度：Medium

2. 眉毛：
   你记得眉毛比较浓，整体接近平直。
   记忆置信度：High

3. 眼睛：
   你记得眼睛偏长，但无法确定具体眼角倾斜程度。
   记忆置信度：Medium

4. 鼻部：
   你只记得鼻尖比较圆润，其他细节不确定。
   记忆置信度：Low

5. 特殊标记：
   你模糊记得左侧面颊可能有一处小标记。
   记忆置信度：Low
```

然后询问用户：

> 这份总结是否准确地反映了你目前的记忆？哪些部分需要修改、删除或保留为不确定？

不能把 Agent 的总结自动视为用户确认。

## 12.16 阶段 12：访谈结束条件

当以下条件满足时，可以结束访谈：

- 用户已经完成自由回忆。
- 主要整体结构已经记录。
- 用户愿意回答的局部特征已经收集。
- 关键特征的记忆来源已经标记。
- 不确定信息已经保留。
- 用户已经获得一次检查和修改摘要的机会。

不要求所有 19 个组件都被描述。

对于记忆画像来说，强迫用户填满所有组件，可能反而增加猜测和记忆污染风险。

## 12.17 访谈问题库的数据结构

建议建立 `knowledge/interview/question_bank.yaml`：

```
question_id: Q-EYE-001

stage: eye_recall

component_id: F07

question_type: open_ended

question_zh: >
  你记得这个人的眼睛整体有什么特点吗？

question_en: >
  What do you remember about the overall appearance of this person's eyes?

purpose:
  - collect_spontaneous_eye_recall

leading_risk: low

requires_prior_free_recall: true

follow_up_questions:
  - Q-EYE-002
  - Q-EYE-003

allowed_answers:
  - free_text
  - uncertain
  - unknown
  - skip

memory_source_default: user_cued_recall
```

## 12.18 问题选择策略

Agent 不应机械地按照问题库顺序逐题询问。

应根据以下信息决定下一问题：

1. 用户已经主动提供了什么信息？
2. 哪些组件完全没有信息？
3. 哪些特征对用户来说特别容易记忆？
4. 用户是否表现出不确定？
5. 是否存在明显的记忆污染风险？
6. 是否有必要进一步澄清某个重要特征？
7. 继续追问是否可能降低记忆质量或让用户开始猜测？

推荐使用优先级：

- 用户主动提到的特殊特征。
- 用户明确记得的高价值特征。
- 影响整体结构的特征。
- 尚未澄清但对画像有帮助的特征。
- 用户主动愿意补充的其他信息。

不要以“问题完成数量”作为访谈质量指标。

# 13. 统一面部数据模型

## 13.1 设计目标

图片逆向描述和认知访谈最终必须使用统一数据结构。

这样可以保证：

- 两种模式共享面部特征知识库。
- 提示词编译器无需分别实现两套逻辑。
- 质量检查逻辑能够复用。
- 后续可以加入人工绘画师的修改记录。
- 可以比较不同信息来源的差异。
- 可以构建长期评测数据集。

统一模型名称：

```
FacialProfile
```

## 13.2 数据结构总体层次

```
FacialProfile
│
├── metadata
│
├── task_context
│
├── image_context
│
├── image_quality_report
│
├── interview_context
│
├── features[]
│   ├── component_id
│   ├── feature_id
│   ├── side
│   ├── observation
│   ├── visibility
│   ├── confidence
│   ├── evidence_source
│   └── limitations
│
├── spatial_relations[]
│
├── asymmetries[]
│
├── distinctive_marks[]
│
├── unknowns[]
│
├── conflicts[]
│
├── summary
│
├── artist_brief
│
├── prompt_output
│
└── audit_log[]
```

## 13.3 顶层数据结构

建议的 JSON：

```
{
  "schema_version": "1.0",
  "profile_id": "FP-000001",
  "created_at": "2026-11-01T12:00:00Z",
  "updated_at": "2026-11-01T12:00:00Z",

  "task_mode": "image_to_description",

  "language": "zh-CN",

  "metadata": {
    "skill_id": "forensic-facial-composite",
    "profile_status": "draft",
    "subject_reference": "subject-1",
    "user_confirmed": false
  },

  "task_context": {
    "purpose": "facial_appearance_description",
    "intended_output": [
      "structured_profile",
      "artist_brief",
      "image_prompt"
    ],
    "forensic_case_context": false
  },

  "image_context": null,

  "image_quality_report": null,

  "interview_context": null,

  "features": [],

  "spatial_relations": [],

  "asymmetries": [],

  "distinctive_marks": [],

  "unknowns": [],

  "conflicts": [],

  "summary": {},

  "artist_brief": null,

  "prompt_output": null,

  "audit_log": []
}
```

## 13.4 task_mode 枚举

```
image_to_description
memory_to_composite
```

不允许使用其他值，除非未来增加经过设计的新工作模式。

## 13.5 Feature Observation 数据结构

> **V1.1 规范提示：** 本节原有 JSON 示例为 V1.0 历史示例，保留用于说明设计演进，不再作为可执行数据契约。V1.1 的唯一规范结构为第 32.4 节定义的 FeatureObservation（含 `laterality`、`source_type`、`confirmation_status`、`knowledge_refs` 与 `evidence_refs`）。Codex 不得直接复制本节旧字段结构作为最终 Schema。

每个面部特征应作为独立观察记录。

```
{
  "observation_id": "OBS-0001",

  "component_id": "F07",

  "feature_id": "F07-01",

  "feature_name_en": "Overall Eye Shape",

  "feature_name_zh": "整体眼形",

  "side": "bilateral",

  "observation": {
    "value": "almond_shaped",
    "display_zh": "杏仁形",
    "display_en": "Almond-shaped",
    "free_text": ""
  },

  "visibility": "clear",

  "confidence": {
    "level": "high",
    "value": null,
    "calibrated": false,
    "basis": "model_observation"
  },

  "evidence_source": "direct_visual_observation",

  "viewpoint": {
    "view": "frontal",
    "side_reference": "unknown"
  },

  "limitations": [],

  "source_refs": [
    "S01"
  ],

  "confirmed_by_user": false
}
```

## 13.6 信息来源枚举

必须严格使用以下来源类型：

| 值                          | 含义                   |
| --------------------------- | ---------------------- |
| `direct_visual_observation` | 从图像直接观察         |
| `user_free_recall`          | 用户自由回忆           |
| `user_cued_recall`          | Agent 提问后用户回忆   |
| `user_confirmed`            | 用户明确确认的描述     |
| `agent_suggestion`          | Agent 提供的候选建议   |
| `external_reference`        | 外部资料或其他合法参考 |
| `unknown`                   | 来源无法确定           |

不能将 `agent_suggestion` 直接提升为 `user_confirmed`。

如果用户明确确认了一个由 Agent 提供的候选特征，应同时保留原始来源和确认过程。

## 13.7 visibility 枚举

```
clear
partial
obscured
not_visible
not_applicable
uncertain
```

## 13.8 confidence 数据结构

建议：

```
{
  "level": "medium",
  "value": null,
  "calibrated": false,
  "basis": "user_self_report"
}
```

其中：

`level`：

```
high
medium
low
unknown
```

`basis`：

```
user_self_report
model_observation
expert_review
unknown
```

如果没有经过校准，不得输出虚假的百分比置信度。

## 13.9 Interview Context

```
{
  "interview_id": "INT-0001",

  "interview_type": "memory_to_composite",

  "observation_time": "unknown",

  "observation_duration": "unknown",

  "viewpoint_recalled": "unknown",

  "lighting_recalled": "unknown",

  "distance_recalled": "unknown",

  "memory_contamination": {
    "previous_photographs_seen": "unknown",
    "previous_composites_seen": "unknown",
    "external_descriptions_received": "unknown",
    "suggestion_exposure": "unknown"
  },

  "interview_stages_completed": [],

  "user_requested_skips": [],

  "notes": ""
}
```

## 13.10 Spatial Relation 数据结构

```
{
  "relation_id": "R07",

  "subject_feature": "F09",

  "reference_feature": "F07",

  "relation_type": "width_relationship",

  "value": "relatively_narrower",

  "description_zh": "鼻部相对于两眼间距较窄。",

  "description_en": "The nose appears relatively narrow compared with the interocular spacing.",

  "visibility": "clear",

  "confidence": {
    "level": "medium",
    "calibrated": false
  },

  "evidence_source": "direct_visual_observation",

  "limitations": [
    "Perspective distortion may affect apparent proportions."
  ]
}
```

## 13.11 Audit Log

所有重要修改必须保留记录。

```
{
  "event_id": "EVT-0001",

  "timestamp": "2026-11-01T12:30:00Z",

  "event_type": "feature_updated",

  "feature_id": "F07-01",

  "previous_value": "unknown",

  "new_value": "almond_shaped",

  "actor": "user",

  "reason": "User clarified the remembered eye shape."
}
```

必须支持：

- 新增特征。
- 修改特征。
- 删除特征。
- 用户确认。
- 用户拒绝。
- Agent 建议。
- 访谈回退。
- Prompt 修订。
- 专家复核。

不得静默覆盖原始回忆或原始观察。

第五部分结束。

下一部分将给出完整的 JSON Schema 设计要求、知识库文件结构与索引策略，以及提示词编译器的输入输出协议。之后再进入专业来源获取、版权、评测和 Codex 开发验收。

# 第六部分：数据验证、知识库组织与提示词编译

# 14. JSON Schema 与数据验证规范

## 14.1 设计目标

结构化数据不仅用于保存结果，还承担以下职责：

- 限制 Agent 的输出格式。
- 防止特征信息丢失。
- 防止未知信息被自动补全。
- 保证不同工作模式的数据兼容。
- 支持后续人工复核。
- 为评测系统提供统一输入。

Codex 必须使用 JSON Schema 对核心输出进行验证。

建议使用 JSON Schema Draft 2020-12。

官方规范：

[https://json-schema.org/draft/2020-12](https://json-schema.org/draft/2020-12)

## 14.2 核心 Schema 文件

至少建立：

```
schemas/
├── facial_profile.schema.json
├── feature_observation.schema.json
├── image_quality.schema.json
├── interview_record.schema.json
├── spatial_relation.schema.json
├── asymmetry.schema.json
├── prompt_output.schema.json
└── source_metadata.schema.json
```

## 14.3 Feature Observation Schema

> **V1.1 规范提示：** 下方原有 Schema 是 V1.0 的不完整示例，仅为历史设计记录保留。其字段集合与第 13.5 节历史示例存在不一致，不可作为最终实现依据。V1.1 必须使用第 32.4.5 节的完整 Schema 契约，并让所有样例通过自动化验证。若本节旧示例与第 32.4 节冲突，以第 32.4 节为准。

下面是核心字段约束示例。Codex 应将其实现为完整 JSON Schema 文件，并补齐类型、必填字段和枚举约束。

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "FeatureObservation",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "observation_id",
    "component_id",
    "feature_id",
    "side",
    "observation",
    "visibility",
    "confidence",
    "evidence_source"
  ],
  "properties": {
    "observation_id": {
      "type": "string"
    },
    "component_id": {
      "type": "string",
      "pattern": "^F(0[1-9]|1[0-9])$"
    },
    "feature_id": {
      "type": "string"
    },
    "side": {
      "enum": [
        "left",
        "right",
        "bilateral",
        "midline",
        "unknown"
      ]
    },
    "observation": {
      "type": "object",
      "required": [
        "value"
      ],
      "properties": {
        "value": {},
        "display_zh": {
          "type": "string"
        },
        "display_en": {
          "type": "string"
        },
        "free_text": {
          "type": "string"
        }
      }
    },
    "visibility": {
      "enum": [
        "clear",
        "partial",
        "obscured",
        "not_visible",
        "not_applicable",
        "uncertain"
      ]
    },
    "confidence": {
      "type": "object",
      "required": [
        "level",
        "calibrated"
      ],
      "properties": {
        "level": {
          "enum": [
            "high",
            "medium",
            "low",
            "unknown"
          ]
        },
        "value": {
          "type": [
            "number",
            "null"
          ],
          "minimum": 0,
          "maximum": 1
        },
        "calibrated": {
          "type": "boolean"
        },
        "basis": {
          "type": "string"
        }
      }
    },
    "evidence_source": {
      "enum": [
        "direct_visual_observation",
        "user_free_recall",
        "user_cued_recall",
        "user_confirmed",
        "agent_suggestion",
        "external_reference",
        "unknown"
      ]
    },
    "limitations": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

## 14.4 必须实现的业务规则

JSON Schema 无法独立验证所有业务逻辑。

因此，必须额外建立 Python 验证器。

至少实现以下规则：

### 规则 1：不可见特征不能具有确定观察值

如果：

```
visibility = not_visible
```

则：

- 不允许将其描述为已确认的直接视觉观察。
- 必须填写不可见原因。
- 不得在 Prompt 中作为确定特征使用。

### 规则 2：Agent 建议不能自动成为用户确认

如果：

```
evidence_source = agent_suggestion
```

则：

```
confirmed_by_user = false
```

除非后续存在明确的用户确认事件，并保留审计记录。

### 规则 3：左右标记必须有依据

如果：

```
side = left
```

或：

```
side = right
```

必须记录左右参照依据。

当镜像状态未知时，优先使用：

```
image_left
image_right
```

不要自动转换为人物解剖学左右。

### 规则 4：置信度不能伪装为校准概率

如果：

```
calibrated = false
```

则系统不得将 `value` 直接展示为经过验证的统计概率。

### 规则 5：每个特征必须有合法组件

例如：

```
F07-01
```

必须属于：

```
F07
```

不能将眼睛特征错误地归入鼻部组件。

### 规则 6：未知项必须在 Prompt 中得到处理

未知特征不能自动转化为模型默认特征。

### 规则 7：来源引用必须存在

如果某个知识条目引用：

```
S01
```

则 `source_manifest` 中必须存在对应的来源记录。

## 14.5 验证器输出

建议统一返回：

```
{
  "valid": false,
  "errors": [
    {
      "code": "UNKNOWN_FEATURE_IN_PROMPT",
      "path": "prompt_output.positive_prompt",
      "message": "A feature marked not_visible was included as a definite prompt attribute."
    }
  ],
  "warnings": [
    {
      "code": "LOW_CONFIDENCE_FEATURE",
      "path": "features[3]",
      "message": "A low-confidence observation is included in the artist brief."
    }
  ]
}
```

验证器必须区分：

- Error：必须修复。
- Warning：需要人工确认。
- Info：提醒性信息。

# 15. 知识库文件组织与索引策略

## 15.1 设计目标

知识库需要同时支持两种访问方式：

1. Agent 通过自然语言读取 Markdown 专业资料。
2. 工程工具通过 YAML/JSON 查询具体面部特征、描述词和关系。

因此，不建议仅使用 Markdown，也不建议把全部知识都存成大型 JSON。

推荐采用混合式知识库。

## 15.2 文件类型分工

| 文件类型    | 用途                             |
| ----------- | -------------------------------- |
| Markdown    | 专业知识解释、工作流程、使用限制 |
| YAML        | 面部特征、术语、访谈问题和规则   |
| JSON        | 结构化数据、运行时档案           |
| JSON Schema | 数据结构验证                     |
| PDF         | 合法获取的原始标准资料           |
| Python      | 知识库构建、校验与评测           |

## 15.3 知识库主目录

建议完整结构：

```
knowledge/
│
├── ontology/
│   ├── components.yaml
│   ├── facial_features.yaml
│   ├── descriptor_dimensions.yaml
│   ├── descriptors_zh_en.yaml
│   ├── spatial_relations.yaml
│   ├── asymmetry_patterns.yaml
│   └── feature_stability.yaml
│
├── anatomy/
│   ├── facial_regions.yaml
│   ├── facial_landmarks.yaml
│   ├── facial_structures.yaml
│   └── anatomical_terms_zh_en.yaml
│
├── observability/
│   ├── visibility_states.yaml
│   ├── image_quality_factors.yaml
│   ├── viewpoint_requirements.yaml
│   └── confidence_rules.yaml
│
├── interview/
│   ├── interview_stages.yaml
│   ├── question_bank.yaml
│   ├── memory_sources.yaml
│   ├── contamination_controls.yaml
│   └── interview_state_machine.yaml
│
├── prompt/
│   ├── prompt_schema.yaml
│   ├── rendering_rules.yaml
│   ├── negative_constraints.yaml
│   └── model_adapters.yaml
│
└── sources/
    ├── source_manifest.yaml
    ├── source_history.yaml
    └── source_dependencies.yaml
```

## 15.4 特征知识条目标准

每个具体特征必须包含：

| 字段                    | 说明                   |
| ----------------------- | ---------------------- |
| feature_id              | 唯一 ID                |
| canonical_name_en       | 标准英文名             |
| canonical_name_zh       | 标准中文名             |
| synonyms                | 同义词                 |
| parent_component        | 所属组件               |
| anatomical_definition   | 解剖学定义或解释       |
| morphology_description  | 形态描述               |
| descriptor_dimensions   | 适用描述维度           |
| allowed_descriptors     | 允许的描述词           |
| view_requirements       | 适合观察的视角         |
| visibility_requirements | 可见性要求             |
| stability_profile       | 稳定性                 |
| common_confusions       | 容易混淆的特征         |
| prompt_rendering        | Prompt 转换规则        |
| source_refs             | 专业资料来源           |
| related_features        | 相关特征               |
| limitations             | 使用限制               |
| status                  | 标准、项目整理或待核实 |

## 15.5 完整特征条目示例

```
feature_id: F09-15

canonical_name_en: Nasal Tip Shape

canonical_name_zh: 鼻尖形态

parent_component: F09

anatomical_definition: >
  The visible morphology of the distal portion of the nose.

morphology_description: >
  Describes the visible shape and contour of the nasal tip.

descriptor_dimensions:
  - shape
  - size
  - projection
  - rotation
  - symmetry

allowed_descriptors:
  - rounded
  - bulbous
  - pointed
  - broad
  - narrow
  - asymmetric
  - uncertain

view_requirements:
  preferred:
    - frontal
    - profile
    - three_quarter

visibility_requirements:
  minimum_visibility:
    - partial

common_confusions:
  - nasal tip projection versus nasal bridge projection
  - lighting shadow versus actual tip contour

stability_profile:
  short_term: high
  long_term: unknown

prompt_rendering:
  rounded: rounded nasal tip
  bulbous: relatively bulbous nasal tip
  pointed: relatively pointed nasal tip

source_refs:
  - S01

related_features:
  - F09-17
  - F09-18

limitations:
  - Perspective distortion may affect apparent shape.

status: project_curated
```

注意：示例中的稳定性值只是结构演示。Codex 必须根据正式来源核实后才能填写最终值。

## 15.6 索引设计

建议建立以下索引：

- `component_id_index`
- `feature_id_index`
- `descriptor_index`
- `anatomical_term_index`
- `spatial_relation_index`
- `interview_question_index`
- `source_reference_index`

如果 Skill 运行环境支持文件检索，可使用目录和关键词检索。

如果未来需要更大规模的语义检索，可增加本地向量索引。

但第一版不应为了使用向量数据库而增加不必要的基础设施。

本项目目前的知识库规模并不要求复杂数据库。

## 15.7 知识库版本管理

每次修改必须记录：

- 版本号。
- 修改日期。
- 修改文件。
- 修改原因。
- 来源变化。
- 是否改变标准定义。
- 是否影响已有数据结构。
- 是否需要重新运行测试。

建议使用语义版本管理：

- Major：知识模型或核心结构不兼容。
- Minor：增加新特征或知识。
- Patch：修正文字、来源或小型规则。

# 16. AI 图像生成提示词系统

## 16.1 设计目标

提示词编译器的作用是：

将结构化面部特征转换为图像生成模型能够理解的视觉表达，同时最大程度保留用户确认或图像直接观察到的特征。

它不是简单的翻译器。

它需要处理：

- 特征优先级。
- 特征之间的关系。
- 左右不对称。
- 未知信息。
- 图像风格。
- 目标视角。
- 用户的迭代修改。
- 不同图像生成模型的提示词差异。

## 16.2 编译流程

```
FacialProfile
     |
     v
Evidence Filtering
     |
     v
Confidence Filtering
     |
     v
Feature Prioritization
     |
     v
Spatial Relation Compilation
     |
     v
Asymmetry Preservation
     |
     v
Prompt Structure Builder
     |
     v
Model Adapter
     |
     v
Positive Prompt + Negative Prompt
```

## 16.3 信息来源过滤

提示词默认只使用：

- 高可信度直接观察。
- 中等可信度直接观察。
- 用户自由回忆。
- 用户明确确认的描述。

对低可信度信息，可以根据用户意愿决定是否纳入，并且必须保留其不确定性。

以下内容不得作为确定特征进入 Prompt：

- 未确认的 Agent 建议。
- 不可见区域。
- 被遮挡区域。
- 用户明确表示不记得的特征。
- 仅凭光照推测的皮肤或眼睛颜色。
- 从其他面部结构未经验证推断出的特征。

## 16.4 特征优先级

建议采用以下工程优先级：

| 优先级 | 特征类别       | 说明                   |
| ------ | -------------- | ---------------------- |
| P0     | 整体轮廓       | 面部外轮廓和下颌结构   |
| P0     | 空间关系       | 五官相对位置和整体比例 |
| P0     | 独特结构       | 明显不对称和特殊形态   |
| P1     | 眼眉结构       | 眼形、眼睑、眉形       |
| P1     | 鼻部结构       | 鼻梁、鼻尖、鼻翼       |
| P1     | 嘴部结构       | 唇形、嘴宽、嘴角       |
| P1     | 下巴与颧部     | 轮廓和突出程度         |
| P2     | 皮肤与局部标记 | 痣、疤痕、纹路         |
| P2     | 发型和胡须     | 可改变外观             |
| P3     | 光照和背景     | 图像呈现因素           |
| P3     | 艺术风格       | 绘画媒介与视觉效果     |

该优先级是项目工程建议，并非经过统一实验验证的特征重要性排名。

用户明确指出某个特征特别重要时，可以提升其优先级。

## 16.5 通用 Prompt 结构

建议采用以下结构：

```
1. Subject and Framing
2. Head Pose and Camera View
3. Overall Facial Outline
4. Facial Composition
5. Eyebrows and Eyes
6. Nose
7. Mouth and Lips
8. Cheeks, Chin and Jawline
9. Skin and Distinctive Marks
10. Hair and Facial Hair
11. Left-Right Asymmetry
12. Expression
13. Lighting and Background
14. Art Medium and Rendering Style
15. Facial Fidelity Constraints
```

## 16.6 通用正向 Prompt 模板

```
Create a highly faithful facial portrait based strictly on the
following structured facial description.

Preserve the specified facial geometry, relative feature placement,
distinctive details, and left-right asymmetry.

Do not beautify, idealize, normalize, or replace unusual features.

SUBJECT AND FRAMING:
[subject and framing]

HEAD POSE AND CAMERA VIEW:
[viewpoint and pose]

OVERALL FACIAL OUTLINE:
[overall face and head contour]

FACIAL COMPOSITION:
[relative proportions and spatial relationships]

EYEBROWS AND EYES:
[eye and eyebrow details]

NOSE:
[nasal structure]

MOUTH AND LIPS:
[mouth and lip details]

CHEEKS, CHIN AND JAWLINE:
[lower face and cheek structure]

SKIN AND DISTINCTIVE MARKS:
[skin texture and local marks]

HAIR AND FACIAL HAIR:
[hair details]

LEFT-RIGHT ASYMMETRY:
[confirmed asymmetry]

EXPRESSION:
[expression]

LIGHTING AND BACKGROUND:
[lighting and background]

ART MEDIUM:
[rendering style]

FACIAL FIDELITY REQUIREMENTS:
Preserve the described facial structure and distinctive details.
Do not automatically symmetrize or beautify the face.
Do not invent unspecified facial features.
```

## 16.7 通用 Negative Prompt

```
generic idealized face,
standardized facial proportions,
facial symmetry correction,
beautified facial structure,
altered face shape,
enlarged eyes,
narrowed nose,
reshaped lips,
changed jawline,
changed chin shape,
missing distinctive marks,
missing scars,
missing moles,
overly smooth plastic skin,
unrequested makeup,
exaggerated expression,
distorted eye geometry,
unrequested facial accessories,
unrequested hairstyle,
unrequested facial hair,
invented facial features
```

Negative Prompt 只是辅助约束，不代表所有图像生成模型都能够严格遵循。

## 16.8 未知特征的处理

如果某个特征未知：

- 默认不写入正向 Prompt。
- 不应写成一个具体的标准形态。
- 如果模型容易自动补全，可使用“不突出、不强调、不自行添加”的限制表达。
- 对重要但未知的特征，建议先询问用户是否希望补充信息。

例如：

```
The side profile of the nose is not specified.
Do not invent a highly distinctive nasal bridge profile.
```

## 16.9 提示词与 Profile 一致性

Prompt Compiler 必须保证：

1. Prompt 中每个具体面部特征都可以追溯到 Profile。
2. 用户确认的左右差异不能被删除。
3. 未知特征不能被自动补全。
4. 用户修改某项特征时，其他已确认特征不应无故变化。
5. 模型适配器不能改变面部特征的语义。
6. 不同语言的 Prompt 必须保持语义一致。

第六部分结束。

下一部分将提供专业资料来源登记、Codex 下载与提取任务、版权处理、知识库更新机制，以及完整的评测体系。资料来源部分会特别标注哪些资料是官方标准、哪些是研究论文、哪些需要进一步核实访问和许可状态。

# 第七部分：专业资料获取、来源管理与评测体系

# 17. 专业资料来源与知识库构建规范

## 17.1 本章目标

Codex 不应只根据本设计文档中的文字描述建立知识库。

本项目要求 Codex 能够根据明确的来源清单，进一步获取合法公开的专业资料，阅读原始文件，提取知识，并建立可追溯的本地知识库。

因此，本章将资料来源分为：

- 官方专业标准。
- 专业组织指南。
- 解剖学资料。
- 同行评审研究。
- 目击者记忆和认知访谈研究。
- Agent Skill 工程规范。
- 图像生成与评测资料。

每一项资料都必须记录版本、发布日期、来源机构、访问状态、版权情况和知识库用途。

## 17.2 资料来源管理原则

### 原则一：官方来源优先

对于 FISWG、IAI、NIST、OSAC 等组织发布的标准和指南，优先从其官方网站下载。

如果官方网站提供多个版本，必须确认当前版本与历史版本的关系。

### 原则二：研究论文优先使用原始出版来源

对于研究论文，优先使用：

- 出版商官方页面。
- PubMed。
- PubMed Central。
- DOI 页面。
- 作者合法公开的机构仓储版本。

不得使用来源不明的论文转载网站代替正式来源。

### 原则三：版权许可必须独立记录

能够公开阅读不代表能够自由复制和重新分发。

Codex 必须区分：

- 可以下载。
- 可以阅读。
- 可以引用。
- 可以提炼摘要。
- 可以重新分发。
- 可以用于商业产品。

不能将这些权限混为一谈。

### 原则四：来源状态必须可核实

每个来源都需要记录：

- `verified`
- `partially_verified`
- `unavailable`
- `access_restricted`
- `superseded`
- `draft`
- `license_unclear`

不能因为某个链接失效，就静默改用不明来源的文件。

## 17.3 P0：核心官方标准和指南

以下资料是知识库构建的第一优先级。

### S01 — FISWG Morphological Analysis Feature List

标题： Facial Image Comparison Feature List for Morphological Analysis

版本： v2.0

批准日期： 2018-09-11

官方 PDF：

[https://www.fiswg.org/FISWG_Morph_Analysis_Feature_List_v2.0_20180911.pdf](https://www.fiswg.org/FISWG_Morph_Analysis_Feature_List_v2.0_20180911.pdf)

官方文档目录：

[https://www.fiswg.org/documents/](https://www.fiswg.org/documents/)

主要用途：

- 建立 19 个面部组件。
- 建立各组件下的面部特征。
- 统一形态学描述术语。
- 建立结构化特征词汇表。
- 设计面部特征观察顺序。

优先级：P0，必须完整阅读。

Codex 必须从原始 PDF 提取所有 19 个组件及其子特征，不能只根据本设计文档中的摘要构建。

### S02 — FISWG Image Factors

标题： Image Factors to Consider in Facial Image Comparison

版本： v1.0

日期： 2021-05-28

官方 PDF：

[https://fiswg.org/fiswg_image_factors_to_consider_in_facial_img_comparison_v1.0_2021.05.28.pdf](https://fiswg.org/fiswg_image_factors_to_consider_in_facial_img_comparison_v1.0_2021.05.28.pdf)

主要用途：

- 图像分辨率。
- 清晰度。
- 光照。
- 噪声。
- 图像伪影。
- 遮挡。
- 姿态。
- 畸变。
- 图像质量门控。

优先级：P0，必须完整阅读。

### S03 — FISWG Physical Stability

标题： Physical Stability of Facial Features of Adults

版本： v2.0

日期： 2021-05-28

官方 PDF：

[https://fiswg.org/fiswg_physical_stability_of_facial_features_of_adults_v2.0_2021.05.28.pdf](https://fiswg.org/fiswg_physical_stability_of_facial_features_of_adults_v2.0_2021.05.28.pdf)

主要用途：

- 面部特征稳定性。
- 年龄变化。
- 体重变化。
- 健康状态变化。
- 表情影响。
- 人为改变。
- 特征随时间变化的记录。

优先级：P0，必须完整阅读。

### S04 — FISWG Methodology Guidelines

标题： Facial Comparison Overview and Methodology Guidelines

当前已检索到的版本： v2.1

批准日期： 2026-02-26

官方文档目录：

[https://www.fiswg.org/documents/](https://www.fiswg.org/documents/)

用途：

- 面部比较方法学。
- 形态学分析的使用范围。
- 分析与比较过程。
- 图像叠加的限制。
- 记录、复核和不确定性处理。

优先级：P0，必须阅读与本项目相关的章节。

重要要求：

不要直接猜测或拼接 PDF 下载地址。Codex 必须从 FISWG 官方文档目录解析实际下载链接，并确认文档标题、版本和批准日期。

### S05 — FISWG Glossary and Acronyms

标题： FISWG Glossary and Acronyms

当前已检索到的版本： v4.0

批准日期： 2026-06-04

官方文档目录：

[https://www.fiswg.org/documents/](https://www.fiswg.org/documents/)

主要用途：

- 专业术语。
- 英文缩写。
- 面部识别和形态学相关定义。
- 统一专业表达。

优先级：P0。

同样必须从官方目录解析下载地址，确认实际版本。

### S06 — FISWG Practitioner Code of Ethics

官方文档目录：

[https://www.fiswg.org/documents/](https://www.fiswg.org/documents/)

主要用途：

- 专业人员伦理。
- 客观性。
- 记录规范。
- 利益冲突。
- 质量控制。
- 结论表达限制。

优先级：P0。

Codex 必须检查目录中的当前版本，记录版本和日期，不得自行猜测文件名。

### S07 — IAI Forensic Art Guidelines

标题： Standards and Guidelines for Forensic Art and Facial Identification

已发现的资料版本： First Edition

PDF：

[https://theiai.org/docs/ForensicArtGuidelinesSGFAFI1stEd.pdf](https://theiai.org/docs/ForensicArtGuidelinesSGFAFI1stEd.pdf)

组织官网：

[https://theiai.org/](https://theiai.org/)

主要用途：

- 法证艺术实践。
- 画像师专业职责。
- 画像构建流程。
- 认知访谈。
- 目击者与画像师协作。
- 画像材料的使用边界。

优先级：P0。

注意：

该资料版本较早。Codex 必须检查 IAI 官网是否存在更新版本、补充指南或修订文件。

不能直接把早期版本的全部实践建议视为当前所有司法辖区的强制规范。

### S08 — IFSA Minimum Requirements for Facial Identification

组织： International Forensic Strategic Alliance

已发现资料：

[https://www.ifsa-forensics.org/wp-content/uploads/2025/12/IFSA-MRD-Facial-Identification.pdf](https://www.ifsa-forensics.org/wp-content/uploads/2025/12/IFSA-MRD-Facial-Identification.pdf)

用途：

- 专业能力要求。
- 图像采集和质量控制。
- 分析过程。
- 结果解释。
- 报告记录。
- 验证与质量管理。

优先级：P0/P1。

Codex 必须验证该文件的正式标题、版本、发布日期和发布状态。若下载地址失效，应从 IFSA 官方网站检索最新文件。

## 17.4 P1：解剖学和面部形态学研究

### S09 — Anatomy, Head and Neck: Face

来源： NCBI Bookshelf / StatPearls

[https://www.ncbi.nlm.nih.gov/sites/books/NBK551530/](https://www.ncbi.nlm.nih.gov/sites/books/NBK551530/)

用途：

- 面部解剖结构。
- 面部区域。
- 软组织。
- 肌肉。
- 面部骨骼。
- 鼻、眼、口、面颊和下颌结构。

优先级：P1。

### S10 — A Standardized Nomenclature for Craniofacial and Facial Anthropometry

作者： Caple, J. & Stephan, C. N.

年份： 2016

DOI：

[https://doi.org/10.1007/s00414-015-1292-1](https://doi.org/10.1007/s00414-015-1292-1)

PubMed：

[https://pubmed.ncbi.nlm.nih.gov/26662189/](https://pubmed.ncbi.nlm.nih.gov/26662189/)

用途：

- 面部解剖标志点术语。
- 颅面测量术语规范。
- 面部标志点定义。
- 测量和复现性相关知识。

优先级：P1。

特别要求：

本项目主要进行定性面部描述，不应因为该文献涉及人体测量学，就直接引入未经校准的二维照片测量。

### S11 — Anatomical Facial Landmark Reliability

标题： A Preliminary Study of the Reliability of Anatomical Facial Landmarks Used in Facial Comparison

年份： 2019

PubMed：

[https://pubmed.ncbi.nlm.nih.gov/30107642/](https://pubmed.ncbi.nlm.nih.gov/30107642/)

DOI：

[https://doi.org/10.1111/1556-4029.13873](https://doi.org/10.1111/1556-4029.13873)

用途：

- 面部解剖标志点定位。
- 不同观察者之间的差异。
- 图像质量对定位的影响。
- 头部角度对观察结果的影响。

优先级：P1。

## 17.5 P1：刑事摹拟画像与认知访谈研究

### S12 — Forensic Procedures for Facial-Composite Construction

作者： Fodarella et al.

年份： 2015

期刊： Journal of Forensic Practice

DOI：

[https://doi.org/10.1108/JFP-10-2014-0033](https://doi.org/10.1108/JFP-10-2014-0033)

用途：

- 认知访谈。
- 整体认知访谈。
- 画像构建程序。
- 不同画像系统的比较。

优先级：P1。

### S13 — Cognitive Alignment of Interview and Construction Procedure

标题： Constructing identifiable composite faces: The importance of cognitive alignment of interview and construction procedure

PubMed：

[https://pubmed.ncbi.nlm.nih.gov/31763863/](https://pubmed.ncbi.nlm.nih.gov/31763863/)

用途：

- 访谈与画像构建方式的匹配。
- 整体回忆与特征回忆。
- 画像可辨识性。
- 访谈流程设计。

优先级：P1。

### S14 — An Overview of the Latest Developments in Facial Imaging

开放全文：

[https://pmc.ncbi.nlm.nih.gov/articles/PMC6427692/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6427692/)

用途：

- 面部画像技术发展。
- 手绘画像。
- 部件选择式画像系统。
- 整体脸部构建方法。
- 进化式画像系统。

优先级：P1。

### S15 — Configural and Featural Information in Facial-Composite Images

PubMed：

[https://pubmed.ncbi.nlm.nih.gov/24796951/](https://pubmed.ncbi.nlm.nih.gov/24796951/)

DOI：

[https://doi.org/10.1016/j.scijus.2013.11.001](https://doi.org/10.1016/j.scijus.2013.11.001)

用途：

- 整体结构信息。
- 局部特征信息。
- 不同画像构建方式的比较。

优先级：P1。

### S16 — The Value of Whole-Face Procedures for the Construction and Naming of Identifiable Likenesses for Recall-Based Methods of Facial-Composite Construction

年份： 2025

DOI：

[https://doi.org/10.1002/acp.70015](https://doi.org/10.1002/acp.70015)

用途：

- 整体面部回忆。
- 回忆时间。
- 画像构建策略。
- 画像可辨识性。

优先级：P1。

注意：

单篇研究的结论不能直接泛化为所有目击者、所有图像生成模型或所有访谈情境。

### S17 — Eyewitness Memory and Misinformation

标题： Do cognitive abilities reduce eyewitness susceptibility to the misinformation effect? A systematic review

年份： 2024

开放全文：

[https://pmc.ncbi.nlm.nih.gov/articles/PMC11680610/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11680610/)

用途：

- 目击者记忆。
- 事后信息影响。
- 记忆污染。
- 访谈防诱导机制。

优先级：P1。

### S18 — Forensic Facial Comparison: Current Status

期刊： Biology

年份： 2021

文章：

[https://www.mdpi.com/2079-7737/10/12/1269](https://www.mdpi.com/2079-7737/10/12/1269)

用途：

- 法证面部比较研究现状。
- 方法学问题。
- 可靠性和局限性。

优先级：P1。

## 17.6 P1：NIST 与 OSAC 标准体系

### S19 — NIST Facial & Iris Identification Subcommittee

[https://www.nist.gov/adlp/spo/organization-scientific-area-committees-forensic-science/facial-iris-identification](https://www.nist.gov/adlp/spo/organization-scientific-area-committees-forensic-science/facial-iris-identification)

用途：

- 面部识别相关标准目录。
- OSAC 标准状态。
- ASTM 标准。
- 图像采集规范。
- 面部比较方法学。

优先级：P1。

### S20 — OSAC 2022-S-0008

标题： Standard Guide for Facial Image Comparison Documentation

[https://www.nist.gov/standard/906](https://www.nist.gov/standard/906)

用途：

- 分析记录。
- 图像来源。
- 处理过程。
- 适用性判断。
- 方法记录。
- 不确定性。
- 质量保证。

优先级：P1。

重要状态说明：

该文件在已检索资料中标记为 OSAC Proposed Draft Standard / In SDO Development，而不是已经完成全部标准化程序的最终 ANSI/ASTM 标准。

Codex 必须从 NIST 页面重新核实当前状态。

本项目可以借鉴其记录透明性，但不得宣称 Skill 已获得该标准认证。

### S21 — NIST Face Recognition Technology Evaluation

[https://pages.nist.gov/frvt/html/frvt11.html](https://pages.nist.gov/frvt/html/frvt11.html)

用途：

- 人脸识别算法评测。
- 人脸特征表示。
- 算法性能。
- 评测方法。
- 误差和适用性。

优先级：P2。

此资料仅作为自动化评测的背景参考。

人脸识别算法的 embedding similarity 不等同于人工绘画或 AI 图像重建的感知相似度。

## 17.7 P0：Agent Skills 开放规范

### S22 — Agent Skills Official Specification

官方网站：

[https://agentskills.io/](https://agentskills.io/)

规范：

[https://agentskills.io/specification](https://agentskills.io/specification)

GitHub：

[https://github.com/agentskills/agentskills](https://github.com/agentskills/agentskills)

用途：

- `SKILL.md` 格式。
- YAML Frontmatter。
- Skill 目录规范。
- references、scripts 和 assets 的使用。
- 渐进式知识加载。
- Skill 兼容性。

优先级：P0。

Codex 必须按照官方规范实现，而不是仅仅创建一个名为 `SKILL.md` 的普通 Markdown 文件。


### S23 — FISWG Visual Image Manipulation Detection in Facial Images

- 发布版本：Version 1.0。
- 批准日期：2024-11-22。
- 官方发布页面显示发布日期：2025-09-03。
- 官方 PDF：
  [https://fiswg.org/fiswg_visual_image_manipulation_detection_in_facial_images_v1.0_2024.11.22.pdf](https://fiswg.org/fiswg_visual_image_manipulation_detection_in_facial_images_v1.0_2024.11.22.pdf)
- 状态：已发布官方指南。
- 用途：了解面部图像操纵类型、可见检测线索以及遇到可疑图像时的处理考虑。
- 重要边界：文件明确区分一般面部图像从业者与数字图像专家的能力范围。视觉筛查不能替代数字图像专家的数字取证分析；本 Skill 只记录可疑迹象并在必要时建议升级处理。

### S24 — FISWG Quality Management Requirements for Forensic Facial Image Comparison

- 版本：Version 1.0。
- 草案发布页面列出的发布日期：2026-09-01。
- 官方草案目录：
  [https://www.fiswg.org/draft-documents/](https://www.fiswg.org/draft-documents/)
- 状态：**Draft for Comment / 草案，不是已批准的最终标准。**
- 用途：跟踪相邻领域法证面部图像比较的质量管理要求，供项目质量管理设计参考。
- 重要边界：仅可标注为草案参考，不得称为已发布正式标准，不得把草案条款直接表述为本 Skill 的强制专业规范。每次引用必须记录当时检索日期与页面显示状态。

# 18. Codex 资料获取与知识库构建任务

## 18.1 下载目录

建议建立：

```
references/
└── original_sources/
    ├── fiswg/
    ├── iai/
    ├── ifsa/
    ├── nist/
    ├── osac/
    ├── anatomy/
    └── research_papers/
```

原始 PDF 必须与项目自行整理的知识摘要分开。

## 18.2 来源抓取流程

```
Source Registry
      |
      v
Official URL Resolution
      |
      v
HTTP Availability Check
      |
      v
Download or Legal Access
      |
      v
File Integrity Check
      |
      v
SHA-256 Calculation
      |
      v
Metadata Registration
      |
      v
Text Extraction
      |
      v
Knowledge Extraction
      |
      v
Human/Automated Review
      |
      v
Structured Knowledge Base
```

## 18.3 下载要求

每个文件必须记录：

- 来源 ID。
- 标题。
- 机构。
- 版本。
- 发布日期。
- 下载日期。
- 原始 URL。
- 本地文件路径。
- 文件格式。
- SHA-256。
- 许可状态。
- 下载状态。
- 文本解析状态。
- 版本状态。

如果下载失败：

1. 记录失败原因。
2. 检查官方目录是否提供其他下载链接。
3. 检查是否存在合法开放版本。
4. 如果仍然失败，标记 `unavailable`。
5. 在最终报告中列出阻塞来源。

禁止静默跳过。

## 18.4 PDF 解析

Codex 应优先使用适合 PDF 的本地文本提取工具。

推荐工具：

- PyMuPDF。
- pdfplumber。
- pypdf。

不同 PDF 可能包含：

- 普通文本。
- 扫描页面。
- 表格。
- 图片。
- 图示。
- 复杂版式。

如果文本抽取结果不完整，必须检查对应页面图像。

不得只根据 PDF 自动抽取的文字，就假设表格和图示内容已经完整提取。

## 18.5 知识提取

提取时必须区分：

### 原文事实

例如：

FISWG 将某个具体面部结构列为一个标准组件。

### 标准解释

例如：

该组件的特征可以通过多个观察维度进行描述。

### 研究发现

例如：

某项研究发现观察者之间的面部标志点定位可能受到图像质量影响。

### 项目设计建议

例如：

本 Skill 使用 `visibility = partial` 表示部分可见。

这四种内容必须具有不同的来源标签。

## 18.6 知识条目的来源追踪

建议使用：

```
source_refs:
  - source_id: S01
    document_version: "2.0"
    page: 12
    section: "Eyes"
    evidence_type: normative_definition

  - source_id: S09
    page: null
    section: "Facial Anatomy"
    evidence_type: anatomical_reference
```

如果无法确认具体页码或章节，不得编造。

可以暂时填写：

```
page: null
section: "pending_verification"
```

并在来源检查报告中列出。

## 18.7 版权与再分发要求

必须严格执行：

1. 允许公开访问，不代表允许完整复制。
2. 论文摘要可以用于建立索引，但不能将付费论文全文复制到知识库。
3. 允许引用的资料必须保留来源。
4. 不得绕过付费墙或访问控制。
5. 不得将未经许可的人脸图像打包分发。
6. 不得将第三方标准名称作为产品认证或背书。
7. 对允许再分发的 FISWG 文件，必须保留其原始免责声明及相关使用条件。
8. 版本更新时保留旧版本和历史记录。

特别注意 FISWG 文件的再分发条件：

- 保留原始免责声明封面。
- 不得暗示 FISWG 或其贡献者为衍生产品背书。
- 引用时标明版本、日期及文件状态。
- 不得把项目自行编写的内容冒充 FISWG 原文。

# 19. 相似度与质量评测体系

## 19.1 评测目标

评测必须回答四个不同问题：

1. Agent 是否准确提取了图像中的面部特征？
2. Agent 是否能够从用户记忆中收集有效的面部信息？
3. 文本描述是否保留了足够多的目标面部结构信息？
4. 图像生成模型能否根据描述生成相似的面部外观？

不能用一个综合分数替代所有评测。

## 19.2 评测数据集

建议分成三个数据集：

### Dataset A：图像特征提取集

包含获得授权的人脸图像及专业标注。

每个样本应包含：

- 原始图像。
- 视角。
- 图像质量。
- 19 类组件标注。
- 主要特征。
- 左右差异。
- 不可观察特征。
- 专家复核记录。

### Dataset B：认知访谈集

由自愿参与者完成记忆回忆实验。

应记录：

- 目标信息。
- 初始自由回忆。
- Agent 访谈记录。
- 用户确认结果。
- 访谈时间。
- 事后信息接触情况。
- 画像构建结果。

不能将真实案件中的敏感目击者资料直接用于测试集。

### Dataset C：图像重建集

包括：

- 结构化目标特征。
- 人工绘画结果。
- 不同图像模型生成结果。
- 用户迭代修改记录。
- 盲评结果。

必须防止目标图像泄漏到 Prompt 或生成模型的参考输入中。

## 19.3 评测数据分割

建议使用：

```
Dataset
├── Training / Development
├── Validation
└── Test
```

对于本项目而言，重点是避免评测泄漏。

同一目标人物的近似重复照片不能随意分散到不同数据集，导致模型在测试阶段实际上见过同一个人的近似图像。

测试集应尽量使用与开发集不同的目标人物。

## 19.4 图像特征提取指标

### A. Feature Coverage

衡量可观察特征是否被正确覆盖。

\[ Coverage = \frac{\text{正确记录的可观察特征数}} {\text{专家标注的可观察特征总数}} \]

### B. Feature Agreement

衡量 Agent 与专家标注之间的特征一致程度。

可以针对不同特征类型分别计算：

- 形状一致性。
- 相对位置一致性。
- 大小描述一致性。
- 左右差异一致性。

### C. Visibility Accuracy

衡量 Agent 是否正确判断特征可见性。

尤其需要关注：

- 不可见特征是否被误判为可见。
- 遮挡特征是否被错误补全。
- 低分辨率特征是否被过度细化。

### D. Unsupported Inference Rate

衡量 Agent 输出了多少没有证据支持的面部特征。

这是本项目非常重要的指标。

\[ UnsupportedRate = \frac{\text{无证据支持的确定性描述数}} {\text{全部确定性描述数}} \]

应尽量降低。

## 19.5 认知访谈评测

重点指标：

- 自由回忆信息保留率。
- 用户主动回忆特征数量。
- 用户提示后回忆特征数量。
- Agent 建议被误认为原始记忆的比例。
- 用户拒绝或不确定信息的正确处理率。
- 访谈中诱导性问题比例。
- 访谈完成时间。
- 用户主观负担。
- 画像师对访谈结果的可用性评分。

必须单独评估记忆污染风险。

不能以“访谈收集到更多特征”作为唯一成功标准。

更多特征可能来自猜测和暗示，而不是真正可靠的记忆。

## 19.6 人工画像盲评

建议邀请多名独立评审：

- 不知道原图是哪一张。
- 不知道哪个生成模型生成了图像。
- 仅根据目标和重建图进行比较。
- 独立评分。
- 使用统一评分标准。

建议评价维度：

| 维度                 | 评分范围 |
| -------------------- | -------- |
| Overall Face Shape   | 0–10     |
| Facial Composition   | 0–10     |
| Eyes and Eyebrows    | 0–10     |
| Nose                 | 0–10     |
| Mouth                | 0–10     |
| Cheeks and Jawline   | 0–10     |
| Distinctive Marks    | 0–10     |
| Left-Right Asymmetry | 0–10     |

可以采用等权评分作为第一版实验方案，但在正式评测前，应由专业人员审查评分量表是否合理。

## 19.7 自动人脸特征向量评测

可以将人脸 embedding 作为辅助指标，但必须满足：

- 仅使用合法授权图像。
- 明确模型和版本。
- 明确相似度计算方式。
- 记录图像质量。
- 不将其解释为身份确认概率。
- 不用单一 embedding 指标替代人工评测。

本项目不应为了追求高分而将目标人脸直接作为图像生成参考输入，因为那会使“文字描述能否重建人脸”的实验失去意义。

## 19.8 90% 目标的正式定义建议

建议将项目 90% 目标分为三个指标：

### 指标 A：关键特征复现率

针对预先定义的高可见、高置信特征，统计生成结果与目标特征之间的一致性。

研发目标：

\[ KeyFeatureAgreement \geq 90\% \]

### 指标 B：专家盲评得分

使用标准化人工评分量表。

研发目标：

\[ ExpertBlindScore \geq 90/100 \]

### 指标 C：关键不对称保留率

对于目标图像中明确存在、且被系统记录的关键左右不对称特征，检查生成图像是否保留。

研发目标：

\[ AsymmetryRetention \geq 90\% \]

以上三个目标必须在明确的样本、图像质量和评测条件下验证。

不得声称这些指标等同于身份识别准确率，也不得将其宣传为任何输入条件下的保证。

## 19.9 统计报告

评测报告必须记录：

- 样本数量。
- 目标人物数量。
- 图像视角分布。
- 图像质量分布。
- 使用的模型和版本。
- 生成参数。
- 评审人数。
- 平均分。
- 中位数。
- 标准差。
- 置信区间。
- 失败案例。
- 不可评估案例。
- 拒绝率。

不允许只报告表现最好的少数案例。

第七部分结束。

下一部分将进入最后的工程交付内容：隐私与伦理要求、完整 `SKILL.md` 初始实现模板、Codex 开发阶段、自动化测试用例、最终验收清单，以及文档交付后的专业复核流程。

# 第八部分：安全规范、Skill 实现与 Codex 开发计划

# 20. 隐私、伦理与法律边界

## 20.1 项目伦理定位

本项目希望通过更规范、更易获取的面部描述与画像辅助技术，为社会调查、人员搜寻和相关专业工作提供帮助。

但技术能够辅助调查，不代表技术输出自动具有司法证据效力。

必须始终区分：

- 面部外观描述。
- 记忆辅助。
- 合成画像。
- 面部图像比较。
- 身份确认。
- 司法证据。

这些任务具有不同的方法学、专业要求和法律责任。

本 Skill 只承担前面三类工作中的辅助任务，不承担身份确认或司法鉴定。

## 20.2 禁止的推断

系统不得根据面部外观推断：

- 真实身份。
- 是否为某个特定人物。
- 是否是某个犯罪嫌疑人。
- 犯罪倾向。
- 危险程度。
- 人格特征。
- 道德品质。
- 智力水平。
- 国籍。
- 种族或民族。
- 宗教。
- 政治倾向。
- 健康状况。
- 其他无法从面部图像合法、可靠确定的敏感属性。

尤其不得使用所谓“犯罪相貌”“罪犯脸型”等伪科学判断。

## 20.3 图像处理隐私

默认原则：

用户提供的人脸图片仅用于当前任务，不默认建立长期人脸数据库。

具体要求：

1. 不默认持久化原始人脸照片。
2. 不将照片发送给未经用户同意的第三方服务。
3. 不将用户照片用于训练模型。
4. 不建立跨任务身份追踪。
5. 不进行反向搜人。
6. 不将照片上传到未经授权的外部图像服务。
7. 如果需要长期保存，必须单独告知用户并取得明确同意。
8. 应提供删除相关数据的方式。
9. 日志默认不保存完整人脸图像。
10. 测试数据必须获得合法使用授权。

## 20.4 真实刑事案件场景

如果用户说明正在处理真实案件，系统应：

- 明确说明这是辅助性工具。
- 不输出身份确认结论。
- 不将生成图描述为已确认嫌疑人肖像。
- 不建议仅凭 AI 图像开展指认。
- 建议由受过专业训练的法证画像师参与。
- 建议遵循适用司法辖区的正式证人访谈和证据管理程序。
- 保留原始访谈记录、图像来源和修改过程。
- 明确记录 AI 参与的环节。

## 20.5 公开传播风险

如果用户准备在社交媒体、新闻媒体或公共渠道发布画像：

必须提醒：

- 画像可能存在错误。
- 画像不是身份确认结果。
- 不应鼓励公众根据画像自行指认某个具体人物。
- 不应将未经确认的特征作为确定事实传播。
- 应避免造成对无关人员的错误怀疑。

# 21. Skill 文件规范与运行协议

## 21.1 Agent Skills 标准

本项目采用 Agent Skills 开放规范。

官方地址：

[https://agentskills.io/specification](https://agentskills.io/specification)

Codex 必须首先阅读当前规范，并按照其要求实现 Skill。

尤其需要检查：

- `SKILL.md` 文件格式。
- YAML Frontmatter。
- `name` 和 `description` 字段。
- Skill 名称限制。
- 资源文件组织。
- 渐进式知识加载。
- 文件引用方式。
- Skill 运行时的可移植性。

## 21.2 SKILL.md Frontmatter

建议初始内容：

```
---
name: forensic-facial-composite
description: >
  Provides structured, non-identifying descriptions of visible facial
  appearance from user-provided images and conducts non-leading,
  memory-based interviews to prepare facial composite briefs and
  image-generation prompts. Use when a user asks to describe visible
  facial features or reconstruct a face from their own recollection.
  This skill does not identify people, confirm identities, or provide
  forensic conclusions.
---
```

注意：

- `name` 必须与目录名称一致。
- `description` 应明确适用场景。
- 不要把全部知识内容放在 Frontmatter 中。
- 如果官方规范有额外字段要求，以官方规范为准。

## 21.3 SKILL.md 正文模板

建议采用以下结构：

```
# Forensic Facial Composite Skill

## Purpose

This skill provides structured facial appearance description
and memory-based composite assistance.

It does not perform identity recognition or forensic identification.

## Task Routing

Determine whether the user requests:

1. Image-to-Description
2. Memory-to-Composite

Do not combine the two workflows unless explicitly requested.

## Global Rules

- Never infer identity.
- Never infer criminality or personality.
- Never invent invisible facial features.
- Preserve uncertainty.
- Preserve left-right asymmetry.
- Keep original memory separate from agent suggestions.
- Do not treat generated images as evidence.

## Workflow A: Image-to-Description

1. Check user authorization and task scope.
2. Read references/00-scope-and-ethics.md.
3. Read references/07-image-quality.md.
4. Read references/03-fiswg-feature-taxonomy.md.
5. Read references/05-facial-spatial-relations.md.
6. Assess image quality.
7. Analyze visible facial components.
8. Record observations in the FacialProfile schema.
9. Validate the profile.
10. Generate artist brief and image prompt.
11. Explain limitations.

## Workflow B: Memory-to-Composite

1. Explain the interview purpose.
2. Check possible memory contamination.
3. Conduct free recall first.
4. Follow the cognitive interview protocol.
5. Use non-leading questions.
6. Record each memory source.
7. Preserve uncertainty.
8. Review the structured profile with the user.
9. Validate the profile.
10. Generate artist brief and image prompt.

## Output Requirements

Always distinguish:

- Direct observation
- User free recall
- User cued recall
- User-confirmed information
- Agent suggestion
- Unknown information

Never convert an unknown feature into a definite facial attribute.

## Knowledge Loading

Load only the references required for the current task.

## Validation

Validate structured output against the JSON schemas
before generating the final report.
```

## 21.4 运行时行为

### 用户只上传图片

默认进入 Image-to-Description。

### 用户只要求根据记忆画脸

默认进入 Memory-to-Composite。

### 用户同时提供图片和记忆

必须先确认两类信息的用途：

- 图片是否用于辅助理解？
- 图片是否为目标人物的真实参考？
- 用户是否希望将图片与记忆进行对照？

不能自动将图片内容混入用户的原始记忆。

### 用户只要求生成 Prompt

如果没有结构化 Profile，Agent 应先确认已有信息是否足够。

不能凭空生成一张标准化人脸，再声称它是用户记忆的还原。

### 用户要求修改生成结果

必须优先修改对应特征字段，不能每次重新生成整套描述。

# 22. Codex 分阶段开发任务

## Phase 0：规范与项目初始化

任务：

1. 阅读 Agent Skills 官方规范。
2. 创建项目目录。
3. 建立 `SKILL.md`。
4. 建立 README。
5. 建立来源登记文件。
6. 建立版本管理。
7. 确定 Python 版本和依赖管理方式。

验收：

- Skill 能被支持 Agent Skills 的环境识别。
- 目录结构正确。
- Frontmatter 合法。
- references 能被正确引用。

## Phase 1：专业资料获取

任务：

1. 获取 FISWG 官方文档目录。
2. 解析相关标准的实际下载地址。
3. 获取 19 组件标准。
4. 获取图像质量指南。
5. 获取成人面部特征稳定性指南。
6. 获取当前方法学指南。
7. 获取当前 Glossary。
8. 获取 IAI 法证艺术指南。
9. 获取 IFSA 相关指南。
10. 登记 NIST/OSAC 资料。
11. 获取合法公开的解剖学资料和研究论文。

验收：

- 所有来源均有唯一 ID。
- 文件具有 SHA-256。
- 版本与日期已登记。
- 版权和使用状态已登记。
- 下载失败有记录。
- 不存在来源不明的替代文件。

## Phase 2：面部知识本体

任务：

1. 建立 19 个组件。
2. 提取所有下属特征。
3. 建立中英双语词典。
4. 建立特征描述维度。
5. 建立解剖学术语。
6. 建立空间关系。
7. 建立左右不对称性。
8. 建立稳定性元数据。
9. 建立可观察性规则。
10. 建立来源引用。

验收：

- 19 类组件全部存在。
- 每类都有具体特征。
- 每项特征都有合法 ID。
- 每项特征都能追溯来源。
- 中英文表达一致。
- 未知和不适用状态均可表达。

## Phase 3：数据结构和验证

任务：

1. 建立 `FacialProfile`。
2. 建立 Feature Observation Schema。
3. 建立 Image Quality Schema。
4. 建立 Interview Schema。
5. 建立 Spatial Relation Schema。
6. 建立 Asymmetry Schema。
7. 建立 Prompt Output Schema。
8. 实现 Python 校验器。
9. 实现来源引用校验。
10. 实现未知信息保护。

验收：

- 所有 JSON Schema 能通过标准验证。
- 非法字段能够被识别。
- 不可见特征不能被当成确定观察。
- Agent 建议不能自动变成用户确认。
- 左右信息不会被错误合并。

## Phase 4：图片逆向描述

任务：

1. 实现图片质量门控。
2. 实现视角分析。
3. 实现整体结构观察。
4. 实现 19 组件观察。
5. 实现空间关系分析。
6. 实现左右不对称分析。
7. 实现置信度和可见性记录。
8. 实现一致性检查。
9. 实现自然语言报告。
10. 实现绘画师简报。

验收：

- 能处理正面、斜面和侧面图像。
- 能正确处理部分遮挡。
- 能对低质量图像降低分析范围。
- 不会补全不可见区域。
- 能保留特殊结构和左右差异。

## Phase 5：认知访谈

任务：

1. 实现访谈状态机。
2. 实现自由回忆。
3. 实现情境回忆。
4. 实现整体面部回忆。
5. 实现 19 组件问题库。
6. 实现非诱导式追问。
7. 实现记忆来源记录。
8. 实现用户置信度。
9. 实现访谈摘要复核。
10. 实现用户修改历史。

验收：

- 自由回忆必须先于候选特征展示。
- 用户可以跳过问题。
- 用户不确定时不能强迫选择。
- Agent 建议不能进入原始记忆记录。
- 用户修改记录完整保留。

## Phase 6：Prompt Compiler

任务：

1. 实现 Profile 到 Prompt 的转换。
2. 实现特征优先级。
3. 实现空间关系转换。
4. 实现不对称性保留。
5. 实现未知特征过滤。
6. 实现 Negative Prompt。
7. 实现模型适配器。
8. 实现局部修订。
9. 实现 Prompt/Profile 一致性检查。

验收：

- Prompt 不会出现 Profile 中不存在的确定性特征。
- 左右不对称性得到保留。
- 未知特征不会被自动补全。
- 修改单项特征不会无故修改其他已确认特征。

## Phase 7：评测系统

任务：

1. 建立测试数据结构。
2. 建立专家标注模板。
3. 建立盲评模板。
4. 建立组件一致性评估。
5. 建立可见性准确率评估。
6. 建立未知信息处理评估。
7. 建立访谈诱导风险评估。
8. 建立提示词保真度评估。
9. 建立自动报告。
10. 建立模型版本对比。

验收：

- 能够重复运行评测。
- 结果可以追溯。
- 评测数据无信息泄漏。
- 不只报告成功案例。
- 90% 目标有明确指标定义。

## Phase 8：最终整合

任务：

1. 完成 Skill 安装测试。
2. 完成不同 Agent 环境测试。
3. 完成知识库完整性测试。
4. 完成端到端测试。
5. 完成隐私检查。
6. 完成版权检查。
7. 完成 README。
8. 完成使用说明。
9. 完成版本发布说明。

验收：

所有核心功能均有测试记录，所有关键知识均有来源，所有输出均能通过结构化验证。

# 23. 自动化测试用例

## 23.1 图片分析测试

| ID      | 测试场景     | 预期行为               |
| ------- | ------------ | ---------------------- |
| IMG-001 | 正面高清人脸 | 完整分析可见组件       |
| IMG-002 | 三分之四侧脸 | 标记视角限制           |
| IMG-003 | 完全侧脸     | 不臆测正面不可见结构   |
| IMG-004 | 低分辨率图片 | 降低细节描述           |
| IMG-005 | 眼镜遮挡     | 正确标记眼部遮挡       |
| IMG-006 | 刘海遮挡     | 不补全眉毛和额头       |
| IMG-007 | 口罩遮挡     | 不描述不可见嘴部       |
| IMG-008 | 强烈侧光     | 标记光照限制           |
| IMG-009 | 自拍广角     | 提示透视失真风险       |
| IMG-010 | 镜像图片     | 不错误转换左右侧       |
| IMG-011 | 明显不对称   | 分别记录左右差异       |
| IMG-012 | 特殊痣或疤痕 | 记录位置和形态         |
| IMG-013 | 胡须遮挡下颌 | 标记下颌线不可充分观察 |
| IMG-014 | 表情夸张     | 区分动态与相对稳定结构 |
| IMG-015 | 图像经过美颜 | 标记可能存在外观改变   |

## 23.2 访谈测试

| ID      | 测试场景                    | 预期行为           |
| ------- | --------------------------- | ------------------ |
| INT-001 | 用户只能记得整体印象        | 不强迫描述局部     |
| INT-002 | 用户不记得眼睛              | 标记 Unknown       |
| INT-003 | 用户不确定鼻形              | 保留低置信度       |
| INT-004 | 用户自由回忆                | 不提前提供候选选项 |
| INT-005 | 用户看过他人画像            | 记录污染风险       |
| INT-006 | 用户受到暗示后改口          | 保留修改历史       |
| INT-007 | 用户拒绝某项问题            | 允许跳过           |
| INT-008 | 用户只记得特殊标记          | 优先细化该标记     |
| INT-009 | 用户要求提前结束            | 正常生成已有资料   |
| INT-010 | 用户将 Agent 建议误认为记忆 | 明确区分来源       |

## 23.3 数据验证测试

| ID      | 测试场景                       | 预期结果 |
| ------- | ------------------------------ | -------- |
| VAL-001 | 缺少组件 ID                    | Error    |
| VAL-002 | 特征 ID 与组件不匹配           | Error    |
| VAL-003 | 不可见特征被写入确定 Prompt    | Error    |
| VAL-004 | Agent 建议自动标记用户确认     | Error    |
| VAL-005 | 未知特征被自动补全             | Error    |
| VAL-006 | 左右侧没有参照依据             | Warning  |
| VAL-007 | 引用了不存在的来源 ID          | Error    |
| VAL-008 | 置信度没有校准却展示概率       | Error    |
| VAL-009 | 同一特征存在无法解释的逻辑冲突 | Warning  |
| VAL-010 | 用户修改记录缺失               | Error    |

## 23.4 Prompt 测试

| ID      | 测试场景         | 预期结果               |
| ------- | ---------------- | ---------------------- |
| PRM-001 | 完整结构化档案   | 正常生成 Prompt        |
| PRM-002 | 部分特征未知     | 不补全未知特征         |
| PRM-003 | 存在明显左右差异 | 保留不对称             |
| PRM-004 | 用户修改鼻部     | 仅更新鼻部相关描述     |
| PRM-005 | 用户修改脸型     | 更新整体结构及相关关系 |
| PRM-006 | 用户删除某项特征 | 不再出现在 Prompt      |
| PRM-007 | 低置信度特征     | 不作为确定属性         |
| PRM-008 | 模型适配         | 不改变特征语义         |

## 23.5 回归测试

每次修改知识库、Prompt Compiler 或访谈流程后，都必须运行完整回归测试。

不能因为增加了一个新的形态词汇，就导致原本正确的左右特征记录失效。

第八部分结束。

下一部分是最终交付章节：Codex 最终应交付的全部文件、项目验收标准、资料更新策略、开发阻塞处理机制，以及最终专业审查清单。

# 第九部分：最终交付、验收与长期维护

# 24. 最终工程交付物

Codex 最终必须交付一个完整的、可以独立安装和使用的 Agent Skill。

不能以创建 `SKILL.md` 文件作为项目完成标准。

## 24.1 必须交付的文件

| 编号 | 交付物               | 要求                          |
| ---- | -------------------- | ----------------------------- |
| D01  | SKILL.md             | 符合 Agent Skills 官方规范    |
| D02  | README.md            | 安装、配置、使用和限制说明    |
| D03  | CHANGELOG.md         | 版本变化记录                  |
| D04  | 19 组件知识库        | 完整结构化定义                |
| D05  | 中英双语术语库       | 标准术语与形态描述            |
| D06  | 空间关系知识库       | 五官相对位置和比例            |
| D07  | 不对称性知识库       | 左右结构差异                  |
| D08  | 特征稳定性知识库     | 时间和状态变化                |
| D09  | 图像质量知识库       | 图像质量与可观察性            |
| D10  | 认知访谈知识库       | CI/H-CI 方法和问题库          |
| D11  | 记忆污染控制规则     | 访谈来源与诱导防护            |
| D12  | FacialProfile Schema | 统一数据结构                  |
| D13  | Prompt Compiler      | 结构化描述转提示词            |
| D14  | 模型适配器           | 不同图像生成模型适配          |
| D15  | 自动化验证工具       | JSON、知识库和来源验证        |
| D16  | 评测工具             | 组件、访谈、Prompt 和盲评指标 |
| D17  | Source Manifest      | 全部专业来源和版权状态        |
| D18  | 测试用例             | 自动化测试与人工测试          |
| D19  | 使用示例             | 两种模式的完整示例            |
| D20  | 专业限制说明         | 伦理、隐私、法律和方法学边界  |

## 24.2 最终项目目录

```
forensic-facial-composite/
│
├── SKILL.md
├── README.md
├── LICENSE
├── CHANGELOG.md
│
├── references/
│   ├── original_sources/
│   │   ├── fiswg/
│   │   ├── iai/
│   │   ├── ifsa/
│   │   ├── nist/
│   │   ├── osac/
│   │   ├── anatomy/
│   │   └── research_papers/
│   │
│   ├── 00-scope-and-ethics.md
│   ├── 01-professional-standards.md
│   ├── 02-facial-anatomy.md
│   ├── 03-fiswg-feature-taxonomy.md
│   ├── 04-facial-morphology-lexicon.md
│   ├── 05-facial-spatial-relations.md
│   ├── 06-facial-asymmetry.md
│   ├── 07-image-quality.md
│   ├── 08-feature-stability.md
│   ├── 09-cognitive-interview.md
│   ├── 10-memory-contamination.md
│   ├── 11-image-analysis-workflow.md
│   ├── 12-memory-interview-workflow.md
│   ├── 13-prompt-engineering.md
│   ├── 14-quality-assurance.md
│   └── 15-source-register.md
│
├── knowledge/
│   ├── ontology/
│   ├── anatomy/
│   ├── observability/
│   ├── interview/
│   ├── prompt/
│   └── sources/
│
├── schemas/
│   ├── facial_profile.schema.json
│   ├── feature_observation.schema.json
│   ├── image_quality.schema.json
│   ├── interview_record.schema.json
│   ├── spatial_relation.schema.json
│   ├── asymmetry.schema.json
│   ├── prompt_output.schema.json
│   └── source_metadata.schema.json
│
├── templates/
│   ├── image_analysis_report.md
│   ├── facial_profile_report.md
│   ├── artist_brief.md
│   ├── interview_summary.md
│   ├── prompt_output.md
│   └── quality_review.md
│
├── prompt_adapters/
│   ├── generic.md
│   ├── midjourney.md
│   ├── stable-diffusion.md
│   ├── flux.md
│   └── other-models.md
│
├── scripts/
│   ├── fetch_sources.py
│   ├── extract_pdf_text.py
│   ├── build_knowledge_index.py
│   ├── validate_knowledge_base.py
│   ├── validate_profile.py
│   └── run_evaluation.py
│
└── tests/
    ├── test_feature_coverage.py
    ├── test_visibility_handling.py
    ├── test_uncertainty.py
    ├── test_left_right_consistency.py
    ├── test_memory_contamination.py
    ├── test_prompt_consistency.py
    └── fixtures/
```

# 25. 项目验收标准

项目验收分为五个阶段。

## 25.1 知识库验收

必须通过

- 完整覆盖 FISWG 19 个面部组件。
- 每个组件均有细分特征。
- 每个特征都有唯一 ID。
- 每个特征都有适用的描述维度。
- 中英文术语能够对应。
- 建立空间关系知识库。
- 建立左右不对称性知识库。
- 建立图像质量知识库。
- 建立稳定性知识库。
- 专业来源可以追溯。
- 标准内容与项目自定义内容明确区分。
- 版权和再分发状态明确。

## 25.2 图片分析验收

- 能够识别图像整体质量限制。
- 能够按 19 个组件进行系统分析。
- 能够区分可见、部分可见和不可见特征。
- 能够记录左右差异。
- 能够描述五官空间关系。
- 能够识别图像造成的潜在失真。
- 能够保留不确定性。
- 能够输出完整结构化档案。
- 能够输出人工绘画师简报。
- 能够生成图像提示词。
- 不会将不可观察信息写成确定事实。

## 25.3 认知访谈验收

- 先自由回忆，再结构化提问。
- 使用开放式非诱导问题。
- 记录信息来源。
- 记录用户主观置信度。
- 允许用户跳过问题。
- 允许用户修改和撤回回答。
- 保留原始记忆。
- 记录 Agent 提议和用户确认的区别。
- 能够输出结构化档案。
- 能够输出画像师简报和提示词。

## 25.4 提示词验收

- Prompt 与结构化档案一致。
- 保留面部整体轮廓。
- 保留五官相对关系。
- 保留关键不对称性。
- 保留用户确认的特殊标记。
- 不自动美化或标准化。
- 不补全未知特征。
- 支持模型适配。
- 支持局部修订。

## 25.5 工程验收

- Skill 能被目标 Agent 环境识别。
- 目录结构符合官方规范。
- 知识文件能够正确加载。
- JSON Schema 验证通过。
- 自动化测试通过。
- 来源检查通过。
- 评测报告能够生成。
- README 完整。
- 安装流程经过实际测试。
- 不依赖未经授权的外部数据。

# 26. 版本维护与知识更新

## 26.1 维护原则

专业标准和研究会持续更新。

知识库不能在第一次构建后就永久固定。

建议采用：

- 标准更新时检查。
- 新研究发表时评估。
- 术语冲突时复核。
- 专家反馈时修订。
- 每次修改运行回归测试。

## 26.2 来源更新机制

建议至少每六个月检查一次核心官方资料。

重点检查：

- FISWG 官方文档目录。
- IAI 官方指南。
- IFSA 相关要求。
- NIST/OSAC 标准状态。
- Agent Skills 官方规范。

注意：

检查频率属于项目维护建议，并非专业组织要求。

## 26.3 标准版本变化

当某项标准发布新版本时：

1. 下载新版本。
2. 保留旧版本。
3. 对比内容。
4. 标记被替代的条目。
5. 检查知识库字段是否需要调整。
6. 更新来源登记。
7. 更新相关 references。
8. 运行回归测试。
9. 在 CHANGELOG 中记录变化。

不能直接覆盖旧版 PDF 或删除旧版本的来源记录。

# 27. 开发过程中的阻塞处理机制

本项目有大量专业知识和外部资料，Codex 不应在遇到不确定问题时自行编造答案。

以下情况必须记录为阻塞或待确认事项：

### 资料问题

- 官方链接失效。
- 资料无法合法获取。
- 版本无法确认。
- 版权许可不清楚。
- PDF 无法完整解析。
- 研究论文存在相互矛盾的结论。

### 专业问题

- 术语无法确认。
- 两个标准对同一概念的定义不同。
- 特征分类边界不清。
- 稳定性无法确定。
- 观察条件不足。
- 研究结论不能直接适用于本项目。

### 工程问题

- 目标 Agent 不支持图像输入。
- 无法加载外部 references。
- 模型不支持结构化输出。
- 图像生成模型无法保留左右差异。
- JSON Schema 无法覆盖某项业务约束。
- 自动化评测存在信息泄漏。

## 27.1 阻塞报告格式

Codex 遇到无法独立解决的问题时，应输出：

```
# Development Blocker Report

## Blocker ID

BLOCK-001

## Category

Professional Knowledge / Source / Engineering / Evaluation

## Description

具体问题。

## Work Completed

已经完成的工作。

## Evidence

相关来源、代码、测试结果或实验记录。

## Impact

对项目的影响。

## Attempted Solutions

已经尝试的解决方案。

## Remaining Uncertainty

尚未解决的部分。

## Required User Decision

需要用户决定的问题。

## Independent Work That Can Continue

不依赖该问题、仍可继续推进的任务。
```

## 27.2 必须保留工作成果

遇到阻塞时：

- 不删除已经建立的知识文件。
- 不覆盖原始资料。
- 不丢弃已完成的测试。
- 不用未经验证的假设替代正式定义。
- 不因为一个来源无法获取而停止其他独立任务。

这是本项目的重要工程要求。

# 28. 项目开发优先级与范围控制

本项目的长期方向比较完整，但第一版必须控制工程范围。

建议分成两个阶段。

## 28.1 第一阶段：专业 Skill MVP

必须完成：

1. 19 类面部特征知识库。
2. 中英术语体系。
3. 图像质量门控。
4. 图片逆向描述工作流。
5. 基础认知访谈。
6. 统一 FacialProfile。
7. Prompt Compiler。
8. 基础质量验证。
9. 来源登记。
10. 自动化测试。

暂不要求：

- 自己训练视觉模型。
- 自己训练图像生成模型。
- 自己构建人脸识别网络。
- 建立大型人脸数据库。
- 开发独立绘图软件。
- 建立完整的法证鉴定系统。
- 开发复杂的图像标注 GUI。

这些内容可能有价值，但不是第一版 Skill 的必要条件。

## 28.2 第二阶段：专业能力增强

第一版完成并经过实际测试后，再考虑：

- 引入专业画像师反馈。
- 引入结构化人工标注工具。
- 引入多图像联合分析。
- 引入多视角面部结构档案。
- 引入图像生成模型对比。
- 引入 Prompt 自动优化。
- 建立画像复现基准数据集。
- 建立专家评审机制。
- 建立更系统的访谈效果实验。

## 28.3 最重要的范围控制原则

第一版的核心不是实现尽可能多的功能，而是验证以下完整闭环：

```
专业知识
    |
    v
结构化特征提取
    |
    v
可靠的面部描述
    |
    v
绘画提示词生成
    |
    v
图像生成
    |
    v
用户反馈
    |
    v
特征修订
    |
    v
更准确的下一轮生成
```

如果这一闭环不能可靠运行，继续增加模型适配器或复杂功能并不会解决根本问题。

# 29. 最终给 Codex 的完整开发指令

以下内容可以作为交给 Codex 的任务说明。

# Codex Implementation Brief — Forensic Facial Composite Skill

你负责实现 `forensic-facial-composite` Agent Skill。

本项目不是简单的 Prompt 集合，而是一套基于专业面部形态学知识、图像观察规范和认知访谈方法的结构化面部描述与合成画像辅助系统。

## 核心功能

实现两种独立工作模式：

1. Image-to-Description：根据用户提供的面部图像，进行质量检查、面部特征观察、空间关系分析和结构化描述。
2. Memory-to-Composite：通过非诱导性认知访谈收集用户的面部记忆，生成结构化面部档案和绘画提示词。

## 必须遵循的专业依据

优先研究 FISWG、IAI、IFSA、NIST/OSAC 资料以及相关同行评审研究。

必须完整建立 FISWG 19 个面部组件的知识结构。

不得把项目自行制定的工程规则冒充正式专业标准。

## 工程要求

1. 遵循 Agent Skills 官方规范。
2. 使用渐进式知识加载。
3. 建立结构化 YAML/JSON 知识库。
4. 建立统一 FacialProfile 数据模型。
5. 使用 JSON Schema 验证数据。
6. 建立来源登记和版本管理。
7. 建立图像质量门控。
8. 建立非诱导性访谈状态机。
9. 建立 Prompt Compiler。
10. 建立左右不对称性保护机制。
11. 建立未知信息保护机制。
12. 建立自动化测试和评测报告。

## 严格禁止

- 不得推断人物身份。
- 不得根据面部推断犯罪倾向、性格或敏感属性。
- 不得补全不可见特征。
- 不得将 Agent 建议冒充用户原始记忆。
- 不得将 AI 画像作为司法鉴定结论。
- 不得将人脸识别 embedding 分数直接解释为重建相似度。
- 不得未经授权下载或分发人脸数据。
- 不得绕过论文付费墙或版权限制。

## 开发顺序

Phase 0：项目初始化和规范确认。

Phase 1：专业资料获取和来源登记。

Phase 2：19 类面部特征知识库。

Phase 3：统一数据结构和验证器。

Phase 4：图片逆向描述。

Phase 5：认知访谈。

Phase 6：Prompt Compiler 和模型适配。

Phase 7：质量评测。

Phase 8：端到端测试和最终交付。

## 开发纪律

遇到专业定义不清、来源失效、版权不明、实验结论冲突或技术能力不足时，必须保留已完成成果并输出 Blocker Report。

不要用猜测填补专业知识空缺。

不要以完成 SKILL.md 作为项目完成标准。

最终必须交付完整知识库、工作流、Schema、来源清单、自动化测试、评测工具、使用说明和限制说明。

## 项目最终目标

建立一套可解释、可追溯、可验证、可持续扩展的人脸结构描述与画像辅助能力。

90% 相似度属于需要通过独立实验验证的研发目标，不是无条件承诺。

# 30. 项目参考资料快速索引

本索引是第 17 章来源登记表的导航副本，不是第二套来源编号。**S01–S22 的 ID、名称和含义以第 17 章为唯一规范定义；本章必须逐项保持一致。** 新增来源只能使用 S23 及之后的编号。任何数据记录中的 `knowledge_refs` 均引用此处所列的稳定 ID，并由 `source_manifest.yaml` 校验。

| ID | 规范来源名称 | 类型 / 状态 | 用途 |
|---|---|---|---|
| S01 | FISWG Morphological Analysis Feature List v2.0 | 官方指南 | 19 个组件与形态学特征框架 |
| S02 | FISWG Image Factors to Consider in Facial Image Comparison v1.0 | 官方指南 | 图像因素、可观察性限制 |
| S03 | FISWG Physical Stability of Facial Features of Adults v2.0 | 官方指南 | 成人面部特征稳定性与时间变化 |
| S04 | FISWG Facial Comparison Overview and Methodology Guidelines v2.1 | 官方指南 | 面部比较方法学背景；不得误作摹拟画像构建流程 |
| S05 | FISWG Glossary and Acronyms v4.0 | 官方术语文件 | 术语与定义 |
| S06 | FISWG Practitioner Code of Ethics v3.0 | 官方伦理文件 | 专业伦理与客观性 |
| S07 | IAI Forensic Art Guidelines, 1st Edition | 专业指南；历史版本 | 法证艺术与复合画像实践背景，版本时效需核实 |
| S08 | IFSA Minimum Requirements for Facial Identification, Version 1 (September 2025) | 专业组织最低要求 | 相邻领域质量管理参考，不是复合画像标准 |
| S09 | Anatomy, Head and Neck: Face | 解剖学参考 | 面部解剖基础 |
| S10 | A Standardized Nomenclature for Craniofacial and Facial Anthropometry | 同行评审研究 | 解剖标志点与术语 |
| S11 | Anatomical Facial Landmark Reliability | 同行评审研究 | 标志点可靠性与测量限制 |
| S12 | Forensic Procedures for Facial-Composite Construction | 同行评审研究 | 画像构建流程研究 |
| S13 | Cognitive Alignment of Interview and Construction Procedure | 同行评审研究 | 访谈与构建程序匹配 |
| S14 | An Overview of the Latest Developments in Facial Imaging | 同行评审综述 | 面部成像背景 |
| S15 | Configural and Featural Information in Facial-Composite Images | 同行评审研究 | 整体与局部信息 |
| S16 | The Value of Whole-Face Procedures for Recall-Based Facial-Composite Construction | 同行评审研究 | 整体面部回忆方法 |
| S17 | Eyewitness Memory and Misinformation | 同行评审综述 | 目击者记忆与污染风险 |
| S18 | Forensic Facial Comparison: Current Status | 同行评审综述 | 相邻领域背景，不直接作为复合画像操作规范 |
| S19 | NIST Facial & Iris Identification Subcommittee | 官方组织页面 | OSAC / 标准体系背景 |
| S20 | OSAC 2022-S-0008 | OSAC Proposed Draft Standard；状态为 In SDO Development（核验时） | 面部图像比较记录标准状态参考 |
| S21 | NIST Face Recognition Technology Evaluation | 官方评测项目 | 仅作自动人脸识别评测背景，不等同于画像相似度评测 |
| S22 | Agent Skills Official Specification | 开放工程规范 | Skill 文件结构、渐进式加载与验证 |
| S23 | FISWG Visual Image Manipulation Detection in Facial Images v1.0 | 官方指南 | 图像篡改可疑迹象筛查与升级处理 |
| S24 | FISWG Quality Management Requirements for Forensic Facial Image Comparison v1.0 | 2026-09-01 发布的 Draft for Comment 草案 | **草案 / 非最终标准**；仅跟踪，不作为强制规范 |

来源登记的完整 URL、版本、发布日期、批准日期、检索日期、版权与许可字段，以 `source_manifest.yaml` 为准。来源链接应从发布机构官方目录解析，不应因文件名拼写或 URL 路径看似异常而自行改写。

# 31. 最终设计结论

本项目最重要的设计成果，不是一个能够生成漂亮人脸的提示词，而是将专业面部知识、图像观察、记忆提取和图像生成连接成一个可验证的系统。

整个系统应当遵循以下逻辑：

第一，专业知识先于模型。

不能让 LLM 自行决定什么是面部特征、如何分类以及如何描述。模型应使用经过整理和来源追踪的专业知识。

第二，结构化信息先于自然语言。

不能仅依赖一段自由文本保存面部信息。每个特征都必须能够被独立记录、修改、检索和验证。

第三，观察与推断必须分离。

模型不能将不可见的信息补全为事实，不能将自己的建议当成用户记忆，也不能将视觉效果当成确定的解剖结构。

第四，整体结构与局部特征必须结合。

五官单独描述不足以重建人脸。空间关系、左右不对称和特殊标记同样重要。

第五，认知访谈必须尊重记忆。

访谈的目的不是让用户回答更多问题，而是最大程度保留用户真正记得的信息，减少诱导和污染。

第六，图像生成必须服从结构化档案。

Prompt Compiler 不应为了生成更漂亮、更符合常见训练数据的脸，而改变用户确认的面部结构。

第七，项目必须通过实验验证。

90% 相似度是值得追求的研发目标，但只有在明确的测试条件、独立评审和可重复实验中才能得出结论。

最终，希望这项 Skill 能够成为一套可供不同 Agent、专业画像师和图像生成工具共同使用的结构化面部知识与描述能力。

它应当是一个可以长期维护、持续扩展、能够接受专业审查的工程项目，而不是依赖某一个大模型的临时能力展示。


# 32. V1.1 修订条款（规范性补充与冲突优先级）

## 32.1 版本说明、适用范围与优先级

本章记录 V1.1 对 V1.0 的规范性修订。除非另有说明，前 1–31 章的原有知识、流程和设计目标继续有效；本章对同一事项作出更严格或不同规定时，以本章为准。Codex 不得只实现本章而跳过前文，也不得以旧章节中的示例覆盖本章的强制约束。

V1.1 的修订性质分为：

- **规范性修正**：修复会导致错误实现、错误来源归属或数据不可验证的问题。
- **覆盖性补充**：补足原知识词典与权威来源之间尚未显式映射的项目。
- **工程化扩展**：项目为实现追溯、隐私、能力检测和测试而增加的字段或规则；不得冒称 FISWG、IAI、IFSA 或 OSAC 的原文要求。
- **待专业核验项**：当前文档无法仅凭已登记来源证明的细节，必须保持待核验状态，不能由模型补写为“标准规定”。

本项目的“刑事摹拟画像”名称描述其研究领域，不表示该 Skill 已获司法机关、专业协会或标准组织认证。输出只能作为辅助描述、训练、研究或专业人员工作底稿。

## 32.2 P0：来源 ID 的唯一性与来源清单单一事实源

### 32.2.1 不可变 ID 规则

1. 第 17 章中 S01–S22 是 V1.1 的规范来源 ID；其编号和含义不可重新分配。
2. 第 30 章只是第 17 章的导航索引，不得另行定义编号。
3. 新增来源只能分配 S23、S24……，不得回收已废弃 ID，不得因来源版本升级而改变 ID 所指的来源家族。
4. 同一来源的新版本应使用同一来源家族 ID，并通过 `version`、`edition`、`publication_date`、`approval_date` 和 `retrieved_at` 区分；若新文档具有独立范围和独立引用意义，可申请新 ID，并在 manifest 中声明 `supersedes` 或 `related_sources`。
5. 来源状态必须区分 `published`、`draft`、`proposed_draft`、`withdrawn`、`superseded`、`historical`、`unknown`。
6. `source_manifest.yaml` 是唯一可被程序读取的来源 ID 定义文件。Markdown 中的来源表为人工可读镜像，CI 必须检查二者完全一致。

### 32.2.2 Source Manifest 最低字段

```yaml
schema_version: "1.0"
manifest_version: "1.1.0"
updated_at: "YYYY-MM-DD"
sources:
  - id: "S01"
    canonical_title: "FISWG Morphological Analysis Feature List"
    issuing_organization: "FISWG"
    document_version: "2.0"
    document_status: "published"
    publication_date: null
    approval_date: "2018-09-11"
    retrieved_at: "YYYY-MM-DD"
    canonical_url: "https://www.fiswg.org/FISWG_Morph_Analysis_Feature_List_v2.0_20180911.pdf"
    local_path: "sources/official/fiswg/morphological_analysis_v2.0.pdf"
    sha256: null
    source_type: "official_guidance"
    relevance: "primary_feature_taxonomy"
    permitted_use: "reference_and_derived_metadata_only"
    redistribution_status: "check_original_terms"
    supersedes: []
    related_sources: []
    notes: "原始文件不定义比较流程，也不提供限制描述表达的分类系统。"
```

上述日期、哈希或许可未知时必须使用 `null` 或明确的 `unknown`，不得猜测。真实 manifest 必须为 S01–S24 分别填写经核验的记录；示例中的空值不是可交付的最终来源记录。

### 32.2.3 CI 校验

- 所有 `knowledge_refs` 必须存在于 manifest。
- 不得出现重复 ID、同一 ID 多重定义、未登记 URL 或断裂的本地路径。
- Markdown 第 17 章和第 30 章的 ID、标题、版本、状态必须与 manifest 对齐。
- 任何来源变更必须更新 `CHANGELOG.md`，并记录变更原因和影响的知识条目。

## 32.3 P0：FISWG 19 组件覆盖矩阵与项目扩展边界

### 32.3.1 来源解释边界

FISWG Morphological Analysis Feature List v2.0 提供 19 个面部组成部分及两层细节特征清单。该文件本身不定义面部比较流程，也不提供一个强制限制描述词表达方式的分类系统。因此：

- F01–F19 是本项目采用的来源框架。
- 原始文件明确列出的特征项目应标记为 `origin: fiswg_explicit`。
- 为了支持观察、数据验证、提示词编译而增加的字段、子类和枚举，应标记为 `origin: project_extension`。
- 解剖学术语补充应标记 `origin: anatomy_reference` 并指向相应来源。
- 不得把项目自定义的特征细分、评价等级或提示词标签称为 FISWG 官方分类。

### 32.3.2 覆盖矩阵（工程实施最低要求）

以下是 Codex 必须逐项检查并映射到结构化词典的覆盖要求。该矩阵是本项目的追踪清单；其中列出的术语不应被理解为逐字引文。Codex 必须回到 S01 原始 PDF 核对每个条目、层级与英文原词，并在 `knowledge/coverage/fiswg_morphology_coverage.yaml` 中记录页码/条目定位。若原文中不存在某个候选细项，应标记 `not_in_source`，不得为了满足清单而归为 FISWG 明文要求。

| 组件 | 原有词典必须补齐或显式核对的项目 | 实施要求 |
|---|---|---|
| F01 Skin | 皮肤整体外观、可见纹理、色调变化、局部可见皮肤标记；与光照、化妆、图像处理造成的表观差异区分 | 不从肤色推断种族、族裔或健康状况；记录成像色偏 |
| F02 Face/Head Outline | 头颅顶部/颅顶轮廓与面部轮廓分开；正面、侧面轮廓分别记录；面部与头部外轮廓不可混为一个字段 | 明确 viewpoint；不可用单一正面图推断完整侧面轮廓 |
| F03 Face/Head Composition | 面部区域构成与比例；鼻宽相对不同眼距参照；嘴宽相对眼距；鼻宽与嘴宽关系；鼻底至上唇、下唇至颏部等相对距离 | 区分 intercanthal distance、interpupillary distance 与其他眼距；只用定性相对描述，不做未经校准的像素/照片人体测量 |
| F04 Hair | 发际线、头发分布、秃发/稀疏区域的模式与范围、头发长度和方向、可见分区 | 发型是可变外观；记录时间点、遮挡与造型影响 |
| F05 Forehead | 额头高度、宽度、轮廓、倾斜、额部与眉弓/发际线关系 | 与 F02/F03 轮廓和比例字段建立关联，不重复生成矛盾结论 |
| F06 Eyebrows | 眉头/眉峰/眉尾形态；眉尾相对内外眼角的水平及垂直位置；眉毛密度、方向、长度、间断 | 左右侧独立记录；妆容和修眉需标记为可变外观 |
| F07 Eyes | 眼裂形态；内外眦；眼睑上/下缘、突出/凹陷与褶皱；眶下沟/眼袋；巩膜可见血管或明显缺损；虹膜颜色、可见范围、直径/位置；瞳孔形态 | 细节必须满足分辨率与光照要求；不根据虹膜颜色推断身份或族群；眼距指标必须定义参照点 |
| F08 Cheeks | 颧部、面颊软组织轮廓、凹陷/丰满度、左右差异 | 表情、体重与头姿可能改变外观 |
| F09 Nose | 鼻根、鼻梁、鼻尖、鼻翼、鼻孔、鼻小柱、鼻底；鼻尖分叉/形态异常候选项；鼻孔内可见毛发 | 仅描述确实可见细节；不要从正面图推断鼻梁侧面曲率 |
| F10 Ears | 耳廓整体、耳轮/对耳轮、耳甲、耳屏/对耳屏、耳垂；Darwin's tubercle、对耳轮脚、耳轮脚、前方结节/切迹、后耳沟及明显耳部异常候选项 | 遮发时不得补全；结构术语需经解剖来源核验 |
| F11 Mouth | 口裂、唇红、唇峰、唇结节/中线沟/唇纹；上下唇接触或闭合；牙齿可见状态及咬合外观；颌前突/颌后缩等外观候选描述 | 不能由牙齿外观推断牙科诊断；张嘴/说话/表情状态必须记录 |
| F12 Chin/Jawline | 颏部形态、下颌缘、下颌角（gonial angle 的可见轮廓描述）、下颌缘软组织/jowls、颏唇沟 | 侧面与正面观察分开；不以视觉描述代替测量 |
| F13 Neck | 颈部轮廓、颈部可见结构；喉结/喉部隆起的形态、大小和位置（仅在可见且适用时） | 不根据喉部外观推断性别或其他敏感属性 |
| F14 Facial Hair | 胡须/ moustache / sideburns 的位置、密度、边界、长度、方向、缺口、较长毛发、区域连续性 | 区分剃须、修剪、遮挡、阴影与真实毛发生长模式 |
| F15 Facial Lines | 额纹、眉间纹、鼻根纹、上/下睑褶皱、眶下纹、鼻唇沟、口周纹、颏唇沟、颊部皱褶/沟纹等候选项目 | 表情相关纹路须注明表情状态；区分皱纹、阴影和皮肤纹理 |
| F16 Scars | 疤痕/瘢痕的形态、方向、位置、大小的定性范围、颜色/纹理差异 | 不推断成因、年龄或医疗史 |
| F17 Facial Marks | 痣、雀斑、色素点及其他可见局部标记；形状、相对位置、颜色、边界 | 不作医学诊断；图像质量不足时不把压缩噪声当作标记 |
| F18 Alterations | 穿孔、纹身、植入/修饰等可见人为改变；位置、形态、颜色、可见程度 | 不推断个人身份、文化、信仰或生活方式 |
| F19 Other | 无法归入其他组件、但对可见外观有意义的特征 | 必须说明为何不能归入 F01–F18，防止成为无边界的自由推断容器 |

### 32.3.3 特征覆盖追踪文件

每个 FISWG 原始特征项目必须有一条 coverage record：

```yaml
source_id: "S01"
source_version: "2.0"
source_locator:
  page: null
  section: null
  source_label: null
component_id: "F07"
source_feature_label: "待从原始 PDF 核验的原文标签"
coverage_status: "mapped" # mapped | partial | not_in_source | not_applicable | pending_review
project_feature_ids: []
origin: "fiswg_explicit"
reviewed_by: null
reviewed_at: null
notes: ""
```

发布门槛：`mapped`、`not_in_source`、`not_applicable` 必须有来源定位和审查记录；`partial` 与 `pending_review` 必须列入阻塞报告。不得声称“完整覆盖 FISWG”直到覆盖矩阵自动检查通过且由具备相关专业能力的审查者复核。

### 32.3.4 定性观察优先

本项目不实施未经校准的照片人体测量，不把像素距离、模型估算或单张非标准照片中的比例当作精确解剖测量。相对距离只能作为定性视觉关系使用，并须记录参照点、视角、透视风险和可观察性。FISWG 原文对 `distance` 的语境应按相对距离理解，而非精确测量；照片人体测量具有局限，不应被本 Skill 包装成可靠测量工具。

## 32.4 P0：FeatureObservation 数据契约与左右侧语义

### 32.4.1 设计原则

V1.0 的 FeatureObservation 示例包含字段而旧 Schema 未定义这些字段，同时旧 `side` 枚举不能表达“图像左侧/右侧”与“人物解剖学左侧/右侧”之间的不确定性。V1.1 统一采用 `laterality` 对象，并显式分开知识来源、证据来源、确认状态和审计历史。

### 32.4.2 规范对象示例

```json
{
  "schema_version": "1.1.0",
  "observation_id": "OBS-0001",
  "component_id": "F07",
  "feature_id": "F07-EYE-SHAPE-01",
  "feature_name_en": "Eye aperture shape",
  "feature_name_zh": "眼裂形态",
  "viewpoint": "frontal",
  "laterality": {
    "side": "left",
    "reference_frame": "image",
    "mirror_status": "unknown"
  },
  "observation": {
    "value": "almond_like",
    "display_zh": "外观近似杏仁形",
    "display_en": "almond-like in appearance",
    "free_text": "仅为可见外观描述"
  },
  "visibility": "clear",
  "confidence": {
    "level": "medium",
    "value": null,
    "calibrated": false,
    "basis": "边界可见，但轻微头部旋转影响判断"
  },
  "source_type": "direct_visual_observation",
  "confirmation_status": "unconfirmed",
  "knowledge_refs": ["S01", "S02"],
  "evidence_refs": [
    {
      "evidence_id": "IMG-001-REGION-07",
      "evidence_type": "image_region",
      "asset_id": "IMG-001",
      "region": {"x": null, "y": null, "width": null, "height": null},
      "timecode": null
    }
  ],
  "limitations": ["镜像状态未知，不能映射为人物解剖学左侧"]
}
```

上例是数据结构示范，不是对真实人物的观察结论。`value` 应使用项目词典中的枚举或结构；没有可用值时用明确的 `unknown` 状态，不得写入猜测值。

### 32.4.3 Laterality 规范

- `side`: `left`、`right`、`bilateral`、`midline`、`unknown`。
- `reference_frame`: `image`、`anatomical`、`unknown`。
- `mirror_status`: `original`、`mirrored`、`unknown`。
- `viewpoint`: `frontal`、`left_oblique`、`right_oblique`、`left_profile`、`right_profile`、`unknown`、`other`。

`reference_frame=image` 仅表示画面中的左右；不得自动映射为人物解剖学左右。只有镜像状态、拍摄方向和视角有足够证据时，才允许使用 `reference_frame=anatomical`。镜像未知时，左右侧信息必须保留在图像坐标系中。

### 32.4.4 Source Type 与 Confirmation Status 分离

`source_type` 至少支持：

- `direct_visual_observation`
- `user_free_recall`
- `user_cued_recall`
- `user_response_to_neutral_clarification`
- `agent_suggestion`
- `external_reference`
- `expert_review`
- `unknown`

`confirmation_status` 至少支持：

- `unconfirmed`
- `confirmed_by_user`
- `rejected_by_user`
- `revised_by_user`
- `expert_reviewed`
- `not_applicable`

用户确认不改变原始 `source_type`。例如，Agent 从图像提出一项观察，用户确认后，原始来源仍是 `direct_visual_observation`，另记录确认事件。Agent 建议经用户接受，也必须保留 `agent_suggestion` 作为最初来源，并追加用户确认事件；不得覆盖成用户自发回忆。

### 32.4.5 JSON Schema 最低完整约束

Codex 必须创建可执行的 Draft 2020-12 Schema，并使用真实样例运行验证。以下示例为字段契约基线；实现时可拆分 `$defs`，但不得删去其语义约束。

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.invalid/schemas/feature_observation.schema.json",
  "title": "FeatureObservation",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version", "observation_id", "component_id", "feature_id",
    "feature_name_en", "feature_name_zh", "viewpoint", "laterality",
    "observation", "visibility", "confidence", "source_type",
    "confirmation_status", "knowledge_refs", "evidence_refs", "limitations"
  ],
  "properties": {
    "schema_version": {"type": "string", "const": "1.1.0"},
    "observation_id": {"type": "string", "minLength": 1},
    "component_id": {"type": "string", "pattern": "^F(0[1-9]|1[0-9])$"},
    "feature_id": {"type": "string", "minLength": 1},
    "feature_name_en": {"type": "string", "minLength": 1},
    "feature_name_zh": {"type": "string", "minLength": 1},
    "viewpoint": {"enum": ["frontal", "left_oblique", "right_oblique", "left_profile", "right_profile", "unknown", "other"]},
    "laterality": {
      "type": "object", "additionalProperties": false,
      "required": ["side", "reference_frame", "mirror_status"],
      "properties": {
        "side": {"enum": ["left", "right", "bilateral", "midline", "unknown"]},
        "reference_frame": {"enum": ["image", "anatomical", "unknown"]},
        "mirror_status": {"enum": ["original", "mirrored", "unknown"]}
      }
    },
    "observation": {
      "type": "object", "additionalProperties": false,
      "required": ["value", "display_zh", "display_en", "free_text"],
      "properties": {
        "value": {},
        "display_zh": {"type": "string"},
        "display_en": {"type": "string"},
        "free_text": {"type": "string"}
      }
    },
    "visibility": {"enum": ["clear", "partial", "obscured", "not_visible", "not_applicable", "uncertain"]},
    "confidence": {
      "type": "object", "additionalProperties": false,
      "required": ["level", "value", "calibrated", "basis"],
      "properties": {
        "level": {"enum": ["high", "medium", "low", "unknown"]},
        "value": {"type": ["number", "null"], "minimum": 0, "maximum": 1},
        "calibrated": {"type": "boolean"},
        "basis": {"type": "string"}
      }
    },
    "source_type": {"enum": ["direct_visual_observation", "user_free_recall", "user_cued_recall", "user_response_to_neutral_clarification", "agent_suggestion", "external_reference", "expert_review", "unknown"]},
    "confirmation_status": {"enum": ["unconfirmed", "confirmed_by_user", "rejected_by_user", "revised_by_user", "expert_reviewed", "not_applicable"]},
    "knowledge_refs": {"type": "array", "uniqueItems": true, "items": {"type": "string", "pattern": "^S[0-9]{2,}$"}},
    "evidence_refs": {
      "type": "array", "items": {
        "type": "object", "additionalProperties": false,
        "required": ["evidence_id", "evidence_type", "asset_id", "region", "timecode"],
        "properties": {
          "evidence_id": {"type": "string", "minLength": 1},
          "evidence_type": {"enum": ["image_region", "image_frame", "interview_answer", "user_attachment", "expert_note", "other"]},
          "asset_id": {"type": ["string", "null"]},
          "region": {
            "type": ["object", "null"], "additionalProperties": false,
            "required": ["x", "y", "width", "height"],
            "properties": {
              "x": {"type": ["number", "null"]}, "y": {"type": ["number", "null"]},
              "width": {"type": ["number", "null"]}, "height": {"type": ["number", "null"]}
            }
          },
          "timecode": {"type": ["string", "null"]}
        }
      }
    },
    "limitations": {"type": "array", "items": {"type": "string"}},
    "created_at": {"type": ["string", "null"], "format": "date-time"},
    "updated_at": {"type": ["string", "null"], "format": "date-time"}
  },
  "allOf": [
    {
      "if": {"properties": {"laterality": {"properties": {"reference_frame": {"const": "anatomical"}}}}},
      "then": {"properties": {"laterality": {"properties": {"mirror_status": {"enum": ["original", "mirrored"]}}}}}
    }
  ]
}
```

说明：Schema 只能检查结构和部分条件；“不可见特征不得进入确定 Prompt”“用户拒绝后不得继续作为确认特征”等语义规则必须由 Python 业务验证器实现。`format: date-time` 的验证必须在所用 JSON Schema validator 中显式启用。

### 32.4.6 跨字段业务验证

1. `visibility=not_visible` 时，直接视觉观察值不得被当作已观察事实；如保留先前回忆值，应有非图像证据来源并明确区分。
2. `visibility=obscured` 或 `partial` 时，必须记录遮挡/缺失范围；Prompt 不得将未见部分补成确定结构。
3. `source_type=agent_suggestion` 时，初始 `confirmation_status` 必须为 `unconfirmed`；用户确认只能通过追加事件实现。
4. `confirmation_status=rejected_by_user` 的值必须从当前有效 Profile 与 Prompt 中排除，但原始记录保留。
5. `laterality.reference_frame=anatomical` 时，`mirror_status` 不得为 `unknown`；镜像状态未知时只能使用 `image` 或 `unknown` 参考系。
6. `knowledge_refs` 指向专业知识依据；`evidence_refs` 指向本次个案材料。二者不得互换。
7. 任何基于单一视角的推断必须记录 `limitations`；系统不得把未观察视角的特征提升为高置信观察。
8. `confidence.value` 只有在有校准数据和明确校准方法时才能填写数值；否则必须为 `null` 且 `calibrated=false`。`high/medium/low` 是内部排序标签，不是概率。

## 32.5 P1：证据来源、知识来源与修改历史分离

V1.0 的 `evidence_source` 和 `source_refs` 混合了本次观察证据与知识依据，无法回答“这一特征从哪里来、何时被修改、谁确认过”。V1.1 强制分为四层：

1. `knowledge_refs`：用于支持术语、定义、方法和限制的知识来源 ID（如 S01）。
2. `evidence_refs`：指向当前图像区域、视频帧、访谈回答片段或专家记录。
3. `provenance`：描述信息最初由谁/何种方式产生，包含时间、工作流阶段、模型建议标识等。
4. `confirmation_history`：记录确认、拒绝、修订、复核等事件的不可变事件序列。

推荐事件结构：

```json
{
  "event_id": "EVT-0001",
  "event_type": "user_confirmed",
  "target_observation_id": "OBS-0001",
  "actor_type": "user",
  "timestamp": "2026-11-01T12:30:00Z",
  "previous_value": null,
  "new_value": "almond_like",
  "reason": "用户明确确认该描述符合其记忆",
  "source_evidence_refs": ["INT-ANSWER-004"],
  "supersedes_event_id": null
}
```

事件类型至少包括 `created`、`agent_suggested`、`user_confirmed`、`user_rejected`、`user_revised`、`expert_reviewed`、`prompt_compiled`、`prompt_revised`、`interview_reverted`。原始证据和事件不得静默覆盖或删除。用户要求删除时，按第 32.9 节的数据生命周期执行；审计日志不应保留已要求删除的个人数据副本，除非明确披露并存在适用的合法保留义务。

### 32.5.1 记忆访谈的来源类型

必须区分自由回忆、开放式追问后的回忆、针对已提出选项的回答、Agent 提示、外部照片/描述暴露后的信息。系统应记录访谈问题原文、问题类型、问题顺序、回答原文或经同意的摘要、时间戳，以及用户是否在此前接触过其他图片、画像或描述。不得把受提示后的回答重新标记为自由回忆。

### 32.5.2 修改与版本

每次变更产生新的 Profile revision。当前有效值由事件流投影得出；历史 revision 只读。Prompt 必须记录所使用的 `profile_revision` 和 `compiler_version`，以便复现。

## 32.6 P1：Host Capability Adapter 与执行适配器

### 32.6.1 Agent Skills 不等于统一模型 API

Agent Skills 文件规范规定 Skill 的组织和加载方式，不保证宿主 Agent 具备视觉输入、图像生成、文件访问、脚本执行或联网能力，也不规定所有图像模型的统一 API。因此，本项目不得把“存在 prompt adapter”描述为已经支持模型执行。

### 32.6.2 能力检测契约

运行时启动时建立 `HostCapabilities`：

```json
{
  "vision_input": {"available": false, "provider": null, "limits": []},
  "image_generation": {"available": false, "provider": null, "limits": []},
  "file_access": {"available": false, "read": false, "write": false},
  "script_execution": {"available": false, "languages": []},
  "web_access": {"available": false},
  "structured_output": {"available": false, "formats": []},
  "capability_detection_source": "host_declared",
  "checked_at": null
}
```

字段应根据宿主真实声明填写。未知能力必须是 `available=false` 或 `unknown`，不得通过模型自述推断宿主权限。

### 32.6.3 适配器分层

- **Prompt Adapter**：将内部中立 Prompt 表达转换为不同模型可理解的文本/结构格式；不执行调用。
- **Execution Adapter**：实际调用宿主提供的视觉或图像生成工具，负责输入输出协议、超时、错误、重试和模型元数据。
- **Capability Adapter**：读取宿主能力声明并进行运行时能力门控。
- **Validation Adapter**：验证工具返回的结构、Profile 一致性和输出限制。

每个执行适配器至少声明：`adapter_id`、`provider`、`model_id`、`supported_tasks`、`input_schema`、`output_schema`、`supports_reference_images`、`supports_negative_prompt`、`supports_seed`、`known_limitations`、`version`。

### 32.6.4 能力缺失时的降级

- 无视觉能力：不得声称已分析图像；可提供人工观察表或请求用户提供文字描述。
- 无图像生成能力：只能输出绘画师简报或模型无关 Prompt，不得声称已生成图像。
- 无文件访问能力：不得声称已读取本地来源或保存 Profile。
- 无脚本执行能力：不得声称 JSON Schema、CI 或自动化测试已经运行。
- 无 Web 能力：不得声称来源已在线更新核验。

能力降级必须在输出中说明当前完成了什么、未完成什么，以及原因。

## 32.7 P1：图像篡改迹象筛查与专业升级

### 32.7.1 适用依据

增加 FISWG Visual Image Manipulation Detection in Facial Images v1.0（S23）作为图像可疑操纵筛查的参考。其讨论的风险包括特征插入/移除、平滑处理、复制、拼接/变形以及属性操纵等。视觉筛查存在局限，不能仅凭模型对图像的观察认证图像真实性或证明图像未被修改。

### 32.7.2 Skill 可以做什么

- 记录肉眼可见或模型提示的异常线索，如局部纹理突变、重复区域、边缘不连续、异常平滑、局部光照/噪声不一致等。
- 将每个线索绑定到图像区域和观察置信度。
- 使用 `manipulation_screening_status`：`not_assessed`、`no_obvious_visual_signs`、`suspicious_signs_observed`、`inconclusive`。
- 在报告中明确“未观察到明显迹象”不等于“图像真实/未篡改”。
- 对可疑或重要个案建议取得原始文件、来源链与元数据，并转交具备数字图像取证能力的专业人员。

### 32.7.3 Skill 不得做什么

不得：

- 仅凭视觉线索给出“已篡改”“未篡改”的法证结论。
- 将压缩伪影、锐化、低分辨率或生成模型伪影直接定性为恶意篡改。
- 通过本 Skill 声称验证 EXIF、文件哈希、编辑历史或数字签名，除非宿主确实执行了对应工具并保存可复核结果。
- 将疑似篡改区域中的面部特征作为高置信事实。

## 32.8 P1：90% 相似度目标的可复现评测协议

### 32.8.1 目标解释

“≥90%”是研发目标，不是系统保证，不是身份匹配概率，不是证据强度，也不能用单一人脸嵌入相似度替代。正式报告必须同时给出样本量、数据来源、任务类型、评分者、置信区间、缺失值处理和失败案例。

### 32.8.2 预注册关键特征

在查看生成结果前，由独立标注者依据原始参考材料定义 `key_features`。每个关键特征需包括：组件、可观察性、重要性权重、允许的等价描述、左右侧、证据定位和排除条件。不得在看到生成图后回头挑选“容易命中”的特征。

### 32.8.3 Key Feature Agreement

建议按样本计算：

\[
KFA_i = \frac{\sum_{j \in A_i} w_j m_{ij}}{\sum_{j \in A_i} w_j}
\]

其中：

- `A_i` 是在源材料中可评估且预注册的关键特征集合；
- `w_j` 是预先确定的特征权重；
- `m_ij` 为 1（匹配）、0.5（部分匹配）、0（不匹配）；
- 不可评估特征不进入分子或分母，但必须单独报告数量和原因。

不得将生成结果中“看不出来”的特征默认为匹配。除主指标外必须报告未匹配特征和错误新增特征率。

### 32.8.4 Expert Blind Score

- 至少由 3 名具备相关训练/经验且彼此独立的评审者盲评；研究规模允许时增加评审者。
- 评审者不知道模型版本、生成顺序和其他评审者得分。
- 使用固定量表和评分锚点（例如 1–5）；每个分值必须有可操作定义，不能只写“很像/不像”。
- 报告均值、中位数、标准差、评分分布及评审者间一致性；序数评分优先报告加权 Kappa 或适当的 ICC，并说明模型假设。
- 对整体相似度和关键特征忠实度分别评分，避免整体观感掩盖关键差异。

### 32.8.5 Asymmetry Retention

只对源材料中可观察且预先登记的不对称特征计算：

\[
AR_i = \frac{\text{生成结果中正确保留的不对称关键项数}}{\text{源材料中可评估的不对称关键项总数}}
\]

同时报告方向错误、左右镜像错误和不对称被平均化的比例。若分母为 0，结果应为 `not_applicable`，不能记为 100%。

### 32.8.6 记忆访谈独立评测

记忆访谈数据集应采用经伦理审查或适用研究审查的受控方案。至少比较：

- 自由回忆基线；
- 开放式中性追问；
- 结构化但非诱导的后续访谈；
- 用户主动修订与确认过程。

必须记录问题顺序、提示方式、外部信息暴露和访谈时间。评测目标不应是“收集到的字段越多越好”，而应是信息来源准确、诱导率低、用户能区分确定记忆与不确定记忆、关键描述保真。

### 32.8.7 统计报告

- 预先定义主要终点和次要终点。
- 按数据集/身份/目标面孔分组，避免同一目标的近重复图像跨训练和测试集泄漏。
- 报告样本量和缺失数据；小样本不得夸大外推性。
- 置信区间方法应与抽样单位一致；如同一参与者/目标有多张图像，使用按参与者或目标聚类的 bootstrap，而非把所有图片当作独立样本。
- 至少报告均值、中位数、四分位数、95% CI、失败样本、关键错误类型。
- 嵌入向量或自动人脸识别分数仅作为探索性辅助指标；不得解释为身份概率、法证结论或唯一相似度指标。

### 32.8.8 最低样本与停止规则

本项目当前不在没有先导实验和统计功效分析的情况下规定一个虚假的固定样本数。正式评测前必须通过先导研究估计方差、预期效应和可接受误差，再预注册样本量与停止规则。未完成该步骤前，结果只能称为内部探索性测试。

## 32.9 P1：隐私、数据保留与删除生命周期

### 32.9.1 数据类别

至少区分：

- 原始图像/视频及文件元数据；
- 用户访谈原文与记忆内容；
- 结构化 FacialProfile；
- Prompt 与生成结果；
- 审计事件、诊断日志和错误日志；
- 研究评测数据集。

访谈材料可能包含高度敏感的个人经历或案件信息，应采用比普通图像描述更严格的访问和保留策略。

### 32.9.2 默认最小化

- 默认不持久保存原始图像和访谈录音；如任务需要保存，必须先取得明确同意。
- 临时文件必须限定目录、设置清理策略，并在异常退出后提供清理机制。
- 日志默认不记录原始图像、完整访谈文本、可识别面部图像或不必要的个人信息。
- Profile 默认本地/会话内最小化保存；任何云端同步或第三方模型调用必须明确披露。
- 评测数据必须单独获得适当授权，并去标识化；不能把个案材料自动加入训练集。

### 32.9.3 宿主与供应商边界

Skill 无法单方面保证宿主 Agent、模型提供商、文件系统或图像生成服务不会保留输入、日志或生成结果。必须读取宿主/供应商的实际隐私、保留、训练使用和删除政策；无法确认时明确标记 `provider_retention_policy=unknown`，并提示用户不要上传其无权披露或不愿交由第三方处理的材料。不得宣称“完全本地”“零保留”或“绝不用于训练”，除非执行环境和合同条款能证明。

### 32.9.4 用户控制与删除

提供：

- 任务级临时处理；
- 用户主动保存 Profile；
- 导出；
- 删除 Profile、图像缓存、生成图和关联日志；
- 清理后结果回执（说明已清理的本地范围和无法控制的供应商范围）。

删除功能应有 `deletion_scope` 与 `deletion_result` 记录，但不应为了证明删除而永久保留被删除的敏感内容副本。供应商侧删除若不能由 Skill 触发，必须说明用户需通过供应商/宿主渠道执行。

### 32.9.5 真实案件与未成年人

真实案件、证人/受害者资料、未成年人图像或其他高风险材料，必须要求用户确认其处理权限和用途；对不具备合法授权、明显侵犯隐私或存在报复/骚扰风险的请求，应拒绝或停止处理。不得将本 Skill 用于追踪、识别、定位或锁定具体个人。

## 32.10 P1：IFSA、IAI、OSAC 与 FISWG 来源的适用性说明

- **FISWG S01–S06、S23**：是本项目面部形态学、图像因素、稳定性、术语、伦理和可疑操纵筛查的主要官方资料。各文件的适用范围必须分别说明。
- **IAI S07**：现有可访问指南为第一版历史资料；IAI 的 Forensic Art 与 Facial Identification 是不同专业领域/委员会方向。Composite Drawing 属于从证人记忆构建 likeness 的法证艺术实践背景。不得把旧版指南表述为已核实的最新版本，除非再次从 IAI 官方页面确认。
- **IFSA S08**：文件标题为 `Minimum Requirements for Facial Identification, Incorporating both Facial Recognition System use and Facial Image Comparison`，Version 1，September 2025。其面向法证实验室及面部识别/比较能力的最低要求，涵盖人员、设备、图像采集、分析、报告、验证与质量管理。它是相邻领域的质量体系参考，不是复合画像绘制方法标准。
- **OSAC S20**：截至本次版本核验，NIST OSAC 页面显示 2022-S-0008 处于 `In SDO Development` / OSAC Proposed Draft Standard 状态。此状态必须随时间重新核验，不能写成已发布的正式标准。
- **S24**：FISWG Quality Management Requirements for Forensic Facial Image Comparison v1.0 是 2026-09-01 发布的 Draft for Comment 草案材料。只能登记为草案并跟踪，不得作为已批准正式标准或强制要求。

## 32.11 P0：Agent Skills 文件规范与渐进式加载

### 32.11.1 SKILL.md 入口文件

`SKILL.md` 应保持为简洁的入口和任务路由文件。Agent Skills 规范要求 frontmatter 至少包含 `name` 和 `description`，并遵循命名与长度约束。规范建议主 `SKILL.md` 保持在 500 行以内；详细知识应放入 `references/`、`knowledge/` 或其他文件，并由入口文件按任务需要引用。

不得把 6,000 行级别的完整设计文档原样塞入运行时 `SKILL.md`。本设计文档是 Codex 的工程规格；运行时 Skill 是最终交付物，两者应分离。

### 32.11.2 验证工具

CI 至少执行：

```bash
skills-ref validate path/to/forensic-facial-composite
python -m pytest
python scripts/validate_schemas.py
python scripts/validate_knowledge.py
python scripts/validate_sources.py
python scripts/validate_fiswg_coverage.py
```

如官方工具命令或参数发生变化，Codex 必须以当前 Agent Skills 官方规范/工具说明为准更新 CI，不得为了让命令通过而删除验证步骤。将 `skills-ref` 版本固定在开发依赖中，并记录版本号。

### 32.11.3 引用层级

- `SKILL.md` 只引用一层深度的文件路径。
- 被引用的知识文件不得要求 Agent 再递归加载多层不透明路径。
- 按任务加载：图像工作流加载图像质量、F01–F19、空间关系和数据模型；记忆访谈加载认知访谈、污染控制和数据模型；Prompt 编译加载 Prompt 规则、模型能力和一致性验证。
- 每个知识文件必须有 `purpose`、`when_to_load`、`source_refs` 和 `version` 元数据或等效登记。

## 32.12 P1：照片人体测量与比例描述的限制

本 Skill 的核心是定性形态描述与相对空间关系。不得把普通照片中的像素比例、未经校准的标志点坐标或模型估计值转化为精确人体测量。任何测量实验必须另设研究协议，至少要求：相机/镜头和拍摄距离控制、姿态控制、校准参照、标志点定义、误差分析、观察者间可靠性与适用范围说明。未满足时只能使用诸如“视觉上相对较宽/较窄”的定性语言，并记录透视和姿态限制。

## 32.13 P1：项目许可与第三方资料许可

当前项目目录存在 `LICENSE` 文件，但设计阶段没有明确项目代码、项目自编知识内容和第三方来源资料的许可决策。Codex 不得自行选择 MIT、Apache-2.0、GPL 或其他许可作为既定用户意图。

必须将许可分层：

1. 项目代码许可；
2. 项目原创文档/术语/数据结构许可；
3. 第三方论文、标准、PDF、图片和图表的版权/许可；
4. 生成数据与用户提供图像/访谈材料的权利和使用授权。

FISWG 等来源的下载或引用不等于允许重新分发全文。保留原始封面、免责声明、版本与版权信息；遵守原文对复制、修改和标识使用的限制；不得暗示 FISWG 或贡献者认可本项目。对不允许再分发的材料，只保存合法允许的元数据、链接和内部提取笔记。公开发布前必须由用户决定项目代码与原创内容许可，并完成第三方材料审查。

## 32.14 P0：V1.1 验收门槛与阻塞清单

### 必须通过的自动化门槛

- [ ] S01–S24 来源 ID 唯一，章节 17 与 30 完全一致。
- [ ] `source_manifest.yaml` 是来源 ID 唯一事实源，所有来源字段完整或明确标记未知。
- [ ] 所有 FeatureObservation 示例通过 JSON Schema Draft 2020-12 验证。
- [ ] Schema 中定义的字段与数据模型、示例、Prompt Compiler 输入完全一致。
- [ ] Laterality 镜像语义测试通过，未知镜像状态不会被映射为人物解剖学左右。
- [ ] `knowledge_refs` 与 `evidence_refs` 分离，所有引用均可解析。
- [ ] 用户确认、拒绝、修订均追加事件，不静默覆盖原始来源。
- [ ] FISWG 19 组件覆盖矩阵逐项映射或明确标记为不适用/原文不存在/待核验。
- [ ] 删除所有未登记的图像搜索临时链接和孤立数字行。
- [ ] `skills-ref validate` 通过，主 `SKILL.md` 不超过建议行数，知识采用渐进式加载。
- [ ] Capability Adapter 缺失能力时正确降级，不虚构执行结果。
- [ ] 图像操纵筛查只报告可疑迹象，不给出数字取证认证结论。
- [ ] 评测报告包含分母定义、缺失值处理、评审者一致性和置信区间。
- [ ] 隐私策略明确本地/远端处理、缓存、日志、保留、删除和供应商政策边界。
- [ ] 项目许可决策被记录；第三方资料许可单独登记。

### 必须由专业人员复核的门槛

自动化测试不能证明专业内容正确。以下事项必须由具备相应能力的专业人员复核：

- FISWG 原始特征项目与项目词典的逐项映射；
- 解剖学术语、标志点和空间关系定义；
- 认知访谈问题是否存在诱导性；
- 真实案件场景的伦理与法律边界；
- 评测评分锚点、数据集设计和统计方法。

### 不得宣称完成的情形

只要存在来源 ID 冲突、核心 Schema 无法验证、FISWG 覆盖未完成、镜像语义错误、能力虚报、证据追溯缺失或高风险隐私问题，项目不得标记为 V1.1 通过验收。可以交付部分功能，但必须明确标记为 `partial` 并附阻塞报告。

## 32.15 V1.1 变更记录

| 类别 | V1.1 变更 |
|---|---|
| P0 来源管理 | 固定 S01–S22 规范 ID；第 30 章改为第 17 章的镜像索引；新增 S23、S24 |
| P0 数据模型 | 统一 FeatureObservation 示例与 Schema；使用 laterality 对象解决左右侧和镜像语义 |
| P0 特征覆盖 | 新增 FISWG 19 组件覆盖矩阵与逐项追踪要求 |
| P0 文档清理 | 删除临时图像搜索引用、孤立数字和 URL 跟踪参数；更新目录与版本元数据 |
| P1 可追溯性 | 分离知识来源、个案证据、信息来源类型、确认状态和事件历史 |
| P1 能力适配 | 区分 Prompt Adapter、Execution Adapter、Capability Adapter 与 Validation Adapter |
| P1 图像可信度 | 增加视觉篡改迹象筛查及转交数字图像专家的边界 |
| P1 评测 | 正式定义 KFA、盲评、非对称保留、缺失值和统计报告规则 |
| P1 隐私 | 增加数据分类、最小化、保留、删除、供应商披露和高风险场景规则 |
| P1 来源适用性 | 澄清 IFSA、IAI、OSAC 与 FISWG 文件的范围和状态 |
| P1 工程规范 | 增加 Agent Skills 渐进式加载、`skills-ref validate` 和 CI 要求 |
| P1 许可 | 明确项目代码许可与第三方资料许可必须分层决策 |

