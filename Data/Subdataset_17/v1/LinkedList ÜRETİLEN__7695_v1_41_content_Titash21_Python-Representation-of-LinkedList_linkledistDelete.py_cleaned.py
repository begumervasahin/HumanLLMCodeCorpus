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
            print("You are trying to delete from an empty list")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        temp = self.head
        prev = None
        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next
        if temp is None:
            print("The data you want to delete is not in the list")
            return
        prev.next = temp.next
    def print_list(self):
        if self.head is None:
            print("Empty linked list")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
def main():
    linked_list = LinkedList()
    while True:
        print("\nOPTIONS FOR THIS PROGRAM")
        print("1. To insert at front")
        print("2. Delete a particular node")
        print("3. Print contents of the linked list")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = int(input("Enter data to add in front: "))
            linked_list.insert_at_front(value)
            linked_list.print_list()
        elif choice == 2:
            value = int(input("Enter data to delete: "))
            linked_list.delete_value(value)
            linked_list.print_list()
        elif choice == 3:
            linked_list.print_list()
        elif choice == 4:
            break
        else:
            print("Wrong input! Please try again.")
if __name__ == "__main__":
    main()