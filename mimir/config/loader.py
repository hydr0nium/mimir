from pathlib import Path
from dataclasses import dataclass
from configparser import ConfigParser, Error as ConfigError
from shutil import which
from mimir.util.output import error, info, get
from mimir.util.constants import PACKAGE_MANAGERS, CONFIG_FILE, CONFIG_PATH

        
class Config: 
    
    def load_existing_config():
        config = ConfigParser()
        try:
            config.read(CONFIG_FILE)
            for package_manager in PACKAGE_MANAGERS:
                if not which(package_manager) and config.getboolean("package_managers", package_manager):
                    return Config.fix_config(f"Package Manager mismatch found. This can cause problems.\nFound '{package_manager}' in config but it is not installed!")
                    
            return config
        except ConfigError as e:
            return Config.fix_config(f"Found malformed config file.")


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
    
    def fix_config(error_msg):
        error(error_msg)
        new_config = get("Do you want to create a new config? [y/n]: ")
        if new_config != "y":
            error(f"Quitting")
            exit()
        info("Created new config file")
        return Config.create_new_config()

    def create_tag_db():
        raise NotImplemented
        

def load_config():
    if CONFIG_FILE.exists():
        config = Config.load_existing_config()
        return config
    else:
        config = Config.create_new_config()
        return config



