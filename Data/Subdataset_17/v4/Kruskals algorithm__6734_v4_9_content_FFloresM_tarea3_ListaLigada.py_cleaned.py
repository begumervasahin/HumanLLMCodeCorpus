class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.sublist_head = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
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
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count
    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            if current == self.tail:
                self.tail = previous
    def display(self):
        current = self.head
        while current is not None:
            print(current.get_data(), end='')
            current = current.get_next()
            if current is not None:
                print(" ->", end=" ")
        print()
