# Machine Setup

## Manager Setup

The chosen OS is Ubuntu Server which contains cloud-init for automated OS installation. After writing the OS iso to disk, fill in and place `/manager/autoinstall.yaml` into the USB's root as, `autoinstall.yaml`

## Worker Setup

Ubuntu Server for Raspberry Pi is chosen for the workers. Using Raspberry Pi Imager, two files will be written to the USB root, `network-config` and `user-data`. Fill in and replace the files with the ones found in `/worker`