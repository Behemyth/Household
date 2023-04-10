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

- [Github Documentation for Deployment Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)
    - `ssh-keygen -t ed25519 -C "<email>"` on the Server

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

