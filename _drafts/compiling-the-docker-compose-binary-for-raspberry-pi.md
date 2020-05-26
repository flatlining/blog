---
layout: post
title:  "Compiling the docker-compose binary for Raspberry Pi"
author: Matias S.
categories: [container]
tags: [linux,raspberry pi,arm,docker]
---

Nowadays the hassles of installing docker on a Raspberry Pi are mostly gone, besides specialized distros like [dietpi](https://dietpi.com/) - where the installation is one command-line away - or [hypriot](https://blog.hypriot.com/) - which comes with it preinstallled and optimized - the official documentation already includes instructions for using an officla `arm` supported repository:

![Install docker using the repository]({{ "/assets/compiling-the-docker-compose-binary-for-raspberry-pi-arm.png" | relative_url }})

But trying to install docker-compose using the [official instructions](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)...

![Install docker-compose]({{ "/assets/compiling-the-docker-compose-binary-for-raspberry-pi-compose-install.png" | relative_url }})

...will return an error, or not, since the command fail without any warning:

![No visible error]({{ "/assets/compiling-the-docker-compose-binary-for-raspberry-pi-compose-install-error.png" | relative_url }})

But try to use it afterwards to see what happens, those keen on the eye will noticed that the download was only 9kb, the size of the `404 Not Found` error response, check it by going to [https://github.com/docker/compose/releases/download/1.25.5/docker-compose-Linux-armv7l](https://github.com/docker/compose/releases/download/1.25.5/docker-compose-Linux-armv7l).
