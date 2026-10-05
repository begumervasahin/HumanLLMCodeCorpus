class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def insert_after_key(self, data, key):
        new_node = Node(data)
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                break
            current_node = current_node.next
        if current_node is None:
            print("Key not found")
        else:
            new_node.next = current_node.next
            current_node.next = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
singly_linked_list = SinglyLinkedList()
while True:
    print("1. Insert at beginning")
    print("2. Insert after key")
    print("3. Insert at end")
    print("4. Display list")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter the element to insert: ")
        singly_linked_list.insert_at_beginning(data)
    elif choice == 2:
        data = input("Enter the element to insert: ")
        key = input("Enter the key after which to insert: ")
        singly_linked_list.insert_after_key(data, key)
    elif choice == 3:
        data = input("Enter the element to insert: ")
        singly_linked_list.insert_at_end(data)
    elif choice == 4:
        singly_linked_list.display()
    else:
        print("Invalid input")