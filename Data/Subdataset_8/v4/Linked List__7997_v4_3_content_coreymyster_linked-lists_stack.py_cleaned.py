class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
class UnorderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def push(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    def pop(self):
        current = self.head
        if current is None:
            return None
        self.head = current.get_next()
        return current.get_data()
mylist = UnorderedList()
mylist.push(80)
print(mylist.size())
mylist.push(3)
mylist.push(67)
mylist.push(15)
print(mylist.size())
print(mylist.search(15))
mylist.pop()
print(mylist.size())
print(mylist.search(15))
mylist.push(15)
print(mylist.size())
