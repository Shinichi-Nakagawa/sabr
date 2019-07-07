#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

__author__ = 'Shinichi Nakagawa'


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    return ''


setup(
    name='sabr',
    version='2.0',
    description='SABRmetrics calculator for Python',
    long_description=read_file('README.rst'),
    author='Shinichi Nakagawa',
    author_email='spirits.is.my.rader@gmail.com',
    url='https://github.com/Shinichi-Nakagawa/sabr',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    include_package_data=True,
    keywords=['baseball', 'MLB', 'SABRmetrics', 'SABR', 'Major league baseball'],
    license='MIT License',
)
