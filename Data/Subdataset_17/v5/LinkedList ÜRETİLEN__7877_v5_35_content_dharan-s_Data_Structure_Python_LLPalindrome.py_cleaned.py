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
    def find_middle_last_element(self):
        if self.head is None:
            print("List is empty")
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle_value = slow.value
        last_value = self.tail.value if self.tail else "None"
        print("Middle element:", middle_value)
        print("Last element:", last_value)
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
        if self.head is None:
            print("List is empty")
            return
        middle_node = self.find_middle()
        second_half_start = self.reverse_list(middle_node.next if middle_node else None)
        palindrome = self.compare_halves(self.head, second_half_start)
        self.reverse_list(second_half_start)
        print("Palindrome" if palindrome else "Not palindrome")
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    def reverse_list(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    def compare_halves(self, first_half, second_half):
        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True
linked_list = LinkedList()
linked_list.create()
linked_list.display()
linked_list.is_palindrome()