
from mimir.database.handler import check_install, get_installed_package, remove_package_from_db
from mimir.util.packages import get_package
from subprocess import run as subprocess_run, CalledProcessError
from mimir.util.output import error,info,get


def main(args, config):
    package_name = args.package_name
    if not check_install(package_name):
        error("Package not found!")
        return
    package = get_installed_package(package_name)
    installed_name = package[0]
    package_manager = package[1]
    globals()[package_manager + "_uninstall"](installed_name)
    remove_package_from_db(package_name)

def apt_uninstall(package):
	package_manager = "apt"
	command = ["sudo", package_manager, "remove", package]
	run(command, package_manager, package)

def pacman_uninstall(package):
	package_manager = "pacman"
	command = ["sudo", package_manager, "-R", package]
	run(command, package_manager, package)

def pipx_uninstall(package):
	package_manager = "pipx"
	command = [package_manager, "uninstall", package]
	run(command, package_manager, package)

def yay_uninstall(package):
	package_manager = "yay"
	command = [package_manager, "-R", package]
	run(command, package_manager, package)


def snap_uninstall(package):
	package_manager = "snap"
	command = ["sudo", package_manager, "uninstall", package]
	run(command, package_manager, package)

def flatpak_uninstall(package):
	package_manager = "flatpak"
	command = [package_manager, "uninstall", package]



def run(command, package_manager, package):
	info(f"Using {package_manager}")
	confirm(package, package_manager)
	while True:
		try:
			result = subprocess_run(command, check=True)
			break
		except CalledProcessError as e:
			error(f"There was an error uninstalling '{package}' with {package_manager}! Here is the {package_manager} error:")
			print(e.stderr)
			break
		except KeyboardInterrupt:
			res = get(f"Are you sure you want to quit? This will potentially break the internal database! [y/n]: ")
			if res != "y":
				error(f"Quitting")
				exit()


def confirm(package, package_manager):
	res = get(f"Are you sure you want to uninstall '{package}' from {package_manager}? [y/n]: ")
	if res != "y":
		error(f"Aborting")
		exit()