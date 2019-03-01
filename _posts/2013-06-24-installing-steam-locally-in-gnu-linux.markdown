---
layout: post
title:  "Installing Steam locally in GNU/Linux"
author: Matias S.
date:   2013-06-24 03:00 -0300
categories: [fun]
tags: [linux,ubuntu,steam,games]
---

[Steam](http://store.steampowered.com/) for GNU/Linux has been around for a while now, and thanks to the efforst of [Valve](http://www.valvesoftware.com/) more and more games are been released to the open-source OS!

But since I'm a bit paranoid, I choose to install it at my `$HOME` folder, avoiding any unnecessary permissions (*root-less* installation).

I've been using it like this for quite a while, with no noticeable downside.

## How-to

![Steam on Linux](/assets/installing-steam-locally-in-gnu-linux-screenshot.png)

### Dependencies

First, with the help of you distro package manager make sure the following dependencies are installed:

- python
- curl
- jockey-common
- libc6 (\>= 2.15)
- python-apt
- xterm ou gnome-terminal ou konsole
- xz-utils
- zenity

### Installation

Then, get the installer from the [official site](http://store.steampowered.com/about/) or download the [.deb](http://en.wikipedia.org/wiki/Deb_\(file_format\)) from Valve's [repository](http://media.steampowered.com/client/installer/steam.deb) as pointed out in their [github page](https://github.com/ValveSoftware/steam-for-linux).

Copy the installer to a temporary folder (e.g.: `~/temp/`), and extract it:

```console
$ ar x steam.deb
```

Extract the `data.tar.gz` file:

```console
$ tar xf data.tar.gz
```

Now extract [Steam](http://store.steampowered.com/) to it's final destination folder (e.g.: `~/steam/`):

```console
$ tar xf ~/temp/usr/lib/steam/bootstraplinux_ubuntu12_32.tar.xz ~/steam/
```

Go to the directory `~/steam/` and execute [Steam](http://store.steampowered.com/):

```console
$ ./steam.sh
```

In the first run all the necessary files will be downloaded and soon it will be ready for game!
