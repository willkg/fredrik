===========================
Deploying a Fredrik project
===========================

At some point, you might want to deploy your app somewhere. There
are a bunch of Platform-as-a-Service systems that you could
deploy to. This very very loosely covers how to do that.

You'll need to know how to use git and be managing your Fredrik
project with git. If you're not, then you should go learn git.
That's outside the scope of this documentation.

.. contents::
   :local:


OpenShift
=========

1. If you don't have an OpenShift account, then `create one
   <https://www.openshift.com/>`_.

2. Once you have an account, you can create an OpenShift app
   for your Fredrik project like this::

       rhc app create -a '<name>' --no-git -t python-2.7

   You want to do ``--no-git`` otherwise OpenShift creates
   the git repository for you and populates it with stuff.

   After you do that, it'll create the app and spit out some lines of
   output. One of those is the git url.

3. If you're not using git, then cd to your project root directory
   and do::

       git init

   Then add the files for your project and commit them.

4. Then add the new remote::

       git remote add upstream -m master <git-url>

   using the git url they give you.

   That names the remote "upstream". If you want to use a different name
   that's fine.

5. When you want to push changes from your master branch, do::

       git push upstream


.. SeeAlso::

   https://www.openshift.com/
     OpenShift site

   https://www.openshift.com/developers/python
     OpenShift Python app hosting

   https://github.com/openshift/flask-example
     OpenShift Flask example app

   https://www.openshift.com/developers/deploying-and-building-applications
     Deploying changes for OpenShift applications


Heroku
======

FIXME
