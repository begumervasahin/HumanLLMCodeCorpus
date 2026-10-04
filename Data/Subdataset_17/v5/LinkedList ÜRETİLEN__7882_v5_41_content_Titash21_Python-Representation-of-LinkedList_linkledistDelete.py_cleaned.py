class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete_value(self, data):
        if self.head is None:
            print("You are trying to delete from an empty list.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next
        if current is None:
            print("The data you want to delete is not in the list.")
            return
        prev.next = current.next
    def print_list(self):
        if self.head is None:
            print("Empty linked list.")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next
def display_menu():
    print("\nOPTIONS FOR THIS PROGRAM")
    print("1. Insert at front")
    print("2. Delete a particular node")
    print("3. Print contents of the linked list")
    print("4. Exit")
def main():
    linked_list = LinkedList()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue
        if choice == 1:
            try:
                value = int(input("Enter data to add in front: "))
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                continue
            linked_list.insert_at_front(value)
        elif choice == 2:
            try:
                value = int(input("Enter data to delete: "))
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                continue
            linked_list.delete_value(value)
        elif choice == 3:
            linked_list.print_list()
        elif choice == 4:
            break
        else:
            print("Wrong input! Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()