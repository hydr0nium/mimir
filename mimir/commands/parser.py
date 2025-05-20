import argparse


def parse_arguments():
  parser = argparse.ArgumentParser(prog="mimir", usage="%(prog)s [command]")
  parser._positionals.title = "Available Commands"

  sub_parser = parser.add_subparsers(dest='command', required=True)
  sub_parser.metavar = ""
  init_install_parser(sub_parser)
  init_search_parser(sub_parser)
  init_help_parser(sub_parser)
  init_version_parser(sub_parser)
  return parser

def init_install_parser(sub_parser: argparse._SubParsersAction):
  install_parser = sub_parser.add_parser('install', help="Install a pentesting tool")
  install_parser._positionals.title = 'Arguments'
  return install_parser

def init_search_parser(sub_parser):
  search_parser = sub_parser.add_parser('search', help="Search-engine like hacking tool search")
  search_parser._positionals.title = 'Arguments'
  return search_parser

def init_help_parser(sub_parser: argparse._SubParsersAction):
  help_parser = sub_parser.add_parser("help", help="Show help")
  help_parser._positionals.title = 'Arguments'
  return help_parser

def init_version_parser(sub_parser: argparse._SubParsersAction):
  help_parser = sub_parser.add_parser("version", help="Show version")
  help_parser._positionals.title = 'Arguments'
  return help_parser