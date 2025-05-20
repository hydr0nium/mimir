from pathlib import Path
from dataclasses import dataclass
from configparser import ConfigParser
from shutil import which
from mimir.util.output import error, info, get

HOME_DIRECTORY = Path.home()
CONFIG_PATH =  HOME_DIRECTORY / Path('.config/mimir')
CONFIG_FILE = CONFIG_PATH / Path('mimir.conf')
DEFAULT_DB_PATH = CONFIG_PATH
PACKAGE_MANAGERS = ["apt", "pacman", "pipx", "cargo", "gem"]
        
class Config: 
    
    def load_existing_config():
        config = ConfigParser()
        try:
            config.read(CONFIG_FILE)
            for package_manager in PACKAGE_MANAGERS:
                if not which(package_manager) and config.getboolean("package_managers", package_manager):
                    error(f"Package Manager mismatch found. This can cause problems. Found '{package_manager}' in config but not installed!")
                    update_config = get("Do you want to update package managers in config file? [y/n]: ").strip()
                    if update_config != "y":
                        error(f"Quitting")
                        exit()
                    info("Updated config file")
                    return Config.create_new_config()
            return config
        except:
            error(f"Found malformed config file.")
            new_config = get("Do you want to create a new config [y/n]: ").strip()
            if new_config != "y":
                error(f"Quitting")
                exit()
            info("Created new config file")
            return Config.create_new_config()

    def create_new_config():
        config = ConfigParser()
        CONFIG_PATH.mkdir(exist_ok=True, parents=True)
        with open(CONFIG_FILE, 'w') as config_file:
            config['settings'] = {}
            general = config['settings']
            config['package_managers'] = {}
            managers = config['package_managers']
            for package_manager in PACKAGE_MANAGERS:
                if which(package_manager):
                    managers[package_manager] = 'True'
                else:
                    managers[package_manager] = 'False'
            config.write(config_file)
            return config
        

def load_config():
    if CONFIG_FILE.exists():
        config = Config.load_existing_config()
        return config
    else:
        config = Config.create_new_config()
        return config



