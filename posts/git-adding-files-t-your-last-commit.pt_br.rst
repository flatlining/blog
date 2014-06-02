.. title: GIT: Adicionando arquivos ao seu último commit!
.. slug: git-adicionando-arquivos-ao-seu-ultimo-commit
.. date: 26-04-2014 23:51:44 UTC-03:00
.. tags: git, desenvolvimento
.. link: http://lostechies.com/derickbailey/2010/06/09/git-oops-i-forgot-to-add-those-new-files-before-committing/
.. description: Adicione facilmente arquivos ao último commit do GIT
.. type: text

.. role:: console(code)
    :language: console


Mais de uma vez ao utilizar o git_ eu esqueci de adicionar um arquivo à um commit, como no exemplo:

.. code:: console

    $ git status
    On branch master
    Your branch is up-to-date with 'origin/master'.

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

        new file:   posts/git-adding-files-t-your-last-commit.rst

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        posts/git-adding-files-t-your-last-commit.rst.pt_br

    $ git commit -am "en/pt_br: GIT: Adding files to your last commit!"
    [master cfa764b] en/pt_br: GIT: Adding files to your last commit!
     1 file changed, 9 insertions(+)
     create mode 100644 posts/git-adding-files-t-your-last-commit.rst
    $ git status
    On branch master
    Your branch is ahead of 'origin/master' by 1 commit.
      (use "git push" to publish your local commits)

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        posts/git-adding-files-t-your-last-commit.rst.pt_br

    nothing added to commit but untracked files present (use "git add" to track)

Uma forma terrível de arrumar esse erro é fazendo outro *commit* especificando o erro na mensagem, outra forma **genial** é utilizando o parâmetro :console:`--amend` do comando :console:`commit` para adicionar um arquivo ao último *commit*.

.. TEASER_END

Primeiramente adicione o arquivo faltante:

.. code:: console

    $ git add posts/git-adding-files-t-your-last-commit.rst.pt_br

Então *commite* ele utilizando o parâmetro :console:`--amend`:

.. code:: console

    $ git commit --amend -C HEAD
    [master f813cd5] en/pt_br: GIT: Adding files to your last commit!
     2 files changed, 18 insertions(+)
     create mode 100644 posts/git-adding-files-t-your-last-commit.rst
     create mode 100644 posts/git-adding-files-t-your-last-commit.rst.pt_br

O :console:`-C` indica ao :console:`commit` para utilizar como mensagem a mesma utilizada pelo *commit* **HEAD**, se o parâmetro :code:`-C HEAD` for omitido o editor de mensagem será aberto.

Note que exise somente um *commit* para a mensagem *en/pt_br: GIT: Adding files to your last commit!*:

.. code:: console

    $ git log
    commit f813cd5eb640aae1a45936af1bf80699f4064bad
    Author: Matias Schertel <matias@schertel.co>
    Date:   Sat Apr 26 23:56:22 2014 -0300

        en/pt_br: GIT: Adding files to your last commit!

    commit 9f0380e37ff0e3861d27faf79d2a12716571e8ff
    Merge: 63b749d 7acc31f
    Author: Matias Schertel <matias@schertel.co>
    Date:   Sat Apr 26 23:48:22 2014 -0300

        Merge branch 'master' of git:co-schertel-blog

Mantenha em mente que o :console:`--amend` irá alterar o **SHA1 ID** do *commit*.

.. _git: http://git-scm.com/
