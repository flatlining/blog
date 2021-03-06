---
layout: post
title:  "Arch Linux ARM image for Raspberry Pi"
author: Matias S.
date:   2015-08-09 23:51 -0300
categories: [raspberry pi]
tags: [linux,arch]
---

Currently neither [Raspberry Pi](https://www.raspberrypi.org/) nor the [Arch Linux ARM](http://archlinuxarm.org/) website offer an image ready for use of Arch Linux for Raspberry Pi, and because of that I created this small step by steps on how to do it on Linux.

## Tutorial

1.  Download the last release [image](http://archlinuxarm.org/developers/downloads) for your Pi (ARM).
1.  Create a image file of 2gb:
    ```console
    $ dd if=/dev/zero of=arch.img bs=1M count=1850
    ```
1.  Partition the image file[^1]:
    ```console
    $ fdisk arch.img
    ```
    1.  Type **o**. This will clear out any partitions on the drive.
    1.  Type **p** to list partitions. There should be no partitions left.
    1.  Type **n**, then **p** for primary, **1** for the first partition on the drive, press ENTER to accept the default first sector, then type **+100M** for the last sector.
    1.  Type **t**, then **c** to set the first partition to type W95 FAT32 (LBA).
    1.  Type **n**, then **p** for primary, **2** for the second partition on the drive, and then press ENTER twice to accept the default first and last sector.
    1.  Write the partition table and exit by typing **w**.
1.  Check the partitions created:
    ```console
    $ fdisk -l arch.img
    ```
1.  Mount the **boot** partition[^2]:
    ```console
    $ losetup -v -f -o $((2048 * 512)) --sizelimit 104857600 arch.img
    ```
1.  Mount the **root** partition:
    ```console
    $ losetup -v -f -o $((206848 * 512)) --sizelimit 1833959424 arch.img
    ```
1.  Format and mount **boot** partition
    ```console
    $ mkfs.vfat /dev/loop0
    $ mkdir boot
    $ mount /dev/loop0 boot
    ```
1.  Format and mount **root** partition
    ```console
    $ mkfs.ext4 /dev/loop1
    $ mkdir root
    $ mount /dev/loop1 root
    ```
1.  Become **root**:
    ```console
    $ sudo su -
    ```
1. Extract **image** files:
   ```console
   $ bsdtar -xpf ArchLinuxARM-rpi-latest.tar.gz -C root
   $ sync
   ```
1. Copy **boot** files:
   ```console
   $ mv root/boot/* boot
   $ sync
   ```
1. Unmount partitions:
   ```console
   $ umount boot root
   $ rmdir boot root
   ```
1. Back to your user:
   ```console
   $ exit
   ```
1. Detach partitions:
   ```console
   $ losetup -d /dev/loop0
   $ losetup -d /dev/loop1
   ```

Your image is ready to be used!

---

[^1]: [Raspberry Pi, SD Card Creation](http://archlinuxarm.org/platforms/armv6/raspberry-pi)
[^2]: [Calculate offset and sizelimit of a partition](http://unix.stackexchange.com/a/72449)
