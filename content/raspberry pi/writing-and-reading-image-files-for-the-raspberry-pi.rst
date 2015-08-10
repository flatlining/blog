Writing and reading image files for the Raspberry Pi
####################################################

:status: published
:date: 2014-03-08T18:24-03:00
:modified: 2014-03-08T18:24-03:00
:tags: linux
:slug: writing-and-reading-image-files-for-the-raspberry-pi
:lang: en
:authors: Matias S.
:summary:

.. http://elinux.org/RPi_Easy_SD_Card_Setup

.. role:: console(code)
   :language: console

The `Raspberry Pi`_ is this small cool ARM based board that you can use for endless projects and is compatible with many GNU/Linux distributions!

It main storage is a simple SD card that goes into a slot in the board and in this card is where you must install the linux distro you choose to use.

Attention
    In this article, to exemplify the installation of a distro, we will use the `ARM`_ compatible version of `Arch Linux`_, being installed in a Ubuntu environment.

Writing the image
=================

To write an image file to a SD card follow these steps:

1. Download the the latest zip containing the image:

   * `Image file`_
   * `MD5 sum`_

2. Extract the zip file to your hard drive, giving you the image **archlinux-hf-\*.img**.

3. Open a terminal window and go the the directory where the image was extracted.

4. Insert the card in your computer (at least 2GB [#]_).

5. Find out the path to the card:

   a) With the command :console:`df -h` list all mounted partitions.

   b) Your card partition will be listed as something like **/dev/mmcblk0p1**.

   c) The sd card itself is the partition path minus the **pX** part, so something like **/dev/mmcblk0**, take note of it.

6. Unmount the card with the command:

   .. code-block:: console

      $ sudo umount /dev/mmcblk0

7. To write the image to the card use:

   .. code-block:: console

      $ sudo dd bs=1M if=archlinux-hf-*.img of=/dev/mmcblk0

8. It could take a while, so *relax*.

9. After is done run the command :console:`sync` to ensure the cache is flushed and it safe to remove the card:

   .. code-block:: console

      $ sudo sync

10. Remove it, insert it in the Pi.

11. Have fun!

Reading the image
=================

After a while using your system you will have a fully personalized linux installation with your favorite programs in it.

But not everything are roses, SD cards are susceptible to corruption and a bad block can ruin your system, because of that is always handy to have a backup copy for easy recover!

And backing it up is pretty similar to how we write it in the first place:

1. Insert the card with your system image in your computer.

2. Like when writing your image, use the :console:`df -h` command to find the path to the card.

3. Unmount it with :console:`sudo umount /dev/path_to_card`.

4. Now, use the :console:`dd` command to write an image of the card to a file:

   .. code-block:: console

      $ sudo dd bs=1M if=/dev/path_to_card of=mylinux.image

5. Execute the :console:`sync` to flush the cache:

   .. code-block:: console

      $ sudo sync

6. Remove your card.

That's it! Now you have a full backup of your customized system, if you have any problem just write it to a card line we did in the first part of this article and it will be as good as new!

.. attention::
    The generated image can only be written to a card with the same (or larger) size, so the backup of a 4GB card can be written to a 8GB card, but not to a 2GB one.

----

.. [#] Each system have it's own minimum space spec, make sure to check it in the systems site

.. _Raspberry Pi: http://www.raspberrypi.org/
.. _ARM: https://en.wikipedia.org/wiki/ARM_architecture
.. _Arch Linux: http://archlinuxarm.org/platforms/armv6/raspberry-pi
.. _Image file: http://archlinuxarm.org/os/ArchLinuxARM-rpi-latest.zip
.. _MD5 sum: http://archlinuxarm.org/os/ArchLinuxARM-rpi-latest.zip.md5
