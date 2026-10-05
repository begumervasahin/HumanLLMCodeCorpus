from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    def search(self, item):
        current = self.head
        while current:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False
    def remove(self, item):
        current = self.head
        previous = None
        while current:
            if current.get_data() == item:
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            previous = current
            current = current.get_next()
    def selection_sort(self):
        current = self.head
        while current:
            minimum = current
            item = current.get_next()
            while item:
                if item.get_data() < minimum.get_data():
                    minimum = item
                item = item.get_next()
            if minimum != current:
                current.get_data(), minimum.get_data() = minimum.get_data(), current.get_data()
            current = current.get_next()
    def print_linked(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()