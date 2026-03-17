# 核心设计系统

这些规则适用于**所有**可视化模块。来源于 Claude.ai 的生产级设计规范。

## 设计哲学

- **无缝（Seamless）**：widget 应该感觉像是聊天界面的自然延伸
- **扁平（Flat）**：不用渐变、网格背景、噪点纹理或装饰效果。干净的纯色表面
- **紧凑（Compact）**：核心内容放 widget 内，解释文本放正常回复中
- **内容分离**：所有解释性文字、描述、介绍和总结写在回复文本中，不放在 widget HTML/SVG 内

## 暗色模式

默认暗色主题。`#1a1a1a` 背景，`#e0e0e0` 主文字色。

**所有颜色必须在暗色模式下可读**——心理测试：如果背景接近纯黑，每个文字元素是否仍然可读？

- SVG 中：使用预置颜色类（`c-blue`、`c-teal` 等）自动处理暗色模式
- SVG `<text>` 必须携带类名（`t`、`ts`、`th`）——不要省略 fill 或使用 `fill="inherit"`
- HTML 中：总是用 CSS 变量。不要硬编码如 `color: #333`——在暗色模式下不可见

## CSS 变量

### 背景色
- `--color-background-primary`（白色/主背景）
- `--color-background-secondary`（表面色）
- `--color-background-tertiary`（页面背景）
- `--color-background-info/danger/success/warning`

### 文字色
- `--color-text-primary`（黑/主文字）
- `--color-text-secondary`（弱化文字）
- `--color-text-tertiary`（提示文字）
- `--color-text-info/danger/success/warning`

### 边框色
- `--color-border-tertiary`（0.15α，默认）
- `--color-border-secondary`（0.3α，悬停）
- `--color-border-primary`（0.4α）
- `-info/-danger/-success/-warning`

### 排版
- `--font-sans`、`--font-serif`、`--font-mono`
- `--border-radius-md`（8px）、`--border-radius-lg`（12px）、`--border-radius-xl`（16px）

## 排版规则

- **字体大小**：h1 = 22px, h2 = 18px, h3 = 16px，全部 `font-weight: 500`。正文 = 16px, weight 400, `line-height: 1.7`
- **只用两种字重**：400（regular）和 500（medium）。不要用 600 或 700
- **全部小写句式**（Sentence case）。不要用 Title Case 或 ALL CAPS
- **不要句中加粗**。实体名、类名、函数名用 `code style`，不用 **bold**
- **最小字号**：11px。不能更小
- **不要用 emoji**——用 CSS 形状或 SVG path 代替

## 布局规则

- Widget 容器是 `display: block; width: 100%`。内容自然填充，不需要包裹 div
- 不要用 `position: fixed`——会导致 iframe 高度塌缩
- 不要用选项卡、轮播或 `display: none` 的隐藏内容
- 不要嵌套滚动——自适应高度
- 圆角：HTML 用 `var(--border-radius-md)`/`-lg`，SVG 用 `rx="4"` 或 `rx="8"`
- 单侧边框（`border-left` 等）不要加圆角

## 编码规则

- **无注释**：不要写 `<!-- comments -->` 或 `/* comments */`（浪费 token）
- **无渐变/阴影**：不要 drop shadows, blur, glow, neon
- **无深色背景**在外层容器上（透明即可——宿主提供背景）
- **无 DOCTYPE/html/head/body**——只输出内容片段
- **数字格式化**：所有显示数字必须经过 `Math.round()`、`.toFixed(n)` 或 `Intl.NumberFormat`
- 间距：垂直用 rem（1rem, 1.5rem, 2rem），组件内部用 px（8px, 12px, 16px）

## CDN 允许列表

外部资源只能从以下源加载：
- `cdnjs.cloudflare.com`
- `esm.sh`
- `cdn.jsdelivr.net`
- `unpkg.com`

其他来源会被静默阻止。

## 脚本加载

脚本在内容之后执行。通过 CDN `<script src="...">` 加载（UMD 全局变量），
然后在后续 `<script>` 中使用全局变量。不要用 `type="module"`（除 mermaid.js 外）。

**脚本加载顺序**：CDN 脚本可能在下一个 `<script>` 执行时尚未加载完成。
总是在 CDN script 标签上用 `onload="initChart()"` 回调，
并在内联脚本末尾添加 `if (window.Chart) initChart();` 作为兜底。

## 色彩系统

9 个色彩坡度，每个 7 档（50 最浅到 900 最深）：

| 类名 | 50 | 100 | 200 | 400 | 600 | 800 | 900 |
|------|-----|-----|-----|-----|-----|-----|------|
| `c-purple` | #EEEDFE | #CECBF6 | #AFA9EC | #7F77DD | #534AB7 | #3C3489 | #26215C |
| `c-teal` | #E1F5EE | #9FE1CB | #5DCAA5 | #1D9E75 | #0F6E56 | #085041 | #04342C |
| `c-coral` | #FAECE7 | #F5C4B3 | #F0997B | #D85A30 | #993C1D | #712B13 | #4A1B0C |
| `c-pink` | #FBEAF0 | #F4C0D1 | #ED93B1 | #D4537E | #993556 | #72243E | #4B1528 |
| `c-gray` | #F1EFE8 | #D3D1C7 | #B4B2A9 | #888780 | #5F5E5A | #444441 | #2C2C2A |
| `c-blue` | #E6F1FB | #B5D4F4 | #85B7EB | #378ADD | #185FA5 | #0C447C | #042C53 |
| `c-green` | #EAF3DE | #C0DD97 | #97C459 | #639922 | #3B6D11 | #27500A | #173404 |
| `c-amber` | #FAEEDA | #FAC775 | #EF9F27 | #BA7517 | #854F0B | #633806 | #412402 |
| `c-red` | #FCEBEB | #F7C1C1 | #F09595 | #E24B4A | #A32D2D | #791F1F | #501313 |

### 颜色分配原则

- 颜色编码**含义**，不编码顺序。不要像彩虹一样循环用色
- 按**类别**分组——同类节点共享一种颜色
- 灰色用于中性/结构性节点
- 每个图只用 **2-3 种颜色**
- 优先用 purple、teal、coral、pink 做通用分类
- blue、green、amber、red 保留给有语义含义的场景（信息、成功、警告、错误）

### 暗色模式配色速查

- **暗色模式**：800 填充 + 200 描边 + 100 标题 / 200 副标题
- 在有色背景上的文字，总用同一坡度的 800 或 900 档。不要用黑色或灰色

### 在 SVG 中使用

- `c-{ramp}` 类加在 `<g>` 上包裹 shape + text，或直接加在 `<rect>`/`<circle>`/`<ellipse>` 上
- 不要加在 `<path>` 上——path 不会得到坡度填充
- 暗色模式自动处理
