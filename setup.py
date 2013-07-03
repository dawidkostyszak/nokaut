#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='nokaut',
    version='0.1',
    description='Coroutine-based networking library',
    author='Linden Lab',
    author_email='sldev@lists.secondlife.com',
    url='http://wiki.secondlife.com/wiki/Eventlet',
    packages=['nokaut'],
    install_requires = [
        'lxml',
    ],
)
