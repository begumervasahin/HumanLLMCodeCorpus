class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printing(self):
        print_value = self.head
        while print_value is not None:
            print(print_value.data)
            print_value = print_value.next
    def begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def between(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
    def end(self, data):
        newest = Node(data)
        if self.head is None:
            self.head = newest
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = newest
    def delete(self, data):
        current = self.head
        if current is not None and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None
x = LinkedList()
x.head = Node("Aimie Ojuba")
data2 = Node("latifs")
data3 = Node("Toni")
data4 = Node("slap")
x.head.next = data2
data2.next = data3
data3.next = data4
x.begin("imaa")
x.end("beast")
x.between(x.head.next, "shile")
x.delete("slap")
x.printing()