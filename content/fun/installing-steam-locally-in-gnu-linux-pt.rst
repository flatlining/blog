Instalando o Steam localmente no GNU/Linux
##########################################

:status: published
:date: 2013-06-24T03:00-03:00
:modified: 2013-06-24T03:00-03:00
:tags: linux, ubuntu, steam, games
:slug: installing-steam-locally-in-gnu-linux
:lang: pt
:authors: Matias S.
:summary: Instale o Steam na pasta home do seu usuário no linux, evitando assim o acesso a permissões desnecessárias

.. role:: console(code)
   :language: console

Já faz um tempo que o Steam_, plataforma de distribuição de jogos da Valve_, teve sua versão para GNU/Linux lançada trazendo com ela diversos títulos que antes estavam somente disponíveis para outros sistemas operacionais.

Porém como sou meio paranóico optei por instala-lo na minha pasta :console:`$HOME` evitando assim qualquer permissão de acesso desnecessária (*root-less*). Já venho utilizando-o dessa forma faz algum tempo, sem nenhum contratempo.

A Receita
=========

.. figure:: {filename}/images/installing-steam-locally-in-gnu-linux-screenshot.png
   :target: {filename}/images/installing-steam-locally-in-gnu-linux-screenshot.png
   :width: 100%
   :align: center
   :alt: Steam no Linux

   Steam no Linux

Dependências
------------

Use seu gerenciador de pacotes preferido e certifique-se que as seguintes dependências estão instaladas:

* python
* curl
* jockey-common
* libc6 (>= 2.15)
* python-apt
* xterm ou gnome-terminal ou konsole
* xz-utils
* zenity

Instalação
----------

Baixe o instalador do `site oficial <http://store.steampowered.com/about/>`_ pelo GNU/Linux ou diretamente o arquivo `.deb`_ do `repositório <http://media.steampowered.com/client/installer/steam.deb>`_ da Valve como recomendado pela mesma no seu github [1]_

Crie um diretório temporário e copie o instalador para ele (e.g.: :console:`~/temp/`)

Extraia o conteúdo do instalador:

.. code-block:: console

   $ ar x steam.deb

Extraia os dados do arquivo :console:`data.tar.gz`:

.. code-block:: console

   $ tar xf data.tar.gz

Extraia agora o Steam_ para seu diretório de preferência (e.g.: :console:`~/steam/`):

.. code-block:: console

   $ tar xf ~/temp/usr/lib/steam/bootstraplinux_ubuntu12_32.tar.xz ~/steam/

Finalmente acesse o diretório :console:`~/steam/` e execute o Steam_ com o comando:

.. code-block:: console

   $ ./steam.sh

Na primeira execução ele ira fazer o download dos arquivos necessários e em seguida estará pronto para uso!

----

.. [1] https://github.com/ValveSoftware/steam-for-linux

.. _Steam: http://store.steampowered.com/
.. _Valve: http://www.valvesoftware.com/
.. _.deb: http://en.wikipedia.org/wiki/Deb_(file_format)
