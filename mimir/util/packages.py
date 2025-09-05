import json
import tomllib
from mimir.util.constants import PACKAGE_FILE, PACKAGE_URL, PACKAGE_TOML_BASE
import requests
from mimir.util.output import info, error, debug, okay


def get_package(package_name: str):
    package_json = get_package_json()
    try:
        package_json[package_name]
    except:
        error(f"Could not find package with name '{package_name}'")
        exit()
    package = get_package_toml(package_name)
    return package


def get_package_json():
    if not PACKAGE_FILE.exists():
        okay("It seems like your run mimir for the first time. It downloads the package database. This may take some time.")
        package_json = download_package_json()
        save_package_json(package_json)
        okay("First time download finished")
        package_json = json.loads(package_json)
        return package_json["packages"]

    with open(PACKAGE_FILE, "r") as f:
        package_json = json.load(f)
        return package_json["packages"]

def get_description(package_name):
    packages_json = get_package_json()
    return packages_json[package_name]["description"]

# Apparently there is some caching problem with this idk why. It shouldn't cache stuff but it somehow does?!
def get_package_toml(package_name):
    try:
        info("Downloading toml file for package")
        package_toml = requests.get(PACKAGE_TOML_BASE + package_name + ".toml")
        if package_toml.status_code == 404:
            error("Package '{package_name}' on remote not found")
            exit()
    except requests.exceptions.RequestException:
        error("Could not download toml file. Please check your internet connection")
        exit()
    return tomllib.loads(package_toml.text)


def save_package_json(content):
    with open(PACKAGE_FILE, "w") as f:
            f.write(content)


def download_package_json():
    try:
        info("Downloading packages.json file")
        package_json = requests.get(PACKAGE_URL)
        if package_json.status_code == 404:
            error("Packages.json on remote not found")
            exit()
    except requests.exceptions.RequestException:
        error("Could not download packages.json file. Please check your internet connection")
        exit()
    return package_json.text
