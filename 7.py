#! /usr/bin/env python

import unittest
import helper


def find_prime(n):
    prime_counter = 1
    last_prime = 0
    i = 2
    while prime_counter <= n:
        if helper.isprime(i):
            prime_counter += 1
            last_prime = i
        i += 1

    return last_prime


class TestCase(unittest.TestCase):
    # @unittest.skip
    def test_my_test(self):
        self.assertEqual(find_prime(6), 13)
        self.assertEqual(find_prime(10001), 104743)


unittest.main()
