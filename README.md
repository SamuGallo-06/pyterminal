# Pyterminal

Small helper functions to color and format terminal output (bold, italic, red, blue, etc.) and to clear the screen without using `os.system`.

Files
- `src/pyterminal/pyterminal.py` — implementation of all helpers.

Quick start
- Import the helpers (adjust path depending on how you run your project):
    - If `src` is on your PYTHONPATH or package-installed:
        from pyterminal import bold, green, clear
    - For direct import during development:
        from src.pyterminal.pyterminal import bold, green, clear

Basic usage
- Wrap text with style/color functions; they return strings with ANSI escapes:
    print(bold(green("Hello World!")))
- Functions are chainable:
    print(italic(blue(bold("Status:"))), "OK")
- Clear the screen without calling external commands:
    clear()  # clears the terminal using ANSI sequences

Notes
- These helpers use ANSI escape codes; they work on terminals that support ANSI (Linux, macOS, Windows 10+ with VT100 support).
- Combine as needed; each function returns the formatted string so you can nest or concatenate.

Example snippets
- Colored and styled text:
    print(bold(red("Error:"), " File not found"))
- Inline usage:
    print(f"{underline('Path:')} {cyan('/home/user')}")

API (common helpers)
- Text styles: bold(...), italic(...), underline(...), dim(...), reverse(...)
- Foreground colors: black(...), red(...), green(...), yellow(...), blue(...), magenta(...), cyan(...), white(...)
- Background colors: bg_black(...), bg_red(...), bg_green(...), ...
- Utility: clear()  # clear screen
- All functions accept and return plain strings, so results can be printed or composed.

If you want, I can generate a short reference table with exact function names and example outputs based on the current `pyterminal.py`.