class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head
        if not current:
            print("Empty List!!!")
            return
        while current:
            print(str(current.data), end=" ")
            current = current.next
            if current:
                print("-->", end=" ")
        print()
my_list = LinkedList()
for i in range(1, 6):
    my_list.add_to_start(i)
my_list.display()
for i in [12, 13, 3]:
    my_list.add_to_end(i)
my_list.display()
