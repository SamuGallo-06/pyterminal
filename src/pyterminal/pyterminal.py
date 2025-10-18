_CLEAR_SCREEN = "\033c"
_PINK = '\033[95m'
_BLUE = '\033[94m'
_CYAN = '\033[96m'
_MAGENTA = '\033[95m'
_GRAY = '\033[90m'
_GREEN = '\033[92m'
_YELLOW = '\033[93m'
_RED = '\033[91m'
_BOLD = '\033[1m'
_UNDERLINE = '\033[4m'
_ITALIC = '\033[3m'
_ENDC = '\033[0m'
_BLACK_FG = '\033[30m'
_WHITE_FG = '\033[97m'
_BG_BLACK = '\033[40m'
_BG_RED = '\033[41m'
_BG_GREEN = '\033[42m'
_BG_YELLOW = '\033[43m'
_BG_BLUE = '\033[44m'
_BG_MAGENTA = '\033[45m'
_BG_CYAN = '\033[46m'
_BG_WHITE = '\033[47m'
_BRIGHT_RED = '\033[91m'
_BRIGHT_GREEN = '\033[92m'
_BRIGHT_YELLOW = '\033[93m'
_BRIGHT_BLUE = '\033[94m'
_BRIGHT_MAGENTA = '\033[95m'
_BRIGHT_CYAN = '\033[96m'
_BRIGHT_WHITE = '\033[97m'

def bold(string):
    return _BOLD + string + _ENDC

def underline(string):
    return _UNDERLINE + string + _ENDC

def yellow(string):
    return _YELLOW + string + _ENDC

def red(string):
    return _RED + string + _ENDC

def cyan(string):
    return _CYAN + string + _ENDC

def magenta(string):
    return _MAGENTA + string + _ENDC

def blue(string):
    return _BLUE + string + _ENDC

def gray(string):
    return _GRAY + string + _ENDC

def italic(string):
    return _ITALIC + string + _ENDC

def pink(string):
    return _PINK + string + _ENDC

def clear_screen():
    print(_CLEAR_SCREEN)

def colorize(code, string):
    return code + string + _ENDC

def black(string):
    return colorize(_BLACK_FG, string)

def white(string):
    return colorize(_WHITE_FG, string)

def bright_red(string):
    return colorize(_BRIGHT_RED, string)

def bright_green(string):
    return colorize(_BRIGHT_GREEN, string)

def bright_yellow(string):
        return colorize(_BRIGHT_YELLOW, string)

def bright_blue(string):
    return colorize(_BRIGHT_BLUE, string)

def bright_magenta(string):
    return colorize(_BRIGHT_MAGENTA, string)

def bright_cyan(string):
    return colorize(_BRIGHT_CYAN, string)

def bright_white(string):
    return colorize(_BRIGHT_WHITE, string)

def bg_black(string):
    return colorize(_BG_BLACK, string)

def bg_red(string):
    return colorize(_BG_RED, string)

def bg_green(string):
    return colorize(_BG_GREEN, string)

def bg_yellow(string):
    return colorize(_BG_YELLOW, string)

def bg_blue(string):
    return colorize(_BG_BLUE, string)

def bg_magenta(string):
    return colorize(_BG_MAGENTA, string)

def bg_cyan(string):
    return colorize(_BG_CYAN, string)

def bg_white(string):
    return colorize(_BG_WHITE, string)