#!/usr/bin/env python3
# coding: utf-8

import unittest
import six
import addhelper


class TestAddEngine(unittest.TestCase):
    def test_add(self):
        eng = addhelper.AddEngine()
        result = eng.add(1,2)
        self.assertEqual(3,result)

if __name__ == '__main__':
    print("PY Version 2: ",six.PY2)
    print("PY Version 3: ",six.PY34)
    unittest.main()