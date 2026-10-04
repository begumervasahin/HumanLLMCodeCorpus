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
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    def size(self):
        count = 0
        current = self.head
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
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty list")
        current = self.head
        self.head = current.get_next()
        return current.get_data()
if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.push(80)
    print("Size after pushing 80:", my_list.size())
    my_list.push(3)
    my_list.push(67)
    my_list.push(15)
    print("Size after pushing 3 more elements:", my_list.size())
    print("Search for 15:", my_list.search(15))
    my_list.pop()
    print("Size after popping one element:", my_list.size())
    print("Search for 15 after pop:", my_list.search(15))
    my_list.push(15)
    print("Size after pushing 15 again:", my_list.size())
