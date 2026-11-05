"""Rewrite the black_arch Omarchy theme's terminal colours in the BlackWhite Warm style."""
import re
import sys
from pathlib import Path

# Usage: python3 warm_terminals.py [theme_dir]   (default: this repo), then `omarchy theme refresh`
THEME = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]

# BlackWhite Warm terminal palette: grayscale base, soft low-chroma hues for the
# semantic ANSI colours, borrowed from the Zed theme (sand, soft red/green, muted blue).
FG, BRIGHT_FG, BG = "#DCDCDC", "#FFFFFF", "#000000"
CURSOR, SEL_BG, SEL_FG = "#FFFFFF", "#FFFFFF", "#000000"
ANSI = {  # name: (normal, bright)
    "black": ("#262626", "#6E6E6E"),  # bright black = autosuggestions / dim output, now visible
    "red": ("#E08080", "#EC9A9A"),
    "green": ("#9DC48A", "#B5D6A3"),
    "yellow": ("#D5D09D", "#E6E1B4"),
    "blue": ("#9DB2CF", "#B6C7DE"),
    "magenta": ("#C9A3B6", "#DDBCCB"),
    "cyan": ("#9EC4BE", "#B8D6D1"),
    "white": (FG, BRIGHT_FG),
}
NAMES = list(ANSI)
normal = [ANSI[n][0] for n in NAMES]
bright = [ANSI[n][1] for n in NAMES]
low = lambda c: c.lower()

HEADER = """# ────────────────────────────────────────────────────────────
# Omarchy black_arch Theme for {app} - BlackWhite Warm palette
# Original theme by Ankur  https://github.com/ankur311sudo
# ────────────────────────────────────────────────────────────
"""

# --- colors.toml (what Omarchy actually renders the terminal configs from) ---
p = THEME / "colors.toml"
text = p.read_text()
updates = {"foreground": FG, "cursor": CURSOR, "selection_background": SEL_BG, "selection_foreground": SEL_FG}
for i in range(8):
    updates[f"color{i}"] = normal[i]
    updates[f"color{i + 8}"] = bright[i]
for key, val in updates.items():
    text, n = re.subn(rf'^({key}\s*=\s*")#[0-9A-Fa-f]{{6}}(")', rf"\g<1>{val}\g<2>", text, flags=re.M)
    assert n == 1, key
p.write_text(text)

# --- alacritty.toml ---
ala = HEADER.format(app="Alacritty") + f"""
[window]
# window padding {{px}}
padding.x = 20
padding.y = 20
decorations = "none"

[font]
size = 12.0


[colors.primary]
foreground = "{low(FG)}"
background = "{low(BG)}"
bright_foreground = "{low(BRIGHT_FG)}"

[colors.selection]
text = "{low(SEL_FG)}"
background = "{low(SEL_BG)}"

[colors.cursor]
text = "{low(BG)}"
cursor = "{low(CURSOR)}"

[colors.normal]
""" + "".join(f'{n:<7} = "{low(c)}"\n' for n, c in zip(NAMES, normal)) + "\n[colors.bright]\n" + "".join(
    f'{n:<7} = "{low(c)}"\n' for n, c in zip(NAMES, bright)
)
(THEME / "alacritty.toml").write_text(ala)

# --- foot.ini ---
foot = HEADER.format(app="foot") + f"""
[colors]
foreground = {low(FG)[1:]}
background = {low(BG)[1:]}

selection-foreground = {low(SEL_FG)[1:]}
selection-background = {low(SEL_BG)[1:]}

# cursor = <text under cursor> <cursor>
cursor = {low(BG)[1:]} {low(CURSOR)[1:]}

"""
for i, n in enumerate(NAMES):
    foot += f"# {n}\nregular{i} = {low(normal[i])[1:]}\nbright{i}  = {low(bright[i])[1:]}\n\n"
(THEME / "foot.ini").write_text(foot.rstrip() + "\n")

# --- ghostty.conf ---
gh = HEADER.format(app="Ghostty") + f"""
background = {low(BG)}
foreground = {low(FG)}
cursor-color = {low(CURSOR)}
selection-background = {low(SEL_BG)}
selection-foreground = {low(SEL_FG)}

""" + "".join(f"palette = {i}={low(c)}\n" for i, c in enumerate(normal)) + "\n" + "".join(
    f"palette = {i + 8}={low(c)}\n" for i, c in enumerate(bright)
)
(THEME / "ghostty.conf").write_text(gh)

# --- kitty.conf ---
kitty = HEADER.format(app="kitty") + f"""
foreground              {FG}
background              {BG}
selection_foreground    {SEL_FG}
selection_background    {SEL_BG}

cursor                  {CURSOR}
cursor_text_color       {BG}

url_color               {ANSI["blue"][0]}

# Window borders
active_border_color     #989898
inactive_border_color   #262626
bell_border_color       {ANSI["red"][0]}
visual_bell_color       none

# Tab bar
active_tab_foreground   #000000
active_tab_background   #CBC4A2
inactive_tab_foreground #9A9A9A
inactive_tab_background #0A0A0A
tab_bar_background      #000000
tab_bar_margin_color    none

# ANSI 16 colours
""" + "".join(f"color{i:<2} {c}\n" for i, c in enumerate(normal)) + "\n" + "".join(
    f"color{i + 8:<2} {c}\n" for i, c in enumerate(bright)
) + f"""
# Marks
mark1_foreground #000000
mark1_background {ANSI["yellow"][0]}
mark2_foreground #000000
mark2_background {ANSI["green"][0]}
mark3_foreground #000000
mark3_background {ANSI["blue"][0]}
"""
(THEME / "kitty.conf").write_text(kitty)
print("ok")
