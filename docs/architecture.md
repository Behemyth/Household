# Architecture

## Overview

A portable homelab cluster built from 4 Raspberry Pi 5s, managed by a MikroTik router and exposed to the internet through Pangolin Cloud with a Newt tunnel client running as a container on the MikroTik.

## Network Topology

```mermaid
graph TB
    internet((Internet))
    pangolin_cloud((Pangolin Cloud))

    subgraph Home Network
        home_router[Home Router<br/>Dynamic IP]

        subgraph Cluster LAN – 10.42.0.0/24
            mikrotik[MikroTik hEX S 2025<br/>DHCP · L2 Bridge<br/>Newt Container<br/>10.42.0.1]
            pi1[mini-wumpus<br/>Raspberry Pi 5<br/>10.42.0.10]
            pi2[mini-mush<br/>Raspberry Pi 5<br/>10.42.0.11]
            pi3[mini-mouse<br/>Raspberry Pi 5<br/>10.42.0.12]
            pi4[mini-sota<br/>Raspberry Pi 5<br/>10.42.0.13]
        end
    end

    internet <--> pangolin_cloud
    pangolin_cloud <-.->|Reverse Tunnel| mikrotik
    home_router --- mikrotik
    mikrotik --- pi1
    mikrotik --- pi2
    mikrotik --- pi3
    mikrotik --- pi4
```

| Device | Hostname | IP | Role |
|--------|----------|----|------|
| MikroTik hEX S (2025) | — | 10.42.0.1 | DHCP server, L2 bridge, Newt tunnel client (container) |
| Raspberry Pi 5 | mini-wumpus | 10.42.0.10 | K3s node |
| Raspberry Pi 5 | mini-mush | 10.42.0.11 | K3s node |
| Raspberry Pi 5 | mini-mouse | 10.42.0.12 | K3s node |
| Raspberry Pi 5 | mini-sota | 10.42.0.13 | K3s node |

### Key points

- **Dynamic IP** — The home connection has no static IP. Pangolin Cloud provides a stable public endpoint. A Newt tunnel client runs as a container on the MikroTik, maintaining the reverse tunnel to Pangolin Cloud.
- **DHCP** — The MikroTik assigns IPs to all Pis on the `10.42.0.0/24` subnet.
- **L2 bridge** — The MikroTik bridges all Pi-facing ports at layer 2. Routing/NAT between the cluster and the home network is TBD.
- **MikroTik model** — hEX S (2025), product code E60iUGS. ARM 32-bit, 512 MB RAM, 128 MB NAND, USB 3.0. Supports RouterOS v7 containers.

## Boot & Provisioning Flow

```mermaid
flowchart TD
    A[Flash SD cards with Ubuntu + cloud-init] --> B[Insert SD cards into Pis]
    B --> C[Power on Pis]
    C --> D[cloud-init runs on first boot]
    D --> E[Network configured via DHCP from MikroTik]
    E --> F[Install ansible-core via pip]
    F --> G[Clone behemyth/homelab from GitHub]
    G --> H[Run autoinstall playbook]
    H --> I[init_manager role on control plane Pi]
    H --> J[init_worker role on agent Pis]
    I --> K[K3s server initialized]
    J --> L[K3s agents join cluster]
    L --> M[Cluster ready]
    K --> M
```

### Current state

- The `init_manager` role updates APT and configures DHCP (via `synodic.core.dhcp`). DHCP responsibility is moving to the MikroTik, so this role will be reworked.
- The `init_worker` role is a stub.
- SD card flashing is manual — automation is a goal but the method is TBD.

## Software Stack

```mermaid
graph TB
    pangolin_cloud((Pangolin Cloud))

    subgraph MikroTik hEX S 2025
        newt[Newt Container<br/>Tunnel Client]
        dhcp[DHCP Server]
    end

    subgraph K3s Cluster – 4x Raspberry Pi 5
        direction TB

        subgraph Control Plane – 1 Pi
            k3s_server[K3s Server]
        end

        subgraph Agents – 3 Pis
            k3s_agent1[K3s Agent]
            k3s_agent2[K3s Agent]
            k3s_agent3[K3s Agent]
        end

        k3s_server --- k3s_agent1
        k3s_server --- k3s_agent2
        k3s_server --- k3s_agent3

        subgraph Workloads – TBD
            workload[Services deployed via K3s]
        end
    end

    pangolin_cloud <-.->|Reverse Tunnel| newt
    newt --> k3s_server
```

### Decisions

| Topic | Status |
|-------|--------|
| MikroTik model | E60iUGS (hEX S 2025) — decided |
| Ingress method | Pangolin Cloud + Newt container on MikroTik — decided |
| K3s topology (dedicated control plane vs. dual-role) | TBD |
| Which Pi is the control plane | TBD |
| Cluster workloads | TBD |
| SD card flashing automation | TBD |
| Network boot (PXE) as alternative to SD | Open to exploring |

## Ansible Structure

This cluster is managed by the `behemyth.homelab` Ansible collection.

| Playbook | Target | Purpose |
|----------|--------|---------|
| `setup.yml` | localhost | Developer workstation setup |
| `install.yml` | managers, workers | Full cluster initialization |
| `autoinstall.yml` | localhost, workers | First-boot provisioning via cloud-init |

| Role | Applied to | Purpose |
|------|-----------|---------|
| `init_manager` | Manager Pi | APT update, DHCP setup (being reworked) |
| `init_worker` | Worker Pis | TBD (stub) |
> **Note:** The MikroTik (including the Newt container) is configured via RouterOS CLI/WinBox, not Ansible.