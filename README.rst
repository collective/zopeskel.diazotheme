Introduction
============

This is a ZopeSkel template package for creating a skeleton Plone add-on
package. The skeleton package creates a Diazo (plone.app.theming) theme package
and associated css and js resources for use with plone.app.theming in
Plone 4.2+.

Use this package when you want to package a Diazo theme as a Plone add on,
particularly if you need to override viewlet or skin templates in the process.

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

And run the buildout

Usage
======

Creating a dexterity content package, typically done in your buildout's src
directory. Command line for creating a package named diazotheme.mytheme would be::

  ../bin/zopeskel diazotheme diazotheme.mytheme

This will create a Python package with a directory structure like this::

    diazotheme.mytheme/
    |-- diazotheme
    |   +-- mytheme
    |       |-- diazo_resources
    |       |   +-- static
    |       |-- locales
    |       |-- profiles
    |       |   +-- default
    |       +-- template_overrides
    |-- diazotheme.mytheme.egg-info
    +-- docs

The typically customized parts are in the diazotheme.mytheme/diazotheme/mytheme subdirectory.

diazo_resources
---------------

This is where you'll put your Diazo resources including a rules XML file and one or more template HTML files.
You may wish to interactively develop these theme elements in the theming editor (for Plone 4.3+), then export the resources and add them here.

A sample theme is included to use as a starting point.
Just replace it if you don't need it.
The sample theme's key feature is that it makes use of all of Plone's CSS and JavaScript as a starting point.

NOTE: The Diazo theme will be available in Plone even if you have not installed the package.
It will not be applied, though, until enabled in the Theme configlet of site setup.

diazo_resources/static
----------------------

This is the conventional place to put static resources like CSS, JS and image files.
There's nothing magic about "static". Remove or replace it if it fits your needs.

locales
-------

If your templates include translatable messages, you may provide translation files in this directory.
Ignore it if you don't need translations.

profiles, profiles/default
--------------------------

This is the Generic Setup profile for the add on.
The is applied when you use the "add ons" configlet in site setup to install the package.

This profile has a couple of important features:

* It sets up a BrowserLayer, which insures tha template overrides and registry settings do not affect other Plone installations unless this theme is installed.

* It has template registrations for CSS and JavaScript resource registries.
  These allow you to incorporate static resources which are part of the theme into the Plone resource registries for efficient merging with other CSS and JS resources.

template_overrides
------------------

You may use this directory to override any Plone viewlet, portlet or skin template.

To override a template, copy or create a template in this directory using the full dotted name of the template you wish to override.

For example, if you wish to override the standard Plone footer, you would find the original at::

    plone.app.layout/plone/app/layout/viewlets/footer.pt

The full, dotted name for this resource is::

    plone.app.layout.viewlets.footer.pt

Template overrides are only applied when the BrowserLayer is installed.
So, they won't affect Plone installations where this package is not installed.

A sample override for the Plone footer is included. Delete it if you don't need it.

See the documentation for `z3c.jbot <https://pypi.python.org/pypi/z3c.jbot>`_.

