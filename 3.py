from math import sqrt, ceil
import unittest

"""
Prime < 100

2, 3, 5, 7, 11, 13, 17,
19, 23, 29, 31, 37, 41,
43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97
"""


def is_prime(prime):
    # http://stackoverflow.com/a/4117879/2050629
    return all(prime % i for i in range(2, ceil(sqrt(prime))))


def highest_prime_factor_new(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i += 1

    return n


def highest_prime_factor(number):
    # max_number = int(number/2) if sqrt(number) <= number/2 else int(sqrt(number))
    for each in range(int(number / 2), 1, -1):
        if number % each:
            continue

        if not is_prime(each):
            continue

        return each


class TestCase(unittest.TestCase):
    @unittest.skip("not today")
    def test_highest_prime_factor(self):
        self.assertEqual(highest_prime_factor(26), 13)  # [2, 13]
        self.assertEqual(highest_prime_factor(30), 5)  # [2, 3, 5]
        self.assertEqual(highest_prime_factor(13195), 29)  # [5, 7, 13, 29]
        self.assertEqual(highest_prime_factor(600851475143), 6857)  # [5, 7, 13, 29]

    def test_highest_prime_factor_new(self):
        # self.assertEqual(highest_prime_factor(26), 13)  # [2, 13]
        self.assertEqual(highest_prime_factor(30), 5)  # [2, 3, 5]
        self.assertEqual(highest_prime_factor(13195), 29)  # [5, 7, 13, 29]
        self.assertEqual(highest_prime_factor(600851475143), 6857)  # [5, 7, 13, 29]

    def test_is_prime(self):
        self.assertEqual(is_prime(3), True)

unittest.main()

# for each in range(2, 100):
#     print(each, highest_prime_factor(each))

# print(highest_prime_factor(600851475143))
