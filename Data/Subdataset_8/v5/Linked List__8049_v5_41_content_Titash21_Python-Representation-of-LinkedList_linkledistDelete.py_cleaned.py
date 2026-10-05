class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def delete_value(self, data):
        if self.head is None:
            print("Cannot delete from an empty list")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            while current is not None and current.data != data:
                prev = current
                current = current.next
            if current is None:
                print("Data not found in the list")
            else:
                prev.next = current.next
    def print_list(self):
        if self.head is None:
            print("Empty linked list")
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next
def main():
    print("OPTIONS FOR THIS PROGRAM")
    print("1. Insert at the front")
    print("2. Delete a node")
    print("3. Print contents of the linked list")
    choice = int(input("Enter your choice: "))
    if choice not in [1, 2, 3]:
        print("Invalid choice! Exiting...")
        return
    linked_list = LinkedList()
    if choice == 1:
        value = int(input("Enter data to insert at the front: "))
        linked_list.insert_at_front(value)
    elif choice == 2:
        value = int(input("Enter data to delete: "))
        linked_list.delete_value(value)
    linked_list.print_list()
    repeat = input("Do you want to continue (yes/no)? ").lower()
    if repeat == 'yes':
        main()
    else:
        linked_list.print_list()
if __name__ == "__main__":
    main()