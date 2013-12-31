.. link: 
.. description: Como preparar um ambiente de desenvolvimento python no ubuntu de forma simples e direta
.. category: python
.. tags: linux, ubuntu, python, ambiente
.. date: 2013/02/24 20:05:33
.. title: Ambiente Python com Pythonbrew
.. slug: ambiente-python-com-pythonbrew

.. http://docutils.sourceforge.net/docs/user/rst/quickref.html

.. role:: bash(code)
    :language: bash

Neste artigo será mostrado de forma simples e direta como criar um ambiente de desenvolvimento python_ no ubuntu_ utilizando as ferramentas pythonbrew_ e virtualenv_.

.. TEASER_END

Atenção
    Este artigo foi publicado em dois posts separados no portal Pletax_, `Gerenciando múltiplas versões do python com pythonbrew`_ e `Versionamento de bibliotecas python com virtualenv`_.

Passo a Passo
-------------

Requisitos
**********

* Uma instalação do ubuntu funcional e atualizada. Este tutorial é baseado na versão `quantal quetzal`_, porém deve funcionar igualmente em outras versões
* Conexão ativa com a internet :)
* Familiariedade com o uso do terminal

Pythonbrew
**********

O pythonbrew_ está para o python_ de forma semelhante a como o rvm_ está para o ruby_. Ele facilita (e muito) a instalação e o gerenciamento de múltiplas instâncias do python_ no diretório :bash:`$HOME` do usuário.

Os seguintes comandos serão todos realizados em uma janela de terminal.

Instalação [#]_
^^^^^^^^^^^^^^^

Primeiramente, para evitar qualquer problema com dependências, você deve instalar os seguintes pacotes no ubuntu:

.. code:: bash

    sudo apt-get install curl build-essential libbz2-dev libsqlite3-dev zlib1g-dev libxml2 libxml2-dev libxslt1-dev libgdbm-dev libssl-dev tk-dev libexpat1-dev libncursesw5-dev

Então, para instalá-lo, entre com o comando:

.. code:: bash

    curl -kL http://xrl.us/pythonbrewinstall | bash

após a instalação abra o arquivo :bash:`~/.bashrc` no gedit com o comando:

.. code:: bash

    gedit ~/.bashrc

e adicione a seguinte linha no final do arquivo:

.. code:: bash

    [[ -s $HOME/.pythonbrew/etc/bashrc ]] && source $HOME/.pythonbrew/etc/bashrc

Feche e abra novamente a janela do terminal e o pythonbrew_ estará instalado e pronto para usar!

Utilização [#]_
^^^^^^^^^^^^^^^

Para começar vamos instalar uma versão do python em sua pasta de usuário. Para listar as versões disponíveis para instalação utilize o comando:

.. code:: bash

    pythonbrew list -k

E para instalar, por exemplo, a versão 2.7.3, use:

.. code:: bash

    pythonbrew install Python-2.7.3

ou somente:

.. code:: bash

    pythonbrew install 2.7.3

Aguarde a instalação. Para listar as versões instaladas entre com o comando:

.. code:: bash

    pythonbrew list

Se alguma das versões locais for a versão ativa ela estará marcada na lista com um ``*``.

.. _versão ativa:

Existem duas maneiras de usar uma das versões instaladas:

.. code:: bash

    pythonbrew use 2.3.7

Ao utilizar o parâmetro :bash:`use` a versão selecionada permanecerá ativa somente na sessão atual do terminal.

Ou você poderá utilizar o comando:

.. code:: bash

    pythonbrew switch 2.7.3

Ativando assim a versão **2.7.3** globalmente (para seu usuário).

Se desejar desinstalar uma versão local do python_ use o comando:

.. code:: bash

    pythonbrew uninstall 2.7.3

E para retornar a usar a versão nativa do ubuntu_ desativando o pythonbrew_ use:

.. code:: bash

    pythonbrew off

Para uma lista completa dos comando disponíveis entre com:

.. code:: bash

    pythonbrew -h

Virtualenv
**********

O virtualenv_ é uma ferramenta para criar ambientes de desenvolvimento isolados para o python_, ou seja, pacotes de *bibliotecas* e *dependências* independentes que podem ser alternados livremente.

Por exemplo, você poderia ter dois projetos, um dependente do django_ versão 1.4.3 e outro da 1.5, como manter as duas versões instaladas simultaneamente? Simples! Basta criar dois ambientes independentes com o virtualenv_ onde serão instaladas as dependências de cada projeto, bastando alternar entre eles dependendo do projeto em que você irá trabalhar.

Instalação
^^^^^^^^^^

Para nossa sorte o pythonbrew_ é facilmente integrado ao virtualenv_.

.. _ativá-lo:

Primeiro certifique-se de que a `versão ativa`_ do python_ é a que você quer utilizar e então ative o virtualenv_ para ela:

.. code:: bash

    pythonbrew venv init

E aguarde a instalação.

Utilização
^^^^^^^^^^

Para criar um novo ambiente utilize, por exemplo:

.. code:: bash

    pythonbrew venv create django143

Entre com o seguinte comando para listar todos os ambientes disponíveis para a versão ativa do python_:

.. code:: bash

    pythonbrew venv list

Ative um ambiente com o comando:

.. code:: bash

    pythonbrew venv use django143

Note que o nome do ambiente aparecerá ao lado da prompt de comando, apartir de agora todas as mudanças de bibliotecas afetarão somente o ambiente ativo, por exemplo:

.. code:: bash

    pip install Django==1.4.3

Irá instalar a versão **1.4.3** do django_ somente no ambiente **django143**.

Para sair de um ambiente e retornar para o padrão basta entrar com o comando

.. code:: bash

    deactivate

Outros comandos também estão disponíveis, como:

Deletar um ambiente:

.. code:: bash

    pythonbrew venv delete [enviroment]

Renomear um ambiente:

.. code:: bash

    pythonbrew venv rename [enviroment] [new_name]

Clonar um ambiente:

.. code:: bash

    pythonbrew venv clone [enviroment] [clone_name]

Observações
^^^^^^^^^^^

Tenha em mente que o ambiente do virtualenv_ está atrelada à versão do python_ ativa e não estará disponível para outras versões. e.g.:

    O ambiente **django143** criado com a versão **2.7.3** do python ativa não estará disponível quando a versão **3.3.0** (ou qualquer outra que não for a 2.7.3) for a ativa.

Conclusão
---------

Vemos que a utilização do pythonbrew_ em conjunto com o virtualenv_ permite um controle minucioso sobre seu ambiente de desenvolvimento python_, permitindo controle total das bibliotecas e suas versões instaladas, permitindo flexibilidade no trabalho com diversos projetos distintos.

Obrigado, e até mais!

----

.. [#] `Instalação pythonbrew`_
.. [#] `Utilização pythonbrew`_

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
.. _Instalação pythonbrew: http://github.com/utahta/pythonbrew#installation
.. _Utilização pythonbrew: http://github.com/utahta/pythonbrew#usage