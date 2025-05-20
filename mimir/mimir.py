from mimir.commands.parser import parse_arguments
from mimir.config.loader import load_config
import mimir.commands.install as mimir_install
import mimir.commands.search as mimir_search
import mimir.commands.version as mimir_version



def main():

    parser = parse_arguments()
    args = parser.parse_args()
    config = load_config()

    match args.command:
        case "install":
            mimir_install.main(args, config)
        case "search":
            mimir_search.main(args, config)
        case "update":
            raise NotImplemented
        case "list":
            raise NotImplemented
        case "version":
            mimir_version.main()
        case "help":
            parser.print_help()
        case _:
            parser.print_help()
	