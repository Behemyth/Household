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

## Directory Structure

### /inventory

### /ansible

Installing the stuff onto the nodes

```bash
ansible-playbook ansible/install.yml
```

### /roles

Reusable crap

### /tests

pytest tests verifying server infrastructure so that ansible is garunteed to connect