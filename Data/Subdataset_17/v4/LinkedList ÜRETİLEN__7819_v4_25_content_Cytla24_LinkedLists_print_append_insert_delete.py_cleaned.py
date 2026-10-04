class Node:
    def __init__(self, data_value=None):
        self.data_value = data_value
        self.next_value = None
class LinkedList:
    def __init__(self):
        self.head_value = None
    def print_list(self):
        current_node = self.head_value
        while current_node is not None:
            print(current_node.data_value)
            current_node = current_node.next_value
    def insert_at_beginning(self, data_value):
        new_node = Node(data_value)
        new_node.next_value = self.head_value
        self.head_value = new_node
    def insert_between(self, prev_node, data_value):
        if prev_node is None:
            print("Previous node must be in the LinkedList.")
            return
        new_node = Node(data_value)
        new_node.next_value = prev_node.next_value
        prev_node.next_value = new_node
    def insert_at_end(self, data_value):
        new_node = Node(data_value)
        if self.head_value is None:
            self.head_value = new_node
            return
        last_node = self.head_value
        while last_node.next_value is not None:
            last_node = last_node.next_value
        last_node.next_value = new_node
    def delete_node(self, key):
        current_node = self.head_value
        if current_node is not None and current_node.data_value == key:
            self.head_value = current_node.next_value
            current_node = None
            return
        prev = None
        while current_node is not None and current_node.data_value != key:
            prev = current_node
            current_node = current_node.next_value
        if current_node is None:
            return
        prev.next_value = current_node.next_value
        current_node = None
linked_list = LinkedList()
linked_list.head_value = Node("Aimie Ojuba")
node2 = Node("Latifs")
node3 = Node("Toni")
node4 = Node("Slap")
linked_list.head_value.next_value = node2
node2.next_value = node3
node3.next_value = node4
linked_list.insert_at_beginning("Imaa")
linked_list.insert_at_end("Beast")
linked_list.insert_between(linked_list.head_value.next_value, "Shile")
linked_list.delete_node("Slap")
linked_list.print_list()