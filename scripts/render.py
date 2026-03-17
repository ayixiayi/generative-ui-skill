#!/usr/bin/env python3
"""
Generative UI Renderer — wraps widget code fragments into a complete HTML file
and optionally opens it in the default browser.

Usage:
    python3 render.py --title "My Widget" --type html --content-file /tmp/content.html --output /tmp/widget.html
    python3 render.py --title "My Diagram" --type svg --content-file /tmp/diagram.svg --output /tmp/diagram.html
    python3 render.py --title "My Widget" --type html --content-file /tmp/content.html --output /tmp/widget.html --open

Arguments:
    --title         Window/page title
    --type          Content type: html or svg
    --content-file  Path to the widget code fragment file
    --output        Output HTML file path
    --open          Open in default browser after rendering (optional)
"""

import argparse
import sys
import webbrowser
from pathlib import Path


def get_shell_template():
    """Read the shell.html template from assets/."""
    skill_dir = Path(__file__).parent.parent
    template_path = skill_dir / "assets" / "shell.html"
    if not template_path.exists():
        print(f"Error: Template not found at {template_path}", file=sys.stderr)
        sys.exit(1)
    return template_path.read_text(encoding="utf-8")


def wrap_svg_content(svg_code: str) -> str:
    """Wrap SVG in a centered flex container."""
    return (
        '<div style="display: flex; align-items: center; justify-content: center; '
        'min-height: 80vh;">\n'
        f"{svg_code}\n"
        "</div>"
    )


def render(title: str, content_type: str, content: str) -> str:
    """Render widget content into a complete HTML page."""
    template = get_shell_template()

    if content_type == "svg":
        content = wrap_svg_content(content)

    html = template.replace("{{TITLE}}", title)
    html = html.replace("{{CONTENT}}", content)

    return html


def main():
    parser = argparse.ArgumentParser(description="Generative UI Renderer")
    parser.add_argument("--title", required=True, help="Page title")
    parser.add_argument(
        "--type",
        required=True,
        choices=["html", "svg"],
        help="Content type: html or svg",
    )
    parser.add_argument(
        "--content-file", required=True, help="Path to content fragment file"
    )
    parser.add_argument("--output", required=True, help="Output HTML file path")
    parser.add_argument(
        "--open", action="store_true", help="Open in browser after rendering"
    )

    args = parser.parse_args()

    content_path = Path(args.content_file)
    if not content_path.exists():
        print(f"Error: Content file not found: {content_path}", file=sys.stderr)
        sys.exit(1)

    content = content_path.read_text(encoding="utf-8")
    html = render(args.title, args.type, content)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")

    print(f"Rendered: {output_path} ({len(html)} bytes)")
    print(f"Title: {args.title}")
    print(f"Type: {args.type}")

    if args.open:
        url = f"file://{output_path.resolve()}"
        try:
            webbrowser.open(url)
            print(f"Opened in browser: {url}")
        except Exception as e:
            print(f"Could not open browser: {e}", file=sys.stderr)
            print(f"Open manually: {url}")


if __name__ == "__main__":
    main()
