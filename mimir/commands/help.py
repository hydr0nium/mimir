from mimir.commands.parser import get_parsers
from mimir.util.output import error, title, end

def main(args, config):
    command = args.subcommand
    SUBPARSER = get_parsers()
    try:
        SUBPARSER[command].print_help()
    except KeyError:
        error(f"Could not find command: {command}")
