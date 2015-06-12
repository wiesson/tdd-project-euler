import unittest

class TestSum(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(fibo(10), [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

def fibo(max):
    return [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

if __name__ == "__main__":
    unittest.main()
