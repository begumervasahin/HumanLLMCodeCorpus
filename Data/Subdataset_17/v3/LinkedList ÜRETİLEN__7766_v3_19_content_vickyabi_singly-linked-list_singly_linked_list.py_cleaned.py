class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_position(self, data, key):
        if self.head is None:
            print("The list is empty.")
            return
        current_node = self.head
        while current_node is not None and current_node.data != key:
            current_node = current_node.next
        if current_node is None:
            print(f"Node with data {key} not found.")
        else:
            new_node = Node(data)
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
    def print_list(self):
        if self.head is None:
            print("The list is empty.")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print("None")
def main():
    singly_linked_list = SinglyLinkedList()
    menu =
    while True:
        print(menu)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            data = input("Enter the element to insert: ")
            singly_linked_list.insert_at_beginning(data)
        elif choice == 2:
            data = input("Enter the element to insert: ")
            key = input("Enter the element after which to insert: ")
            singly_linked_list.insert_at_position(data, key)
        elif choice == 3:
            data = input("Enter the element to insert: ")
            singly_linked_list.insert_at_end(data)
        elif choice == 4:
            singly_linked_list.print_list()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()