.. link:
.. description: A simple and direct approach on the creation of a python development environment using ubuntu and the pythonbrew and virtualenv tools
.. tags: python, linux, development
.. date: 2013/02/24 20:05:33
.. title: Python environment with Pythonbrew
.. slug: python-environment-with-pythonbrew


.. http://docutils.sourceforge.net/docs/user/rst/quickref.html

.. role:: bash(code)
    :language: bash

In this articles a simple and direct approach on the creation of a python_ development environment using ubuntu_ and the pythonbrew_ and virtualenv_ tools.

.. TEASER_END

Attention
    This articles was publish in two separeted post at the Pletax_ portal, `Gerenciando múltiplas versões do python com pythonbrew`_ and `Versionamento de bibliotecas python com virtualenv`_ (both in brazilian portuguese).

Step by Step
============

Requirements
------------

* An updated ubuntu_ instalation. This tutorial is based on the `quantal quetzal`_ release, but should work with other versions
* An internet connection :)
* Familiarity with terminal use

Pythonbrew
----------

The pythonbrew_ is to python_ what rvm_ is to ruby_ (mostly). Facilitating the process of installation and management of multiple python_ instances on the users :bash:`$HOME` folder.

All the following commands must be executed in a terminal window.

Installation [#]_
^^^^^^^^^^^^^^^^^

First of all install the required dependencies:

.. code:: bash

 sudo apt-get install curl build-essential libbz2-dev libsqlite3-dev zlib1g-dev libxml2 libxml2-dev libxslt1-dev libgdbm-dev libssl-dev tk-dev libexpat1-dev libncursesw5-dev

Then install it with the command:

.. code:: bash

    curl -kL http://xrl.us/pythonbrewinstall | bash

After the installation open :bash:`~/.bashrc` with gedit:

.. code:: bash

    gedit ~/.bashrc

And add this line at the end of the file:

.. code:: bash

    [[ -s $HOME/.pythonbrew/etc/bashrc ]] && source $HOME/.pythonbrew/etc/bashrc

Restart the terminal session (open and close the terminal window :D) and the pythonbrew_ will be ready to use!

How to use it [#]_
^^^^^^^^^^^^^^^^^^

First let's install a python_ version in your user folder. to list the available versions use the command:

.. code:: bash

    pythonbrew list -k

And to install, for example the version 2.7.3, use:

.. code:: bash

    pythonbrew install Python-2.7.3

Or just:

.. code:: bash

    pythonbrew install 2.7.3

After the installation is done you can list the locally available version with:

.. code:: bash

    pythonbrew list

The active version will be marked with a ``*`` (no version marked means the system version is been used).

.. _active version:

There are two ways of activating the instances:

.. code:: bash

    pythonbrew use 2.3.7

When using the :bash:`use` parameter the version will be activeted only to the current session.

Or you can use:

.. code:: bash

    pythonbrew switch 2.7.3

Activating the version **2.7.3** globally (for your user).

To uninstall an instance enter the command:

.. code:: bash

    pythonbrew uninstall 2.7.3

And to rollback to the system version deactivating the pythonbrew_ use:

.. code:: bash

    pythonbrew off

For a complete list of command use the application help:

.. code:: bash

    pythonbrew -h

Virtualenv
----------

With virtualenv_ you can create isolated environments of development for python_, that is *bundles* of *modules* and *libraries* that can be activated and deactivated freely.

For example, if you have two django_ projects, one using version 1.4.3 and other version 1.5, You could create two virtualenv_ environments where all the correct dependencies of each project will be installed, and then activating the required environment depending on which project you are working.

Installation
^^^^^^^^^^^^

The pythonbrew_ is easily integrated with virtualenv_.

.. _activate it:

First make sure that the `active version`_ of python is the one that you want to use, then active the virtualenv_:

.. code:: bash

    pythonbrew venv init

And wait for the installation to finish.

How to use it
^^^^^^^^^^^^^

To create a new environment use:

.. code:: bash

    pythonbrew venv create django143

Then use the following command to list the available environments to the current python_ instance:

.. code:: bash

    pythonbrew venv list

And to activate a specific environment:

.. code:: bash

    pythonbrew venv use django143

Check that the current environment is displayed between parentesis beside the command prompt. From now on all libraries installed will only affect this environment, for example:

.. code:: bash

    pip install Django==1.4.3

Will install django_ version **1.4.3** only in the environment **django143**.

To close an environment use:

.. code:: bash

    deactivate

Other usefull commands:

Delete an environment:

.. code:: bash

    pythonbrew venv delete [enviroment]

Rename an environment:

.. code:: bash

    pythonbrew venv rename [enviroment] [new_name]

Clone an environment:

.. code:: bash

    pythonbrew venv clone [enviroment] [clone_name]

Observations
^^^^^^^^^^^^

Keep in mind the the virtualenv_ environment is attached to the active python_ version and won't be available for other versions. e.g.:

    For example: the **django143** environment create with the **2.7.3** version won't be available when the version **3.3.0** is active.

Conclusion
==========

We can see that the use of pythonbrew_ and virtualenv_ together allow a great level of control over you development environments in a way that you can easily work with different version of the same library.

Cheers!

----

References
==========

.. [#] `Installing pythonbrew`_
.. [#] `Using pythonbrew`_

.. _Pletax: http://www.pletax.com/
.. _Gerenciando múltiplas versões do python com pythonbrew: http://www.pletax.com/2013/03/gerenciando-multiplas-versoes-do-python-com-pythonbrew/
.. _Versionamento de bibliotecas python com virtualenv: http://www.pletax.com/2013/04/versionamento-de-bibliotecas-python-com-virtualenv/
.. _python: http://www.python.org/
.. _ubuntu: http://www.ubuntu.com/
.. _pythonbrew: http://github.com/utahta/pythonbrew
.. _virtualenv: http://www.virtualenv.org/
.. _Quantal Quetzal: http://wiki.ubuntu.com/QuantalQuetzal
.. _rvm: http://rvm.io/
.. _ruby: http//www.ruby-lang.org/
.. _django: http://www.djangoproject.com/
.. _Installing pythonbrew: http://github.com/utahta/pythonbrew#installation
.. _Using pythonbrew: http://github.com/utahta/pythonbrew#usage
