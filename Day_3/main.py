class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Stack:
    def __init__(self):
        self.head: Node | None = None
        self.item: int = 0

    def __len__(self) -> int:
        """Return length of list. Speed is O(1)"""
        return self.item

    def push(self, data) -> None:
        """Add a new node to the top of the stack. speed is O(1)"""
        new_node: Node = Node(data)
        if self.head:
            new_node.prev = self.head
            self.head: Node = new_node
        else:
            self.head: Node = new_node

        self.item += 1

    def pop(self) -> Node | None:
        """remove and return the top most node. Speed is O(1)"""
        current = self.head
        if not current:
            return None
        self.head = current.prev
        current.prev = None
        self.item -= 1
        return current.data

    def top(self) -> Node:
        """Return the top most value of the stack. Speed is O(1)"""
        return self.head.data

    def clear(self):
        """clear the entire stack"""
        self.head = None
        self.item = 0

