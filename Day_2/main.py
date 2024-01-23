class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.tail: Node | None = None
        self.head: Node | None = None
        self.item: int = 0

    def __len__(self) -> int:
        """Return length of list. Speed is O(1)"""
        return self.item

    def __iter__(self):
        """Return a generator object containing node data.
            Speed is O(n)"""
        current = self.tail
        while current:
            value: str | int = current.data  # assuming values will be str or int
            current: Node = current.next
            yield value

    def append(self, data) -> None:
        """Add a new node to the end of the list. speed is O(1)"""
        new_node: Node = Node(data)
        if self.head:
            new_node.prev: Node = self.head
            self.head.next: Node = new_node
            self.head: Node = new_node
        else:
            self.head: Node = new_node
            self.tail: Node = self.head

        self.item += 1

    def remove(self, data) -> None:
        """remove node base on it data. Speed is O(n)"""
        current = self.tail
        node_deleted = False
        if current is None:
            node_deleted = False
        elif current.data == data:
            self.tail = current.next
            self.tail.prev = None
            node_deleted = True
        elif self.head.data == data:
            self.head = self.head.prev
            self.head.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

    def search(self, data) -> bool:
        """search for existence of data. Return true if found otherwise, false. Speed is O(n)"""
        current: Node = self.tail
        while current:
            value: str | int = current.data  # assuming values will be str or int
            if value == data:
                return True  # return true if found
            else:
                current: Node = current.next  # move to next node if not found

        return False  # return false if list is empty

    def clear(self):
        """clear the entire linkedlist"""
        self.tail = None
        self.head = None
        self.item = 0
