# Black Ansible

playbooks and tasks to do server connection init and basic setup

## plays and roles included

### server connection init

- setup ansible running environment
- configure sudoer
- add system admin users and ssh key pairs
- configure ssh

### server setup

- configure apt
- configure ipv6
- configure dns 
- configure hosts
- common settings
	- hostname
	- package upgrade
	- package install/remove
	- set default editor
- configure timezone
- configure locale
- configure ntp
- configure sysctl
- pin linux kernel
- manage iptables with ufw
- manage users and ssh keys (support host-level management)

## how to use it in your ansible project

1.clone this repo as submodule to your ansible project

2.add roles/plugins path to your `ansible.cfg`

```
roles_path=./roles:./black-ansible/roles
callback_plugins=./black-ansible/plugins/callback
lookup_plugins=./black-ansible/plugins/lookup
```
3.link black-ansible playbooks folder to you playbook path
 ## test

All roles tested on ubuntu 14.04 and part are tested on 16.04

## TODO
- add config example
- seperate reboot role
- add missing default for roles

