class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
    def add_node_last(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        self.tail = new_node
    def insert_node(self, value, new_value):
        if self.tail.value == value:
            self.add_node_last(new_value)
        elif self.head.value == value:
            new_node = Node(new_value)
            new_node.next = self.head.next
            new_node.prev = self.head
            new_node.next.prev = new_node
            self.head.next = new_node
        else:
            current = self.head.next
            while current.value != value:
                current = current.next
            new_node = Node(new_value)
            new_node.next = current.next
            new_node.next.prev = new_node
            new_node.prev = current
            current.next = new_node
    def remove_node(self, value):
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head.next
            while current.value != value:
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
    def show_reverse(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev
    def show(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
doubly_list = DoublyLinkedList(10)
doubly_list.add_node_last(20)
doubly_list.add_node_last(30)
doubly_list.add_node_last(40)
doubly_list.remove_node(40)
print("Doubly Linked List:")
doubly_list.show()
print("\nDoubly Linked List in Reverse:")
doubly_list.show_reverse()