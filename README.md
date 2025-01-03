# Household
Home server management.

Contents:

- [Machine Setup ](#machine-setup)  
- [Development Setup ](#development-setup)  
- [Directory Structure](#directory-structure)  

## Server Stuff I'm Using

- Docker
- Ceph
- Traefik
- Portainer

## Machine Setup 

- SSH Key Setup on the host if you don't already have one
    - `ssh-keygen -t ed25519`
    - The public key will be used for the worker and manager configuration

- SSH Key Setup for `mini-behemyth`
    - `ssh-keygen -t ed25519 -f manager-ssh`
    - The public and private key will be used for the manager configuration
    - The public key will be used for the worker configuration

Follow the steps listed in [the boot configuration files](/config/boot/README.md). 

## Development Setup 

**Must be run through WSL**, and **not** on the shared mount.

- Clone the repository to a directory of choice
    - `git clone https://github.com/Behemyth/Household.git`

- Setup `pipx` and `pdm` if they are not already on the distribution
    - `sudo apt install pipx`
    - `pipx ensurepath`
    - `pipx install pdm`

- Install the python dependencies with the `pdm` tool
    - Set the git repository as the current directory
    - `pdm install`

- Log into Azure for key vault access
    - `az login --service-principal --username <client-id> --password <client-secret> --tenant <tenant-id>`

## First-time Server Setup

### Network Setup

- Install the manager OS with the instruction described in [Machine Setup](#machine-setup)
    
- Create DMZ to `mini-behemyth` from router

- Forward ports to `mini-behemyth`
    - 60
    - 22
    - 443

- Add Static Route from router
    - Destination: `10.42.0.0`
    - Gateway: `10.4.2.42`
    - Netmask: `255.255.255.0`
    - Metric: `0`

- Setup Static Worker Ips: 

    | Hostname | IP Address | `mini-behemyth` Connection |
    | :--- | :--- | :--- |
    | mini-behemyth | 10.4.2.42 | Wired connection 1 |
    | mini-wumpus | 10.42.0.10 | Wired connection 2 |
    | mini-mush | 10.42.0.11 | Wired connection 3 |
    | mini-mouse | 10.42.0.12 | Wired connection 4 |
    | mini-sota | 10.42.0.13 | Wired connection 5 |

### Connect

```bash
ssh <username>@<hostname>
```

## Directory Structure

### **/ansible**

Installing the stuff onto the workers

```bash
ansible-playbook ansible/install.yml
```
#### **/inventory**

##### *hosts.yml*
List of the devices

#### **/roles**

### **/tests**
