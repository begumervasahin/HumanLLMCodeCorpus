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
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    def insert_node(self, target_value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current and current.value != target_value:
            current = current.next
        if not current:
            print(f"Value {target_value} not found in the list.")
            return
        new_node.next = current.next
        if new_node.next:
            new_node.next.prev = new_node
        current.next = new_node
        new_node.prev = current
        if current == self.tail:
            self.tail = new_node
    def remove_node(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
        if not current:
            print(f"Value {value} not found in the list.")
            return
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
    def show_reverse(self):
        current = self.tail
        while current:
            print(current.value, end=" ")
            current = current.prev
        print()
    def show(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()
if __name__ == "__main__":
    d_list = DoublyLinkedList(10)
    d_list.add_node_last(20)
    d_list.add_node_last(30)
    d_list.add_node_last(40)
    d_list.remove_node(40)
    print("Forward traversal:")
    d_list.show()
    print("Reverse traversal:")
    d_list.show_reverse()