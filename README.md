# Household
Home server management

## Server Stuff I'm Using

- Docker
- Gluster
- Traefik
- Portainer
- HAProxy

## Development Setup 

Must be run through WSL

Install the python dependencies with the `pdm` tool

```bash
pdm install
```

## Node Setup

### Debian
- Create User on Host
    - A part of the OS installation
    
- User Permissions on Host
    - `su -`
    - `apt update`
    - `apt install sudo -y`
    - `su - <username>`

- SSH Key Setup on Client
    - `ssh-keygen -b 4096`
    - `ssh-copy-id <username>@<hostname>`

- Disable SSH Passwords on Host
    - Edit `/etc/ssh/sshd_config`
    - Set `PasswordAuthentication no`
    - Restart

### Connect

`ssh <username>@<hostname>`

## Playbooks

Installing the stuff onto the nodes

```bash
ansible-playbook playbooks/install.yml
```

