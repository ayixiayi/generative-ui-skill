# 生成艺术规范

适用场景：SVG 插画、Canvas 动画、几何图案、创意图形。

*"画一个日落" / "创建一个几何图案"*

## 核心原则

与其他模块相比，艺术类允许更大胆的表达：

- **填满画布**——艺术应感觉丰富，不稀疏
- **大胆用色**：混合不同 `--color-text-*` 类别获取多样性
- **自定义颜色允许**：艺术类是唯一允许自定义 `<style>` 颜色块的地方
- 可使用 `prefers-color-scheme` 做暗色模式变体
- **层叠不透明形状**获取深度
- **有机形态**：`<path>` 曲线、`<ellipse>`、`<circle>`
- **纹理用重复**（平行线、点、阴影线），不用光栅效果
- **几何图案**用 `<g transform="rotate()">` 做放射对称

## SVG 艺术设置

与图表相同的 viewBox 规则：

```svg
<svg width="100%" viewBox="0 0 680 H">
```

## Canvas 动画

允许 CSS `@keyframes` 动画，只动画 `transform` 和 `opacity`。
循环时间控制在 ~2s 以内。

用媒体查询保护：
```css
@media (prefers-reduced-motion: no-preference) {
  .animated { animation: spin 2s linear infinite; }
}
```

## 保真度上限

这些是示意图，不是插画。每个形状应一目了然。
如果一个 `<path>` 需要超过 ~6 段才能画出，就简化它。

- 水箱 = 圆角矩形，不是贝塞尔肖像
- 火焰 = 三个三角形，不是真实的火
- 可识别的轮廓胜过精确的轮廓

## 颜色哲学

对物理对象：
- 暖色（amber, coral, red）= 热/能量/压力
- 冷色（blue, teal）= 冷/平静
- 灰色 = 惰性结构

对抽象主题：
- 暖色 = 活跃/高权重/被关注
- 冷色/灰色 = 休眠/低权重/被忽略

## 物理色彩场景

天空、水面、草地、皮肤、材料等物理色彩场景：全部用硬编码 hex。
不要混合 `c-*` 主题类。
如需暗色变体，用 `@media (prefers-color-scheme: dark)` 显式提供。
