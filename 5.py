#! /usr/bin/env python
from functools import reduce
from math import ceil, sqrt

import unittest


def is_prime(prime):
    # http://stackoverflow.com/a/4117879/2050629
    return all(prime % i for i in range(2, ceil(sqrt(prime))))


def prime_factors(n):
    primes_list = []
    z = n
    while z > 1:
        i = 2
        prime_found = False
        while i * i <= n and not prime_found:
            if z % i == 0:
                prime_found = True
                p = i
            else:
                i = i + 1
        if not prime_found:
            p = z

        primes_list.append(p)
        z = z // p
    return primes_list


def smallest_multiple_slow(n_range):
    n = 1
    while True:
        for each in n_range:
            if n % each:
                break

            if each == 10 and each == len(n_range) + 1:
                print("> " + str(n))
                return True

        n = n + 1

    return False


def smallest_multiple_new(n_range):
    primes = []
    prime_factors_list = []
    for each in n_range:
        if is_prime(each):
            primes.append(each)
        prime_factors_list.append(prime_factors(each))

    primes_per_range_item = {}

    for prime in primes:
        primes_per_range_item[prime] = 0
        for each in prime_factors_list:
            if primes_per_range_item.get(prime) < each.count(prime):
                primes_per_range_item[prime] = each.count(prime)

    num = 1
    for each in [pow(k, v) for (k, v) in primes_per_range_item.items()]:
        num *= each

    print(num)

    return True


class TestCase(unittest.TestCase):
    # @unittest.skip
    def test_smallest_multiple(self):
        self.assertEqual(smallest_multiple_new(range(2, 11)), True)  # [2, 13]
        self.assertEqual(smallest_multiple_new(range(2, 21)), True)  # [2, 13]


unittest.main()
