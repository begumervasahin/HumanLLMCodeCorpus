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
            print("Error: The given previous node cannot be None")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
    def insert_before(self, next_node, new_data):
        if next_node is None:
            print("Error: The given next node cannot be None")
            return
        new_node = Node(new_data)
        new_node.next = next_node
        if next_node.prev is not None:
            new_node.prev = next_node.prev
            next_node.prev.next = new_node
        next_node.prev = new_node
    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
if __name__ == "__main__":
    llist = DoublyLinkedList()
    llist.push(5)
    llist.append(6)
    llist.push(1)
    llist.insert_after(llist.head, 3)
    llist.insert_before(llist.head.next, 2)
    llist.print_list()