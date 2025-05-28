

# \[+\] ============ Mimir ============ \[+\]
##        The hacking package manager

mimir is package manager for pentesting or generally cybersecurity tools. It acts as a meta package manager and broker between
the installed package managers on that system. If a package is installed it automatically determins how the package can be installed
on that system and remembers how it was installed. It also features a rich search-engine-like search function that accounts for typos
and 'tagged' search. 

# TODO

-   [X] Implement tool installer
-   [X] Implement tool searcher
-   [X] Implement list feature
-   [X] Implement version feature
-   [ ] Implement package info feature
-   [ ] Implement updater
-   [ ] Imlement upgrader
-   [X] Create config functionality
-   [X] Create local sqlite backend for installed tools


# Contribution:
## How to add a package:
1. Edit the package file in `packages/packages.json`. The blueprint looks like this:
```json
[...]
"toolname": {
                "name": "name_of_toml_without_extension", 
                "version": "1.0",
                "tags":  ["first_tag", "second_tag", "third_tag", "..."],
                "description": "Here is some description ..."
            }
[...]
```
2. Add a `some_package.toml` file. Note that the name field in the `packages.json` needs to match the name of the file without the extension. Here is the blueprint of that file:
```toml
[package]
name = "toolname" # Same as key in packages.json

[apt]
available = false # Set this to true of the package can be installed with this package manager
name = "toolname" # Name of the apt package. Doesn't matter if available is false

[pacman]
available = false # Set this to true of the package can be installed with this package manager
name = "toolname" # Name of the pacman package. Doesn't matter if available is false

[pipx]
available = false # Set this to true of the package can be installed with this package manager
name = "toolname" # Name of the pipx package. Doesn't matter if available is false
# git = git+https://[...] # Use instead of name if you want 'pure' git installs

[gem]
available = false # Set this to true of the package can be installed with this package manager
name = "toolname" # Name of the gem package. Doesn't matter if available is false

[snap]
available = false # Set this to true of the package can be installed with this package manager
name = "toolname" # Name of the snap package. Doesn't matter if available is false

[flatpak]
available = false # Set this to true of the package can be installed with this package manager
name = "toolname" # Name of the flatpak package. Doesn't matter if available is false

[cargo]
available = false # Set this to true of the package can be installed with this package manager
name = "toolname" # Name of the cargo package. Doesn't matter if available is false

[yay]
available = false # Set this to true of the package can be installed with this package manager
name = "toolname" # Name of the yay package. Doesn't matter if available is false
```
3. Create a `pull request` for review. After the pull request is accepted your package should be good to go if people update their local `packages.json`.
