
from mimir.util.packages import get_package
from mimir.util.constants import PACKAGE_MANAGERS
from subprocess import run as subprocess_run, CalledProcessError
from mimir.util.output import error,info,get, okay
from mimir.database.handler import add_installed_package

def main(args, config):
	package_name = args.package_name
	package = get_package(package_name)
	info(f"Preparing to install package: '{package_name}'")
	install(package, config)
	okay(f"Successfully installed '{package_name}'")


def install(package, config):
	info(f"Searching through available package managers")
	for PACKAGE_MANAGER in PACKAGE_MANAGERS:
		if package[PACKAGE_MANAGER]["available"] and config.getboolean("package_managers", PACKAGE_MANAGER):
			manager = PACKAGE_MANAGER
			details = package[PACKAGE_MANAGER]
			break
	else:
		error(f"Could not find package!")
		exit()
	globals()[manager + "_install"](details)
	add_installed_package(package["package"]["name"], details["name"], manager)

def apt_install(details):
	package = details["name"]
	package_manager = "apt"
	command = ["sudo", package_manager, "install", package]
	run(command, package_manager, package)

def pacman_install(details):
	package = details["name"]
	package_manager = "pacman"
	command = ["sudo", package_manager, "-S", package]
	run(command, package_manager, package)

def pipx_install(details):
	package = details["name"]
	if "git" in details:
		package = details["git"]
	package_manager = "pipx"
	command = [package_manager, "install", package]
	run(command, package_manager, package)

def yay_install(details):
	package = details["name"]
	package_manager = "yay"
	command = [package_manager, "-S", package]
	run(command, package_manager, package)


def snap_install(details):
	package = details["name"]
	package_manager = "snap"
	command = ["sudo", package_manager, "install", package]
	run(command, package_manager, package)

def flatpak_install(details):
	package = details["name"]
	package_manager = "flatpak"
	command = [package_manager, "install", package]
	run(command, package_manager, package)

def cargo_install(details):
	package = details["name"]
	package_manager = "cargo"
	command = [package_manager, "install", package]
	run(command, package_manager, package)

def gem_install(details):
	package = details["name"]
	package_manager = "gem"
	command = [package_manager, "install", package]
	run(command, package_manager, package)



def run(command, package_manager, package):
	info(f"Using {package_manager}")
	confirm(package, package_manager)
	while True:
		try:
			result = subprocess_run(command, check=True)
			break
		except CalledProcessError as e:
			error(f"There was an error installing '{package}' with {package_manager}! Here is the {package_manager} error:")
			print(e.stderr)
			break
		except KeyboardInterrupt:
			res = get(f"Are you sure you want to quit? This will potentially break the internal database! [y/n]: ")
			if res != "y":
				error(f"Quitting")
				exit()




def confirm(package, package_manager):
	res = get(f"Are you sure you want to install '{package}' with {package_manager}? [y/n]: ")
	if res != "y":
		error(f"Aborting")
		exit()
