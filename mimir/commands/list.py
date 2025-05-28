from mimir.database.handler import get_installed_packages


def main(args, config):
    packages = get_installed_packages()
    print("="*10 + "Installed Packages" + "="*10)
    for package in packages:
        print(package[0])
    print("="*10 + "="*18 + "="*10)

