# First-time Server Setup

## Machine Setup 

- SSH Key Setup on the host if you don't already have one. I'm using a WSL instance on my desktop as the host.
    - `ssh-keygen -t ed25519`
    - The public key will be used for the worker and manager configuration

- SSH Key Setup for `mini-behemyth`, or whatever you name the manager
    - `ssh-keygen -t ed25519 -f manager-ssh`
    - The public and private key will be used for the manager configuration
    - The public key will be used for the worker configuration

Follow the steps listed in [the boot configuration files](/config/boot/README.md) for either the manager or workers. 

## Network Setup

- Install the OSs with the instruction described in [Machine Setup](#machine-setup)
    
- Add a static DHCP entry for `mini-behemyth`. This gives the benefit of hostname discovery with a consistent ip address.

- Create DMZ to `mini-behemyth` from router. In essence, forwarding all ports.

**NOTE** I recently removed the static route from the router.
- Add Static Route from router
    - Destination: `10.42.0.0`
    - Gateway: `10.4.2.42`
    - Netmask: `255.255.255.0`
    - Metric: `0`

### Manager Setup

The setup on the manager machine will look like this:

| Hostname | IP Address | `mini-behemyth` Interface Name |
| :--- | :--- | :--- |
| mini-behemyth | 10.42.0.1 | enp1s0 |
| mini-wumpus | 10.42.0.10 | enp2s0 |
| mini-mush | 10.42.0.11 | enp3s0 |
| mini-mouse | 10.42.0.12 | enp4s0 |
| mini-sota | 10.42.0.13 | enp5s0 |

## Connect

```bash
ssh synodic@<hostname>
```