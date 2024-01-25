class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Queue:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.item: int = 0

    def __len__(self) -> int:
        """Return length of list. Speed is O(1)"""
        return self.item

    def enqueue(self, data) -> None:
        """Add a new node to the tail of the queue. speed is O(1)"""
        new_node: Node = Node(data)
        if not self.tail:
            self.head: Node = new_node
            self.tail: Node = new_node
        else:
            self.tail.prev = new_node
            self.tail = new_node

        self.item += 1

    def dequeue(self) -> Node | None:
        """remove the node at the head. Speed is O(1)"""
        current = self.head
        if not current:
            return None
        self.head = current.prev
        current.prev = None
        self.item -= 1
        return current.data

    def clear(self):
        """clear the entire stack"""
        self.head = None
        self.tail = None
        self.item = 0

