class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
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
            self.head.next: Node = new_node
            self.head: Node = new_node
        else:
            self.head: Node = new_node
            self.tail: Node = new_node

        self.item += 1

    def remove(self, data) -> None:
        """remove node base on it data. Speed is O(n)"""
        current: Node = self.tail
        previous: Node = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail: Node = current.next
                else:
                    previous.next: Node = current.next
                self.item -= 1

            previous: Node = current
            current: Node = current.next
