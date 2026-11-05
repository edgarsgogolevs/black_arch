# Black_Arch - Omarchy Theme

A dead simple theme for the digital minimalist. (Inspired by Felix theme)
<img width="2237" height="1397" alt="screenshot-2026-01-08_18-38-59" src="https://github.com/user-attachments/assets/58d71b64-6f70-4a1d-a5b7-d2d5cfd1a886" />
<img width="2237" height="1397" alt="screenshot-2026-01-07_20-08-11" src="https://github.com/user-attachments/assets/de886e32-249a-4abd-813c-da67092f0953" />

<img width="2240" height="1400" alt="screenshot-2025-12-12_12-45-16" src="https://github.com/user-attachments/assets/d0b5e7fc-9b5c-4e3b-a0d8-71cd89a3c9b4" />
<img width="2240" height="1400" alt="screenshot-2026-01-05_12-55-18" src="https://github.com/user-attachments/assets/af3e59da-f237-4101-a574-b2fb1086761d" />


## Installation

To install this theme, simply use the `omarchy-theme-install` command:

```sh
omarchy-theme-install https://github.com/ankur311sudo/black_arch.git
```

---

## This fork: BlackWhite Warm

A readability pass over the original palette. It is still black and white at heart, with soft, low-chroma warm accents so terminal output stays easy to read.

- **Terminals** (`colors.toml`, which Omarchy renders into Alacritty/Kitty/Foot/Ghostty, plus the shipped terminal files): off-white `#DCDCDC` text, a visible bright-black `#6E6E6E` for autosuggestions and dim output, and muted red `#E08080`, green `#9DC48A`, sand `#D5D09D`, blue `#9DB2CF`, rose `#C9A3B6`, and teal `#9EC4BE`.
- **`extras/zed/`**: Zed themes *BlackWhite*, *BlackWhite Warm*, and *BlackWhite Warmer*. `gen.py` regenerates `blackwhite.json`. Symlink that file into `~/.config/zed/themes/`.
- **`extras/herdr/theme.toml`**: the matching `[theme.custom]` block for herdr.
- **`extras/scripts/warm_terminals.py`**: rewrites `colors.toml` and the terminal configs from one palette. Run `omarchy theme refresh` afterwards.

```sh
omarchy-theme-install https://github.com/edgarsgogolevs/black_arch.git
```
