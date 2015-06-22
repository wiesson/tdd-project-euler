#! /usr/bin/env python

import unittest


def my_test_function(x):
    return x


class TestCase(unittest.TestCase):
    # @unittest.skip
    def test_highest_prime_factor(self):
        self.assertEqual(my_test_function(True), True)  # [2, 13]


unittest.main()
