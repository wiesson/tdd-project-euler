#! /usr/bin/env python

import unittest
import math


def euler_six(n):
    return sum(n) ** 2 - sum([x ** 2 for x in n])


class TestCase(unittest.TestCase):
    # @unittest.skip
    def test_my_test(self):
        self.assertEqual(euler_six(range(11)), 2640)
        self.assertEqual(euler_six(range(101)), 25164150)


unittest.main()
