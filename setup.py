#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='nokaut',
    version='0.1',
    description='Coroutine-based networking library',
    author='Dawid Kostyszak',
    author_email='dawid.kostyszak@stxnext.pl',
    url='http://stxnext.pl',
    packages=['nokaut'],
    install_requires = [
        'lxml',
        'mock',
    ],
    entry_points={
          'console_scripts': [
              'nokaut = nokaut.scripts:parser']
              }
)
