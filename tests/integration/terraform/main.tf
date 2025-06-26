terraform {
  required_providers {
    lxd = {
      source  = "sl1pm4t/lxd"
      version = "~> 1.7"
    }
  }
}

provider "lxd" {}

resource "lxd_container" "manager" {
  name   = "manager-1"
  image  = "ubuntu:22.04"
  devices = {
    eth0 = {
      name = "eth0"
      network = "lxdbr0"
      type = "nic"
    }
  }
}

resource "lxd_container" "worker" {
  count  = 4
  name   = "worker-${count.index + 1}"
  image  = "ubuntu:22.04"
  devices = {
    eth0 = {
      name = "eth0"
      network = "lxdbr0"
      type = "nic"
    }
  }
}

output "manager_ip" {
  value = lxd_container.manager[0].ipv4_address
}

output "worker_ips" {
  value = [for w in lxd_container.worker : w.ipv4_address]
}