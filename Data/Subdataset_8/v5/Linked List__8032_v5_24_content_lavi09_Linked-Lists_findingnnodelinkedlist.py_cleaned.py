class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def find_nth_node_from_end(self, n):
        if not self.head:
            return None
        slow_pointer = self.head
        fast_pointer = self.head
        for _ in range(n):
            if fast_pointer is None:
                return None
            fast_pointer = fast_pointer.next
        while fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        return slow_pointer.data
llist = LinkedList()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_list()
print("2nd node from the end:", llist.find_nth_node_from_end(2))