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

### SSH Setup
- Create User on Server
    - A part of the OS installation
    
- User Permissions on Server
    - `su -`
    - `apt update`
    - `apt install sudo -y`
    - `su - <username>`

- SSH Key Setup on Development Machine
    - `ssh-keygen -b 4096`
    - `ssh-copy-id <username>@<hostname>`

- Disable SSH Passwords on Server
    - Edit `/etc/ssh/sshd_config`
    - Set `PasswordAuthentication no`
    - Restart

### Github Setup

- Generate key pair
    -`ssh-keygen -t ed25519 -C "<email>" -f id_github`
    -`ssh-copy-id -i id_github <username>@<hostname>`
    - Add private key to Github Secrets

### Router

- Expose Ports and Forward to Server
    - 443
    - 22

### Connect

```bash
ssh <username>@<hostname>
```

## Playbooks

Installing the stuff onto the nodes

```bash
ansible-playbook playbooks/install.yml
```

