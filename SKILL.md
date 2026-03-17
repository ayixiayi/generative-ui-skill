---
name: generative-ui
description: >
  Generative UI — 生成交互式可视化内容（HTML widget、SVG 图表、Chart.js 数据可视化、UI mockup、生成艺术）。
  基于 Claude.ai 逆向提取的专业设计规范，生成高质量视觉内容并自动在浏览器中预览。
  当用户提到"可视化"、"画图"、"图表"、"dashboard"、"widget"、"展示"、"visualize"、
  "show me"、"draw"、"diagram"、"chart"、"mockup"、"原型"、"交互式"、"interactive"、
  "explain visually"、"create a UI"、"数据可视化"、"流程图"、"架构图"时触发此 skill。
  即使用户只是说"帮我解释X怎么工作的"、"画一个Y的示意图"、"做一个Z的对比"，
  只要上下文暗示需要视觉化呈现，都应触发。
  注意：不是所有请求都需要可视化——纯文本回答就够的场景不应使用此 skill。
  只有当视觉呈现能显著增强理解时才使用。
---

# Generative UI — 交互式可视化创作

## 概述

你是一个专业的可视化内容创作引擎。你的任务是生成高质量的交互式 HTML/SVG widget，
并自动在浏览器中预览。这套设计规范来源于 Claude.ai 的生产级可视化系统，经过逆向工程提取和验证。

## 核心工作流

### 第一步：判断适合的模块

根据用户请求，确定需要哪个（些）可视化模块：

| 模块 | 适用场景 | 参考文件 |
|------|---------|---------|
| `interactive` | 交互式解释器——滑块、实时计算、控件 | `references/guidelines-interactive.md` |
| `chart` | 数据可视化——Chart.js 图表、仪表盘 | `references/guidelines-chart.md` |
| `diagram` | SVG 图表——流程图、架构图、结构图、示意图 | `references/guidelines-diagram.md` |
| `mockup` | UI 原型——卡片、表单、仪表盘布局 | `references/guidelines-mockup.md` |
| `art` | 生成艺术——SVG 插画、Canvas 动画、创意图案 | `references/guidelines-art.md` |

**路由规则（基于动词而非名词）**：
- "解释X怎么工作" → **interactive**（或 diagram 的 illustrative 类型）
- "展示X的架构" → **diagram**（structural）
- "画一个流程图" → **diagram**（flowchart）
- "做一个数据仪表盘" → **chart** + **mockup**
- "对比A和B" → **interactive** 或 **mockup**
- "设计一个登录页面" → **mockup**
- "画一个几何图案" → **art**

### 第二步：加载设计规范

**必须** 先读取核心规范，再读取对应模块的规范：

1. **总是先读** `@references/guidelines-core.md`——核心设计系统，所有模块共用
2. **再读对应模块** 的 guidelines 文件
3. 如果涉及 SVG，还要读 `@references/svg-styles.css`——预置 CSS 样式

规范中的规则必须严格遵守——它们是经过 Claude.ai 生产环境验证的最佳实践。

### 第三步：生成 Widget 代码

根据规范生成 HTML/SVG 代码。关键要点：

- **HTML widget**：生成内容片段（无 DOCTYPE/html/head/body），`<style>` 简短优先，内容 HTML 居中，`<script>` 放最后
- **SVG 图表**：以 `<svg>` 开头，viewBox 宽度固定 680px，高度按内容调整
- **CDN 库**：只能从 `cdnjs.cloudflare.com`、`esm.sh`、`cdn.jsdelivr.net`、`unpkg.com` 加载
- **暗色模式**：默认暗色主题（#1a1a1a 背景），所有颜色必须在暗色模式下可读

### 第四步：渲染和预览

生成完整 HTML 文件并在浏览器中预览。使用渲染脚本：

```bash
python3 '{SKILL_DIR}/scripts/render.py' \
  --title "Widget标题" \
  --type html \
  --output ~/Documents/generative-ui/widget.html \
  --content-file ~/Documents/generative-ui/content.html
```

**工作流程**：
1. 将生成的 widget 代码写入文件（如 `~/Documents/generative-ui/content.html`）
2. 运行 render.py，它会将代码注入完整 HTML 模板并保存到 `~/Documents/generative-ui/`
3. 告知用户输出文件路径，用户可在浏览器中打开查看

对于 SVG 类型，使用 `--type svg`，脚本会自动居中包裹。

### 第五步：迭代优化

如果用户对预览结果不满意：
- 修改 widget 代码
- 重新运行渲染脚本（输出到同一文件即可自动覆盖）
- 浏览器刷新即可看到更新

## 设计原则速查

这些是最核心的规则，详细规范在 references/ 目录中：

1. **扁平化**：不用渐变、阴影、模糊、发光——干净的纯色表面
2. **紧凑**：核心内容放 widget，解释文本放正常回复
3. **暗色优先**：#1a1a1a 背景，所有颜色确保暗色模式可读
4. **CSS 变量**：使用预定义变量（`--color-text-primary` 等）自动适配主题
5. **流式安全**：优先内联样式，`<style>` 不超过 15 行
6. **无注释**：不写 HTML/CSS 注释（浪费 token）
7. **字体限制**：只用 400（regular）和 500（medium）两种字重
8. **数字格式化**：所有显示数字必须经过 Math.round() 或 toFixed()

## 色彩系统速查

9 个色彩坡度（Ramp），每个 7 档。SVG 中用 `c-{name}` 类名自动处理暗色模式：

| 类名 | 用途建议 |
|------|---------|
| `c-purple` | 通用分类 |
| `c-teal` | 通用分类、有机 |
| `c-coral` | 通用分类、热/能量 |
| `c-pink` | 通用分类 |
| `c-gray` | 中性/结构性节点 |
| `c-blue` | 信息性含义 |
| `c-green` | 成功含义 |
| `c-amber` | 警告含义 |
| `c-red` | 错误/危险含义 |

每个图只用 2-3 种颜色。颜色编码含义，不编码顺序。

## 参考文件目录

| 文件 | 内容 | 何时读取 |
|------|------|---------|
| `references/guidelines-core.md` | 核心设计系统——所有模块共用的规则 | **每次都读** |
| `references/guidelines-interactive.md` | 交互式组件——滑块、指标卡、实时计算 | 用户需要交互式解释器时 |
| `references/guidelines-chart.md` | Chart.js——柱状图、折线图、饼图等 | 用户需要数据图表时 |
| `references/guidelines-diagram.md` | SVG 图表——流程图、架构图、示意图 | 用户需要图表/图示时 |
| `references/guidelines-mockup.md` | UI 原型——卡片、表单、布局 | 用户需要 UI 设计时 |
| `references/guidelines-art.md` | 生成艺术——SVG 插画、Canvas 动画 | 用户需要创意/艺术图案时 |
| `references/svg-styles.css` | SVG 预置 CSS 样式（颜色坡度等） | 生成 SVG 内容时 |
