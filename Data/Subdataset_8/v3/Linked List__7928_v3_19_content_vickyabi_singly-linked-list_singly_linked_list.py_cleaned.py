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
    def insert_at_position(self, data, key):
        new_node = Node(data)
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node:
            if current_node.data == key:
                break
            current_node = current_node.next
        if current_node is None:
            print("Key not found")
            return
        new_node.next = current_node.next
        current_node.next = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
def handle_user_input(linked_list):
    while True:
        print("\nMenu:")
        print("1. Insert at beginning")
        print("2. Insert at position")
        print("3. Insert at end")
        print("4. Display list")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            data = input("Enter the element to insert at the beginning: ")
            linked_list.insert_at_beginning(data)
        elif choice == '2':
            data = input("Enter the element to insert: ")
            key = input("Enter the element after insertion: ")
            linked_list.insert_at_position(data, key)
        elif choice == '3':
            data = input("Enter the element to insert at the end: ")
            linked_list.insert_at_end(data)
        elif choice == '4':
            print("\nLinked List:")
            linked_list.print_list()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")
if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    handle_user_input(singly_linked_list)