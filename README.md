PINK = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
GRAY = '\033[90m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALIC = '\033[3m'
ENDC = '\033[0m'

def bold(string):
    return BOLD + string + ENDC

def underline(string):
    return UNDERLINE + string + ENDC

def yellow(string):
    return YELLOW + string + ENDC

def red(string):
    return RED + string + ENDC

def cyan(string):
    return CYAN + string + ENDC

def magenta(string):
    return MAGENTA + string + ENDC

def blue(string):
    return BLUE + string + ENDC

def gray(string):
    return GRAY + string + ENDC

def italic(string):
    return ITALIC + string + ENDC

def pink(string):
    return PINK + string + ENDC