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
