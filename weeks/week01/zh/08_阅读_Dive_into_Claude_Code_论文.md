# 讲义 08｜阅读 3：Dive into Claude Code（论文）
*Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems*
作者：Jiacheng Liu, Xiaohan Zhao, Xinyi Shang, Zhiqiang Shen（MBZUAI VILA Lab / UCL）
arXiv:2604.14228v3（2026-10-10），共 55 页

## 官方材料 / Official materials
| 材料 Material | 链接 Link |
|---|---|
| 论文 Paper | [arXiv PDF](https://arxiv.org/pdf/2604.14228) |
| 代码 Code | [GitHub VILA-Lab/Dive-into-Claude-Code](https://github.com/VILA-Lab/Dive-into-Claude-Code) |

下面按论文主线做导读式讲解，覆盖关键数字，不是全文翻译。

## 研究对象与方法
- 分析公开的 Claude Code TypeScript 源码（v2.1.88），再和两个开源代理系统比较：**OpenClaw**（多渠道个人助理网关）和 **Hermes Agent**（单进程、多界面的助理）。

## 一句话结论
核心是一个简单的 **while 循环**（调用模型 → 执行工具 → 重复）；**大部分代码都在循环周围的系统里**。

> [!WARNING]
> **补充**
> 这和讲义 03 的 200 行代码、讲义 04 的“框架”概念完全对得上。

## 五个价值观（Five Values）
1. Human decision authority：人保有最终决定权
2. Safety, security, and privacy：安全、防护与隐私
3. Reliable execution：可靠执行
4. Capability amplification：放大能力
5. Contextual adaptability：适应不同场景

## 设计原则（论文共 13 条，表 1。以下是能从表里识别出的部分）
| 英文 | 中文 |
|---|---|
| Deny-first with human escalation | 默认拒绝，拿不准就交给人 |
| Graduated trust spectrum | 分级信任：从严格到放手的一条连续光谱 |
| Defense in depth | 多层防御 |
| Externalized (configurable) policy | 策略写在外部配置里，不硬编码 |
| Context as scarce resource | 把上下文当稀缺资源 |
| Append-only durable state | 只追加的持久化状态（会话日志） |
| Minimal scaffolding | 最少的脚手架，把推理交给模型 |
| Values over rules | 讲价值判断，不搞死板规则 |
| Composable extensibility | 多种可组合的扩展机制 |
| Reversibility-weighted risk | 按“能不能撤销”来衡量风险 |
| Transparent file-based config & memory | 配置和记忆用透明的文件存储（不用数据库或向量检索） |
| Isolated subagent boundaries | 子代理之间隔离 |
| Graceful recovery and resilience | 出错能优雅恢复，只在真正恢复不了时才打扰人 |

## 关键架构（对应论文章节）
- **权限系统（§5）**：7 种权限模式，从 `plan`（所有计划都要用户批准）到 `default`、`acceptEdits`，再到 `bypassPermissions`（几乎不询问）；还有一个基于机器学习的分类器。规则是**deny 优先**：宽泛的拒绝规则不能被更具体的允许规则覆盖（例如“禁止所有 shell 命令”不能被“允许 npm test”覆盖）；支持按内容匹配，比如 `Bash(prefix:npm)`。之后还有可选的 shell 沙箱。
- **对比其他系统**：SWE-Agent 和 OpenHands 靠 Docker 容器隔离；Aider 靠 Git 回滚做安全网；Claude Code 在可选沙箱之上叠加多层策略，用简单性换取对每个动作的细粒度控制。
- **五层压缩流水线（§7.3）**：每次调用模型前依次执行
  1. Budget reduction：限制单条工具结果的大小
  2. Snip：剪掉较早的历史
  3. Microcompact：细粒度压缩（与缓存有关）
  4. Context collapse：折叠很长的历史
  5. Auto-compact：语义汇总（就是讲义 05 里的压缩提示词）
- **四种扩展机制（§6）**：MCP、plugins（插件，既是打包格式也是分发渠道）、skills、hooks（27 种事件类型）。论文专门讨论了为什么要四种：它们占用上下文的代价不同。
- **上下文与记忆（§7）**：CLAUDE.md 分层加载 + 自动记忆。
- **子代理（§8）**：通过 Agent 工具委派；隔离运行；有独立的 sidechain transcripts（旁支记录）；**只把汇总结果返回父代理**，以节省上下文。
- **会话存储**：只追加（append-oriented）。

## 三个系统的对比
| 层面 | Claude Code | OpenClaw | Hermes |
|---|---|---|---|
| 安全 | 逐个动作审核 | 守住边界（perimeter）级别的访问 | 在多个界面上做逐个动作的审批 |
| 运行时 | 单个 CLI 循环 | 运行时嵌在网关控制面里 | 单进程，角色由入口决定 |
| 上下文/扩展 | 扩展上下文窗口 | 网关级的能力注册 | 可插拔的记忆和模型后端 |

## 其他值得注意的数字
- 引用的纵向数据（McCain et al., 2026）：用户自动批准的比例从不到 50 次会话时的约 20%，上升到 750 次会话时的 40% 以上 → 信任是逐步建立的（论文说“co-constructed”，由模型、用户和产品共同构建）。
- 论文最后提出了未来代理系统的 **6 个开放方向**（第 13 节）。

> [!WARNING]
> **补充**
> - 你写的 skills 属于“低常驻成本”的扩展；MCP 工具定义会常驻上下文 → 跟讲义 04 的结论一致。
> - 读法建议：先读 §1–3（价值观与总体架构），再按兴趣读 §5（权限）、§6（扩展）、§7（上下文/压缩）、§8（子代理）。
