class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total
    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
    def get(self, index):
        if index >= self.length():
            print('Index out of bounds')
            return None
        current_idx = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_idx == index:
                return current_node.data
            current_idx += 1
    def erase(self, index):
        if index >= self.length():
            print('Index out of bounds')
            return
        current_idx = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_idx == index:
                last_node.next = current_node.next
                return
            current_idx += 1
my_list = LinkedList()
my_list.append(2)
my_list.append(1)
my_list.erase(1)
my_list.display()