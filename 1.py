import unittest

class TestSum(unittest.TestCase):
    def test_generate_natural_numbers(self):
        self.assertEqual(generate_natural_numbers(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_find_three_five_in_natural_numbers(self):
        self.assertEqual(find_three_five_in_array(list(range(1, 10))), 23)
        self.assertEqual(find_three_five_in_array(list(range(1, 8))), 14)

def generate_natural_numbers(max):
    return list(range(0, max))

def find_three_five_in_array(r):
    li = []

    for each in r:
        if(each % 3 == 0 or each % 5 == 0):
            li.append(each)

    return sum(li)

if __name__ == "__main__":
    print(find_three_five_in_array(list(range(1, 1000))))

    unittest.main()
