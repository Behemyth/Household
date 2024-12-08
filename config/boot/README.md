# Machine Setup

We provide [network-config](#network-config), [meta-data](#meta-data), and [user-data](#user-data) files which use cloud-init to config the OS on its first boot. Depending on if your configuring the [manager]() or [worker]() you can find the repspective files that you should place next to the OS image in subdirectories to this README.

**Make sure to replace information marked <TODO> with the proper configuration for your machine**

## `network-config`

The initial netplan configuration for the network.

The format of this file is YAML, in the form expected by netplan which is
documented at:

https://netplan.io/

Examples for wifi and ethernet are included, but you may also configure bonds,
bridges, etc. in this file.


## `meta-data`

The meta-data of the cloud-init seed. This mostly exists to define the
identifier of the instance, but also to specify that the data-source in this
case is entirely local (the user-data file; see below). If you wish to use a
remote data-source with cloud-init, you can override this and specify that
source by appending something like the following to cmdline.txt:

ds=nocloud-net;seedfrom=http://10.0.0.2:8000/

Where 10.0.0.2:8000 is an HTTP server serving alternate meta-data, user-data,
and (optionally) vendor-data files. Please note that network-config will *not*
be read from remote data-sources; only the local one will be applied.

The format of this file is YAML, and is documented at:

https://cloudinit.readthedocs.io/en/latest/topics/instancedata.html


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