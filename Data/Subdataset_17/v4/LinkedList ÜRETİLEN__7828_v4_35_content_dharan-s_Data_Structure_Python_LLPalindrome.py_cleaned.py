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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def insert_at_end_notail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.value, end=" ")
                current = current.next
            print()
    def create(self):
        num_nodes = int(input("Enter the number of nodes: "))
        for _ in range(num_nodes):
            data = int(input("Enter data to be inserted: "))
            self.insert_at_end_notail(data)
    def tail_element(self):
        if self.tail:
            print("Tail element:", self.tail.value)
    def middle_last_element(self):
        if self.head is not None:
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print("Middle element:", slow.value)
            print("Last element:", (self.tail.value if self.tail else "None"))
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    def palindrome(self):
        if self.head is None:
            print("List is empty")
            return
        slow = self.head
        fast = self.head
        prev_of_slow = None
        while fast and fast.next:
            fast = fast.next.next
            prev_of_slow = slow
            slow = slow.next
        second_half = None
        if fast:
            second_half = slow.next
        else:
            second_half = slow
        second_half = self.reverse_half(second_half)
        palindrome = True
        first_half = self.head
        while second_half:
            if first_half.value != second_half.value:
                palindrome = False
                break
            first_half = first_half.next
            second_half = second_half.next
        if prev_of_slow:
            prev_of_slow.next = self.reverse_half(second_half)
        if palindrome:
            print("Palindrome")
        else:
            print("Not palindrome")
    def reverse_half(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
linked_list = LinkedList()
linked_list.create()
linked_list.display()
linked_list.palindrome()