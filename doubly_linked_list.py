class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None