import argparse


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
  return parser

def init_install_parser(sub_parser: argparse._SubParsersAction):
  install_parser = sub_parser.add_parser('install', help="Install a tool")
  install_parser._positionals.title = 'Arguments'
  install_parser.add_argument("package_name")
  return install_parser

def init_update_parser(sub_parser: argparse._SubParsersAction):
  update_parser = sub_parser.add_parser('update', help="Update a tool")
  update_parser._positionals.title = 'Arguments'
  update_parser.add_argument("package_name")
  return update_parser

def init_uninstall_parser(sub_parser: argparse._SubParsersAction):
  uninstall_parser = sub_parser.add_parser('uninstall', help="Uninstall a tool")
  uninstall_parser._positionals.title = 'Arguments'
  uninstall_parser.add_argument("package_name")
  return uninstall_parser

def init_search_parser(sub_parser):
  search_parser = sub_parser.add_parser('search', help="Search-engine like tool search")
  search_parser._positionals.title = 'Arguments'
  search_parser.add_argument("search_string")
  return search_parser

def init_help_parser(sub_parser: argparse._SubParsersAction):
  help_parser = sub_parser.add_parser("help", help="Show help")
  help_parser._positionals.title = 'Arguments'
  return help_parser

def init_list_parser(sub_parser: argparse._SubParsersAction):
  list_parser = sub_parser.add_parser("list", help="List all installed packages")
  list_parser._positionals.title = 'Arguments'
  return list_parser

def init_version_parser(sub_parser: argparse._SubParsersAction):
  version_parser = sub_parser.add_parser("version", help="Show version")
  version_parser._positionals.title = 'Arguments'
  return version_parser