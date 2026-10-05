class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, newdata):
        self.data = newdata
    def set_next(self, newnext):
        self.next = newnext
class LinkedListUno:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def length(self):
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
        while not found and current is not None:
            if current.get_data() == item:
                found = True
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
            else:
                previous = current
                current = current.get_next()
    def selection_sort(self):
        current = self.head
        while current.get_next() is not None:
            minimum = current
            min_val = current.get_data()
            item = current.get_next()
            while item is not None:
                if min_val > item.get_data():
                    min_val = item.get_data()
                    minimum = item
                item = item.get_next()
            minimum.set_data(current.get_data())
            current.set_data(min_val)
            current = current.get_next()