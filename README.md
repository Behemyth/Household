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

Follow the steps listed in [the boot configuration files](/config/boot/README.md). 

## Development Setup 

Must be run through WSL, and not on the shared mount.

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
    
**This section can be replaced with ansible**
- SSH Key Setup on `mini-behemyth`
    - `ssh-keygen -t ed25519 -C "<email>"`
    - `ssh-copy-id <username>@<hostname>`

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
    | mini-wumpus | 10.42.0.10 | Wired connection 3 |
    | mini-mush | 10.42.0.11 | Wired connection 5 |
    | mini-mouse | 10.42.0.12 | Wired connection 2 |
    | mini-sota | 10.42.0.13 | Wired connection 4 |

#### Manager Setup

- SSH Key Setup on `mini-behemyth`
    - `ssh-keygen -t ed25519 -C "<email>"`

- Enable password authentication temporarily on `mini-behemyth`
    - `sudo nano /etc/ssh/sshd_config`
    - Set `ChallengeResponseAuthentication yes`
    - Set `PasswordAuthentication yes`
    - `sudo service sshd restart`


- For each worker:
    - Enable password authentication temporarily
        - `sudo nano /etc/ssh/sshd_config`
        - Set `ChallengeResponseAuthentication yes`
        - Set `PasswordAuthentication yes`
        - `sudo service sshd restart`

    - Copy the ID to the worker from `mini-behemyth`
        - `ssh-copy-id <username>@<hostname>`

    - Copy the ID to the worker from `behemyth`
        - `ssh-copy-id -o ProxyJump=<username>@mini-behemyth <username>@<hostname>`

    - Disable password authentication
        - `sudo nano /etc/ssh/sshd_config`
        - Set `ChallengeResponseAuthentication no`
        - Set `PasswordAuthentication no`
        - `sudo service sshd restart`

- Disable password authentication for `mini-behemyth`
    - `sudo nano /etc/ssh/sshd_config`
    - Set `ChallengeResponseAuthentication no`
    - Set `PasswordAuthentication no`
    - `sudo service sshd restart`

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
