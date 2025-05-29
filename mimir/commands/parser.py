import argparse


SUBPARSER = {}

def parse_arguments():

  global_parser = argparse.ArgumentParser(add_help=False)
  global_parser.add_argument('--debug', action='store_true', help='Print debug messages')
  global_parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose messages')

 
  parser = argparse.ArgumentParser(prog="mimir", usage="%(prog)s [command]")
  parser._positionals.title = "Available Commands"

  sub_parser = parser.add_subparsers(dest='command', required=True)
  sub_parser.metavar = ""
  init_install_parser(sub_parser, global_parser)
  init_uninstall_parser(sub_parser, global_parser)
  init_search_parser(sub_parser, global_parser)
  init_help_parser(sub_parser, global_parser)
  init_version_parser(sub_parser, global_parser)
  init_list_parser(sub_parser, global_parser)
  init_update_parser(sub_parser, global_parser)
  init_info_parser(sub_parser, global_parser)
  init_updaterepo_parser(sub_parser, global_parser)
  return parser

def init_install_parser(sub_parser: argparse._SubParsersAction, global_parser):
  install_parser = sub_parser.add_parser('install', help="Install a tool", parents=[global_parser])
  SUBPARSER["install"] = install_parser
  install_parser._positionals.title = 'Arguments'
  install_parser.add_argument("package_name", help="The package that should be installed")
  return install_parser

def init_update_parser(sub_parser: argparse._SubParsersAction, global_parser):
  update_parser = sub_parser.add_parser('update', help="Update a tool", parents=[global_parser])
  SUBPARSER["update"] = update_parser
  update_parser._positionals.title = 'Arguments'
  update_parser.add_argument("package_name",  help="The package that should be updated")
  return update_parser

def init_uninstall_parser(sub_parser: argparse._SubParsersAction, global_parser):
  uninstall_parser = sub_parser.add_parser('uninstall', help="Uninstall a tool", parents=[global_parser])
  SUBPARSER["uninstall"] = uninstall_parser
  uninstall_parser._positionals.title = 'Arguments'
  uninstall_parser.add_argument("package_name", help="The package that should be uninstalled")
  return uninstall_parser

def init_search_parser(sub_parser, global_parser):
  search_parser = sub_parser.add_parser('search', help="Search-engine like tool search", parents=[global_parser])
  SUBPARSER["search"] = search_parser
  search_parser._positionals.title = 'Arguments'
  search_parser.add_argument("search_string", help="The string to be searched for")
  search_parser.add_argument("-l", "--limit", default=10, type=int, help="This limits the number of results (default: %(default)d)")
  search_parser.add_argument("-s", "--min-score", dest="min_score", default=40, type=int, help="The minimum 'match score' a package needs to have to be displayed (0-100) (default: %(default)d)")
  return search_parser

def init_help_parser(sub_parser: argparse._SubParsersAction, global_parser):
  help_parser = sub_parser.add_parser("help", help="Show help", parents=[global_parser])
  SUBPARSER["help"] = help_parser
  help_parser._positionals.title = 'Arguments'
  help_parser.add_argument("subcommand", default="help", type=str, nargs='?' , help="The command you want help for")
  return help_parser

def init_list_parser(sub_parser: argparse._SubParsersAction, global_parser):
  list_parser = sub_parser.add_parser("list", help="List all installed packages", parents=[global_parser])
  SUBPARSER["list"] = list_parser
  list_parser._positionals.title = 'Arguments'
  return list_parser

def init_version_parser(sub_parser: argparse._SubParsersAction, global_parser):
  version_parser = sub_parser.add_parser("version", help="Show version", parents=[global_parser])
  SUBPARSER["version"] = version_parser
  version_parser._positionals.title = 'Arguments'
  return version_parser

def init_updaterepo_parser(sub_parser: argparse._SubParsersAction, global_parser):
  updaterepo_parser = sub_parser.add_parser("update-repo", help="Update the local packages.json file", parents=[global_parser])
  SUBPARSER["update-repo"] = updaterepo_parser
  updaterepo_parser._positionals.title = 'Arguments'
  return updaterepo_parser

def init_info_parser(sub_parser: argparse._SubParsersAction, global_parser):
  info_parser = sub_parser.add_parser('info', help="Info for a package", parents=[global_parser])
  SUBPARSER["info"] = info_parser
  info_parser._positionals.title = 'Arguments'
  info_parser.add_argument("package_name", help="The package you want info on")
  return info_parser

def get_parsers():
  return SUBPARSER