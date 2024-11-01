sharuaa@Sharubaa:/mnt/c/WINDOWS/system32$ cd ~
sharuaa@Sharubaa:~$ cat ashwin.pem
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyY/OcClXtZJ/LLaIPGF2enYFxXeLloywVWnr1xdtfmYO2EgI
U5s4QcOfznOSCRMuXrdaPFm4wdcelQClcXdSW8vi4glVlSUgReRHaa7tMVAU/s1i
HdUbXL3DFbCHiUvxUQ3DqFlqfIi9t/HJ6l5OJg2IQv26K06X3w6fvmr/B/B7kqKF
1QOUIVSopIMzfReBEV5SpeK7bao984DxH0Qm1GnzYqJ2H4w5gGezDiMd2WhsVVGD
G8j8bqo4D50VnseJgAyKwhuObsh2juyn8PciB6VQbgWxpTJcqhEi8++OhBoSg85D
KEj4sAekPlc30vP4LCcySwsBmmBQW/i0LubuwQIDAQABAoIBABhhO5AXgBNnR9ip
r2rWQxVm5yXOYuTv2XhLWopmvAi44XzJobAzKyfROKgpFHXiiw5L0S9RjuZrVbii
HmDOFPkjfSroBCEJH5E0nmqrDOeVDyUOxJplJ20dStZ5xrsVo3exWYQoZJfxljkE
lu6xP3Sc2Gl59SW92OLTCwFmQbi856FkGvEFoBveAS1034DvPL6gTGH5sFMQpoJM
zxp5KcnqPkcYyMbsETHW2GmFQvbf0JsjOrpjajp7QHrFiGcGQhte1FfZzPQrWWta
FbKk1Qk4hmjNJTumytnCavBVY+7Ko1CV8b9jr2VfxPDtkfpeEAO73GTL+VAgtBBw
UR7juo0CgYEA9s0hoRzSNJpntesucUroGtkjtmy4hIHyUfTauV1Gdqmhqv+cKRXs
J1T35DE81i9dnvDD71l3+zv/4PqGVlfK0moKvj1iPMes5qzzUzMKyWyy84z0MU4m
HooMQFipcd0ejln6TNyAYRc5B5D6eBnWlQlqnuWrQGc9CArNdeVO1GMCgYEA0RME
74i70PZe8mscmXJEJJGmzBM/pgW/r7O/ZQaby2OWciIDbkc/oqB4rlSP1/wcMZKL
xeSLTxiWi3au2XuKpWaFDcOY1jky9Oj/dyT9olUTQDDiBusmg6uGAlP04dZ4M98f
OvGaUiENk5RyUyZ+32FDXqM03SGiMcVSE2S5/4sCgYBghaN0XlA7sHOFK2BzgIc8
ENYtv2F+uU+rC+cK/dbUC82lkehiDSfZzhpRDYyse8PSqHkIv+XzxOhy9afaVuWE
22IuOtWTzcfqQ5O6Y0kBs9hc9jB+pAC2iuj1tXc3h/IuXDRPISG4Vxu/wMykcf6B
NTiUwl/yhS3SWl82j6L/3wKBgQCJEALoVadrMljEa9vv7K0nnCTRHL1ZReOIeDo9
LLvt9nemkw3UufjJ0JHNF7rFSY3iIcRoE5AQZnorK78s7ITUMgWAJH6J0i3JyQXR
QfrU9RkNt/41suso3sWXuRqNA2ECAIAk0EbvGKQh3+ui/1Wlc8oKvMvnPClsn4NT
G3GkSQKBgQDZjAKTPCLjk4ka6PnZcz1AU2DZJrVtfM4jY1SRP7HiiXjtPMq0QlMM
7GNbTb5fD5OgiloJWVGQtPmMnlcHka3EdB0rkp7UPggCXdQAVBTAM/ecqXyPveXL
hBVlClhwe0l8yyqai+/a8bLIUpZDwBj6F6PwUtcDSEyq6A72ZpPdQw==
-----END RSA PRIVATE KEY-----sharuaa@Sharubaa:~$ ssh -i ashwin.pem ubuntu@3.95.6.170
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.19.0-1025-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Sep 29 19:24:09 UTC 2023

  System load:  0.0               Processes:             95
  Usage of /:   20.6% of 7.57GB   Users logged in:       0
  Memory usage: 24%               IPv4 address for eth0: 172.31.86.10
  Swap usage:   0%

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ip-172-31-86-10:~$ docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
-bash: syntax error near unexpected token `do'
ubuntu@ip-172-31-86-10:~$ docker.io
docker.io: command not found
ubuntu@ip-172-31-86-10:~$ docker-doc
docker-doc: command not found
ubuntu@ip-172-31-86-10:~$ sudo apt-get remove $pkg; done
-bash: syntax error near unexpected token `done'
ubuntu@ip-172-31-86-10:~$ sudo apt-get remove $pkg
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
ubuntu@ip-172-31-86-10:~$ sudo apt-get update
Hit:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Get:3 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports InRelease [109 kB]
Get:4 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:5 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [14.1 MB]
Get:6 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [804 kB]
Get:7 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/universe Translation-en [5652 kB]
Get:8 http://security.ubuntu.com/ubuntu jammy-security/main Translation-en [169 kB]
Get:9 http://security.ubuntu.com/ubuntu jammy-security/main amd64 c-n-f Metadata [11.3 kB]
Get:10 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [889 kB]
Get:11 http://security.ubuntu.com/ubuntu jammy-security/restricted Translation-en [143 kB]
Get:12 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 c-n-f Metadata [532 B]
Get:13 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [785 kB]
Get:14 http://security.ubuntu.com/ubuntu jammy-security/universe Translation-en [144 kB]
Get:15 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 c-n-f Metadata [16.7 kB]
Get:16 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [36.5 kB]
Get:17 http://security.ubuntu.com/ubuntu jammy-security/multiverse Translation-en [7060 B]
Get:18 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 c-n-f Metadata [260 B]
Get:19 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/universe amd64 c-n-f Metadata [286 kB]
Get:20 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [217 kB]
Get:21 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/multiverse Translation-en [112 kB]
Get:22 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/multiverse amd64 c-n-f Metadata [8372 B]
Get:23 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [1014 kB]
Get:24 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/main Translation-en [227 kB]
Get:25 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/main amd64 c-n-f Metadata [15.6 kB]
Get:26 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [905 kB]
Get:27 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/restricted Translation-en [146 kB]
Get:28 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 c-n-f Metadata [532 B]
Get:29 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [987 kB]
Get:30 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/universe Translation-en [215 kB]
Get:31 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 c-n-f Metadata [21.9 kB]
Get:32 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [41.6 kB]
Get:33 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/multiverse Translation-en [9768 B]
Get:34 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 c-n-f Metadata [472 B]
Get:35 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [41.7 kB]
Get:36 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports/main Translation-en [10.5 kB]
Get:37 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports/main amd64 c-n-f Metadata [388 B]
Get:38 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports/restricted amd64 c-n-f Metadata [116 B]
Get:39 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [24.3 kB]
Get:40 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports/universe Translation-en [16.4 kB]
Get:41 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 c-n-f Metadata [640 B]
Get:42 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports/multiverse amd64 c-n-f Metadata [116 B]
Fetched 27.4 MB in 5s (5551 kB/s)
Reading package lists... Done
ubuntu@ip-172-31-86-10:~$ sudo apt-get install ca-certificates curl gnupg
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
gnupg is already the newest version (2.2.27-3ubuntu2.1).
gnupg set to manually installed.
The following packages will be upgraded:
  ca-certificates curl libcurl4
3 upgraded, 0 newly installed, 0 to remove and 126 not upgraded.
Need to get 640 kB of archives.
After this operation, 23.6 kB of additional disk space will be used.
Get:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/main amd64 ca-certificates all 20230311ubuntu0.22.04.1 [155 kB]
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/main amd64 curl amd64 7.81.0-1ubuntu1.13 [194 kB]
Get:3 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libcurl4 amd64 7.81.0-1ubuntu1.13 [290 kB]Fetched 640 kB in 0s (21.6 MB/s)
Preconfiguring packages ...
(Reading database ... 64295 files and directories currently installed.)
Preparing to unpack .../ca-certificates_20230311ubuntu0.22.04.1_all.deb ...
Unpacking ca-certificates (20230311ubuntu0.22.04.1) over (20211016ubuntu0.22.04.1) ...
Preparing to unpack .../curl_7.81.0-1ubuntu1.13_amd64.deb ...
Unpacking curl (7.81.0-1ubuntu1.13) over (7.81.0-1ubuntu1.10) ...
Preparing to unpack .../libcurl4_7.81.0-1ubuntu1.13_amd64.deb ...
Unpacking libcurl4:amd64 (7.81.0-1ubuntu1.13) over (7.81.0-1ubuntu1.10) ...
Setting up ca-certificates (20230311ubuntu0.22.04.1) ...
Updating certificates in /etc/ssl/certs...
rehash: warning: skipping ca-certificates.crt,it does not contain exactly one certificate or CRL
19 added, 6 removed; done.
Setting up libcurl4:amd64 (7.81.0-1ubuntu1.13) ...
Setting up curl (7.81.0-1ubuntu1.13) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
Processing triggers for ca-certificates (20230311ubuntu0.22.04.1) ...
Updating certificates in /etc/ssl/certs...
0 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
Scanning processes...
Scanning linux images...

Running kernel seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
ubuntu@ip-172-31-86-10:~$ sudo install -m 0755 -d /etc/apt/keyrings
ubuntu@ip-172-31-86-10:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
ubuntu@ip-172-31-86-10:~$ sudo chmod a+r /etc/apt/keyrings/docker.gpg
ubuntu@ip-172-31-86-10:~$ echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
ubuntu@ip-172-31-86-10:~$ sudo apt-get update
Hit:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Get:3 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-backports InRelease [109 kB]
Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease
Get:5 https://download.docker.com/linux/ubuntu jammy InRelease [48.9 kB]
Get:6 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [1014 kB]
Get:7 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [905 kB]
Get:8 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [987 kB]
Get:9 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [41.6 kB]
Get:10 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages [22.2 kB]
Fetched 3246 kB in 1s (2335 kB/s)
Reading package lists... Done
ubuntu@ip-172-31-86-10:~$ echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
pdateubuntu@ip-172-31-86-10:~$ echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
ubuntu@ip-172-31-86-10:~$
ubuntu@ip-172-31-86-10:~$ echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null sudo apt-get update
ubuntu@ip-172-31-86-10:~$ echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
ubuntu@ip-172-31-86-10:~$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  docker-ce-rootless-extras libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli docker-ce-rootless-extras docker-compose-plugin libltdl7
  libslirp0 pigz slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 126 not upgraded.
Need to get 114 MB of archives.
After this operation, 409 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/universe amd64 pigz amd64 2.6-1 [63.6 kB]
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 libltdl7 amd64 2.4.6-15build2 [39.6 kB]
Get:3 https://download.docker.com/linux/ubuntu jammy/stable amd64 containerd.io amd64 1.6.24-1 [28.6 MB]
Get:4 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 libslirp0 amd64 4.6.1-1build1 [61.5 kB]
Get:5 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy/universe amd64 slirp4netns amd64 1.0.1-2 [28.2 kB]
Get:6 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-buildx-plugin amd64 0.11.2-1~ubuntu.22.04~jammy [28.2 MB]
Get:7 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce-cli amd64 5:24.0.6-1~ubuntu.22.04~jammy [13.3 MB]
Get:8 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce amd64 5:24.0.6-1~ubuntu.22.04~jammy [22.6 MB]
Get:9 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce-rootless-extras amd64 5:24.0.6-1~ubuntu.22.04~jammy [9032 kB]
Get:10 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-compose-plugin amd64 2.21.0-1~ubuntu.22.04~jammy [11.9 MB]
Fetched 114 MB in 2s (51.4 MB/s)
Selecting previously unselected package pigz.
(Reading database ... 64308 files and directories currently installed.)
Preparing to unpack .../0-pigz_2.6-1_amd64.deb ...
Unpacking pigz (2.6-1) ...
Selecting previously unselected package containerd.io.
Preparing to unpack .../1-containerd.io_1.6.24-1_amd64.deb ...
Unpacking containerd.io (1.6.24-1) ...
Selecting previously unselected package docker-buildx-plugin.
Preparing to unpack .../2-docker-buildx-plugin_0.11.2-1~ubuntu.22.04~jammy_amd64.deb ...
Unpacking docker-buildx-plugin (0.11.2-1~ubuntu.22.04~jammy) ...
Selecting previously unselected package docker-ce-cli.
Preparing to unpack .../3-docker-ce-cli_5%3a24.0.6-1~ubuntu.22.04~jammy_amd64.deb ...
Unpacking docker-ce-cli (5:24.0.6-1~ubuntu.22.04~jammy) ...
Selecting previously unselected package docker-ce.
Preparing to unpack .../4-docker-ce_5%3a24.0.6-1~ubuntu.22.04~jammy_amd64.deb ...
Unpacking docker-ce (5:24.0.6-1~ubuntu.22.04~jammy) ...
Selecting previously unselected package docker-ce-rootless-extras.
Preparing to unpack .../5-docker-ce-rootless-extras_5%3a24.0.6-1~ubuntu.22.04~jammy_amd64.deb ...
Unpacking docker-ce-rootless-extras (5:24.0.6-1~ubuntu.22.04~jammy) ...
Selecting previously unselected package docker-compose-plugin.
Preparing to unpack .../6-docker-compose-plugin_2.21.0-1~ubuntu.22.04~jammy_amd64.deb ...
Unpacking docker-compose-plugin (2.21.0-1~ubuntu.22.04~jammy) ...
Selecting previously unselected package libltdl7:amd64.
Preparing to unpack .../7-libltdl7_2.4.6-15build2_amd64.deb ...
Unpacking libltdl7:amd64 (2.4.6-15build2) ...
Selecting previously unselected package libslirp0:amd64.
Preparing to unpack .../8-libslirp0_4.6.1-1build1_amd64.deb ...
Unpacking libslirp0:amd64 (4.6.1-1build1) ...
Selecting previously unselected package slirp4netns.
Preparing to unpack .../9-slirp4netns_1.0.1-2_amd64.deb ...
Unpacking slirp4netns (1.0.1-2) ...
Setting up docker-buildx-plugin (0.11.2-1~ubuntu.22.04~jammy) ...
Setting up containerd.io (1.6.24-1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service → /lib/systemd/system/containerd.service.Setting up docker-compose-plugin (2.21.0-1~ubuntu.22.04~jammy) ...
Setting up libltdl7:amd64 (2.4.6-15build2) ...
Setting up docker-ce-cli (5:24.0.6-1~ubuntu.22.04~jammy) ...
Setting up libslirp0:amd64 (4.6.1-1build1) ...
Setting up pigz (2.6-1) ...
Setting up docker-ce-rootless-extras (5:24.0.6-1~ubuntu.22.04~jammy) ...
Setting up slirp4netns (1.0.1-2) ...
Setting up docker-ce (5:24.0.6-1~ubuntu.22.04~jammy) ...
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /lib/systemd/system/docker.service.
Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /lib/systemd/system/docker.socket.
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
Scanning processes...
Scanning linux images...

Running kernel seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
ubuntu@ip-172-31-86-10:~$ sudo systemctl start docker
ubuntu@ip-172-31-86-10:~$ docker version
Client: Docker Engine - Community
 Version:           24.0.6
 API version:       1.43
 Go version:        go1.20.7
 Git commit:        ed223bc
 Built:             Mon Sep  4 12:31:44 2023
 OS/Arch:           linux/amd64
 Context:           default
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version": dial unix /var/run/docker.sock: connect: permission denied
ubuntu@ip-172-31-86-10:~$ sudo usermod -aG docker ubuntu
ubuntu@ip-172-31-86-10:~$
logout
Connection to 3.95.6.170 closed.
sharuaa@Sharubaa:~$ ssh -i ashwin.pem ubuntu@3.95.6.170
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.19.0-1025-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Sep 29 19:52:03 UTC 2023

  System load:  0.18017578125     Processes:                102
  Usage of /:   29.9% of 7.57GB   Users logged in:          0
  Memory usage: 29%               IPv4 address for docker0: 172.17.0.1
  Swap usage:   0%                IPv4 address for eth0:    172.31.86.10


Expanded Security Maintenance for Applications is not enabled.

128 updates can be applied immediately.
68 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Fri Sep 29 19:24:11 2023 from 192.197.54.35
ubuntu@ip-172-31-86-10:~$ docker version
Client: Docker Engine - Community
 Version:           24.0.6
 API version:       1.43
 Go version:        go1.20.7
 Git commit:        ed223bc
 Built:             Mon Sep  4 12:31:44 2023
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          24.0.6
  API version:      1.43 (minimum version 1.12)
  Go version:       go1.20.7
  Git commit:       1a79695
  Built:            Mon Sep  4 12:31:44 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.24
  GitCommit:        61f9fd88f79f081d64d6fa3bb1a0dc71ec870523
 runc:
  Version:          1.1.9
  GitCommit:        v1.1.9-0-gccaecfc
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
ubuntu@ip-172-31-86-10:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
ubuntu@ip-172-31-86-10:~$ docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
ubuntu@ip-172-31-86-10:~$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
719385e32844: Pull complete
Digest: sha256:4f53e2564790c8e7856ec08e384732aa38dc43c52f02952483e3f003afbf23db
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

ubuntu@ip-172-31-86-10:~$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

ubuntu@ip-172-31-86-10:~$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    9c7a54a9a43c   4 months ago   13.3kB
ubuntu@ip-172-31-86-10:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
ubuntu@ip-172-31-86-10:~$ docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED              STATUS                          PORTS     NAMES
9fc995d11ebf   hello-world   "/hello"   About a minute ago   Exited (0) About a minute ago             compassionate_johnson
c7dadf720985   hello-world   "/hello"   2 minutes ago        Exited (0) 2 minutes ago                  eloquent_almeida
ubuntu@ip-172-31-86-10:~$ docker search ubuntu
NAME                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
ubuntu                           Ubuntu is a Debian-based Linux operating sys…   16445     [OK]
websphere-liberty                WebSphere Liberty multi-architecture images …   297       [OK]
open-liberty                     Open Liberty multi-architecture images based…   62        [OK]
neurodebian                      NeuroDebian provides neuroscience research s…   104       [OK]
ubuntu-debootstrap               DEPRECATED; use "ubuntu" instead                52        [OK]
ubuntu-upstart                   DEPRECATED, as is Upstart (find other proces…   115       [OK]
ubuntu/nginx                     Nginx, a high-performance reverse proxy & we…   100
ubuntu/squid                     Squid is a caching proxy for the Web. Long-t…   67
ubuntu/cortex                    Cortex provides storage for Prometheus. Long…   4
ubuntu/apache2                   Apache, a secure & extensible open-source HT…   60
ubuntu/kafka                     Apache Kafka, a distributed event streaming …   35
ubuntu/mysql                     MySQL open source fast, stable, multi-thread…   53
ubuntu/bind9                     BIND 9 is a very flexible, full-featured DNS…   62
ubuntu/prometheus                Prometheus is a systems and service monitori…   51
ubuntu/zookeeper                 ZooKeeper maintains configuration informatio…   12
ubuntu/postgres                  PostgreSQL is an open source object-relation…   31
ubuntu/redis                     Redis, an open source key-value store. Long-…   19
ubuntu/grafana                   Grafana, a feature rich metrics dashboard & …   9
ubuntu/memcached                 Memcached, in-memory keyvalue store for smal…   5
ubuntu/dotnet-aspnet             Chiselled Ubuntu runtime image for ASP.NET a…   11
ubuntu/dotnet-deps               Chiselled Ubuntu for self-contained .NET & A…   11
ubuntu/prometheus-alertmanager   Alertmanager handles client alerts from Prom…   9
ubuntu/dotnet-runtime            Chiselled Ubuntu runtime image for .NET apps…   10
ubuntu/cassandra                 Cassandra, an open source NoSQL distributed …   2
ubuntu/telegraf                  Telegraf collects, processes, aggregates & w…   4
ubuntu@ip-172-31-86-10:~$ docker search github
NAME                                         DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker-dev                                   DEPRECATED; use https://github.com/moby/moby…   102       [OK]
docker/github-actions                        Experimental image for providing functionali…   20
cockroachdb/github-pages                     Ruby github-pages/jekyll build for docs repo.   1                    [OK]
grafana/github-repo-metrics                                                                  0
spack/github-actions                         Container images used with Github Actions as…   0
okteto/github-runner                                                                         0
femtopixel/github-release-notifier           Github Release Notifier (Multiarch)             1
finalgene/github-release                     GitHub-Release binary for CI                    3                    [OK]
linuxserver/github-desktop                                                                   2
vitess/github                                Build docker images using github actions        0
longhornio/github-runner-authorizer                                                          0
longhornio/github-bot                                                                        0
openintegrationhub/github-adapter            GitHub Adapter for Open Integration Hub.        0
observabilitystack/github-actions-exporter                                                   0
observabilitystack/github_exporter                                                           0
openintegrationhub/github-adapter-template                                                   0
percona/percona-xtradb-cluster               Percona XtraDB Cluster docker image | https:…   162
rezoleo/github-project-automation            A Probot to automatically add issues and PRs…   0
vmware/veba-event-router                     https://github.com/vmware-samples/vcenter-ev…   5
observabilitystack/github-exporter                                                           0
mattermost/mattermost-prod-web               Part of the Mattermost production docker com…   15                   [OK]
newrelic/k8s-webhook-cert-manager            Certificate Manager for Kubernetes Webhook (…   0
datadog/system-tests                         Base images for https://github.com/DataDog/s…   1
mattermost/mattermost-operator               Mattermost Operator for Kubernetes. https://…   0
tacc/github-runner-python3                                                                   0
ubuntu@ip-172-31-86-10:~$ docker search spotify
NAME                               DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
spotify/docker-gc                  Garbage collection of Docker containers and …   88                   [OK]
spotify/cassandra                  Cassandra images optimized for fast startup     132                  [OK]
spotify/alpine                     Alpine image with `bash` and `curl`.            13                   [OK]
spotify/kafka                      A simple docker image with both Kafka and Zo…   413                  [OK]
spotify/techdocs                    TechDocs plugin to Spotify's Backstage         1
spotify/busybox                    Spotify fork of https://hub.docker.com/_/bus…   1
spotify/lighthouse-audit-service                                                   0
spotify/helios-solo-base           Base image with dependencies for spotify/hel…   1
spotify/helios-solo                Helios cluster in a Docker container            2
spotify/bigtable-emulator                                                          5
spotify/xcmetrics                                                                  2
spotify/kafkaproxy                                                                 8                    [OK]
spotify/backstage-cookiecutter     Cookiecutter for Backstage. Backstage is an …   6
spotify/helios-agent                                                               2
spotify/nginx-alpine               For testing helios.                             1
spotify/memcached-mini             For testing helios.                             0
spotify/luigi                      A minimal Docker image containing luigi serv…   2
spotify/docker-uhttpd              A fork of https://hub.docker.com/r/fnichol/d…   0
spotify/heroic                     The Heroic Time Series Database https://spot…   3                    [OK]
spotify/skill-exchange-service     Backend Java service supporting the Skill Ex…   0
spotify/helios-master                                                              2
spotify/scratch                    An empty image. DO NOT DELETE. NEEDED BY INT…   1
spotify/proto-registry             An implementation of the Protobuf Registry A…   0                    [OK]
musicblend/spotifyauth             This image serves as an API the authenticate…   0
spotify/zookeeper                  For testing helios.                             3
ubuntu@ip-172-31-86-10:~$ docker search ubuntu
NAME                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
ubuntu                           Ubuntu is a Debian-based Linux operating sys…   16445     [OK]
websphere-liberty                WebSphere Liberty multi-architecture images …   297       [OK]
open-liberty                     Open Liberty multi-architecture images based…   62        [OK]
neurodebian                      NeuroDebian provides neuroscience research s…   104       [OK]
ubuntu-debootstrap               DEPRECATED; use "ubuntu" instead                52        [OK]
ubuntu-upstart                   DEPRECATED, as is Upstart (find other proces…   115       [OK]
ubuntu/nginx                     Nginx, a high-performance reverse proxy & we…   100
ubuntu/squid                     Squid is a caching proxy for the Web. Long-t…   67
ubuntu/cortex                    Cortex provides storage for Prometheus. Long…   4
ubuntu/apache2                   Apache, a secure & extensible open-source HT…   60
ubuntu/kafka                     Apache Kafka, a distributed event streaming …   35
ubuntu/mysql                     MySQL open source fast, stable, multi-thread…   53
ubuntu/bind9                     BIND 9 is a very flexible, full-featured DNS…   62
ubuntu/prometheus                Prometheus is a systems and service monitori…   51
ubuntu/zookeeper                 ZooKeeper maintains configuration informatio…   12
ubuntu/postgres                  PostgreSQL is an open source object-relation…   31
ubuntu/redis                     Redis, an open source key-value store. Long-…   19
ubuntu/grafana                   Grafana, a feature rich metrics dashboard & …   9
ubuntu/memcached                 Memcached, in-memory keyvalue store for smal…   5
ubuntu/dotnet-aspnet             Chiselled Ubuntu runtime image for ASP.NET a…   11
ubuntu/dotnet-deps               Chiselled Ubuntu for self-contained .NET & A…   11
ubuntu/prometheus-alertmanager   Alertmanager handles client alerts from Prom…   9
ubuntu/dotnet-runtime            Chiselled Ubuntu runtime image for .NET apps…   10
ubuntu/cassandra                 Cassandra, an open source NoSQL distributed …   2
ubuntu/telegraf                  Telegraf collects, processes, aggregates & w…   4
ubuntu@ip-172-31-86-10:~$ docker run ubuntu
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
445a6a12be2b: Pull complete
Digest: sha256:aabed3296a3d45cede1dc866a24476c4d7e093aa806263c27ddaadbdce3c1054
Status: Downloaded newer image for ubuntu:latest
ubuntu@ip-172-31-86-10:~$ docker ps -a
CONTAINER ID   IMAGE         COMMAND       CREATED          STATUS                      PORTS     NAMES
1a5a955241b3   ubuntu        "/bin/bash"   22 seconds ago   Exited (0) 21 seconds ago             inspiring_shannon
9fc995d11ebf   hello-world   "/hello"      7 minutes ago    Exited (0) 7 minutes ago              compassionate_johnson
c7dadf720985   hello-world   "/hello"      8 minutes ago    Exited (0) 8 minutes ago              eloquent_almeida
ubuntu@ip-172-31-86-10:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
ubuntu@ip-172-31-86-10:~$ docker run ubuntu
ubuntu@ip-172-31-86-10:~$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
ubuntu        latest    c6b84b685f35   6 weeks ago    77.8MB
hello-world   latest    9c7a54a9a43c   4 months ago   13.3kB
ubuntu@ip-172-31-86-10:~$ docker run -it ubuntu /bin/bash
root@722f3a6c1587:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@722f3a6c1587:/# ubuntu@ip-172-31-86-10:~$ docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS              PORTS     NAMES
722f3a6c1587   ubuntu    "/bin/bash"   About a minute ago   Up About a minute             hungry_montalcini
ubuntu@ip-172-31-86-10:~$ docker stop
"docker stop" requires at least 1 argument.
See 'docker stop --help'.

Usage:  docker stop [OPTIONS] CONTAINER [CONTAINER...]

Stop one or more running containers
ubuntu@ip-172-31-86-10:~$ docker stop hungry_montalcini
hungry_montalcini
ubuntu@ip-172-31-86-10:~$ docker run -it ubuntu /bin/bash
root@344924659aae:/# ubuntu@ip-172-31-86-10:~$ docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS          PORTS     NAMES
344924659aae   ubuntu    "/bin/bash"   15 seconds ago   Up 14 seconds             eloquent_ride
ubuntu@ip-172-31-86-10:~$ docker exec -it eloquent_ride /bin/bash
root@344924659aae:/# docker ps
bash: docker: command not found
root@344924659aae:/# read escape sequence
ubuntu@ip-172-31-86-10:~$ docker stop eloquent_ride
eloquent_ride
ubuntu@ip-172-31-86-10:~$ git clone http://github.com/rwpazzi/lectured
Cloning into 'lectured'...
Username for 'https://github.com': sharubaa
Password for 'https://sharubaa@github.com':
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/rwpazzi/lectured/'
ubuntu@ip-172-31-86-10:~$ git clone http://github.com/rwpazzi/lecture4
Cloning into 'lecture4'...
warning: redirecting to https://github.com/rwpazzi/lecture4/
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.
Resolving deltas: 100% (1/1), done.
ubuntu@ip-172-31-86-10:~$ ls
apt-get  lecture4  sudo  update
ubuntu@ip-172-31-86-10:~$ cd lecture4/
ubuntu@ip-172-31-86-10:~/lecture4$ ls
Dockerfile
ubuntu@ip-172-31-86-10:~/lecture4$ cat Dockerfile
FROM ubuntu:20.04

# Avoinding tzdata interactive prompt
ENV DEBIAN_FRONTEND=noninteractive

# Install Apache
RUN apt-get update && \
 apt-get -y install apache2

# Add your own content to the deafult webpage (index.html)
RUN echo 'This is my INFR2670 webpage running in a container!' > /var/www/html/index.html

# Apache configuration
RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh && \
 echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh && \
 echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh && \
 echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh && \
 chmod 755 /root/run_apache.sh

EXPOSE 80

CMD /root/run_apache.sh
ubuntu@ip-172-31-86-10:~/lecture4$ docker build -t webserver .
[+] Building 25.5s (8/8) FINISHED                                                                        docker:default
 => [internal] load build definition from Dockerfile                                                               0.2s
 => => transferring dockerfile: 699B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  0.2s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/ubuntu:20.04                                                    0.3s
 => [1/4] FROM docker.io/library/ubuntu:20.04@sha256:33a5cc25d22c45900796a1aca487ad7a7cb09f09ea00b779e3b2026b4fc2  2.4s
 => => resolve docker.io/library/ubuntu:20.04@sha256:33a5cc25d22c45900796a1aca487ad7a7cb09f09ea00b779e3b2026b4fc2  0.0s
 => => sha256:33a5cc25d22c45900796a1aca487ad7a7cb09f09ea00b779e3b2026b4fc2faba 1.13kB / 1.13kB                     0.0s
 => => sha256:3246518d9735254519e1b2ff35f95686e4a5011c90c85344c1f38df7bae9dd37 424B / 424B                         0.0s
 => => sha256:6df89402372646d400cf092016c28066391a26f5d46c00b1153e75003465484d 2.30kB / 2.30kB                     0.0s
 => => sha256:edaedc954fb53f42a7754a6e2d1b57f091bc9b11063bc445c2e325ea448f8f68 27.51MB / 27.51MB                   0.5s
 => => extracting sha256:edaedc954fb53f42a7754a6e2d1b57f091bc9b11063bc445c2e325ea448f8f68                          1.7s
 => [2/4] RUN apt-get update &&  apt-get -y install apache2                                                       19.8s
 => [3/4] RUN echo 'This is my INFR2670 webpage running in a container!' > /var/www/html/index.html                0.6s
 => [4/4] RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh &&  echo 'mkdir -p /var/run/apache2' >> /root/r  0.4s
 => exporting to image                                                                                             1.7s
 => => exporting layers                                                                                            1.7s
 => => writing image sha256:afab5bdd930aec9654f0f6c0560582ed599073fb5156c1bcc08093f40f67ab18                       0.0s
 => => naming to docker.io/library/webserver                                                                       0.0s
ubuntu@ip-172-31-86-10:~/lecture4$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
webserver     latest    afab5bdd930a   2 minutes ago   233MB
ubuntu        latest    c6b84b685f35   6 weeks ago     77.8MB
hello-world   latest    9c7a54a9a43c   4 months ago    13.3kB
ubuntu@ip-172-31-86-10:~/lecture4$ docker run --name myserver -d -p  80:80 webserver
958a74b8c523f8993979fee1a3c814a92bc1621d20413f57e52afff3b95d009f
ubuntu@ip-172-31-86-10:~/lecture4$ docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS                               NAMES
958a74b8c523   webserver   "/bin/sh -c /root/ru…"   24 seconds ago   Up 22 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   myserver
ubuntu@ip-172-31-86-10:~/lecture4$
logout
Connection to 3.95.6.170 closed.
sharuaa@Sharubaa:~$ ssh -i ashwin.pem ubuntu@3.95.6.170
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.19.0-1025-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Sep 29 20:27:38 UTC 2023

  System load:  0.0               Processes:                108
  Usage of /:   34.2% of 7.57GB   Users logged in:          0
  Memory usage: 35%               IPv4 address for docker0: 172.17.0.1
  Swap usage:   0%                IPv4 address for eth0:    172.31.86.10


Expanded Security Maintenance for Applications is not enabled.

128 updates can be applied immediately.
68 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Fri Sep 29 19:52:07 2023 from 192.197.54.35
ubuntu@ip-172-31-86-10:~$ git clone http://github.com/rwpazzi/lecture4
fatal: destination path 'lecture4' already exists and is not an empty directory.
ubuntu@ip-172-31-86-10:~$ cd lecture4/
ubuntu@ip-172-31-86-10:~/lecture4$ docker exec -it myserver /bin/bash
root@958a74b8c523:/# cd var/www/htm
bash: cd: var/www/htm: No such file or directory
root@958a74b8c523:/# cd var/www/html
root@958a74b8c523:/var/www/html# read escape sequence
ubuntu@ip-172-31-86-10:~/lecture4$ docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                               NAMES
958a74b8c523   webserver   "/bin/sh -c /root/ru…"   3 minutes ago   Up 3 minutes   0.0.0.0:80->80/tcp, :::80->80/tcp   myserver
ubuntu@ip-172-31-86-10:~/lecture4$ docker stop myserver
myserver
ubuntu@ip-172-31-86-10:~/lecture4$ cd
ubuntu@ip-172-31-86-10:~$ nano Dockerfile
ubuntu@ip-172-31-86-10:~$ nano script.py
ubuntu@ip-172-31-86-10:~$ ls
Dockerfile  apt-get  lecture4  script.py  sudo  update
ubuntu@ip-172-31-86-10:~$ docker build -t hello2670 .
[+] Building 0.5s (6/6) FINISHED                                                                         docker:default
 => [internal] load build definition from Dockerfile                                                               0.0s
 => => transferring dockerfile: 100B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:2                                                        0.4s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [1/2] FROM docker.io/library/python:2@sha256:cfa62318c459b1fde9e0841c619906d15ada5910d625176e24bf692cf8a2601d  0.0s
 => => resolve docker.io/library/python:2@sha256:cfa62318c459b1fde9e0841c619906d15ada5910d625176e24bf692cf8a2601d  0.0s
 => ERROR [2/2] ADD script.python /                                                                                0.0s
------
 > [2/2] ADD script.python /:
------
Dockerfile:2
--------------------
   1 |     FROM python:2
   2 | >>> ADD script.python /
   3 |     CMD ["python","./script.py"]
   4 |
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref 27202219-e7af-40a1-b6d1-37c3bfb04390::zb2o886j65gsgr36w1fua7400: "/script.python": not found
ubuntu@ip-172-31-86-10:~$ nano Dockerfile
ubuntu@ip-172-31-86-10:~$ docker build -t hello2670 .
[+] Building 26.3s (7/7) FINISHED                                                                        docker:default
 => [internal] load build definition from Dockerfile                                                               0.0s
 => => transferring dockerfile: 96B                                                                                0.0s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:2                                                        0.1s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 65B                                                                                   0.0s
 => [1/2] FROM docker.io/library/python:2@sha256:cfa62318c459b1fde9e0841c619906d15ada5910d625176e24bf692cf8a2601  25.1s
 => => resolve docker.io/library/python:2@sha256:cfa62318c459b1fde9e0841c619906d15ada5910d625176e24bf692cf8a2601d  0.0s
 => => sha256:68e7be49c28c89833fc91b44a8c1db6982b52695749d57c3d6fe995a9bb1df5f 8.93kB / 8.93kB                     0.0s
 => => sha256:7e2b2a5af8f65687add6d864d5841067e23bd435eb1a051be6fe1ea2384946b4 50.38MB / 50.38MB                   1.0s
 => => sha256:dc3f0c679f0f4c39597721c1df5cdb4f9685b26bd789a44eeb406835a1800d5f 10.00MB / 10.00MB                   0.5s
 => => sha256:cfa62318c459b1fde9e0841c619906d15ada5910d625176e24bf692cf8a2601d 2.14kB / 2.14kB                     0.0s
 => => sha256:c934af72b8bd03b9804d5bde2569c320926e70392d708d113a2e71bcf98c8a20 2.22kB / 2.22kB                     0.0s
 => => sha256:09b6f03ffac4cb4e42f8ab0bfc480bd3a3fa20e1ddee37784db63bc886b0cbb3 7.81MB / 7.81MB                     0.5s
 => => sha256:fd4b47407fc30b8206971ec60f280b107b00df8007da2fb912ebb8656b53695e 51.83MB / 51.83MB                   1.9s
 => => sha256:b32f6bf7d96d26a22dc62da6522f384dcdc936c30c88b233d378e06cf127346d 192.17MB / 192.17MB                 5.9s
 => => sha256:6f4489a7e4cfcda98c90d9fb220ab8dbf5e40a7a6d756ed414707967aa96bfbd 5.79MB / 5.79MB                     1.3s
 => => sha256:af4b99ad9ef03daa029d78458e669f135a3c41764bbc154e9d56a3d9b2ee7bf1 18.33MB / 18.33MB                   2.1s
 => => extracting sha256:7e2b2a5af8f65687add6d864d5841067e23bd435eb1a051be6fe1ea2384946b4                          5.8s
 => => sha256:39db0bc48c262bd32f4b201a4fad3dde162e73d3d1135fdaab433477156ad816 1.89MB / 1.89MB                     2.1s
 => => sha256:acb4a89489fc21e4c05c6ef86dacf640cab884b3b3e207cfd5ad24da02f14661 7.68MB / 7.68MB                     2.7s
 => => extracting sha256:09b6f03ffac4cb4e42f8ab0bfc480bd3a3fa20e1ddee37784db63bc886b0cbb3                          0.4s
 => => extracting sha256:dc3f0c679f0f4c39597721c1df5cdb4f9685b26bd789a44eeb406835a1800d5f                          0.4s
 => => extracting sha256:fd4b47407fc30b8206971ec60f280b107b00df8007da2fb912ebb8656b53695e                          3.3s
 => => extracting sha256:b32f6bf7d96d26a22dc62da6522f384dcdc936c30c88b233d378e06cf127346d                         10.2s
 => => extracting sha256:6f4489a7e4cfcda98c90d9fb220ab8dbf5e40a7a6d756ed414707967aa96bfbd                          0.4s
 => => extracting sha256:af4b99ad9ef03daa029d78458e669f135a3c41764bbc154e9d56a3d9b2ee7bf1                          1.1s
 => => extracting sha256:39db0bc48c262bd32f4b201a4fad3dde162e73d3d1135fdaab433477156ad816                          0.2s
 => => extracting sha256:acb4a89489fc21e4c05c6ef86dacf640cab884b3b3e207cfd5ad24da02f14661                          0.4s
 => [2/2] ADD script.py /                                                                                          0.8s
 => exporting to image                                                                                             0.1s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:a8b727cbc34d24e14465fdc178de3d3d67b4a392fbe451e6436ba5155e45c345                       0.0s
 => => naming to docker.io/library/hello2670                                                                       0.0s
ubuntu@ip-172-31-86-10:~$ docker tag webserver:latest sharubaa/sharubaa:hello2670
ubuntu@ip-172-31-86-10:~$ docker tag webserver:latest sharubaa/sharubaa:webserver
ubuntu@ip-172-31-86-10:~$ docker push sharubaa/sharubaa:webserver
The push refers to repository [docker.io/sharubaa/sharubaa]
bf6e694433a3: Preparing
a98ab443f74a: Preparing
826ff77f974f: Preparing
954c82bdeb5f: Preparing
denied: requested access to the resource is denied
ubuntu@ip-172-31-86-10:~$ docker login
Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com/ to create one.
You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at https://docs.docker.com/go/access-tokens/

Username: sharubaa
Password:
Error response from daemon: Get "https://registry-1.docker.io/v2/": unauthorized: incorrect username or password
ubuntu@ip-172-31-86-10:~$ docker login
Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com/ to create one.
You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at https://docs.docker.com/go/access-tokens/

Username: sharubaa
Password:
WARNING! Your password will be stored unencrypted in /home/ubuntu/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
ubuntu@ip-172-31-86-10:~$ docker push sharubaa/sharubaa:webserver
The push refers to repository [docker.io/sharubaa/sharubaa]
bf6e694433a3: Pushed
a98ab443f74a: Pushed
826ff77f974f: Pushed
954c82bdeb5f: Mounted from library/ubuntu
webserver: digest: sha256:f476ad771540a59a8b478ab504111fe2e51d0ccec9484d011de5886b0a8289a3 size: 1155
ubuntu@ip-172-31-86-10:~$ docker tag hello2670 sharubaa/infr2670:hello2670
ubuntu@ip-172-31-86-10:~$ docker tag hello2670 sharubaa/sharubaa:hello2670
ubuntu@ip-172-31-86-10:~$ docker push sharubaa/sharubaa:hello2670
The push refers to repository [docker.io/sharubaa/sharubaa]
85e950cffcaf: Pushed
e571d2d3c73c: Mounted from library/python
da7b0a80a4f2: Mounted from library/python
ceee8816bb96: Mounted from library/python
47458fb45d99: Mounted from library/python
46829331b1e4: Mounted from library/python
d35c5bda4793: Mounted from library/python
a3c1026c6bcc: Mounted from library/python
f1d420c2af1a: Mounted from library/python
461719022993: Mounted from library/python
hello2670: digest: sha256:de6a4e42036d959692812d171063823efc5ac162c609f3d7106e22e88761d11e size: 2428
ubuntu@ip-172-31-86-10:~$ docker ps-q
docker: 'ps-q' is not a docker command.
See 'docker --help'
ubuntu@ip-172-31-86-10:~$ docker ps -q
ubuntu@ip-172-31-86-10:~$ docker ps -a -q
958a74b8c523
344924659aae
722f3a6c1587
068455080a7d
1a5a955241b3
9fc995d11ebf
c7dadf720985
ubuntu@ip-172-31-86-10:~$ docker tag hello2670 sharubaa/sharubaa:hello2670
ubuntu@ip-172-31-86-10:~$ docker pull richarddoc/infr2670:webserver
webserver: Pulling from richarddoc/infr2670
edaedc954fb5: Already exists
40ef70634c15: Pull complete
068c5df5f817: Pull complete
e2cd45e8d2a5: Pull complete
Digest: sha256:ffa0c510420613d5662cb9e6447f86f55d0a922eaa75387ecb20426549fdbdf9
Status: Downloaded newer image for richarddoc/infr2670:webserver
docker.io/richarddoc/infr2670:webserver
ubuntu@ip-172-31-86-10:~$ docker pull sharubaa/sharubaa:webserver
webserver: Pulling from sharubaa/sharubaa
Digest: sha256:f476ad771540a59a8b478ab504111fe2e51d0ccec9484d011de5886b0a8289a3
Status: Image is up to date for sharubaa/sharubaa:webserver
docker.io/sharubaa/sharubaa:webserver
ubuntu@ip-172-31-86-10:~$ docker pull sharubaa/sharubaa:hello2670
hello2670: Pulling from sharubaa/sharubaa
Digest: sha256:de6a4e42036d959692812d171063823efc5ac162c609f3d7106e22e88761d11e
Status: Image is up to date for sharubaa/sharubaa:hello2670
docker.io/sharubaa/sharubaa:hello2670
ubuntu@ip-172-31-86-10:~$ packet_write_wait: Connection to 3.95.6.170 port 22: Broken pipe
sharuaa@Sharubaa:~$ ssh -i ashwin.pem ubuntu@3.95.6.170
ssh: connect to host 3.95.6.170 port 22: Connection timed out
sharuaa@Sharubaa:~$ ssh -i ashwin.pem ubuntu@3.95.6.170
ssh: connect to host 3.95.6.170 port 22: Connection timed out
sharuaa@Sharubaa:~$ ssh -i ashwin.pem ubuntu@1) Launch a Ubuntu VM on AWS. Use an existing key or create a new one. Use an existing security group or create a new one. Add port 80 to this security group.
 the VM-bash: syntax error near unexpected token `)'


# Fsharuaa@Sharubaa:~$
irst, masharuaa@Sharubaa:~$ 2) SSH to your VM
-bash: syntax error near unexpected token `)'
sharuaa@Sharubaa:~$
sharuaa@Sharubaa:~$ ssh -i yourkey.pem ubuntu@ip_of_your_VM
ke sure Warning: Identity file yourkey.pem not accessible: No such file or directory.
to uninstall these old packages:
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
# Add the repository to Apt sources:
echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# Install docker
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl start docker

docker version  #if it shows permission denied at the bottom, add ubuntu to the group and run docker version again
sudo usermod -aG docker ubuntu
CTRL+D
ssh back into the VM
docker version
4) Test Docker

docker run hello-world
The Hands-On

Follow along with me in class. We are going to build an image using a Dockerfile. This image will have Ubuntu as base and it will ship with a webserver (Apache).

Next, we will execute the image (a running docker image is a container).

I will also show you how to create a Docker image to run your own Python program.

Then we will use DockerHub to push/pull our images from the repository.

Deliverables

1) Push the web server and the python images we create during the lecture to DockerHub.

Submit the command(s) you used to push the image as well as screenshots that show both images on Dockerhub (use your name as your dockerhub user). Go into your repository, then click on the Tags tab - it lists all your images there.
2) Pull the two images above and execute the containers.

Submit the command(s) you used to pull the images from Dockerhub. Also, submit screenshots of the resuts of "docker ps -a", along with a screenshot of your browser pointing to the IP of the VM (showing the webpage we just created).
3) Create a simple bash script that stops all containers (you can use nested commands in the script)

Submit the script code and a screenshot of its execution and the results of "docker ps -a“.
4) Create a simple bash script that removes all containers

Submit the script code and a screenshot of its execution and the results of "docker ps -a“
Put everything into a PDF file and submit.ssh: Could not resolve hostname ip_of_your_vm: Name or service not known
sharuaa@Sharubaa:~$ 3) Install docker on the VM
-bash: syntax error near unexpected token `)'
sharuaa@Sharubaa:~$
sharuaa@Sharubaa:~$ # First, make sure to uninstall these old packages:
sharuaa@Sharubaa:~$ for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
[sudo] password for sharuaa:
Sorry, try again.
[sudo] password for sharuaa:




Sorry, try again.
[sudo] password for sharuaa:
sudo: 3 incorrect password attempts
[sudo] password for sharuaa:
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package 'docker-doc' is not installed, so not removed
The following packages were automatically installed and are no longer required:
  efibootmgr libefiboot1 libefivar1
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package 'docker-compose' is not installed, so not removed
The following packages were automatically installed and are no longer required:
  efibootmgr libefiboot1 libefivar1
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package podman-docker
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package 'containerd' is not installed, so not removed
The following packages were automatically installed and are no longer required:
  efibootmgr libefiboot1 libefivar1
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package 'runc' is not installed, so not removed
The following packages were automatically installed and are no longer required:
  efibootmgr libefiboot1 libefivar1
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.
sharuaa@Sharubaa:~$ ssh -i ashwin.pem ubuntu@3.94.179.106
The authenticity of host '3.94.179.106 (3.94.179.106)' can't be established.
ECDSA key fingerprint is SHA256:avApMqSOlpVmiRyNcF9bfTcSaPi6Wq7Pv1K2YSOpLN0.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '3.94.179.106' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.19.0-1025-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat Sep 30 00:17:37 UTC 2023

  System load:  0.228515625       Processes:                101
  Usage of /:   50.4% of 7.57GB   Users logged in:          0
  Memory usage: 29%               IPv4 address for docker0: 172.17.0.1
  Swap usage:   0%                IPv4 address for eth0:    172.31.86.10


Expanded Security Maintenance for Applications is not enabled.

128 updates can be applied immediately.
68 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Fri Sep 29 20:27:40 2023 from 192.197.54.35
ubuntu@ip-172-31-86-10:~$ docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED       STATUS                     PORTS     NAMES
958a74b8c523   webserver     "/bin/sh -c /root/ru…"   4 hours ago   Exited (137) 4 hours ago             myserver
344924659aae   ubuntu        "/bin/bash"              4 hours ago   Exited (137) 4 hours ago             eloquent_ride
722f3a6c1587   ubuntu        "/bin/bash"              4 hours ago   Exited (137) 4 hours ago             hungry_montalcini
068455080a7d   ubuntu        "/bin/bash"              4 hours ago   Exited (0) 4 hours ago               priceless_faraday
1a5a955241b3   ubuntu        "/bin/bash"              4 hours ago   Exited (0) 4 hours ago               inspiring_shannon
9fc995d11ebf   hello-world   "/hello"                 4 hours ago   Exited (0) 4 hours ago               compassionate_johnson
c7dadf720985   hello-world   "/hello"                 4 hours ago   Exited (0) 4 hours ago               eloquent_almeida
ubuntu@ip-172-31-86-10:~$ Connection to 3.94.179.106 closed by remote host.
Connection to 3.94.179.106 closed.
sharuaa@Sharubaa:~$