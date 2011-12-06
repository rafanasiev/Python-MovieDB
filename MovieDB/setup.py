#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# $Id: setup.py,v 1.4 2011-11-12 15:54:44 ruslan Exp $

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name'          : 'MovieDB',
    'version'       : '0.1.0',
    'author'        : 'Ruslan A. Afanasiev',
    'author_email'  : 'ruslan.afanasiev@gmail.com',
    'packages'      : ['lib'],
    'scripts'       : ['bin/moviedb.py'],
    'license'       : 'LICENSE.txt',
    'description'   : 'MovieDB manages your own movie library',
    'long_description' : open('README.txt').read(),
    'install_requires' : [],
}

setup(**config)
