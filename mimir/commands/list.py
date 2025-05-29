from mimir.database.handler import get_installed_packages
from mimir.util.output import title,end

def main(args, config):
    packages = get_installed_packages()
    title_txt = "Installed Packages"
    title(title_txt)
    for package in packages:
        print(f"{package[0]} ({package[2]})")
    end(title_txt)

