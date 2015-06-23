#! /usr/bin/env python

import unittest
import math


def euler_six(n):
    sum_of_squares = 0
    for each in n:
        sum_of_squares += each * each

    return (sum(n) * sum(n)) - sum_of_squares


class TestCase(unittest.TestCase):
    # @unittest.skip
    def test_my_test(self):
        self.assertEqual(euler_six(range(1, 11)), 2640)
        self.assertEqual(euler_six(range(1, 21)), 25164150)


unittest.main()
