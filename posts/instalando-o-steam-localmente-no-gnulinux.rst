.. link: http://steamcommunity.com/app/221410/discussions/7/846939071149987459/#c846939071182282142
.. description: Tutorial de como instala o Steam na pasta home do seu usuário no linux, evitando assim o acesso a permissões desnecessárias
.. tags: linux, games, steam
.. date: 2013/06/24 00:29:46
.. title: Installing Steam locally on GNU/Linux
.. slug: installing-steam-locally-on-gnulinux


.. http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. http://docutils.sourceforge.net/docs/ref/rst/directives.html
.. http://rst.ninjs.org/
.. https://gist.github.com/dupuy/1855764

.. role:: console(code)
    :language: console

Steam_ for GNU/Linux has been around for a while now, and thanks to the efforst of Valve_ more and more games are been released to the open-source OS!

But since I'm a bit paranoid, I choose to install it at my :console:`$HOME` folder, avoiding any unnecessary permissions (*root-less* installation).

I've been using it like this for quite a while, with no noticeable downside.

.. TEASER_END

How-to
======

Dependencies
------------

.. figure:: /images/instalando-o-steam-localmente-no-gnulinux-screenshot.png
   :target: /images/instalando-o-steam-localmente-no-gnulinux-screenshot.png
   :figwidth: 300 px
   :align: right
   :alt: Steam On Linux

   Steam On Linux

First, with the help of you distro package manager make sure the following dependencies are installed:

* python
* curl
* jockey-common
* libc6 (>= 2.15)
* python-apt
* xterm ou gnome-terminal ou konsole
* xz-utils
* zenity

Installation
------------

Then, get the installer from the `official site <http://store.steampowered.com/about/>`_ or download the `.deb`_ from Valve's `repository <http://media.steampowered.com/client/installer/steam.deb>`_ as pointed out in their github page [1]_

Copy the installer to a temporary folder (e.g.: :console:`~/temp/`), and extract it:

.. code:: console

    $ ar x steam.deb

Extract the :console:`data.tar.gz` file:

.. code:: console

    $ tar xf data.tar.gz

Now extract Steam_ to it's final destination folder (e.g.: :console:`~/steam/`):

.. code:: console

    $ tar xf ~/temp/usr/lib/steam/bootstraplinux_ubuntu12_32.tar.xz ~/steam/

Go to the directory :console:`~/steam/` and execute Steam_:

.. code:: console

    $ ./steam.sh

In the first run all the necessary files will be downloaded and soon it will be ready for game!

----

References
==========

.. [1] https://github.com/ValveSoftware/steam-for-linux

.. _Steam: http://store.steampowered.com/
.. _Valve: http://www.valvesoftware.com/
.. _.deb: http://en.wikipedia.org/wiki/Deb_(file_format)
