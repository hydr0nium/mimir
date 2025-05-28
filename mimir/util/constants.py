from pathlib import Path

HOME_DIRECTORY = Path.home()
CONFIG_PATH =  HOME_DIRECTORY / Path('.config/mimir')
CONFIG_FILE = CONFIG_PATH / Path('mimir.conf')
INSTALLED_DB = CONFIG_PATH / Path('installed.db')
PACKAGE_FILE = CONFIG_PATH / Path('packages.json')
PACKAGE_URL = "https://raw.githubusercontent.com/hydr0nium/mimir/refs/heads/main/packages/packages.json"
PACKAGE_TOML_BASE = "https://raw.githubusercontent.com/hydr0nium/mimir/refs/heads/main/packages/"
PACKAGE_MANAGERS = ["apt", "pacman", "yay", "pipx", "flatpak", "snap", "gem", "cargo"]