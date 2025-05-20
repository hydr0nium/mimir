

def okay(message: str):
    print(f"[+] {message}")

def error(message: str):
    print(f"[!] {message}")

def info(message: str):
    print(f"[*] {message}")

def debug(message: str):
    print(f"[?] {message}")

def get(message: str):
    return input(f"[*] {message}")
