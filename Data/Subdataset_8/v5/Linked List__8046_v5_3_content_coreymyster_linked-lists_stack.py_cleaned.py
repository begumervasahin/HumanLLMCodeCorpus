class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self, new_data):
        self.data = new_data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
class UnorderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def add_first(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    def size(self):
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
    def remove_first(self):
        if self.is_empty():
            return None
        removed_item = self.head.get_data()
        self.head = self.head.get_next()
        return removed_item
mylist = UnorderedList()
mylist.add_first(80)
print(mylist.size())
mylist.add_first(3)
mylist.add_first(67)
mylist.add_first(15)
print(mylist.size())
print(mylist.search(15))
mylist.remove_first()
print(mylist.size())
print(mylist.search(15))
mylist.add_first(15)
print(mylist.size())
