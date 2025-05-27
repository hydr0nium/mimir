
from mimir.util.packages import get_package
from mimir.util.constants import PACKAGE_MANAGERS
from subprocess import run, CalledProcessError
from mimir.until.output import error

def main(args, config):
	package_name = args.package_name
	package = get_package(package_name)
	print(package)


def install(package):
	for PACKAGE_MANAGER in PACKAGE_MANAGERS:
		if package[PACKAGE_MANAGER]["available"]:
			package_manager = PACKAGE_MANAGER + "_install"
			name = package[PACKAGE_MANAGER]["name"]
			break
	globals()[package_manager](name)

def apt_install(package):
	try:
		result = run(["sudo", "apt", "install", package], check=True, text=True, capture_output=True)
	except CalledProcessError as e:
		error(f"There was an error installing '{package}' with apt! Here is the apt error:")
		print(e.output)
		print(e.stderr)
		exit()

