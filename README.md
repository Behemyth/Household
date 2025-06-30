# Homelab
Home server management.
___

## Development Setup 

**Must be run through WSL**, and **not** on the shared mount.

**TODO: Bypass the vscode-ansible extension requiring absolute paths**

- Setup `pipx` and `pdm` if they are not already on the distribution
    - `sudo apt install pipx`
    - `pipx ensurepath`
    - `pipx install pdm`

- Install the python dependencies with the `pdm` tool
    - `pdm install`

- Install system dependencies with a `pdm` script
    - `pdm setup`

## Directory Structure

### **/ansible**

#### **/inventory**

##### *hosts.yml*
List of the devices

#### **/roles**

### **/tests**
