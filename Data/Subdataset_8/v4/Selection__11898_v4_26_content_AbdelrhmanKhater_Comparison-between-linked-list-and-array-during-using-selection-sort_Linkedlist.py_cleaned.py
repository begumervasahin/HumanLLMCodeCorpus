class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
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
        self.head = Node(None)
    def is_empty(self):
        return self.head.get_next() == None
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head.get_next())
        self.head.set_next(temp)
    def size(self):
        current = self.head.get_next()
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count
    def search(self, item):
        current = self.head.get_next()
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    def remove(self, item):
        current = self.head.get_next()
        previous = None
        found = False
        while not found and current is not None:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())