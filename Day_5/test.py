import unittest
from main import unsorted_search, sorted_search
unsorted_list = [7, 9, 2, 6, 4, 5]
sorted_list = [3, 4, 5, 6,7]


class MyTestCase(unittest.TestCase):

    def test_unsorted_search(self):
        """search for value and compare the index"""
        self.assertEqual(unsorted_search(unsorted_list, 5), 5)

    def test_sorted_search(self):
        """search for value and check the index"""
        self.assertEqual(sorted_search(sorted_list, 3), 0)

if __name__ == '__main__':
    unittest.main()
