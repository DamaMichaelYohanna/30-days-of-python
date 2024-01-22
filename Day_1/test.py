import unittest
from main import SinglyLinkedList

singlylinkedlist: SinglyLinkedList = SinglyLinkedList()


class MyTestCase(unittest.TestCase):

    def test_append(self):
        """test if item is added successfully."""
        self.assertEqual(singlylinkedlist.append("hello"), None)

    def test_length(self):
        """test the length of the singlylinkedlist"""
        self.assertEqual(len(singlylinkedlist), 1)  # add assertion here

    def test_remove(self):
        """test if item is remove successfully."""
        singlylinkedlist.remove("hello")
        self.assertEqual(len(singlylinkedlist), 0)

    def test_search(self):
        found = singlylinkedlist.search("hello")
        self.assertEqual(found, False)

    def test_clear(self):
        singlylinkedlist.clear()
        self.assertEquals(singlylinkedlist.head, None)

if __name__ == '__main__':
    unittest.main()
