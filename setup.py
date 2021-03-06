#!/usr/bin/env python

from setuptools import setup

setup(
    name="seedcount",
    version="0.0.1",
    packages=[],
    entry_points={
        'console_scripts': ['seed_buy = seed_buy.__main__:main']
        
    }
)