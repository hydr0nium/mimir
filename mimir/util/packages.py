import json
import tomllib
from mimir.util.constants import PACKAGE_FILE, PACKAGE_URL, PACKAGE_TOML_BASE
import requests
from mimir.util.output import info, error, debug


def get_package(package_name: str):
    package_json = get_package_json()
    try:
        package = package_json[package_name]
    except:
        error(f"Could not find package with name '{package_name}'")
        exit()
    package_name = package["name"]
    package = get_package_toml(package_name)
    return package


def get_package_json():
    if not PACKAGE_FILE.exists():
        package_json = download_package_json()
        with open(PACKAGE_FILE, "w") as f:
            f.write(package_json)
        package_json = json.loads(package_json)
        return package_json["packages"]

    with open(PACKAGE_FILE, "r") as f:
        package_json = json.load(f)
        return package_json["packages"]



# Apparently there is some caching problem with this idk why. It shouldn't cache stuff but it somehow does?!
def get_package_toml(package_name):
    try:
        info("Downloading toml file for package")
        package_toml = requests.get(PACKAGE_TOML_BASE + package_name + ".toml")
    except requests.exceptions.RequestException:
        error("Could not download toml file. Please check your internet connection!")
    return tomllib.loads(package_toml.text)


def download_package_json():
    try:
        info("Downloading packages.json file")
        package_json = requests.get(PACKAGE_URL)
    except requests.exceptions.RequestException:
        error("Could not download packages.json file. Please check your internet connection!")
    return package_json.text