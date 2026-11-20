"""Generate the profile header SVGs (dark and light) from the Tetsu Studio landing tokens."""
import sys

WHOAMI = sys.argv[3] if len(sys.argv) > 3 else "tetsustudio"
from pathlib import Path

out = Path(sys.argv[1])
path = Path(sys.argv[2]).read_text().strip()

MODES = {
    "dark": dict(bg="#070708", surface="#151517", fg="#ffffff", muted="#8f8f90", border="#262628",
                 ember="#ff5a1f", hot="#ffd38a"),
    "light": dict(bg="#ffffff", surface="#fafafa", fg="#000000", muted="#737373", border="#e0e0e0",
                  ember="#e2470f", hot="#f59e0b"),
}

HEAD = "ui-rounded, 'Nunito', 'SF Pro Rounded', 'Segoe UI', system-ui, sans-serif"
MONO = "ui-monospace, 'JetBrains Mono', SFMono-Regular, Menlo, Consolas, monospace"
SANS = "'Inter', -apple-system, 'Segoe UI', system-ui, sans-serif"


def header(c):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400" role="img" aria-label="Tetsu Studio: software forjado a medida">
  <defs>
    <linearGradient id="ember" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox" spreadMethod="reflect">
      <stop offset="0.1" stop-color="{c['ember']}"/>
      <stop offset="0.5" stop-color="{c['hot']}"/>
      <stop offset="0.9" stop-color="{c['ember']}"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-0.5 0;0.5 0;-0.5 0" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.82" cy="0.5" r="0.45">
      <stop offset="0" stop-color="{c['ember']}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{c['ember']}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="1.1" fill="{c['fg']}" fill-opacity="0.07"/>
    </pattern>
    <clipPath id="frame"><rect width="1200" height="400" rx="24"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="1200" height="400" fill="{c['bg']}"/>
    <rect width="1200" height="400" fill="url(#dots)"/>
    <rect width="1200" height="400" fill="url(#glow)">
      <animate attributeName="opacity" values="0.7;1;0.7" dur="5s" repeatCount="indefinite"/>
    </rect>
    <svg x="830" y="70" width="260" height="260" viewBox="18 -95 980 980">
      <g transform="translate(0 818) scale(1 -1)"><path d="{path}" fill="url(#ember)"/></g>
    </svg>
    <text x="72" y="104" font-family="{MONO}" font-size="15" letter-spacing="4" fill="{c['muted']}">鉄 · TETSU = HIERRO</text>
    <text x="72" y="186" font-family="{HEAD}" font-size="66" font-weight="800" letter-spacing="-1.5" fill="{c['fg']}">Software <tspan fill="url(#ember)">forjado</tspan></text>
    <text x="72" y="262" font-family="{HEAD}" font-size="66" font-weight="800" letter-spacing="-1.5" fill="{c['fg']}">a medida.</text>
    <text x="72" y="318" font-family="{SANS}" font-size="20" fill="{c['muted']}">Apps independientes sobre servidores propios. AI first.</text>
    <g font-family="{MONO}" font-size="13" fill="{c['muted']}">
      <circle cx="78" cy="353" r="4" fill="#27c93f"><animate attributeName="opacity" values="1;0.35;1" dur="2.4s" repeatCount="indefinite"/></circle>
      <text x="92" y="357">tetsustudio.com</text>
    </g>
    <rect x="0.5" y="0.5" width="1199" height="399" rx="24" fill="none" stroke="{c['border']}"/>
  </g>
</svg>
"""


def terminal(c):
    lines = [
        ("$", "whoami", c["fg"]),
        ("", WHOAMI, c["muted"]),
        ("$", "cat principios.txt", c["fg"]),
        ("+", "Una app, un problema", "#27c93f"),
        ("+", "Independientes: su base, su deploy", "#27c93f"),
        ("+", "Un solo login para todas (Zitadel)", "#27c93f"),
        ("+", "Local-first cuando suma", "#27c93f"),
    ]
    rows = []
    y = 92
    for prompt, text, color in lines:
        pre = f'<tspan fill="{c["ember"]}">{prompt} </tspan>' if prompt == "$" else (
            f'<tspan fill="{color}">{prompt} </tspan>' if prompt else "  ")
        txt_color = c["fg"] if prompt in ("$", "+") else color
        rows.append(f'<text x="36" y="{y}">{pre}<tspan fill="{txt_color}">{text}</tspan></text>')
        y += 30
    cursor_y = y - 18
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{y + 20}" viewBox="0 0 1200 {y + 20}" role="img" aria-label="Principios de Tetsu Studio">
  <rect x="0.5" y="0.5" width="1199" height="{y + 19}" rx="18" fill="{c['surface']}" stroke="{c['border']}"/>
  <circle cx="34" cy="32" r="6.5" fill="#ff5f56"/><circle cx="56" cy="32" r="6.5" fill="#ffbd2e"/><circle cx="78" cy="32" r="6.5" fill="#27c93f"/>
  <text x="600" y="37" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{c['muted']}">~/tetsustudio</text>
  <line x1="0" y1="56" x2="1200" y2="56" stroke="{c['border']}"/>
  <g font-family="{MONO}" font-size="17">
    {chr(10).join('    ' + r for r in rows)}
    <text x="36" y="{y}"><tspan fill="{c['ember']}">$ </tspan></text>
    <rect x="56" y="{cursor_y}" width="10" height="20" fill="{c['fg']}"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1s" repeatCount="indefinite"/></rect>
  </g>
</svg>
"""


for mode, c in MODES.items():
    (out / f"header-{mode}.svg").write_text(header(c))
    (out / f"terminal-{mode}.svg").write_text(terminal(c))
print("ok")
