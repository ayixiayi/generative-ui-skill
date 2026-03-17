# Chart.js 数据可视化规范

适用场景：柱状图、折线图、饼图、散点图、仪表盘等数据图表。

## 基础模板

```html
<div style="position: relative; width: 100%; height: 300px;">
  <canvas id="myChart"></canvas>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js" onload="initChart()"></script>
<script>
  function initChart() {
    new Chart(document.getElementById('myChart'), {
      type: 'bar',
      data: { labels: ['Q1','Q2','Q3','Q4'], datasets: [{ label: 'Revenue', data: [12,19,8,15] }] },
      options: { responsive: true, maintainAspectRatio: false }
    });
  }
  if (window.Chart) initChart();
</script>
```

## 关键规则

### Canvas 尺寸
- Canvas 不能解析 CSS 变量。颜色用硬编码 hex 或 Chart.js 默认值
- `<canvas>` 包裹在 `<div>` 中，div 设显式 `height` + `position: relative`
- **高度只设在包裹 div 上**，不要设在 canvas 上
- 使用 `responsive: true, maintainAspectRatio: false`
- 横向柱状图：包裹 div 高度至少 `(条数 × 40) + 80` px

### 脚本加载
- UMD 构建：`<script src="https://cdnjs.cloudflare.com/ajax/libs/...">`——设置 `window.Chart` 全局
- 总是用 `onload="initChart()"` 在 CDN script 上
- 内联脚本末尾加 `if (window.Chart) initChart();` 兜底
- 多图表：用唯一 ID（`myChart1`, `myChart2`），每个图表独立的 canvas + div

### 气泡和散点图
- 气泡半径会延伸到坐标轴边界外导致裁剪
- 填充比例范围——`scales.y.min/max` 比数据范围多 ~10%
- 或用 `layout: { padding: 20 }` 作为备选

### X 轴标签
- Chart.js 会自动跳过重叠标签
- ≤12 个类别需要全部显示时：`scales.x.ticks: { autoSkip: false, maxRotation: 45 }`

## 数字格式化

负值：`-$5M` 不是 `$-5M`——符号在货币符号之前。

```javascript
(v) => (v < 0 ? '-' : '') + '$' + Math.abs(v) + 'M'
```

## 图例——总是自定义

禁用 Chart.js 默认图例，构建自定义 HTML 图例：

```javascript
plugins: { legend: { display: false } }
```

```html
<div style="display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 8px; font-size: 12px; color: var(--color-text-secondary);">
  <span style="display: flex; align-items: center; gap: 4px;">
    <span style="width: 10px; height: 10px; border-radius: 2px; background: #3266ad;"></span>
    Chrome 65%
  </span>
  <span style="display: flex; align-items: center; gap: 4px;">
    <span style="width: 10px; height: 10px; border-radius: 2px; background: #73726c;"></span>
    Safari 18%
  </span>
</div>
```

分类数据（饼图、甜甜圈、单系列柱状图）时，在图例标签中包含数值/百分比。

## 仪表盘布局

汇总数字用指标卡片（见 interactive 规范）放在图表上方。
图表 canvas 放在下方，不用卡片包裹。
