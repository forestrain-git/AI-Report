# 操作日志

## [2026-06-10] north-star | 明确项目北星指标与成功标准
- 北星: 制作一个汇报材料，面向中建发展全体员工（领导班子 + 中层 + 基层），让他们都受到震撼、感到有收获、听完以后立马能行动
- 成功标准: 震撼 → 有收获 → 能行动（三层递进，覆盖三层受众）
- 更新文件:
  - [[index.md]] — 顶部新增"项目北星"区块，替换原有项目定位描述
  - [[CLAUDE.md]] — "项目背景"首条替换为北星指标，核心目标重新排序（首要目标明确为汇报材料）

## [2026-06-10] ppt | 重构全球案例融入方式——对照北星优化递进叙事
- 背景: 用户要求对照北星指标（震撼→有收获→能行动），分析全球案例如何纳入PPT大纲
- 核心问题: P12b全球案例是孤立信息页，打断Part 3递进叙事
- 调整方案:
  1. **P6 数据冲击**：新增"全球：整个行业正在被重构"板块（McKinsey数字化指数1.375、RICS采用率1.5%、Eiffage 99%时间节省、Kajima 80%劳动力减少），建立全球紧迫感
  2. **P12b 重构**：删除重复的McKinsey宏观数据（已在P6），精简为3个案例做"震撼锚点"+ 5大对标方向（原6条合并精简），增加演讲备注"不重复宏观数据"
  3. **P30 风险预判**：补充RICS全球调查数据（45%无AI使用、34%早期试点、<1%全组织嵌入），让85%失败率有全球背书
  4. **P34 收尾总结**：第3行更新为"全球+国内+中建"三层证据链
  5. **Part 3 整体**：更新递进逻辑说明（能源央企→建筑央企→国际建筑巨头→中建系→云筑网→中建智能），过渡语同步更新
- 叙事逻辑: 从P6建立全球紧迫感 → P12b用3个案例做震撼锚点 → P30用RICS数据为风险背书 → P34收尾三层证据链，形成完整闭环
- 变更文件: [[ppt/outlines/国企AI宣讲-中高层完整版]]
- 状态: 已完成

## [2026-06-10] ingest | 全球建筑企业AI案例并行搜索与知识库整合
- 背景: 用户要求面向央企总部宣讲必须开阔视野，补充全球建筑企业AI应用案例，要求有说服力且有官方出处
- 搜索方式: 启动 4 个并行子代理（web-access skill + WebSearch/WebFetch）
- 搜索维度:
  - Agent #1 欧洲建筑巨头 → 完成（Vinci/Skanska/Bouygues/ACS/Hochtief/STRABAG/Ferrovial/Eiffage 7家企业）
  - Agent #2 北美建筑企业 → 完成（AECOM/Bechtel/Turner/DPR/Autodesk 5家企业）
  - Agent #3 亚太建筑企业 → 完成（大成/竹中/清水/大林/鹿岛/三星/现代/Lendlease/Woh Hup 9家企业）
  - Agent #4 全球趋势与权威报告 → 完成（McKinsey/PwC/Deloitte/Autodesk/Dodge/RICS/WEF 7份报告）
- 关键发现:
  - McKinsey: 建筑业数字化指数1.375，全球倒数第二，仅高于农业
  - Eiffage: RFP分析2天→20分钟（节省99%），2,500+员工完成强制AI培训
  - Kajima: A4CSEL全自动大坝施工，劳动力减少80%，效率提升3.1倍，零事故
  - Bouygues: HS2项目10分钟生成600万种调度方案，节省4个月
  - Taisei: ChatGPT Enterprise 90%周活跃率，每周节省5.5小时/员工
  - Turner: CraneView智能起重机，周期-30%，安装时间-50%
  - STRABAG: DARIA风险预测，11,000项目训练，80%准确率
  - 全球建筑业AI采用率仅1.5%，但56%高管计划增加投资
- 新增页面:
  - [[wiki/synthesis/全球建筑企业AI应用案例]] — 欧洲/北美/亚太三大区域20+标杆案例、McKinsey/PwC/Deloitte/RICS权威报告、中外对比、PPT宣讲建议
- 更新页面:
  - [[wiki/industry/建筑与环保]] — 新增"全球建筑企业AI标杆案例"章节，10个国际案例速查表+中外对比
  - [[ppt/outlines/国企AI宣讲-中高层完整版]] — 新增P12b全球视野页（McKinsey数据+Eiffage/Kajima/Bouygues三大案例+六大对标方向），P22场景速查表增加"国际对标"列
  - [[index.md]] — 新增全球建筑企业AI案例索引
- 参考来源: 60+ 条URL（含McKinsey/PwC/Deloitte/Autodesk/RICS/Skanska/AECOM/Boston Dynamics/OpenAI/Google Cloud等官方来源）
- 状态: 已完成，可直接用于央企总部宣讲

## [2026-06-10] ppt | 国企宣讲PPT大纲植入建筑央企案例
- 操作: 将补充的建筑央企案例植入 [[ppt/outlines/国企AI宣讲-中高层完整版]]
- 修改页面:
  - **P6 数据冲击**: 新增中铁建设"铁小智"90秒审完22万㎡、中铁十一局入选国资委首批40项AI高价值场景
  - **P12 同行标杆**: 将"制造业"改为**"建筑央企——AI已重新定义施工现场"**，放入中铁建设、中铁十一局、中交"蓝翼"、中冶赛迪4个详细案例
  - **P20 场景速查**: 新增"建筑央企对标"列，各业务线都能看到同行做法
  - **P32 收尾总结**: 更新第3行核心信息，加入中铁90秒审方案
- 结构逻辑: 能源电力(P11) → 建筑央企(P12) → 中建系兄弟(P13-P14) → 自身实践(P15-P18)，形成"行业→同行→同系→自己"的递进

## [2026-06-10] update | 补充建筑央企 AI 落地案例
- 操作: 用户要求为建筑行业宣讲补充建筑央企案例，启动 web-access skill 全网搜索
- 关键发现:
  - 国资委首批 40 项央企 AI 战略性高价值场景（2025.07），建筑领域仅 2 家入选：中铁十一局（大盾构隧道智能建造）、中交集团（绞吸挖泥船智能疏浚）
  - 中交"蓝翼"是央企首个土木建筑行业大模型
  - 中铁建设"铁小智"90 秒完成 22 万㎡方案审核，效率提升 80%
- 更新页面:
  - [[wiki/industry/建筑与环保]] — 大幅扩充"智慧建造与产业数字化"章节，新增建筑央企分类案例（中建/中铁/中铁建/中交/中冶），共 30+ 案例，全部附官方出处
  - [[wiki/industry/国有企业AI应用案例]] — 新增"建筑央企"专章（6 个详细案例 + 8 个速查），更新快速索引和按场景引用表
- 状态: 已完成，可直接用于建筑行业宣讲

## [2026-06-10] ppt | 国企中高层 AI 宣讲完整版 PPT 大纲（40页）
- 操作: 深挖现有知识库全部宣讲素材页面，整合成完整PPT大纲
- 结构: 十个Part / 40页 / 60-75分钟
  - Part 1: 封面与开场（2页）
  - Part 2: 开场钩子——为什么必须现在行动（3页）——"这不是技术选项，这是政治任务"
  - Part 3: 政策锚定——国家战略与考核压力（4页）——国资委考核指标体系、政策逻辑链
  - Part 4: 技术祛魅——AI到底能做什么（5页）——大模型/Agent/RAG类比、技术演进路线
  - Part 5: 同行压力——央企都在做什么（5页）——11家央企标杆案例、场景速查表
  - Part 6: 落地路径——怎么从零开始（4页）——吴恩达五步法、四阶段模型、美的四层架构、教-学-管-评
  - Part 7: 组织保障——谁来推、谁担责（3页）——三层组织架构、考核KPI、ROI量化
  - Part 8: 风险预判——怎么避坑（4页）——85%失败率、五大原因、六条高压线、国产选型决策树
  - Part 9: 行动倡议——从今天开始做什么（4页）——30/60/90天计划、工作组模板、Quick Wins
  - Part 10: 收尾——总结与号召（2页）——八模块一页总结+行动号召
  - 附录: 成熟度自评表、选型对比表、来源链接、Q&A（4页可选）
- 引用的知识库页面:
  - [[wiki/synthesis/国企AI宣讲-政策锚定]]、[[wiki/synthesis/国企AI宣讲-组织保障与ROI]]、[[wiki/synthesis/国企AI宣讲-风险合规]]、[[wiki/synthesis/国企AI宣讲-行动模板]]
  - [[wiki/industry/国有企业AI应用案例]]、[[wiki/concepts/Agent]]、[[wiki/synthesis/AI落地路径]]、[[wiki/synthesis/AI转型风险与对策]]
- 输出: [[ppt/outlines/国企AI宣讲-中高层完整版]]
- 更新: [[index.md]]、[[log.md]]
- 状态: 已完成，可直接用于PPT制作

## [2026-06-09] ingest | 2026年全球企业中高层AI培训全网搜索（8维度）
- 搜索方式: 启动 8 个并行子代理（web-access skill + WebSearch/WebFetch），覆盖全球英文和中文来源
- 搜索维度 8 个:
  - Agent #1 市场规模与趋势 → ✅ 完成（$7.49B市场，CAGR 38.4%）
  - Agent #2 咨询公司AI高管培训 → ✅ 完成（McKinsey/BCG/Deloitte/Accenture/PwC/KPMG/Bain）
  - Agent #3 科技巨头企业AI培训 → ✅ 完成（Google/Microsoft/AWS/IBM/NVIDIA/SAP/Salesforce）
  - Agent #4 商学院高管AI教育 → ✅ 完成（MIT/Stanford/Wharton/Harvard/INSEAD/LBS/清华/中欧/长江）
  - Agent #5 中国企业AI培训实践 → ✅ 完成（央企+民企案例）
  - Agent #6 AI领导力与素养框架 → ✅ 完成（OECD/UNESCO/EU AI Act/国家框架）
  - Agent #7 AI培训效果与ROI → ✅ 完成（250%平均ROI，1030%顶尖）
  - Agent #8 新兴AI培训模式 → ✅ 完成（8大创新模式+平台对比）
- 新增页面 3 个:
  - [[wiki/synthesis/全球企业AI培训全景2026]] — 市场规模（$7.49B/中国市场320亿元）、七大咨询公司对比、科技巨头培训项目、商学院高管课程、八大新兴培训模式、ROI数据（250%-1030%）、C-Suite关键数据速查
  - [[wiki/industry/企业AI培训实践]] — 央企/国企培训案例（国家电网/中国移动/中国石油/中国建筑等）、民企案例（华为/腾讯/阿里/字节/小米）、培训模式与合作方式、对中建发展启示
  - [[wiki/concepts/AI素养与领导力]] — OECD-EC/UNESCO/欧洲委员会AI素养框架、中国/美国/欧盟/新加坡/日本国家框架、AI领导力能力模型（六技能C-Suite/Agentic时代/BCG）、企业AI成熟度模型（Gartner 5层级）、行业特定标准
- 更新页面:
  - [[index.md]] — 新增3个页面索引，更新最近更新日志
- 关键发现:
  - 全球AI培训市场CAGR 32-38.4%，中国市场2026年~320亿元
  - 78%新领导力发展合同将包含AI组件，73% Fortune 500强制AI培训
  - 所有咨询公司2026年重点转向Agentic AI培训
  - 国资委2025年2月"AI+"行动计划要求央企管理层优先培训
  - 华为、腾讯、阿里、字节等民企推行"全员AI化"战略
  - EU AI Act 2026年8月执法，强制AI素养培训，最高罚750万欧元
- 参考来源: 100+ 条URL（含Careertrainer.ai/Deloitte/McKinsey/Gartner/OECD/UNESCO等权威来源）
- 状态: 已写入知识库并更新索引

## [2026-06-09] ingest | 国企中高层AI宣讲素材补充（五大模块）
- 背景: 用户指出原有宣讲结构缺少组织保障、ROI量化、政策锚定、风险合规、行动模板五大模块
- 搜索方式: 启动 6 个并行 Agent（web-access skill + WebSearch/WebFetch）
- 搜索结果:
  - Agent #1 国企AI组织保障与考核机制 → ✅ 完成
  - Agent #2 国企AI投入产出与ROI量化 → ✅ 完成
  - Agent #3 国资委AI政策与数字化转型考核指标 → ⚠️ 报错，主 Agent 直接补充
  - Agent #4 国企AI风险预判与合规素材 → ✅ 完成（内容最丰富）
  - Agent #5 央企AI应用标杆案例 → ⚠️ 超时终止，素材已从其他来源补充
  - Agent #6 高管AI行动模板与培训材料 → ✅ 完成
- 新增页面 4 个:
  - [[wiki/synthesis/国企AI宣讲-政策锚定]] — 国资委考核指标体系、2025两会"AI+"行动、新质生产力战略、央企AI布局行业行动（中国能建/中国海油/南钢）
  - [[wiki/synthesis/国企AI宣讲-组织保障与ROI]] — 三层组织架构模板、领导层配置、差异化KPI、四阶段落地路径、ROI量化、AI成熟度评估、30/60/90天行动计划
  - [[wiki/synthesis/国企AI宣讲-风险合规]] — 数据安全合规体系（6部核心法规）、信创要求、国产大模型选型决策树、供应商锁定防范、知识产权风险、AI项目失败率数据（85%）
  - [[wiki/synthesis/国企AI宣讲-行动模板]] — 吴恩达五步法、南钢百日攻坚案例、试点项目实施流程、高管培训框架、工作组组建方案、成熟度评估模型
- 参考来源: 30+ 条 URL（含安恒信息、普华永道、Gartner、36氪、CSDN等）
- 状态: 已写入知识库并更新索引

## [2026-06-09] ingest | 全网搜集补充知识库：政策/祛魅/同行/路径/风险五大维度
- 搜索维度 5 个：
  - 政策锚定 → 2025 两会"人工智能+"行动、国务院国资委"AI+"专项行动、信创国产化 79 号文
  - 技术祛魅 → Agent 概念科普（大脑 vs 完整员工/发动机 vs 汽车/美食家 vs 主厨类比）
  - 同行压力 → 国家电网"光明"大模型 + 知识管理 TOP15、南方电网"大瓦特"80 场景/80%替代率、厦门银华机械 5G 智慧工厂具体数字
  - 落地路径 → 美的"四层架构"（IaaS→算法平台→应用集成→业务应用）、"教-学-管-评"人才培养闭环
  - 风险预判 → 数据安全（85%企业有数据质量问题）、组织阻力（74%人才短缺）、人才缺口（北京缺口 37 万）
- 新增页面 4 个：
  - [[wiki/synthesis/AI政策与国资导向]] — 政策时间线、三步走路线图、央企 AI 落地进展、对中建发展启示
  - [[wiki/concepts/Agent]] — Agent vs LLM 类比、四大核心能力、央企智能体案例
  - [[wiki/synthesis/AI落地路径]] — 美的四层架构详解、教-学-管-评全链条、央企四步走建议
  - [[wiki/synthesis/AI转型风险与对策]] — 数据安全/组织阻力/人才缺口识别 + 央企做法 + 对策
- 更新页面 2 个：
  - [[wiki/industry/国有企业AI应用案例]] — 深化国家电网（光明大模型/TOP15/1855 项标准）、南方电网（10 个场景/具身智能/80 倍效率）、厦门银华机械（5G 智慧工厂具体数字/AI+安全/行政助手 30 倍）
  - [[index.md]] — 新增政策与战略、Agent 概念索引
- 状态: 已完成，可直接引用

## [2026-06-09] update | AnySearch 全网搜索培训相关成功案例
- 工具: AnySearch CLI（anysearch-skill）
- 搜索维度 6 个:
  - 央企 AI 数字化转型 → 中国石油昆仑大模型、南方电网"大瓦特"
  - 建筑行业 AI → 上海"天蝉"机器人、TransBIM、重庆梁平智能建造
  - 环保水务 AI → 剑企 AI-OS（江陵）、德清 L4 污水厂、首创环保、上海西岑
  - 投资领域 AI → 蚂蚁金融大模型、金证优智、艾景特、国信证券、恒生聚源
  - 双碳 ESG AI → 磐石·禹衡碳核算、碳衡科技青钥碳管家、中信 PathMatch
  - 企业 AI 培训 → 黑龙江交投 1.6 万人、中建五局近 4 万人 94% 活跃率
- 更新页面:
  - [[wiki/industry/国有企业AI应用案例]] — 新增中国石油、南方电网"大瓦特"、黑龙江交投、中建五局案例；更新快速索引、金句表、场景引用表
  - [[wiki/industry/建筑与环保]] — 新增投资/环保/建造/双碳四大领域 12 个标杆案例及来源链接
- 状态: 已纳入知识库，可直接引用

## [2026-04-27] init | 初始化 AI 知识库
- 重构 CLAUDE.md: 从物业管理知识库规范改为 AI 知识库与科普 PPT 制作规范
- 创建目录结构:
  - raw/: inbox, papers, articles, news, assets
  - wiki/: sources, concepts, models, tools, industry, synthesis
  - ppt/: outlines, scripts, assets
  - scripts/
- 创建初始文件: index.md, log.md
- 状态: 等待资料导入

## [2026-04-27] ingest | 全网资料搜索与知识库构建
- 搜索范围: AI 入门科普、Claude Code 教程、Obsidian 知识库、企业 AI 培训案例
- 创建概念页面 4 个:
  - [[wiki/concepts/人工智能]] — AI 基础概念，零基础友好
  - [[wiki/concepts/大语言模型]] — LLM 工作原理，类比解释
  - [[wiki/concepts/提示工程]] — RTFC 框架，场景模板
  - [[wiki/concepts/知识库与RAG]] — RAG 概念，Obsidian 目录结构
- 创建模型页面 3 个:
  - [[wiki/models/Claude]] — Anthropic 模型系列，安全对齐
  - [[wiki/models/DeepSeek]] — 国产模型，MoE 架构
  - [[wiki/models/GPT-4]] — OpenAI 模型系列，生态最完善
- 创建工具页面 4 个:
  - [[wiki/tools/ChatGPT]] — 对话工具，多模态
  - [[wiki/tools/Kimi]] — 国产长文本工具
  - [[wiki/tools/Claude-Code]] — AI 编程助手，知识库管理
  - [[wiki/tools/Obsidian]] — 本地笔记工具，第二大脑
- 创建综合页面 2 个:
  - [[wiki/synthesis/AI学习路径]] — 五阶段学习路线，零基础到进阶
  - [[wiki/synthesis/工具选型指南]] — 按场景和岗位的工具推荐
- 创建 PPT 大纲 1 个:
  - [[ppt/outlines/AI-01-AI入门与知识库构建]] — 35页，2小时培训大纲
    - Part1: AI 是什么？（20分钟）
    - Part2: AI 能帮你做什么？（30分钟）
    - Part3: 和 AI 说话的艺术（20分钟）
    - Part4: 构建你的第二大脑（40分钟）
    - Part5: 实战演练（10分钟）
- 更新: [[index.md]]、[[log.md]]
- 目标受众: 中建发展总部员工，零基础，落脚 Claude Code + Obsidian 知识库构建

## [2026-04-27] update | 针对性调整 PPT — 融入中建发展业务场景
- 背景调研:
  - 搜索中建发展定位、业务、组织架构
  - 确认目标实体: 中建发展集团有限公司（CSCEC二级子公司，总部北京）
  - 核心业务: 产业投资、生态环保（中建生态环境/中建环能）、产业数字化（中建电商/中建智能）、绿色低碳/双碳
  - 战略: "123N" — 1个核心+2个聚焦（生态环保+产业数字化）+3支队伍+N家上市公司
- PPT 调整内容:
  1. 页数从 35 页扩展到 **40 页**
  2. **开场破冰**: 加入中建发展元素，用宁夏二泉环境（污水处理企业）案例引发共鸣
  3. **AI比喻**: 从"工厂进化"改为"建筑行业进化"
  4. **新增"中建发展四大业务×AI"页**: 投资/环保/数字化/双碳各配 AI 应用场景
  5. **演示案例全面替换为真实业务场景**:
     - 投资岗: 村镇污水处理项目可行性分析框架
     - 环保岗: 读100页环保政策文件提取要点
     - 综合管理岗: 季度经营分析会纪要整理
     - 双碳岗: ESG报告"环境责任"章节撰写
     - 数字化岗: Claude Code辅助农污治理数据看板开发
  6. **提示词对比**: 全部改为中建发展真实场景（投资分析/会议纪要/双碳政策解读）
  7. **现场练习**: 改为"双碳研究员写建筑行业碳排放核算简报"
  8. **知识库痛点**: 从通用痛点改为中建发展专属（政策文件/项目经验/跨部门信息/写报告）
  9. **知识库目录结构**: 设计专属版本（融入投资/环保/双碳/数字化业务场景）
  10. **Claude Code命令**: 增加实战命令示例（项目复盘/知识连接/基于知识库回答）
  11. **新增"讲师参考附录"**: 公司定位、四大业务板块、核心数据、听众画像
- 创建行业页面 1 个:
  - [[wiki/industry/建筑与环保]] — AI在建筑环保行业的应用概览
- 更新: [[index.md]]、[[log.md]]

## [2026-06-09] ingest | 导入 AI 学习资源与国企 AI 落地案例
- 来源: 用户提供（网络搜索整理）
- 创建页面 2 个:
  - [[wiki/synthesis/AI学习资源汇总]] — 非技术高管 AI 学习资源（5 项精选）
    - h9-tec/AI_tools_nontechnical（GitHub  curated 清单）
    - Microsoft AI for Beginners（24 课系统课程）
    - AI for Everyone / Andrew Ng（Coursera 6 小时经典）
    - Elements of AI（欧盟推广，170 万+学员，含中文）
    - Anthropic Claude Tutorial（9 章交互式练习）
    - 附 3 条学习路径（快速通识/系统理解/工具驱动）
    - 附 PPT 引用建议（4 个常见宣讲场景）
  - [[wiki/industry/国有企业AI应用案例]] — 8 家央企/国企标杆案例
    - 能源电力：国家电网（知识管理）、南方电网（投诉率↓40%）
    - 制造工业：厦门银华机械（获奖案例）、美的集团（四层架构）
    - 采购供应链：中石化/国家电网（采购数字化三阶段）
    - 人力资源：中智集团（DeepSeek 部署，党务效率↑40%）
    - 消费品：伊利集团（全链数字化）、中国移动（云计算培训）
    - 附宣讲金句（"高层热情、中层火热、基层抵触"）
    - 附场景速查表（7 个常见问题 → 对应案例 + 关键数字）
- 更新: [[index.md]]、[[log.md]]

## [2026-06-09] ingest | 拉取 Microsoft AI for Beginners 课程资料
- 来源: WebFetch 抓取 https://github.com/microsoft/AI-For-Beginners
- 保存文件:
  - [[raw/articles/Microsoft_AI_for_Beginners]] — 原始 README 内容（课程结构、24课列表、动手实验、核心特点）
  - [[wiki/sources/Microsoft_AI_for_Beginners]] — 源摘要页面（含 frontmatter、课程分析、高管适配建议）
- 核心发现:
  - 12周24课，50+语言支持（含中文），PyTorch+TensorFlow双框架
  - 11个动手实验，覆盖感知机到深度强化学习
  - 涵盖前沿：LLM、提示工程、多模态(CLIP/VQGAN)
  - 未覆盖：AI in Business、经典ML、Azure服务、对话式AI
- 高管适配分析:
  - 建议精读10课（概念为主）：AI导论、框架介绍、迁移学习、Transformer、LLM与提示工程、AI伦理等
  - 建议跳过14课（纯技术实现）：感知机、MLP、OpenCV、GAN、RNN实现、目标检测、强化学习等
  - 提供两条精简路径：快速认知（6-8小时）和扩展视野（+3-4小时）
- 更新: [[index.md]]（源文件摘要章节）、[[log.md]]

## [2026-06-09] ingest | 拉取 Andrew Ng "AI for Everyone" 课程信息
- 来源: Coursera 公开页面 + DeepLearning.AI 官网
- 操作:
  - WebFetch 获取 https://www.coursera.org/learn/ai-for-everyone 课程概览
  - WebFetch 获取 https://www.deeplearning.ai/courses/ai-for-everyone 详细大纲
  - 保存原始资料: [[raw/articles/AI_for_Everyone_Andrew_Ng]]
  - 创建源摘要: [[wiki/sources/AI_for_Everyone_Andrew_Ng]]
  - 更新 [[index.md]] 源文件摘要索引
- 关键信息:
  - 讲师: Andrew Ng（DeepLearning.AI 创始人，Coursera 联合创始人）
  - 评分: 4.8/5（52,547+ 评价）
  - 时长: 约 7 小时（4 周，每周 2-3 小时）
  - 费用: 免费学习，证书 $49
  - 模块: 4 个（What is AI? / Building AI Projects / Building AI in Your Company / AI and Society）
  - 核心卖点: 零技术门槛，专为企业管理者设计，含 AI Transformation Playbook
- 与培训项目关联: 受众匹配（非技术管理者）、战略视角（企业 AI 转型）、风险意识（伦理与就业）、时间友好（7 小时碎片化）

## [2026-06-09] ingest | 拉取 Anthropic Claude Tutorial 官方教程资源
- 来源: WebFetch 抓取 GitHub 公开仓库 + platform.claude.com/cookbook + WebSearch 补充
- 操作:
  - WebFetch 获取 https://github.com/anthropics/prompt-eng-interactive-tutorial（9章交互式教程结构）
  - WebFetch 获取 https://github.com/anthropics/courses（5大课程模块结构）
  - WebFetch 获取 https://platform.claude.com/cookbook/（67个Cookbook案例）
  - WebSearch 搜索 "Anthropic Claude tutorial chapters interactive exercises"（补充 Academy 和社区资源）
  - 官方文档站点（docs.anthropic.com）301重定向至 platform.claude.com，返回404，未成功获取
- 保存文件:
  - [[raw/articles/Anthropic_Claude_Tutorial]] — 综合整理原始资料（9章教程+5大课程+67 Cookbook+13 Academy课程+社区资源）
  - [[wiki/sources/Anthropic_Claude_Tutorial]] — 源摘要页面（含 frontmatter、章节概览、适用性评估）
- 核心发现:
  - 9章交互式提示工程教程：初级3章+中级4章+高级2章，Jupyter Notebook格式，含Example Playground
  - 5大课程模块：API基础→提示工程→真实世界提示→提示评估→工具使用
  - 67个Cookbook案例：14类别，覆盖Agent、RAG、多模态、工具使用等
  - 13门免费Academy课程：Claude 101、API开发、Claude Code实战、MCP协议等
  - 社区补充：Panaversity的Claude Code练习（8模块33练习+3综合项目）
- 与培训项目关联:
  - 直接关联 [[wiki/tools/Claude-Code]] 和 [[wiki/models/Claude]]
  - 管理层建议学习第1-3章（基础概念）+ 第9章行业案例
  - 技术团队建议学习全系列+Cookbook实战
  - 全部免费，使用最低成本模型（Claude 3 Haiku）
- 更新: [[index.md]]（源文件摘要章节）、[[log.md]]

## [2026-06-09] ingest | 拉取 Elements of AI 课程资源
- 来源: WebFetch 抓取 https://www.elementsofai.com/ + WebSearch 补充课程大纲
- 保存文件:
  - [[raw/articles/Elements_of_AI]] — 完整课程介绍（六章大纲、学习目标、全球影响）
  - [[wiki/sources/Elements_of_AI]] — 源摘要页面（含 frontmatter、章节概览、国企培训适配分析）
- 关键信息:
  - 主办方: 赫尔辛基大学 + MinnaLearn，2018年上线
  - 规模: 200万+学员，170+国家，约40%女性，25%为40岁以上
  - 语言: 25+种语言含中文，欧盟150万欧元资助
  - 时长: 约25小时，完全免费，LinkedIn证书
  - 六章结构: 什么是AI→AI问题求解→现实世界中的AI→机器学习→神经网络→影响与启示
- 与培训项目关联: 中文支持/免费无版权/欧盟官方背书/零基础友好/第六章"社会影响"特别适合国企管理者

## [2026-06-09] fix | 补全 GitHub 仓库原始 README（curl 直拉）
- 操作: 用 `curl -sL https://raw.githubusercontent.com/.../README.md` 直拉原始文件，替换 agent 整理的摘要版
- Microsoft AI for Beginners: 102 行 → **227 行**（原始 README 含完整徽章、安装指引、贡献指南、许可证）
- AI_tools_nontechnical: 1211 行 → **1186 行**（agent 整理版已较完整，原始版略精简）
- 更新: `raw/articles/Microsoft_AI_for_Beginners.md`、`raw/articles/AI_tools_nontechnical.md`

## [2026-06-09] ingest | 拉取 h9-tec AI_tools_nontechnical 工具清单
- 来源: WebFetch 抓取 https://github.com/h9-tec/AI_tools_nontechnical（README完整内容）
- 保存文件:
  - [[raw/articles/AI_tools_nontechnical]] — 完整 README（12周路径、工具清单、提示词模板、行业应用）
  - [[wiki/sources/AI_tools_nontechnical]] — 源摘要页面（含 frontmatter、核心要点、培训适配建议）
- 关键信息:
  - 定位: 面向非技术人员的完整AI学习路线图，100%免费资源
  - 12周三阶段路径: 基础(1-4周)→应用(5-8周)→精通(9-12周)，每天30-45分钟
  - 工具生态: Tier1必备5款(ChatGPT/Claude/Gemini/Perplexity/BingChat)→Tier2专业20+款→Tier3试用策略
  - CLEAR提示词框架: Context/Length/Example/Audience/Role，配套10通用模板+3行业模板
  - 十大常见错误: 模糊提问、缺乏迭代、忽视幻觉、隐私泄露等，每错配对比示例
  - 六大行业方案: 医疗/教育/营销/软件开发/法律/金融的专用工具+场景模板
- 与培训项目关联: 受众完全匹配零基础非技术管理者；"十大错误"可转化为互动案例；商业/办公模板可直接复用；建议提取Week1-2作为1天集中培训素材

## [2026-04-29] ppt | 更新PPT大纲第40页：部署交互式数据大屏
- 操作: 改造 vue-big-screen（财务数据大屏）→ 部署到 GitHub Pages
- 仓库: [forestrain-git/vue-big-screen](https://github.com/forestrain-git/vue-big-screen)
- 在线访问: https://forestrain-git.github.io/vue-big-screen/
- 添加 .nojekyll + docs/ 目录解决 GitHub Pages 渲染问题
- 更新 PPT 第 40 页演示链接：静态 mockup → 线上交互式数据大屏

## [2026-04-30] ppt | 用AIPPT框架重构PPT大纲
- 框架: AIPPT——分享经历，建议行动，不吹不黑不说教
- 核心变更: 从"培训课程"结构（AI是什么→工具→提示词→场景）改为"个人经历"叙事（AI觉醒四阶段）
- 阶段叙事:
  - 第1阶段: 3月以前，窗口依赖——聊天+复制粘贴，AI=高级百度
  - 第2阶段: 3月上半月，AI编程的觉醒——Windsurf震惊，信心爆棚，垃圾站智能体项目，Kimi救场，央企信任
  - 第3阶段: 3月下半月，龙虾依赖——牛吹大了睡不着，三省六部制约束，从惊艳到失控，AI是放大器不是神
  - 第4阶段: 4月，走向CC依赖——危机倒逼进化，CC+OB不失忆AI，知识库搭建，能力边界拓展（看到即占有/想到即实现/获知即学会）
  - 当前: 物尽其用——窗口/Kimi/龙虾/CC各司其职
- 新增内容: 个人思考（工具→机器→AI的进化）、学AI花钱建议（李笑来时间观）
- 输出: [[ppt/outlines/AI-01-AI入门与知识库构建]] — 44页

## [2026-04-30] ppt | 根据定位重新梳理大纲
- 定位调整:
  - 讲述者: 中建智能总经理，24年前程序员（2002年），2009年加入中建后没写代码
  - 时长: 90分钟→60分钟
  - 受众: 中建发展总部员工→上级单位各部门（都认识，前戏缩短）
  - 页数: 44页→34页（含交流页）
- 核心修改:
  - 时间线修正: "3个月"→"两个月"
  - 人设重修: 从"20年程序员"改为"24年前程序员，近20年没写代码"——突出反差
  - 压缩开场自我介绍（大家都认识）
  - 删除冗余过渡页，每个阶段精简1-2页
  - 合并"工具矩阵"和"工作流"页
  - 技术细节进一步精简
  - 新增收尾"交流"页
- 输出: [[ppt/outlines/AI-01-AI入门与知识库构建]] — 34页

## [2026-04-30] ppt | 整体风格调校——保持正式框架，内容层面保留松弛感
- 调整原则: PPT整体框架、章节标题、结构描述保持正式和专业，具体页面内容和演讲备注保持交流感
- 具体修改:
  - 标题规范化: "今天不讲大道理"→"为什么我来做这个分享"、"龙虾——让我又爱又恨"→"自动化工具的双面性" 等
  - 删除过于随意的措辞: 前戏、吹牛、拍砖、过气程序员
  - 保留但调整了口语化表达的位置——从标题和框架描述下放到页面内容和演讲备注
  - 新增"关于学习AI的投入"页（第31页），之前编辑中被遗漏，现补回
  - 结尾页从"随便聊"改为"自由交流"
  - 删除"推荐的几个段子"章节——融入演讲备注而非单独列出
