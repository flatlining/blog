---
layout: post
title:  "Writing and reading image files for the Raspberry Pi"
author: Matias S.
date:   2014-03-08 18:24 -0300
categories: [raspberry pi]
tags: [linux]
---

The [Raspberry Pi](http://www.raspberrypi.org/) is this small cool ARM based board that you can use for endless projects and is compatible with many GNU/Linux distributions!

It main storage is a simple SD card that goes into a slot in the board and in this card is where you must install the linux distro you choose to use.

Attention  
: In this article, to exemplify the installation of a distro, we will use the [ARM](https://en.wikipedia.org/wiki/ARM_architecture) compatible version of [Arch Linux](http://archlinuxarm.org/platforms/armv6/raspberry-pi), being installed in a Ubuntu environment.

## Writing the image

To write an image file to a SD card follow these steps:

1. Download the the latest zip containing the image:
   - [Image file](http://archlinuxarm.org/os/ArchLinuxARM-rpi-latest.zip)
   - [MD5 sum](http://archlinuxarm.org/os/ArchLinuxARM-rpi-latest.zip.md5)
1. Extract the zip file to your hard drive, giving you the image **archlinux-hf-\*.img**.
1. Open a terminal window and go the the directory where the image was extracted.
1. Insert the card in your computer (at least 2GB\[1\]).
1. Find out the path to the card:
   1. With the command `df -h` list all mounted partitions.
   1. Your card partition will be listed as something like **/dev/mmcblk0p1**.
   1. The sd card itself is the partition path minus the **pX** part, so something like **/dev/mmcblk0**, take note of it.
1. Unmount the card with the command:
   ```console
   $ sudo umount /dev/mmcblk0
   ```
1. To write the image to the card use:
   ```console
   $ sudo dd bs=1M if=archlinux-hf-*.img of=/dev/mmcblk0
   ```
1. It could take a while, so *relax*.
1. After is done run the command `sync` to ensure the cache is flushed
   and it safe to remove the card:
   ```console
   $ sudo sync
   ```
1. Remove it, insert it in the Pi.
1. Have fun!

## Reading the image

After a while using your system you will have a fully personalized linux installation with your favorite programs in it.

But not everything are roses, SD cards are susceptible to corruption and a bad block can ruin your system, because of that is always handy to have a backup copy for easy recover!

And backing it up is pretty similar to how we write it in the first place:

1. Insert the card with your system image in your computer.
1. Like when writing your image, use the `df -h` command to find the path to the card.
1. Unmount it with `sudo umount /dev/path_to_card`.
1. Now, use the `dd` command to write an image of the card to a file:
   ```console
   $ sudo dd bs=1M if=/dev/path_to_card of=mylinux.image
   ```
1. Execute the `sync` to flush the cache:
   ```console
   $ sudo sync
   ```
1. Remove your card.

That's it! Now you have a full backup of your customized system, if you have any problem just write it to a card line we did in the first part of this article and it will be as good as new!

Attention
: The generated image can only be written to a card with the same (or larger) size, so the backup of a 4GB card can be written to a 8GB card, but not to a 2GB one.
