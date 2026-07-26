# Homelab

This project manages a portable four-node Raspberry Pi 5 homelab. A MikroTik
router isolates the cluster from each location's upstream network, K3s runs the
workloads, and Pangolin Cloud provides stable remote access through an outbound
Newt tunnel.

## Start here

- [Architecture](architecture.md) explains the current and target network,
  address plan, provisioning lifecycle, ownership boundaries, and implementation
  status.
- [Commissioning and relocation](setup.md) describes safe cabling, first
  RouterOS access, node preparation, the planned operator commands, and the
  normal plug-and-power workflow.
- [Remote management](remote-management.md) defines the Back to Home bootstrap
  path, Pangolin private administration, recovery limitations, and safe
  RouterOS change procedure.

## Operational goal

Initial commissioning is an explicit, validated bootstrap operation. After
that, moving the lab should require only an Ethernet-based upstream connection,
the four direct Pi links, and power. RouterOS restores the stable LAN, the
host-level Newt service reconnects to Pangolin Cloud, system services start
K3s, and Flux reconciles workloads from Git.

The automation needed to reach that experience is still being implemented.
The documentation labels target behavior separately from capabilities already
present in the repository.
