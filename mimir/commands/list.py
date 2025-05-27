from mimir.database.handler import get_installed_packages


def main(args, config):
    packages = get_installed_packages()
    print(packages)
