#!/usr/bin/env python3
# coding: utf-8

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "addhelper",
    version = "0.0.1",
    author = "Jon Summer",
    author_email = "__replace_the_email__@here.com",
    description = ("a tool for add two numbers"),
    license = "MIT",
    url = "https://jonsummer.github.io/",
    packages=find_packages(),
    long_description=read('README.md'),
    test_suite="tests",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    options={'bdist_wheel':{'universal':'1'}},
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
    install_requires=[ "six >= 1.11.0, <2.0.0" ],
)