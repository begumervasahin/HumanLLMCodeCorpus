class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_after_node(self, prev_node, data):
        if prev_node is None:
            print("Previous node must be valid.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None
linked_list = LinkedList()
linked_list.head = Node("Aimie Ojuba")
data2 = Node("latifs")
data3 = Node("Toni")
data4 = Node("slap")
linked_list.head.next = data2
data2.next = data3
data3.next = data4
linked_list.insert_at_beginning("imaa")
linked_list.insert_at_end("beast")
linked_list.insert_after_node(data2, "shile")
linked_list.delete_node("slap")
linked_list.print_list()