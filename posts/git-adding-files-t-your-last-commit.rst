.. title: GIT: Adding files to your last commit!
.. slug: git-adding-files-to-your-last-commit
.. date: 2014/04/26 23:51:44
.. tags: git, development
.. link: http://lostechies.com/derickbailey/2010/06/09/git-oops-i-forgot-to-add-those-new-files-before-committing/
.. description: Easily add missing files t your last GIT commit
.. type: text

.. role:: console(code)
    :language: console

More than once when using git_ I forgot to add a file to a commit, like with this post:

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

One terrible way to fix this is commiting the missing files and specifying the mistake in the commit message, another **awesome** way would be using the :console:`--amend` parameter of the :console:`commit` command to add the files to the last commit.

.. TEASER_END

First stage the missing files:

.. code:: console

    $ git add posts/git-adding-files-t-your-last-commit.rst.pt_br

Then commit them using the :console:`--amend` parameter:

.. code:: console

    $ git commit --amend -C HEAD
    [master f813cd5] en/pt_br: GIT: Adding files to your last commit!
     2 files changed, 18 insertions(+)
     create mode 100644 posts/git-adding-files-t-your-last-commit.rst
     create mode 100644 posts/git-adding-files-t-your-last-commit.rst.pt_br

The :console:`-C` tell the commit to use the commiting message of **HEAD**, if you omit the :code:`-C HEAD` the message editor will open.

Note the we only have one commit with the message *en/pt_br: GIT: Adding files to your last commit!*:

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

Keep in mind that :console:`--amend` will change the **SHA1 ID** of the commit.

.. _git: http://git-scm.com/
