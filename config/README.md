# Machine Setup

## Manager Setup

The chosen OS is Ubuntu Server which contains cloud-init for automated OS installation. After writing the OS iso to disk, fill in and place `/manager/autoinstall.yaml` into the USB's root as, `autoinstall.yaml`

Add `autoinstall` to the kernel command to bypass the "Continue with autoinstall" question.

## Worker Setup

Raspberry Pi Lite OS