class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def insert_at_end_no_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()
    def create(self):
        num_nodes = int(input("Enter the number of nodes: "))
        for _ in range(num_nodes):
            data = int(input("Enter data to be inserted: "))
            self.insert_at_end_no_tail(data)
    def tail_element(self):
        if self.tail:
            print("Tail element:", self.tail.value)
    def middle_and_last_element(self):
        if not self.head:
            return
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        print("Middle element:", slow_ptr.value)
        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        print("Last element:", last_ptr.value)
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    def is_palindrome(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            print("Palindrome")
            return
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        prev = None
        current = slow_ptr
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        first_half = self.head
        second_half = prev
        while second_half:
            if first_half.value != second_half.value:
                print("Not a palindrome")
                return
            first_half = first_half.next
            second_half = second_half.next
        print("Palindrome")
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.create()
    linked_list.display()
    linked_list.is_palindrome()