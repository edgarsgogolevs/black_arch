"""Generate the BlackWhite Zed themes (grayscale, matched to Omarchy Black_arch)."""
import json
import sys
from pathlib import Path

# Usage: python3 gen.py [output.json]   (default: blackwhite.json next to this script)
OUT = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("blackwhite.json")

BG = "#000000"

# Gray ladder (contrast vs #000 in comments). Steps are roughly even in perceived lightness.
WHITE = "#FFFFFF"   # 21.0  functions, definitions, titles
INK = "#DCDCDC"     # 15.1  body text: variables, properties  (off-white -> less halation)
LIGHT = "#C2C2C2"   # 11.9  types / constructors (italic)
MID = "#969696"     #  7.0  keywords, operators
DIM = "#7C7C7C"     #  5.0  comments (italic), punctuation
PUNCT = "#828282"   #  5.3  punctuation
FAINT = "#6E6E6E"   #  4.2  inline completions / ghost text (meant to recede)

# Status hues, kept soft so they sit next to grayscale without shouting.
GREEN = "#7BC47B"
SAND = "#D5D09D"
RED = "#E08080"
BLUE = "#9DB2CF"


def s(color, style=None, weight=None):
    return {"color": color, "font_style": style, "font_weight": weight}


def syntax(p):
    return {
        "attribute": s(p["special"], "italic"),
        "boolean": s(p["number"]),
        "comment": s(p["comment"], "italic"),
        "comment.doc": s(p["doc"], "italic"),
        "constant": s(p["number"]),
        "constant.builtin": s(p["number"]),
        "constructor": s(p["type"], "italic"),
        "embedded": s(p["ink"]),
        "emphasis": s(p["ink"], "italic"),
        "emphasis.strong": s(p["white"], None, 700),
        "enum": s(p["type"], "italic"),
        "function": s(p["white"]),
        "function.builtin": s(p["white"]),
        "function.definition": s(p["white"], None, 700),
        "function.method": s(p["white"]),
        "function.special.definition": s(p["white"], None, 700),
        "hint": s(p["comment"], "italic"),
        "keyword": s(p["keyword"]),
        "label": s(p["special"], "italic"),
        "link_text": s(p["ink"], "italic"),
        "link_uri": s(p["link_uri"]),
        "number": s(p["number"]),
        "operator": s(p["operator"]),
        "predictive": s(p["faint"], "italic"),
        "preproc": s(p["keyword"]),
        "primary": s(p["ink"]),
        "property": s(p["prop"]),
        "punctuation": s(p["punct"]),
        "punctuation.bracket": s(p["punct"]),
        "punctuation.delimiter": s(p["punct"]),
        "punctuation.list_marker": s(p["list_marker"]),
        "punctuation.markup": s(p["special"]),
        "punctuation.special": s(p["special"]),
        "string": s(p["string"]),
        "string.escape": s(p["escape"], None, 700),
        "string.regex": s(p["string"]),
        "string.special": s(p["string"]),
        "string.special.symbol": s(p["number"]),
        "tag": s(p["white"]),
        "text.literal": s(p["string"]),
        "title": s(p["white"], None, 700),
        "type": s(p["type"], "italic"),
        "type.builtin": s(p["type"], "italic"),
        "variable": s(p["ink"]),
        "variable.builtin": s(p["special"], "italic"),
        "variable.parameter": s(p["ink"]),
        "variable.special": s(p["special"], "italic"),
        "variant": s(p["type"], "italic"),
    }


def style(p):
    st = {
        "accents": [WHITE, "#BDBDBD", "#8C8C8C"],
        "background": BG,
        "foreground": p["ink"],
        "border": "#262626",
        "border.variant": "#1A1A1A",
        "border.focused": "#5A5A5A",
        "border.selected": "#5A5A5A",
        "border.transparent": "#00000000",
        "border.disabled": "#1A1A1A",
        "elevated_surface.background": "#0E0E0E",
        "surface.background": BG,
        "drop_target.background": "#FFFFFF1A",
        "element.background": "#0E0E0E",
        "element.hover": "#1A1A1A",
        "element.active": "#2E2E2E",
        "element.selected": "#262626",
        "element.disabled": "#121212",
        "ghost_element.background": "#00000000",
        "ghost_element.hover": "#1A1A1A",
        "ghost_element.active": "#2E2E2E",
        "ghost_element.selected": "#262626",
        "ghost_element.disabled": "#00000000",
        "text": p["ui_text"],
        "text.muted": "#9A9A9A",
        "text.placeholder": "#6E6E6E",
        "text.disabled": "#5A5A5A",
        "text.accent": WHITE,
        "icon": "#D0D0D0",
        "icon.muted": "#8C8C8C",
        "icon.disabled": "#4A4A4A",
        "icon.placeholder": "#6E6E6E",
        "icon.accent": WHITE,
        "status_bar.background": BG,
        "title_bar.background": BG,
        "title_bar.inactive_background": BG,
        "toolbar.background": BG,
        "tab_bar.background": "#0A0A0A",
        "tab.inactive_background": "#0A0A0A",
        "tab.active_background": BG,
        "search.match_background": p["search"],
        "search.active_match_background": "#D5D09D59",
        "panel.background": BG,
        "panel.focused_border": "#5A5A5A",
        "panel.indent_guide": "#1C1C1C",
        "panel.indent_guide_active": "#3A3A3A",
        "panel.indent_guide_hover": "#4A4A4A",
        "pane.focused_border": "#5A5A5A",
        "pane_group.border": "#262626",
        "scrollbar.thumb.background": "#FFFFFF24",
        "scrollbar.thumb.hover_background": "#FFFFFF3D",
        "scrollbar.thumb.active_background": "#FFFFFF59",
        "scrollbar.thumb.border": "#00000000",
        "scrollbar.track.background": "#00000000",
        "scrollbar.track.border": "#00000000",
        "minimap.thumb.background": "#FFFFFF1F",
        "minimap.thumb.hover_background": "#FFFFFF33",
        "minimap.thumb.active_background": "#FFFFFF4D",
        "minimap.thumb.border": "#00000000",
        "editor.foreground": p["ink"],
        "editor.background": BG,
        "editor.gutter.background": BG,
        "editor.subheader.background": "#0A0A0A",
        "editor.active_line.background": p["active_line"],
        "editor.highlighted_line.background": "#1A1A1A",
        "editor.debugger_active_line.background": "#D5D09D1F",
        "editor.line_number": p["line_number"],
        "editor.active_line_number": p["ui_text"],
        "editor.hover_line_number": "#9A9A9A",
        "editor.invisible": "#333333",
        "editor.wrap_guide": "#161616",
        "editor.active_wrap_guide": "#2A2A2A",
        "editor.indent_guide": p["indent"],
        "editor.indent_guide_active": p["indent_active"],
        "editor.document_highlight.read_background": "#FFFFFF14",
        "editor.document_highlight.write_background": "#FFFFFF1F",
        "editor.document_highlight.bracket_background": "#FFFFFF24",
        "terminal.background": BG,
        "terminal.foreground": p["ink"],
        "terminal.bright_foreground": WHITE,
        "terminal.dim_foreground": "#8C8C8C",
        "link_text.hover": WHITE,
        "players": [
            {"cursor": p["cursor"], "background": p["cursor"], "selection": p["selection"]},
            {"cursor": "#BDBDBD", "background": "#BDBDBD", "selection": "#BDBDBD26"},
            {"cursor": "#8C8C8C", "background": "#8C8C8C", "selection": "#8C8C8C26"},
            {"cursor": SAND, "background": SAND, "selection": "#D5D09D26"},
        ],
        "version_control.added": GREEN,
        "version_control.added_background": "#7BC47B1F",
        "version_control.deleted": RED,
        "version_control.deleted_background": "#E080801F",
        "version_control.modified": SAND,
        "version_control.modified_background": "#D5D09D1F",
        "version_control.renamed": BLUE,
        "version_control.conflict": SAND,
        "version_control.ignored": "#5A5A5A",
        "version_control.word_added": "#7BC47B40",
        "version_control.word_deleted": "#E0808040",
        "version_control.conflict_marker.ours": "#7BC47B26",
        "version_control.conflict_marker.theirs": "#9DB2CF26",
    }

    # Terminal: same grayscale ordering as the Black_arch Alacritty palette, but the
    # "bright black" (used for autosuggestions / dim output) is lifted from #262626 so
    # it is actually visible, and bright variants are a step lighter than normal.
    ansi = p.get("ansi") or {
        "black": ("#262626", "#6E6E6E"),
        "red": ("#646464", "#808080"),
        "green": ("#8E8E8E", "#ABABAB"),
        "yellow": ("#B9B9B9", "#D2D2D2"),
        "blue": ("#989898", "#B4B4B4"),
        "magenta": ("#747474", "#909090"),
        "cyan": ("#585858", "#7A7A7A"),
        "white": ("#D4D4D4", "#FFFFFF"),
    }
    for name, (normal, bright) in ansi.items():
        st[f"terminal.ansi.{name}"] = normal
        st[f"terminal.ansi.bright_{name}"] = bright
        st[f"terminal.ansi.dim_{name}"] = normal

    def status(key, color, bg_alpha="1F"):
        st[key] = color
        st[f"{key}.background"] = color + bg_alpha
        st[f"{key}.border"] = color

    status("conflict", SAND)
    status("created", GREEN)
    status("deleted", RED)
    status("error", RED)
    status("hint", "#9A9A9A")
    status("info", BLUE)
    status("modified", SAND)
    status("renamed", BLUE)
    status("success", GREEN)
    status("warning", SAND)
    for key in ("hidden", "ignored", "unreachable"):
        st[key] = "#6E6E6E"
        st[f"{key}.background"] = "#00000000"
        st[f"{key}.border"] = "#1A1A1A"
    st["predictive"] = p["faint"]
    st["predictive.background"] = "#0E0E0E"
    st["predictive.border"] = "#1A1A1A"

    st["syntax"] = syntax(p)
    return st


# Pure grayscale: strings get their own light-gray step.
GRAY = {
    "white": WHITE, "ink": INK, "prop": "#CFCFCF", "type": LIGHT,
    "keyword": MID, "operator": MID, "special": MID, "list_marker": MID, "link_uri": MID,
    "comment": DIM, "doc": "#8E8E8E", "punct": PUNCT, "faint": FAINT,
    "string": "#BABABA", "number": WHITE, "escape": WHITE,
    "ui_text": "#E8E8E8", "cursor": WHITE, "selection": "#FFFFFF33", "search": "#FFFFFF2E",
    "active_line": "#111111", "line_number": "#4E4E4E",
    "indent": "#1C1C1C", "indent_active": "#3A3A3A",
}

# Same, but literals carry a faint warm tint borrowed from the git "modified" sand.
# Terminal palette shared with the Omarchy black_arch terminals + herdr (BlackWhite Warm).
WARM_ANSI = {
    "black": ("#262626", "#6E6E6E"),
    "red": ("#E08080", "#EC9A9A"),
    "green": ("#9DC48A", "#B5D6A3"),
    "yellow": ("#D5D09D", "#E6E1B4"),
    "blue": ("#9DB2CF", "#B6C7DE"),
    "magenta": ("#C9A3B6", "#DDBCCB"),
    "cyan": ("#9EC4BE", "#B8D6D1"),
    "white": ("#DCDCDC", "#FFFFFF"),
}

WARM = GRAY | {"string": "#CBC4A2", "number": "#E2C9A8", "ansi": WARM_ANSI}

# Every role gets its own soft, low-chroma warm hue, so categories separate by hue
# *and* lightness instead of lightness alone. Everything is warm-shifted (ink, greys,
# selection) to cut glare on pure black, and comments are lifted to ~6.5:1.
#   sand = strings   peach = numbers/constants/escapes   dusty rose = keywords
#   sage = types     warm white = functions             warm grey = punctuation/comments
WARMER = {
    "white": "#FBF6EE", "ink": "#E3DCD0", "prop": "#D2CABD", "type": "#BCC59E",
    "keyword": "#D4A5AB", "operator": "#B3AA9D", "special": "#D4A5AB",
    "list_marker": "#E8B88F", "link_uri": "#BCC59E",
    "comment": "#9A9084", "doc": "#ABA092", "punct": "#958D82", "faint": "#7A7166",
    "string": "#D6CB98", "number": "#E8B88F", "escape": "#E8B88F",
    "ui_text": "#EEE8DE", "cursor": "#FBF6EE", "selection": "#F2E2C438", "search": "#E8D9B036",
    "active_line": "#15120F", "line_number": "#5C554D",
    "indent": "#1F1C18", "indent_active": "#3F3A33",
    "ansi": WARM_ANSI,
}

theme = {
    "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
    "name": "BlackWhite",
    "author": "APS",
    "themes": [
        {"name": "BlackWhite", "appearance": "dark", "style": style(GRAY)},
        {"name": "BlackWhite Warm", "appearance": "dark", "style": style(WARM)},
        {"name": "BlackWhite Warmer", "appearance": "dark", "style": style(WARMER)},
    ],
}

with open(OUT, "w") as f:
    json.dump(theme, f, indent=2)
    f.write("\n")


# --- contrast report -------------------------------------------------------
def lum(h):
    h = h.lstrip("#")[:6]
    c = [int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


for t in theme["themes"]:
    print(f"== {t['name']}")
    seen = {}
    for k, v in t["style"]["syntax"].items():
        seen.setdefault(v["color"], []).append(k)
    for c, ks in sorted(seen.items(), key=lambda kv: -lum(kv[0])):
        print(f"  {c}  {ratio(c, BG):5.1f}:1 vs bg   {ratio(c, t['style']['editor.active_line.background']):5.1f}:1 vs active line   {', '.join(ks[:5])}{'…' if len(ks) > 5 else ''}")
