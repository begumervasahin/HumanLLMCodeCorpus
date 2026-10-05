class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def insert_node(self, data):
        self.size += 1
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def get_size(self):
        return self.size
    def insert_end(self, data):
        self.size += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node
    def traverse_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
    def remove_node(self, data):
        if not self.head:
            print('Linked list is empty')
            return
        self.size -= 1
        if self.head.data == data:
            self.head = self.head.next_node
            return
        previous_node = None
        current_node = self.head
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node
        if current_node is None:
            print('Data not found in the linked list')
            return
        previous_node.next_node = current_node.next_node
my_list = LinkedList()
my_list.insert_node(10)
my_list.insert_node(35)
my_list.insert_node(67)
my_list.insert_node(89)
my_list.insert_node(341)
print("The size of the list is:", my_list.get_size())
my_list.insert_end(671)
print("The size of the list is:", my_list.get_size())
my_list.traverse_list()
my_list.remove_node(20)
print("The size of the list is:", my_list.get_size())
my_list.traverse_list()