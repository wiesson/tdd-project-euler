#! /usr/bin/env python

import unittest


def my_test_function(x):
    n = 0
    for a in range(999, 100, -1):
        for b in range(a, 100, -1):
            x = a * b
            if x > n:
                s = str(a * b)
                if s == s[::-1]:
                    n = a * b
    return n


class TestCase(unittest.TestCase):
    # @unittest.skip
    def test_highest_prime_factor(self):
        self.assertEqual(my_test_function(True), True)  # [2, 13]

# unittest.main()

print(my_test_function(3))