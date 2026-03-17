# SVG 图表/图示规范

适用场景：流程图、架构图、结构图、示意图。这是最复杂的可视化类型。

## 图表类型选择

**根据意图选择，不是根据主题**。问：用户想**记录**这个，还是**理解**它？

### 参考类图表（Reference）——用户想要一张可以指向的"地图"
- **流程图（Flowchart）**——顺序步骤、分支决策、数据转换
  - 触发："走一遍流程"、"有哪些步骤"、"什么流程"
- **结构图（Structural）**——东西包含在其他东西里
  - 触发："什么架构"、"怎么组织的"、"X 在哪里"

### 直觉图表（Intuition）——用户想"感受"某事物如何运作
- **示意图（Illustrative）**——画出机制本身
  - 物理对象用截面图、剖面图
  - 抽象概念用空间隐喻
  - 触发："X 到底怎么工作"、"解释 X"、"我不理解 X"

### 路由决策表

| 用户说 | 类型 | 画什么 |
|--------|------|--------|
| "LLM 怎么工作" | **示意图** | Token 行，堆叠层板，注意力线 |
| "transformer 架构" | 结构图 | 标签框：embedding, attention, FFN |
| "注意力怎么工作" | **示意图** | 一个 query token，扇形线到每个 key |
| "训练步骤是什么" | 流程图 | Forward → loss → backward → update |
| "数据库 schema" | **mermaid.js** | `erDiagram` 语法 |

**示意图是默认选择**——对于"X 怎么工作"的问题，不要退缩到流程图。

## SVG 通用设置

### ViewBox

```svg
<svg width="100%" viewBox="0 0 680 H">
```

- 宽度固定 680px——匹配容器宽度，1:1 像素对应
- 高度 H 按内容调整：最低元素底边 + 40px
- 安全区域：x=40 到 x=640，y=40 到 y=(H-40)
- **不要改 680**——改了会导致字体缩放不正确

### ViewBox 安全检查

1. 找最低元素：所有 rect 的 max(y + height)，所有 text 的 max(y)
2. viewBox 高度 = 该值 + 40px
3. 所有内容在 x=0 到 x=680 范围内
4. `text-anchor="end"` 的文字向左延伸——检查是否超出 x=0
5. 不要用负坐标

### 预置类

已在 shell.html 中加载：

- `class="t"` = 14px 主文字
- `class="ts"` = 12px 次要文字
- `class="th"` = 14px 500 字重标题
- `class="box"` = 中性矩形（bg-secondary 填充 + border 描边）
- `class="node"` = 可点击组（cursor pointer + hover 效果）
- `class="arr"` = 箭头线（1.5px）
- `class="leader"` = 虚线引导线
- `class="c-{ramp}"` = 彩色节点（c-blue, c-teal 等）

### 箭头标记

每个 SVG 开头必须包含：

```svg
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
```

用 `marker-end="url(#arrow)"` 引用。

## 流程图规则

### 尺寸

- 框之间最少 60px 间距
- 框内 24px padding
- 文字距边缘 12px
- 箭头头部距框 10px
- 单行框高 44px，双行框高 56px

### 文字宽度估算

14px 字体：每字符约 8px 宽。"Load Balancer"（13 字符）需要至少 140px 宽的框。
特殊字符（化学式、数学符号）额外加 30-50%。

### 布局

- 优先单方向流（全部上下 或 全部左右）
- 最多 4-5 个节点
- 680px 宽度下复杂布局会崩

### 单行节点（44px）

```svg
<g class="node c-blue">
  <rect x="100" y="20" width="180" height="44" rx="8" stroke-width="0.5"/>
  <text class="th" x="190" y="42" text-anchor="middle" dominant-baseline="central">T-cells</text>
</g>
```

### 双行节点（56px）

```svg
<g class="node c-blue">
  <rect x="100" y="20" width="200" height="56" rx="8" stroke-width="0.5"/>
  <text class="th" x="200" y="38" text-anchor="middle" dominant-baseline="central">Dendritic cells</text>
  <text class="ts" x="200" y="56" text-anchor="middle" dominant-baseline="central">Detect foreign antigens</text>
</g>
```

### 连接线

```svg
<line x1="200" y1="76" x2="200" y2="120" class="arr" marker-end="url(#arrow)"/>
```

箭头不能穿过其他框。如果直线路径穿过了，用 L 形弯路绕开：
```svg
<path d="M x1 y1 L x1 ymid L x2 ymid L x2 y2" class="arr" fill="none" marker-end="url(#arrow)"/>
```

### 循环不画成环

Krebs cycle、事件循环等——不要画环形布局。改用步进器（stepper）或线性布局 + 返回箭头。

## 结构图规则

### 容器

- 外层容器：大圆角矩形，rx=20-24，最浅填充（50 档），0.5px 描边
- 内部区域：中等圆角，rx=8-12，下一档填充
- 最少 20px 内边距
- 最多 2-3 层嵌套

### 颜色

嵌套区域用不同坡度——父子相同类名会产生相同填充，层次消失。

## 示意图规则

### 物理对象
画简化版——截面、剖面、示意图。水箱是圆角矩形 + 底部燃烧器。

### 抽象概念
用空间隐喻——transformer 是堆叠的水平板，注意力线连接 token。
hash table 是一排桶，item 落入其中。

### 与流程图/结构图的区别

- **形状自由**：使用 `<path>`、`<ellipse>`、`<circle>`、`<polygon>` 和曲线
- **布局跟随对象几何**：高瘦的对象画高瘦的图，不强制网格
- **颜色编码强度**：暖色 = 热/活跃，冷色 = 冷/静止
- **层叠重叠允许**（但文字除外——文字需要 8px 净空）
- **允许一个渐变**——唯一例外，只用于显示连续物理属性

### 优先交互

如果真实系统有控制手段，给图也加上。水箱有恒温器 → 加滑块。
这时用 HTML widget + 内联 SVG，不用纯 SVG。

### ERD / 数据库 Schema

用 **mermaid.js**，不用 SVG：

```html
<div id="erd"></div>
<script type="module">
import mermaid from 'https://esm.sh/mermaid@11/dist/mermaid.esm.min.mjs';
const dark = matchMedia('(prefers-color-scheme: dark)').matches;
await document.fonts.ready;
mermaid.initialize({
  startOnLoad: false,
  theme: 'base',
  fontFamily: 'system-ui, sans-serif',
  themeVariables: {
    darkMode: dark,
    fontSize: '13px',
    lineColor: dark ? '#9c9a92' : '#73726c',
    textColor: dark ? '#c2c0b6' : '#3d3d3a',
  },
});
const { svg } = await mermaid.render('erd-svg', `erDiagram
  USERS ||--o{ POSTS : writes
  POSTS ||--o{ COMMENTS : has`);
document.getElementById('erd').innerHTML = svg;
</script>
```

## 通用检查清单

- [ ] viewBox 高度足够（最低元素 + 40px）
- [ ] 所有内容在 x=0..680 范围内
- [ ] 没有箭头穿过不相关的框
- [ ] 文字没有溢出框
- [ ] 每个 `<text>` 有类名（t/ts/th）
- [ ] 每个连接路径有 `fill="none"`
- [ ] 用了 `dominant-baseline="central"` 做垂直居中
- [ ] 描边宽度 0.5px
