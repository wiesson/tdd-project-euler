#! /usr/bin/env python

import unittest


def my_test_function(n):
    return n


class TestCase(unittest.TestCase):
    # @unittest.skip
    def test_my_test(self):
        self.assertEqual(my_test_function(n), n)


unittest.main()
