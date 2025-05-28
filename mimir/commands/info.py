from mimir.database.handler import get_installed_package
from mimir.util.packages import get_description
from mimir.util.output import debug, title, end, info, okay, error
from subprocess import run as subprocess_run, CalledProcessError
import re

def main(args, config):
    package_name = args.package_name
    package_installed = get_installed_package(package_name)
    installed = package_installed != None
    title_txt = "Package Info"
    title(title_txt)
    print(f"Package: {package_name} {'(Installed)' if installed else '(Not Installed)'} {'(' + package_installed[1] + ')' if installed else ''}")
    if installed:
        version = get_version(package_installed)
        print(f"Version: {version}")
    print(f"Description: {get_description(package_name)}")
    end(title_txt)


def get_version(package_installed):
    pkg_name = package_installed[0]
    pkg_manager = package_installed[1]
    version = globals()[pkg_manager + "_version"](pkg_name)
    return version

def apt_version(pkg_name):
    pkg_manager = "apt"
    pattern = r".*Installed: (.*)"
    command = ["apt", "show", pkg_name]
    result = run(command, pkg_manager, pkg_name)
    m = re.search(pattern, result)
    return m.group(1)

def pacman_version(pkg_name):
    pkg_manager = "pacman"
    pattern = pkg_name + r" (.*)$"
    command = ["pacman", "-Q", pkg_name]
    result = run(command, pkg_manager, pkg_name)
    m = re.search(pattern, result)
    return m.group(1)

def pipx_version(pkg_name):
    pkg_manager = "pipx"
    pattern = r".*package " + pkg_name + r" (.*),"
    command = ["pipx", "list"] # Thanks to pipx we need to get all packages and filter for the one installed ...
    result = run(command, pkg_manager, pkg_name)
    m = re.search(pattern, result)
    return m.group(1)

def run(command, package_manager, package):
    try:
        result = subprocess_run(command, check=True, capture_output=True, text=True)
    except CalledProcessError as e:
        error(f"There was an error get the version of '{package}' with {package_manager}! Here is the {package_manager} error:")
        print(e.stderr)
        exit()
    return result.stdout
