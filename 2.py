import unittest

class TestSum(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(fib(10), [1, 2, 3, 5, 8])
        self.assertEqual(list(better_fib(10)), [1, 2, 3, 5, 8])

    # def test_even_fibu(self):
    #    self.assertEqual(fibo(10, 2), [2, 8, 34])

def fib(max, modulo=None):
    a = 1
    fibo = list()
    fibo.append(a)
    fibo.append(a + 1)
    while (fibo[-2] + fibo[-1]) < max:
        num = fibo[-2] + fibo[-1]
        fibo.append(num)

    return fibo

def better_fib(limit):
    a, b = 1, 2
    while a < limit:
        yield a
        a, b = b, a + b

def even_fib(limit):
    a, b = 0, 1
    while a < limit:
        if not a % 2:
            yield a
        a, b = b, a + b

if __name__ == "__main__":
    unittest.main()
    # print(sum(even_fib(4000000)))
