---
title:  "How to struct a python library"
date:   2021-01-30
categories: 
  - Python
tags:
  - Project
excerpt: >
  In this post, I would like to explain what is the basic directory structure for a python library.
---

## Introduction

If we want to provide a python library to others, it is best way that we create a pip package. Then anyone who need the library will use pip to install that package. So, the question is, how to struct a python library. In this post, I would like to explain what is the basic directory structure for a python library.

## Standard

Almost every python project apply pip to manage dependencies. The first step to solve the problem is to find what is the standard that pip used. The following link explains the basic concept for `setup.py`.

[https://docs.python.org/3/distutils/setupscript.html](https://docs.python.org/3/distutils/setupscript.html)

The most important options for setup.py packages group, such as package_dir, packages.

## Example

In this tutorial, let us develop a simple package named addhelper, which provides a class named AddEngine. A AddEngine object will help others to add two integers together through calling `add` function.

### 1. Calling example

The calling example is attached below, and the code will be executed perfectly when we devloped a python package named addhelper.

```python
import addhelper

eng = addhelper.AddEngine()
result = eng.add(1,2)
print("Result: ",result)
```

### 2. Create the addhelper package

First of all, we need develope the whole addhelper code. Assuming the root dir is py_lib_root.

```python
# Path Structure: 
#   py_lib_root/addhelper/
#                         __init__.py 
#                         api.py

#!/usr/bin/env python3
# coding: utf-8

import six

class AddEngine:
    def __init__(self):
        pass

    def add(self, a, b):
        return a+b

if __name__ == '__main__':
    a = 1
    b = 2
    eng = AddEngine() 
    result = eng.add(a, b)
    print("%d + %d = %d"%(a, b, result))

```

and in the dir `py_lib_root/addhelper`, the command shows AddEngine object handles two integers and add them together.

```shell
% pwd
py_lib_root/addhelper
% python3 ./api.py 
1 + 2 = 3
```

### 3. Technical problems

Right now, we have developed the main tools AddEngine. However, we faced several technical problems.

Fristly, how to import the package. Assuming we are dir py_lib_root, and we would like to use addhelper package, then we would like to write python code like this.

```python
import addhelper
eng = addhelper.AddEngine()
```

However, AddEngine class is in the file api.py, and now how to export AddEngine to the top level of addhelper.

If we do nothing, we need the following code. But we do not really want to use so long long import syntax.

```python
# PWD: py_lib_root
from addhelper import api as addhelper
end = addhelper.AddEngine()
```

In order to make it easy, we need export AddEngine from api.py module into it's parent module. The `__init__.py` can help us.

```python
# file: __init__.py

#!/usr/bin/env python3
# coding: utf-8

from .api import AddEngine

__all__ = ["AddEngine"]
```

In this way, the calling code will be.

```python
>>> import addhelper
>>> eng = addhelper.AddEngine()
>>> eng.add(1,5)
6
```

### 4. Write a setup.py file

The setup.py file is the soul of a pip package. following the link below we will create our own setup.py file.

[https://pythonhosted.org/an_example_pypi_project/setuptools.html](https://pythonhosted.org/an_example_pypi_project/setuptools.html)

```python
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
```

In this `setup.py` file, some options are more important, such as `python_requires`, and `test_suite`

### 5. Use Makefile to handle build, install and test

Makefile is good tool to handle all kinds of development, such as build, install and test.

```make
.PHONY: all build clean test run

all:build

build: clean
	@python2 ./setup.py build sdist bdist_wheel
	@python3 ./setup.py build sdist bdist_wheel

clean: uninstall
	rm -rf ./build ./dist *.egg-info
run: 
	@python3 ./addhelper/api.py
	@python2 ./addhelper/api.py
	
test: install
	@python3 tests/addhelper_test.py
	@python2 tests/addhelper_test.py

install: build
	@pip3 install --user ./dist/*.whl
	@pip2 install --user ./dist/*.whl

uninstall:
	@pip3 uninstall -y addhelper
	@pip2 uninstall -y addhelper

dep:
	@easy_install --user install  pip==19.2.3
```

### 6. include other files

The python package uses MANIFEST.in to include and exclude files such as Makefile. The following code shows how to write a MANIFEST.in file.

```
graft tests
include Makefile
global-exclude *.py[cod]
```

