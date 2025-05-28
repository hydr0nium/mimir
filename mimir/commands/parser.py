import argparse


SUBPARSER = {}

def parse_arguments():
  parser = argparse.ArgumentParser(prog="mimir", usage="%(prog)s [command]")
  parser._positionals.title = "Available Commands"

  sub_parser = parser.add_subparsers(dest='command', required=True)
  sub_parser.metavar = ""
  init_install_parser(sub_parser)
  init_uninstall_parser(sub_parser)
  init_search_parser(sub_parser)
  init_help_parser(sub_parser)
  init_version_parser(sub_parser)
  init_list_parser(sub_parser)
  init_update_parser(sub_parser)
  init_info_parser(sub_parser)
  return parser

def init_install_parser(sub_parser: argparse._SubParsersAction):
  install_parser = sub_parser.add_parser('install', help="Install a tool")
  SUBPARSER["install"] = install_parser
  install_parser._positionals.title = 'Arguments'
  install_parser.add_argument("package_name", help="The package that should be installed")
  return install_parser

def init_update_parser(sub_parser: argparse._SubParsersAction):
  update_parser = sub_parser.add_parser('update', help="Update a tool")
  SUBPARSER["update"] = update_parser
  update_parser._positionals.title = 'Arguments'
  update_parser.add_argument("package_name",  help="The package that should be updated")
  return update_parser

def init_uninstall_parser(sub_parser: argparse._SubParsersAction):
  uninstall_parser = sub_parser.add_parser('uninstall', help="Uninstall a tool")
  SUBPARSER["uninstall"] = uninstall_parser
  uninstall_parser._positionals.title = 'Arguments'
  uninstall_parser.add_argument("package_name", help="The package that should be uninstalled")
  return uninstall_parser

def init_search_parser(sub_parser):
  search_parser = sub_parser.add_parser('search', help="Search-engine like tool search")
  SUBPARSER["search"] = search_parser
  search_parser._positionals.title = 'Arguments'
  search_parser.add_argument("search_string", help="The string to be searched for")
  search_parser.add_argument("-l", "--limit", default=10, type=int, help="This limits the number of results (default: %(default)d)")
  search_parser.add_argument("-s", "--min-score", dest="min_score", default=40, type=int, help="The minimum 'match score' a package needs to have to be displayed (0-100) (default: %(default)d)")
  return search_parser

def init_help_parser(sub_parser: argparse._SubParsersAction):
  help_parser = sub_parser.add_parser("help", help="Show help")
  SUBPARSER["help"] = help_parser
  help_parser._positionals.title = 'Arguments'
  help_parser.add_argument("subcommand", default="help", type=str, nargs='?' , help="The command you want help for")
  return help_parser

def init_list_parser(sub_parser: argparse._SubParsersAction):
  list_parser = sub_parser.add_parser("list", help="List all installed packages")
  SUBPARSER["list"] = list_parser
  list_parser._positionals.title = 'Arguments'
  return list_parser

def init_version_parser(sub_parser: argparse._SubParsersAction):
  version_parser = sub_parser.add_parser("version", help="Show version")
  SUBPARSER["version"] = version_parser
  version_parser._positionals.title = 'Arguments'
  return version_parser

def init_info_parser(sub_parser: argparse._SubParsersAction):
  info_parser = sub_parser.add_parser('info', help="Info for a package")
  SUBPARSER["info"] = info_parser
  info_parser._positionals.title = 'Arguments'
  info_parser.add_argument("package_name", help="The package you want info on")
  return info_parser

def get_parsers():
  return SUBPARSER