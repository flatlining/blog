---
layout: post
title:  "Compiling the docker-compose binary for Raspberry Pi"
author: Matias S.
categories: [container]
tags: [linux,raspberry pi,arm,docker]
---

Everyone knows the hassles of installing [docker](https://www.docker.com/) on a [Raspberry Pi](https://www.raspberrypi.org/) are mostly gone.

Besides specialized distros like [dietpi](https://dietpi.com/) - where the installation is one command-line away - or [hypriot](https://blog.hypriot.com/) -, which comes with it preinstallled and optimized, the official documentation already includes instructions for using an official `arm` supported repository.

If you consider:

![Install docker using the repository]({{ "/assets/compiling-the-docker-compose-binary-for-raspberry-pi-arm.png" | relative_url }})

But trying to install [docker-compose](https://docs.docker.com/compose/) using the [official instructions](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)...

![Install docker-compose]({{ "/assets/compiling-the-docker-compose-binary-for-raspberry-pi-compose-install.png" | relative_url }})

You'll see it returns an error. Maybe not, since the command fails without any visible error:

![No visible error]({{ "/assets/compiling-the-docker-compose-binary-for-raspberry-pi-compose-install-error.png" | relative_url }})

The download was only 9kb, it was not the expected binary, but the `404 Not Found` error returned when accesing [https://github.com/docker/compose/releases/download/1.25.5/docker-compose-Linux-armv7l](https://github.com/docker/compose/releases/download/1.25.5/docker-compose-Linux-armv7l). There are no [release](https://github.com/docker/compose/releases) builds for `arm` architecture.

It's possible to install `docker-compose` using [pip](https://docs.docker.com/compose/install/#install-using-pip), but what if a pre-compiled binary is desired?

## Compiling

It's actually pretty simple to compile the `docker-compose` binary. The only requirement is a Raspberry Pi with a working `docker` installation.

To build and install the 1.25.5 release:

```sh
# clone the repo
$ git clone https://github.com/docker/compose.git
$ cd compose
# checkout the desired version
$ git checkout 1.25.5
# run the build script
$ ./script/build/linux
# wait a little while... and install it
$ sudo mv dist/docker-compose-Linux-armv7l /usr/local/bin/docker-compose
```

The build script detects the host architecture and compile the binary using the correct docker images, `armhf` on the [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/).

That's it! plain and simple! and don't forget to save it aside so it's easy to reuse it on other boards... because who only has **one** rPi? 🤣
