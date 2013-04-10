from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='zopeskel.diazotheme',
      version=version,
      description="Paster templates for Plone Diazo theme package",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Zope3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone zope diazo',
      author='ZopeSkel Team: Steve McMahon',
      author_email='zopeskel@lists.plone.org',
      url='http://github.com/collective/zopeskel.diazotheme',
      license='GPL 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zopeskel'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'PasteDeploy',
          'Paste',
          'ZopeSkel'
          # -*- Extra requirements: -*-
      ],
      setup_requires=["PasteScript"],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      diazotheme = zopeskel.diazotheme.diazotheme:DiazoTheme
      """,
      )
