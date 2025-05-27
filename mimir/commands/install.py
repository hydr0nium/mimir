
from mimir.util.packages import get_package
from mimir.util.constants import PACKAGE_MANAGERS
from subprocess import run as subprocess_run, CalledProcessError
from mimir.util.output import error,info,get

def main(args, config):
	package_name = args.package_name
	package = get_package(package_name)
	info(f"Preparing to install package: '{package_name}'")
	install(package, config)


def install(package, config):
	info(f"Searching through available package managers")
	for PACKAGE_MANAGER in PACKAGE_MANAGERS:
		if package[PACKAGE_MANAGER]["available"] and config.getboolean("package_managers", PACKAGE_MANAGER):
			manager = PACKAGE_MANAGER + "_install"
			name = package[PACKAGE_MANAGER]["name"]
			break
	globals()[manager](name)

def apt_install(package):
	package_manager = "apt"
	command = ["sudo", package_manager, "install", "-y", package]
	run(command, package_manager, package)

def pacman_install(package):
	package_manager = "pacman"
	command = ["sudo", package_manager, "-Sy", package]
	run(command, package_manager, package)


def run(command, package_manager, package):
	info(f"Using {package_manager}")
	confirm(package, package_manager)
	try:
		result = subprocess_run(command, check=True, text=True, capture_output=True)
	except CalledProcessError as e:
		error(f"There was an error installing '{package}' with {package_manager}! Here is the {package_manager} error:")
		print(e.stderr)

def confirm(package, package_manager):
	res = get(f"Are you sure you want to install '{package}' with {package_manager}? [y/n]: ")
	if res != "y":
		error(f"Aborting")
		exit()
