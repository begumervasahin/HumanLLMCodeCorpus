class Node:
    def __init__(self, value):
        self.info = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def insert_at_end_no_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.info, " ", end='')
                current = current.next
            print()
    def create(self):
        num_nodes = int(input("Enter the number of nodes: "))
        for _ in range(num_nodes):
            data = int(input("Enter data to be inserted: "))
            self.insert_at_end_no_tail(data)
    def tail_element(self):
        if self.head is not None:
            print("Tail element: ", self.tail.info)
    def middle_and_last_element(self):
        if self.head is not None:
            slow_ptr = self.head
            fast_ptr = self.head
            while fast_ptr is not None and fast_ptr.next is not None:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
                if fast_ptr.next is not None:
                    fast_ptr = fast_ptr.next
            print("Middle element: ", slow_ptr.info)
            print("Last element: ", fast_ptr.info)
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    def is_palindrome(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            print("Palindrome")
            return
        self.reverse()
        original = self.head
        reversed_head = self.head
        while original is not None and reversed_head is not None:
            if original.info != reversed_head.info:
                print("Not a palindrome")
                return
            original = original.next
            reversed_head = reversed_head.next
        print("Palindrome")
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.create()
    linked_list.display()
    linked_list.is_palindrome()