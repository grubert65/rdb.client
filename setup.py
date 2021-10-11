#!/usr/bin/env python

"""The setup script."""

import codecs
import os

from setuptools import setup, find_namespace_packages


###################################################################

DESCRIPTION="Abstract Sql class to be subclassed by drivers"
KEYWORDS = [
    'rdb.client',
]
###################################################################

setup(
    name="rdb.client",
    author="Marco Masetti",
    author_email="grubert65@gmail.com",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/x-rst",
    license="BSD",
    url="https://github.com/grubert65/rdb.client",
    keywords=KEYWORDS,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[],
    include_package_data=True,
    packages=find_namespace_packages(include=['rdb.client', 'rdb.client.*']),
    zip_safe=False,
    version="0.1.0",
)
