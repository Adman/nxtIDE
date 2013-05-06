#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='nxtIDE',
      version='0.7',
      description='the only thing you need to play with Lego robots and Python',
      author='XLC Team',
      author_email='xlc.team@gmail.com',
      url='http://xlcteam.github.com/nxtIDE',
      packages=['nxtemu', 'nxted'],
      package_data = {
          'nxtemu': ['nxtemu/*.yml', 'nxtemu/floor/*'],
          'nxted' : ['nxted/*.ini', 'nxted/icons/*']
      },
      entry_points = {
          'console_scripts': [
              'nxtemu = nxtemu.nxtemu:main',
              'nxted = nxted.nxted:main'
              ]     
      }
     )
