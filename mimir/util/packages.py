import json
import tomllib
from mimir.util.constants import PACKAGE_FILE, PACKAGE_URL, PACKAGE_TOML_BASE
import requests


def get_package(package_name: str):
    package_json = get_package_json()
    package = package_json[package_name]
    print(package)
    package_name = package["name"]
    package = get_package_toml(package_name)
    return package


def get_package_json():
    if not PACKAGE_FILE.exists():
        package_json = download_package_json()
        with open(PACKAGE_FILE, "w") as f:
            f.write(package_json)
        return package_json["packages"]

    with open(PACKAGE_FILE, "r") as f:
        package_json = json.load(f)
        return package_json["packages"]

def get_package_toml(package_name):
    package_toml = requests.get(PACKAGE_TOML_BASE + package_name + ".toml")
    return tomllib.loads(package_toml.text)


def download_package_json():
    package_json = requests.get(PACKAGE_URL)
    return package_json.text