# Machine Setup

We provide [network-config](#network-config) and [user-data](#user-data) files which `cloud-init` uses to config the OS on its first boot. Depending on if your configuring the [manager]() or [worker]() you can find the respective files that you should place next to the OS image in subdirectories to this README.

`cloud-init` is a standard most OSs/VMs have. Verify that the one your installing does as well.

The file `meta-data.yaml.template` contains the variables that you should manually replace. These variables are defined in jinja format but we do not use jinja for 

Below is the default description Ubuntu gives for each file.

## `network-config`

The initial netplan configuration for the network.

The format of this file is YAML, in the form expected by netplan which is
documented at:

https://netplan.io/

Examples for wifi and ethernet are included, but you may also configure bonds,
bridges, etc. in this file.

## `user-data`

The user-data of the cloud-init seed. This can be used to customize numerous
aspects of the system upon first boot, from the default user, the default
password, whether or not SSH permits password authentication, import of SSH
keys, the keyboard layout, the system hostname, package installation, creation
of arbitrary files, etc. Numerous examples are included (mostly commented) in
the default user-data.

The format of this file is YAML, and is documented at:

https://cloudinit.readthedocs.io/en/latest/topics/modules.html
https://cloudinit.readthedocs.io/en/latest/topics/examples.html