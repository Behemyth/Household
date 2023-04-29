# Household
Home server management.

Contents:

- [Development Setup ](#development-setup)  
- [Server Setup ](#server-setup)  
- [Directory Structure](#directory-structure)  

## Server Stuff I'm Using

- Docker
- Gluster
- Traefik
- Portainer
- HAProxy

## Development Setup 

Must be run through WSL, and not on the shared mount.

Install the python dependencies with the `pdm` tool

```bash
pdm install
```

Log into Azure for key vault access

## Server Setup

### SSH Setup
- Create User on Server
    - A part of the OS installation
    
- User Permissions on Server
    - `su -`
    - `apt update`
    - `apt install sudo -y`
    - `su - <username>`

- SSH Key Setup on Development Machine
    - `ssh-keygen -t ed25519 -C "<email>"`
    - `ssh-copy-id <username>@<hostname>`

- Disable SSH Passwords on Server
    - Edit `/etc/ssh/sshd_config`
    - Set `PasswordAuthentication no`
    - Restart

### Network Setup

- Expose Ports and Forward to Manager: `mini-behemyth`
    - 443
    - 22

- Add Static IPs to DNS
    - `mini-behemyth` 10.4.2.42

- Setup Static Worker Ips: 

    | Hostname | IP Address | `mini-behemyth` Connection |
    | :--- | :--- | :--- |
    | mini-behemyth | 10.4.2.42 | Wired connection 1 |
    | mini-wumpus | 10.42.0.10 | Wired connection ? |
    | mini-mush | 10.42.0.11 | Wired connection ? |
    | mini-mouse | 10.42.0.12 | Wired connection 2 |
    | mini-sota | 10.42.0.13 | Wired connection ? |

#### Worker Node Setup
- Start network manager
    - `sudo systemctl start NetworkManager.service`
- Enable reboots startups
    - `sudo systemctl enable NetworkManager.service`

- Remove all interfaces except `Wired connection 1`

### Connect

```bash
ssh <username>@<hostname>
```

## Directory Structure

### **/ansible**

Installing the stuff onto the nodes

```bash
ansible-playbook ansible/install.yml
```
#### **/inventory**

##### *hosts.yml*
List of the devices

#### **/roles**

##### *manager-network*
This is a role for setting up the manager network to all the worker nodes

##### *worker-network*
Once the manual labor is done and the manager network is setup, this role modifies all the workers

### **/tests**

pytest tests verifying server infrastructure so that ansible is garunteed to connect and execute as intended