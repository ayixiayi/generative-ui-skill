# 交互式组件规范

适用场景：交互式解释器、滑块控件、实时计算、对比选项、数据记录卡片。

## UI 组件美学

扁平、干净的表面。最小的 0.5px 边框。充裕的留白。
不用渐变、阴影（功能性焦点环除外）。

### 基础 Token

- 边框：总是 `0.5px solid var(--color-border-tertiary)`（或 `-secondary` 强调）
- 圆角：`var(--border-radius-md)` 用于大多数元素，`var(--border-radius-lg)` 用于卡片
- 卡片：白色背景（`var(--color-background-primary)`），0.5px 边框，radius-lg，padding 1rem 1.25rem
- 表单元素（input, select, textarea, button, range）已预置样式——直接写裸标签即可
- 按钮：透明背景，0.5px border-secondary，hover bg-secondary，active scale(0.98)

### 指标卡片（Metric Cards）

用于汇总数字（收入、计数、百分比）：

```html
<div style="background: var(--color-background-secondary); border-radius: var(--border-radius-md); padding: 1rem;">
  <div style="font-size: 13px; color: var(--color-text-secondary);">总收入</div>
  <div style="font-size: 24px; font-weight: 500; margin-top: 4px;">¥128,450</div>
</div>
```

2-4 个一组，用 grid + `gap: 12px` 排列。

### 布局模式

- **编辑式**（解释性内容）：不用卡片包裹，内容自然流动
- **卡片式**（有界对象如联系人、收据）：单张卡片包裹
- 不要在 widget 内放表格——作为 markdown 输出在回复文本中

## 1. 交互式解释器

*"解释复利怎么工作" / "教我排序算法"*

用 HTML widget 做交互控件——滑块、按钮、实时状态显示、图表。
解释性文字放在正常回复中，不嵌入 HTML。

```html
<div style="display: flex; align-items: center; gap: 12px; margin: 0 0 1.5rem;">
  <label style="font-size: 14px; color: var(--color-text-secondary);">年数</label>
  <input type="range" min="1" max="40" value="20" id="years" style="flex: 1;" step="1" />
  <span style="font-size: 14px; font-weight: 500; min-width: 24px;" id="years-out">20</span>
</div>

<div style="display: flex; align-items: baseline; gap: 8px; margin: 0 0 1.5rem;">
  <span style="font-size: 14px; color: var(--color-text-secondary);">¥10,000 →</span>
  <span style="font-size: 24px; font-weight: 500;" id="result">¥38,700</span>
</div>

<div style="margin: 2rem 0; position: relative; height: 240px;">
  <canvas id="chart"></canvas>
</div>
```

## 2. 对比选项

*"对比这些产品的价格和功能" / "帮我选 React 还是 Vue"*

并排卡片网格，用语义颜色突出差异。

- 用 `repeat(auto-fit, minmax(160px, 1fr))` 做响应式列
- 推荐选项用 `border: 2px solid var(--color-border-info)` 强调（2px 是唯一例外）
- 添加小徽章："最受欢迎"——`background: var(--color-background-info); color: var(--color-text-info); font-size: 12px; padding: 4px 12px;`

## 3. 数据记录

*"做一张联系人卡片" / "创建一张订单收据"*

单张卡片包裹全部内容。人物用头像/首字母圆圈。

```html
<div style="background: var(--color-background-primary); border-radius: var(--border-radius-lg); border: 0.5px solid var(--color-border-tertiary); padding: 1rem 1.25rem;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
    <div style="width: 44px; height: 44px; border-radius: 50%; background: var(--color-background-info); display: flex; align-items: center; justify-content: center; font-weight: 500; font-size: 14px; color: var(--color-text-info);">MR</div>
    <div>
      <p style="font-weight: 500; font-size: 15px; margin: 0;">Maya Rodriguez</p>
      <p style="font-size: 13px; color: var(--color-text-secondary); margin: 0;">VP of Engineering</p>
    </div>
  </div>
</div>
```

## 重要注意事项

- **Grid 溢出**：`grid-template-columns: 1fr` 默认有 `min-width: auto`，用 `minmax(0, 1fr)` 修复
- **表格溢出**：多列表格在 ≤700px 下用 `table-layout: fixed` + 显式列宽
- **Mockup 呈现**：小型 UI 组件（手机屏幕、聊天窗口等）放在背景表面上（`var(--color-background-secondary)` 容器）
- **Range slider**：设置 `step="1"`（或 0.1）让输入值本身就是整数
