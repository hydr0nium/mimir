

# \[+\] ============ Mimir ============ \[+\]
##        The hacking package manager

mimir is package manager for pentesting or generally cybersecurity tools. It acts as a meta package manager and broker between
the installed package managers on that system. If a package is installed it automatically determins how the package can be installed
on that system and remembers how it was installed. It also features a rich search-engine-like search function that accounts for typos
and 'tagged' search. 

## Installation
mimir can easily be installed with pipx:
```bash
pipx install git+https://github.com/hydr0nium/mimir.git
```

## Usage
```
usage: mimir [command]

Available Commands:

    install      Install a tool
    uninstall    Uninstall a tool
    search       Search-engine like tool search
    help         Show help
    version      Show version
    list         List all installed packages
    update       Update a tool
    info         Info for a package
    update-repo  Update the local packages.json file

options:
  -h, --help     show this help message and exit

```
You can get more help by running `mimir help [command]` or `mimir [command] --help`

## TODO

-   [X] Implement tool installer
-   [X] Implement tool searcher
-   [X] Implement list feature
-   [X] Implement version feature
-   [X] Implement package info feature
-   [X] Implement updater
-   [X] Implement update-repo
-   [ ] Detect currently installed packages on first start
-   [ ] Implement updater for all packages 
-   [ ] Add overwrite to package manager choice
-   [ ] Finished info command
-   [X] Implement better debug mode
-   [X] Implement verbose mode
-   [X] QoL package format change
-   [X] Create config functionality
-   [X] Create local sqlite backend for installed tools


# Contribution:
## How to add a package:
1. Edit the package file in `packages/packages.json`. The `toolname` represents the name that is used to install the package with mimir:
```json
[...]
"toolname": {
                "tags":  ["first_tag", "second_tag", "third_tag", "..."],
                "description": "Here is some description ..."
            }
[...]
```
2. Add a `toolname.toml` file. Note that the name in the `packages.json` and the name of the toml file (without the extension) need to be the same. You only need to add the sections that are usable:
```toml
[apt]
name = "toolname" # Name of the apt package.

[pacman]
name = "toolname" # Name of the pacman package.

[pipx]
name = "toolname" # Name of the pipx package.
# git = git+https://[...] # Use instead of name if you want 'pure' git installs

[gem]
name = "toolname" # Name of the gem package.

[snap]
name = "toolname" # Name of the snap package.

[flatpak]
name = "toolname" # Name of the flatpak package.

[cargo]
name = "toolname" # Name of the cargo package.

[yay]
name = "toolname" # Name of the yay package.

[go]
name = "github.com/..." Path to the github of the package
```
3. Create a `pull request` for review. After the pull request is accepted your package should be good to go if people update their local `packages.json`.
