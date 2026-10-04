class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node cannot be None")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
    def insert_before(self, next_node, new_data):
        if next_node is None:
            print("The given next node cannot be None")
            return
        new_node = Node(new_data)
        new_node.next = next_node
        new_node.prev = next_node.prev
        if next_node.prev is not None:
            next_node.prev.next = new_node
        else:
            self.head = new_node
        next_node.prev = new_node
    def sorted_insert(self, data):
        new_node = Node(data)
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push(5)
    dll.append(6)
    dll.push(1)
    dll.insert_after(dll.head, 3)
    dll.insert_before(dll.head.next, 2)
    dll.print_list()