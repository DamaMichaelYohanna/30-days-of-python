import unittest
from main import Queue

queue: Queue = Queue()
queue.enqueue("first item")


class MyTestCase(unittest.TestCase):

    def test_dequeue(self):
        """test if item is remove successfully."""
        self.assertEqual(queue.dequeue(), "first item")

    def test_enqueue(self):
        """test if item is added successfully."""
        self.assertEqual(queue.enqueue("hello"), None)

    def test_length(self):
        """test the length of the singlylinkedlist"""
        self.assertEqual(len(queue), 1)  # add assertion here

    def test_zclear(self):
        queue.clear()
        self.assertEquals(queue.head, None)

if __name__ == '__main__':
    unittest.main()
