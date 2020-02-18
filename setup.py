#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

PACKAGE_NAME = "hashcode20"

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, PACKAGE_NAME, '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()


setup(
    name=about["__title__"],
    description=about['__description__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about["__email__"],
    long_description=readme,
    packages=find_packages(),
    install_requires=[],
    tests_require=[],
    entry_points={
        'console_scripts': ["hashcode20=hashcode20.__main__:main"],
    },
    classifiers=[
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT Software License',
            'Programming Language :: Python :: 3.7',
    ],
    license=about['__license__']
)
