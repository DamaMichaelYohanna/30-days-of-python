import unittest
from main import binary_search
sorted_list = [3, 4, 5, 6,7]


class MyTestCase(unittest.TestCase):

    def test_binary_search(self):
        """search for value and compare the index"""
        self.assertEqual(binary_search([3, 4, 5, 6,7], 6), 3)


if __name__ == '__main__':
    unittest.main()
