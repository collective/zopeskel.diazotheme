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

