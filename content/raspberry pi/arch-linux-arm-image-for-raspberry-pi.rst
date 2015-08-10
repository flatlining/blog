Arch Linux ARM image for Raspberry Pi
#####################################

:status: published
:date: 2015-08-09T23:51-03:00
:modified: 2015-08-09T23:51-03:00
:tags: linux, arch
:slug: arch-linux-arm-image-for-raspberry-pi
:lang: en
:authors: Matias S.
:summary: Create an image file of Arch LinuxARM to easily install it anywhere

.. https://wiki.archlinux.org/index.php/Raspberry_Pi
.. http://elinux.org/ArchLinux_Install_Guide
.. http://hreikin.wordpress.com/2013/12/22/arch-linux-raspberry-pi-install-guide/comment-page-1/

Currently neither `Raspberry Pi`_ nor the `Arch Linux ARM`_ website offer an image ready for use of Arch Linux for Raspberry Pi, and because of that I created this small step by steps on how to do it on Linux.

Tutorial
========

1. Download the last release image_ for your Pi (ARM).
2. Create a image file of 2gb:

   .. code-block:: console

      $ dd if=/dev/zero of=arch.img bs=1M count=1850

3. Partition the image file [#]_:

   .. code-block:: console

      $ fdisk arch.img

   a. Type **o**. This will clear out any partitions on the drive.
   b. Type **p** to list partitions. There should be no partitions left.
   c. Type **n**, then **p** for primary, **1** for the first partition on the drive, press ENTER to accept the default first sector, then type **+100M** for the last sector.
   d. Type **t**, then **c** to set the first partition to type W95 FAT32 (LBA).
   e. Type **n**, then **p** for primary, **2** for the second partition on the drive, and then press ENTER twice to accept the default first and last sector.
   f. Write the partition table and exit by typing **w**.

4. Check the partitions created:

   .. code-block:: console

      $ fdisk -l arch.img

5. Mount the **boot** partition [#]_:

   .. code-block:: console

      $ losetup -v -f -o $((2048 * 512)) --sizelimit 104857600 arch.img

6. Mount the **root** partition:

   .. code-block:: console

      $ losetup -v -f -o $((206848 * 512)) --sizelimit 1833959424 arch.img

7. Format and mount **boot** partition

   .. code-block:: console

      $ mkfs.vfat /dev/loop0
      $ mkdir boot
      $ mount /dev/loop0 boot

8. Format and mount **root** partition

   .. code-block:: console

      $ mkfs.ext4 /dev/loop1
      $ mkdir root
      $ mount /dev/loop1 root

9. Become **root**:

   .. code-block:: console

      $ sudo su -

10. Extract **image** files:

    .. code-block:: console

       $ bsdtar -xpf ArchLinuxARM-rpi-latest.tar.gz -C root
       $ sync

11. Copy **boot** files:

    .. code-block:: console

       $ mv root/boot/* boot
       $ sync

12. Unmount partitions:

    .. code-block:: console

       $ umount boot root
       $ rmdir boot root

13. Back to your user:

    .. code-block:: console

       $ exit

14. Detach partitions:

    .. code-block:: console

       $ losetup -d /dev/loop0
       $ losetup -d /dev/loop1

Your image is ready to be used!

----

.. [#] `Raspberry Pi, SD Card Creation`_
.. [#] `Calculate offset and sizelimit of a partition`_

.. _Raspberry Pi: https://www.raspberrypi.org/
.. _Arch Linux ARM: http://archlinuxarm.org/
.. _image: http://archlinuxarm.org/developers/downloads
.. _Raspberry Pi, SD Card Creation: http://archlinuxarm.org/platforms/armv6/raspberry-pi
.. _Calculate offset and sizelimit of a partition: http://unix.stackexchange.com/a/72449
