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
class LinkedList:
    def __init__(self):
        self.head = Node(None)
    def is_empty(self):
        return self.head.get_next() is None
    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head.get_next())
        self.head.set_next(new_node)
    def size(self):
        current = self.head.get_next()
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count
    def search(self, item):
        current = self.head.get_next()
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False
    def remove(self, item):
        current = self.head.get_next()
        previous = self.head
        while current is not None:
            if current.get_data() == item:
                previous.set_next(current.get_next())
                return
            previous = current
            current = current.get_next()
if __name__ == "__main__":
    my_list = LinkedList()
    print(my_list.is_empty())
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    print(my_list.size())
    print(my_list.search(2))
    print(my_list.search(4))
    my_list.remove(1)
    print(my_list.size())
    print(my_list.is_empty())