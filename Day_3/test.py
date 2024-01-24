import unittest
from main import Stack

stack: Stack = Stack()
stack.push("hello")
stack.push("hello")


class MyTestCase(unittest.TestCase):

    def test_push(self):
        """test if item is added successfully."""
        self.assertEqual(stack.push("hello"), None)

    def test_length(self):
        """test the length of the singlylinkedlist"""
        self.assertEqual(len(stack), 2)  # add assertion here

    def test_pop(self):
        """test if item is remove successfully."""
        self.assertEqual(stack.pop(), "hello")

    def test_top(self):
        stack.push("welcome")
        self.assertEqual(stack.top(), "welcome")

    def test_zclear(self):
        stack.clear()
        self.assertEquals(stack.head, None)

if __name__ == '__main__':
    unittest.main()
