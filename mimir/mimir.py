from mimir.commands.parser import parse_arguments
from mimir.config.loader import load_config
import mimir.commands.install as mimir_install
import mimir.commands.search as mimir_search
import mimir.commands.version as mimir_version
import mimir.commands.list as mimir_list
import mimir.commands.uninstall as mimir_uninstall
import mimir.commands.update as mimir_update
import mimir.commands.info as mimir_info
import mimir.commands.help as mimir_help
from mimir.database.handler import create_db


def main():

    parser = parse_arguments()
    args = parser.parse_args()
    config = load_config()
    create_db()

    match args.command:
        case "install":
            mimir_install.main(args, config)
        case "uninstall":
            mimir_uninstall.main(args, config)
        case "search":
            mimir_search.main(args, config)
        case "update":
            mimir_update.main(args, config)
        case "list":
            mimir_list.main(args, config)
        case "info":
            mimir_info.main(args, config)
        case "version":
            mimir_version.main()
        case "help":
            if args.subcommand == "help":
                parser.print_help()
            else:
                mimir_help.main(args, config)
        case _:
            parser.print_help()
	