Introduction
============

This is a ZopeSkel template package for creating a skeleton Plone add-on
package. The skeleton package creates a Diazo theme package
and associated css and js resources for use with plone.app.theming in
Plone 4.2+.

Use this package when you want to build an add-on that adds css or js
functionality without a theme. The advantage of this is that you may
use the functionality with different themes.

This is a development tool. You should be familiar with Plone and buildout to
use it.

Installation
============

Add these lines into buildout::

  [buildout]
  parts =
     zopeskel

  [zopeskel]
  recipe = zc.recipe.egg
  eggs =
     ZopeSkel
     Paste
     PasteDeploy
     PasteScript
     zopeskel.diazotheme
     ${buildout:eggs}

And run the buildout

Usage
======

Creating a dexterity content package, typically done in your buildout's src
directory::

  ../bin/zopeskel diazotheme

Notes
=====

Egg Directories
---------------

In order to support local commands, ZopeSkel/Paster will create Paste,
PasteDeploy and PasteScript eggs inside your product. These are only needed
for development. You can and should remove them from your add-on distribution.

Errors
------

If you hit and error like this::

  pkg_resources.DistributionNotFound: plone.app.relationfield: Not Found for: my.product (did you run python setup.py develop?)

when attempting to run `paster addcontent`, then you need to ensure that
Paster knows about all the relevant eggs from your buildout.

Add `${instance:eggs}` to your `paster` section in your buildout, thusly::

  [zopeskel]
  recipe = zc.recipe.egg
  eggs =
     ...
     ${instance:eggs}
  entry-points = paster=paste.script.command:run

where `instance` is the name of your ``plone.recipe.zope2instance`` section.
Re-run the buildout and the issue should be resolved.
