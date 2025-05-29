from mimir.util.packages import download_package_json, save_package_json
from mimir.util.output import okay

def main(args, config):
    okay("You are updating the local repo file (packages.json). Depending on its size this may take some time.")
    package_json = download_package_json()
    save_package_json(package_json)
    okay("Successfully updated the local packages.json repo")