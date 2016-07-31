#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages
from pyalgs import __author__, __email__, __version__

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="pyalgs",
    version=__version__,
    description="Python Algorithms contains a collection of useful algorithms for educational purposes.",
    long_description=readme + '\n\n' + history,
    author=__author__,
    author_email=__email__,
    url="https://github.com/mihassan/python_algorithms",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords="pyalgs",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    test_suite="tests",
)