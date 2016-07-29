#!/usr/bin/env python
from setuptools import setup, find_packages
from parsexec import __author__, __version__, __license__

setup(
    name='parsexec',
    version=__version__,
    description='parse and execution',
    license=__license__,
    author=__author__,
    author_email='nekoneko.myaomyao@gmail.com',
    url='https://github.com/harukaeru/Parsexec.git',
    keywords='parse execution markdown',
    packages=find_packages(),
    install_requires=[],
)
