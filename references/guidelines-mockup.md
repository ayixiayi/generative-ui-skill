# UI Mockup 规范

适用场景：UI 原型、卡片布局、表单设计、仪表盘。

## 美学原则

扁平、干净、白色表面。最小的 0.5px 边框。充裕的留白。
不用渐变、不用阴影（功能性焦点环除外）。

## 基础 Token

- **边框**：`0.5px solid var(--color-border-tertiary)`（或 `-secondary` 强调）
- **圆角**：`var(--border-radius-md)` 大多数元素，`var(--border-radius-lg)` 卡片
- **卡片**：`var(--color-background-primary)` 背景，0.5px 边框，radius-lg，padding 1rem 1.25rem
- **按钮**：透明背景，0.5px border-secondary，hover bg-secondary，active scale(0.98)
- **表单元素**：已预置样式——直接写裸标签

## 布局模式

### 编辑式（解释性内容）
不用卡片包裹，内容自然流动。

### 卡片式（有界对象）
单张卡片包裹。如联系人记录、收据。

### 仪表盘
指标卡片网格 + 图表。

```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 1.5rem;">
  <div style="background: var(--color-background-secondary); border-radius: var(--border-radius-md); padding: 1rem;">
    <div style="font-size: 13px; color: var(--color-text-secondary);">用户数</div>
    <div style="font-size: 24px; font-weight: 500; margin-top: 4px;">12,458</div>
  </div>
  <div style="background: var(--color-background-secondary); border-radius: var(--border-radius-md); padding: 1rem;">
    <div style="font-size: 13px; color: var(--color-text-secondary);">收入</div>
    <div style="font-size: 24px; font-weight: 500; margin-top: 4px;">¥856K</div>
  </div>
</div>
```

## Mockup 呈现

小型 UI 组件（手机屏幕、聊天窗口、单张卡片、模态框）应放在背景表面上：
- 容器用 `var(--color-background-secondary)` + `border-radius: var(--border-radius-lg)` + padding
- 全宽度 mockup（仪表盘、设置页面、数据表格）不需要额外包裹

## 头像/首字母圆圈

```html
<div style="width: 44px; height: 44px; border-radius: 50%; background: var(--color-background-info); display: flex; align-items: center; justify-content: center; font-weight: 500; font-size: 14px; color: var(--color-text-info);">MR</div>
```

## 图标尺寸

emoji 或内联 SVG 图标：显式设 `font-size: 16px`（emoji）或 `width: 16px; height: 16px`（SVG）。
不要让图标继承容器字号。大号装饰图标最大 24px。

## 注意事项

- **Grid 溢出**：用 `minmax(0, 1fr)` 代替 `1fr`
- **表格溢出**：≤700px 下用 `table-layout: fixed`
- **模态框**：不用 `position: fixed`，用正常流 div + `min-height: 400px` + flex 居中
- **徽章/标签**：有色背景上的文字用同色系最深档——不用黑色或通用灰
