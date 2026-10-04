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
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def find_nth_node_from_end(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        count = 0
        while count < n:
            if ref_ptr is None:
                print(f"The list has fewer than {n} elements.")
                return
            ref_ptr = ref_ptr.next
            count += 1
        while ref_ptr is not None:
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        if main_ptr is not None:
            print(main_ptr.data)
        else:
            print(f"The list has fewer than {n} elements.")
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("The linked list is:")
    llist.print_list()
    print("\nThe 2nd node from the end is:")
    llist.find_nth_node_from_end(2)