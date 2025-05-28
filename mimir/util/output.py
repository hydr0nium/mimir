class term_colors:
    INFO = "\033[1;34m"
    ERROR = "\033[1;31m"
    OKAY = "\033[1;32m"
    DEBUG = "\033[1;33m"
    RESET = "\033[0m"

def okay(message: str):
    print(f"{term_colors.OKAY}[+] {message}{term_colors.RESET}")

def error(message: str):
    print(f"{term_colors.ERROR}[!] {message}{term_colors.RESET}")

def info(message: str):
    print(f"{term_colors.INFO}[*] {message}{term_colors.RESET}")

def debug(message: str):
    print(f"{term_colors.DEBUG}[?] {message}{term_colors.RESET}")

def get(message: str):
    return input(f"{term_colors.INFO}[*] {message}{term_colors.RESET}").strip()

def title(title: str, size=10):
    print("="*size + f"{title}" + "="*size)

def end(title: str, size=10):
    print("="*size + "="*len(title) + "="*size)
