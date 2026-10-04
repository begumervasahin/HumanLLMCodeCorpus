
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
            print(current.data, end=' ')
            current = current.next
        print()
    def find_nth_from_end(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        for _ in range(n):
            if ref_ptr is None:
                print(f"The linked list has less than {n} elements.")
                return
            ref_ptr = ref_ptr.next
        while ref_ptr:
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        print(f"The {n}th node from the end is: {main_ptr.data}")
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Linked List elements:")
    llist.print_list()
    n = 2
    llist.find_nth_from_end(n)