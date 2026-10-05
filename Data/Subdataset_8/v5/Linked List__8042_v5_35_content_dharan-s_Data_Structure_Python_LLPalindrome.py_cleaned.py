class Node:
    def __init__(self, value):
        self.info = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        temp = Node(data)
        if not self.head:
            self.head = temp
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = temp
    def display(self):
        if not self.head:
            print("List is empty")
        else:
            p = self.head
            while p:
                print(p.info, end=' ')
                p = p.next
            print()
    def create(self):
        num_nodes = int(input("Enter the number of nodes: "))
        for _ in range(num_nodes):
            data = int(input("Enter data to be inserted: "))
            self.insert_at_end(data)
    def palindrome(self):
        if not self.head:
            print("List is Empty")
            return
        prev = None
        p = self.head
        while p:
            next_node = p.next
            p.next = prev
            prev = p
            p = next_node
        self.head = prev
        p1 = self.head
        p2 = self.head
        while p2.next:
            p1 = p1.next
            p2 = p2.next
            if p2.next:
                p2 = p2.next
        while p1:
            if p1.info != prev.info:
                print("Not a palindrome")
                return
            p1 = p1.next
            prev = prev.next
        print("Palindrome")
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.create()
    linked_list.display()
    linked_list.palindrome()