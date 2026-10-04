class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node must be in the LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
    def delete_node(self, key):
        current = self.head
        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None
linked_list = LinkedList()
linked_list.head = Node("Aimie Ojuba")
node2 = Node("Latifs")
node3 = Node("Toni")
node4 = Node("Slap")
linked_list.head.next = node2
node2.next = node3
node3.next = node4
linked_list.insert_at_beginning("Imaa")
linked_list.insert_at_end("Beast")
linked_list.insert_after(linked_list.head.next, "Shile")
linked_list.delete_node("Slap")
linked_list.print_list()