class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
class DoublyList:
    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head
    def add_node_last(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    def insert_node(self, val, new_val):
        new_node = Node(new_val)
        if self.tail.value == val:
            self.add_node_last(new_val)
        elif self.head.value == val:
            new_node.next = self.head.next
            if new_node.next:
                new_node.next.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head
        else:
            current = self.head
            while current and current.value != val:
                current = current.next
            if current:
                new_node.next = current.next
                if new_node.next:
                    new_node.next.prev = new_node
                current.next = new_node
                new_node.prev = current
    def remove_node(self, val):
        if self.head.value == val:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif self.tail.value == val:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            current = self.head
            while current and current.value != val:
                current = current.next
            if current:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
    def show_reverse(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
    def show(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
d_list = DoublyList(10)
d_list.add_node_last(20)
d_list.add_node_last(30)
d_list.add_node_last(40)
d_list.remove_node(40)
print("Forward traversal:")
d_list.show()
print("Reverse traversal:")
d_list.show_reverse()