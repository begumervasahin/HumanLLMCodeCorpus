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
    def insert_at_end_notail(self, data):
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
                print(current.info, end=" ")
                current = current.next
            print()
    def create(self):
        num_nodes = int(input("Enter the number of nodes: "))
        for _ in range(num_nodes):
            data = int(input("Enter data to be inserted: "))
            self.insert_at_end_notail(data)
    def get_tail(self):
        if self.head is not None:
            print("Tail element:", self.tail.info)
    def get_middle_and_last_element(self):
        if self.head is not None:
            slow_ptr = self.head
            fast_ptr = self.head
            while fast_ptr.next:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
                if fast_ptr.next is not None:
                    fast_ptr = fast_ptr.next
            print("Middle element:", slow_ptr.info)
            print("Last element:", fast_ptr.info)
    def reverse(self):
        if self.head and self.head.next:
            prev = None
            current = self.head
            while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            self.head = prev
    def is_palindrome(self):
        if self.head and self.head.next:
            p = self.head
            self.reverse()
            q = self.head
            while p and q:
                if p.info != q.info:
                    print("Not a palindrome")
                    return
                p = p.next
                q = q.next
            print("Palindrome")
        elif self.head is None:
            print("List is empty")
        else:
            print("Palindrome")
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.create()
    print("Linked List:")
    linked_list.display()
    linked_list.is_palindrome()