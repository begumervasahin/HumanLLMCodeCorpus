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
        while current.next:
            current = current.next
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        self.tail = new_node
    def insert_node(self, target_value, new_value):
        if self.tail.value == target_value:
            self.add_node_last(new_value)
        else:
            current = self.head.next
            while current.value != target_value:
                current = current.next
            new_node = Node(new_value)
            new_node.next = current.next
            new_node.next.prev = new_node
            new_node.prev = current
            current.next = new_node
    def remove_node(self, target_value):
        if self.head.value == target_value:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.value == target_value:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head.next
            while current.value != target_value:
                current = current.next
            current.prev.next = current.next
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
if __name__ == "__main__":
    d_linked_list = DoublyLinkedList(10)
    d_linked_list.add_node_last(20)
    d_linked_list.add_node_last(30)
    d_linked_list.add_node_last(40)
    d_linked_list.remove_node(40)
    d_linked_list.show()
    d_linked_list.show_reverse()