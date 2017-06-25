#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='drf_zillow',
    url='https://github.com/sassoo/drf_zillow',
    license='BSD',
    description='Zillow API interface for DRF',
    author='Sassoo',
    author_email='noreply@devnull.seriously',
    install_requires=[
        'lxml',
        'requests',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
