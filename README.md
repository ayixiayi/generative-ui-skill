# generative-ui-skill

Generative UI skill for [OpenCode](https://github.com/code-yeongyu/oh-my-opencode) — generate interactive HTML/SVG widgets using Claude.ai's reverse-engineered design system.

Inspired by [pi-generative-ui](https://github.com/Michaelliv/pi-generative-ui).


## What it does

Ask your AI agent to visualize something, and it generates a production-quality interactive widget — charts, diagrams, dashboards, UI mockups — rendered in a dark-themed HTML page you can open in any browser.

- **Interactive explainers** — sliders, live calculations, Chart.js charts
- **SVG diagrams** — flowcharts, architecture diagrams, structural diagrams, illustrative diagrams
- **Data visualization** — Chart.js bar/line/pie/scatter charts with custom legends
- **UI mockups** — cards, forms, dashboards, metric grids
- **Generative art** — SVG illustrations, Canvas animations, geometric patterns

## How it works

The skill bundles **72KB of design guidelines** extracted verbatim from Claude.ai's generative UI system. When triggered, the AI:

1. Routes to the right module (interactive / chart / diagram / mockup / art)
2. Loads the relevant design guidelines into context
3. Generates HTML/SVG code following the production design spec
4. Wraps the code in a full HTML page via `render.py`
5. Opens the result in your browser

The design system includes a 9-color ramp palette, pre-styled form elements, SVG diagram classes, and dark mode CSS variables — all auto-injected by the HTML shell template.

## Install

Copy the `generative-ui` folder into your OpenCode skills directory:

```bash
cp -r generative-ui ~/.config/opencode/skills/
```

Restart OpenCode to pick up the new skill.

## Usage

Just ask your agent to visualize things. The skill triggers automatically on keywords like "visualize", "chart", "diagram", "dashboard", "draw", "mockup", etc.

```
> 帮我做一个交互式的复利计算器
> Draw a microservices architecture diagram
> Create a sales dashboard with metric cards and trend charts
> Visualize how attention mechanism works in transformers
> 画一个几何图案
```

## Trigger phrases

Chinese: 可视化、画图、图表、展示、流程图、架构图、原型、交互式、数据可视化

English: visualize, show me, draw, diagram, chart, mockup, interactive, dashboard, widget, explain visually

## Project structure

```
generative-ui/
├── SKILL.md                           # Entry point: trigger, workflow, module routing
├── assets/
│   └── shell.html                     # HTML template (dark theme + CSS vars + SVG classes)
├── references/
│   ├── guidelines-core.md             # Core design system (shared by all modules)
│   ├── guidelines-interactive.md      # Sliders, metric cards, comparisons
│   ├── guidelines-chart.md            # Chart.js setup, legends, formatting
│   ├── guidelines-diagram.md          # SVG flowcharts, structural, illustrative
│   ├── guidelines-mockup.md           # Cards, forms, dashboard layouts
│   ├── guidelines-art.md              # SVG illustration, Canvas animation
│   └── svg-styles.css                 # Pre-built SVG classes (9 color ramps)
├── scripts/
│   └── render.py                      # CLI: content fragment → full HTML → browser
└── evals/
    └── evals.json                     # Test cases
```

## Design system

The guidelines are extracted from Claude.ai's production `show_widget` / `read_me` tool system. They cover:

- **Dark mode first** — `#1a1a1a` background, all colors tested for readability
- **9 color ramps** — purple, teal, coral, pink, gray, blue, green, amber, red (7 stops each)
- **Pre-styled components** — buttons, inputs, range sliders, metric cards
- **SVG diagram classes** — `.c-blue`, `.th`, `.arr`, `.node` etc. with auto dark mode
- **Chart.js patterns** — canvas sizing, custom legends, tooltip styling, axis formatting
- **Typography** — 2 weights only (400/500), sentence case, no emoji

## Credits

- [pi-generative-ui](https://github.com/Michaelliv/pi-generative-ui) by Michaelliv — the original inspiration
- [Anthropic](https://www.anthropic.com/) — for building the generative UI system we reverse-engineered
- [OpenCode](https://github.com/code-yeongyu/oh-my-opencode) — the extensible AI coding agent

## License

MIT
