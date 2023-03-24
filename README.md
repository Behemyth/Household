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
- Create User and Password
- User Sudo Permission
- SSH Key Setup
- Disable Passwords

## Playbooks

Installing the stuff onto the nodes

```bash
ansible-playbook playbooks/install.yml
```

