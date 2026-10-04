class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.sublist_head = None
    def __repr__(self):
        return f"Node({self.data})"
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False
    def remove(self, item):
        current = self.head
        previous = None
        while current:
            if current.data == item:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                if current == self.tail:
                    self.tail = previous
                return
            previous = current
            current = current.next
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
