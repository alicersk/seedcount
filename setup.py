#!/usr/bin/env python

from setuptools import setup

setup(
    name="seedcount",
    version="0.0.1",
    author="Alice RS",
    author_email="",
    license="GPLv3",
    description="",
    install_requires = ["pandas", "numpy", "streamlit", "altair", "toyplot", "os", "random"],
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        'console_scripts': ['seed_buy = seed_buy.__main__:main']
        
    }
)