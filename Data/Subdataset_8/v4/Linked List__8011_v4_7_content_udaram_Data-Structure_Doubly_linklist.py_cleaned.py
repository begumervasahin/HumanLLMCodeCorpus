class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_at_position(self, pos, data):
        new_node = Node(data)
        if pos == 0:
            self.insert_at_beginning(data)
        else:
            current = self.head
            i = 0
            while current is not None and i != pos - 1:
                i += 1
                current = current.next
            if current is None and pos > i:
                print("INVALID POSITION")
            else:
                new_node.prev = current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
    def display(self):
        current = self.head
        print("\nDoubly Linked List:")
        if current is None:
            print("Empty!!!")
        while current is not None:
            print("<=>", current.data, end=" ")
            current = current.next
    def reverse_display(self):
        current = self.tail
        print("\nDoubly Linked List in Reverse:")
        if current is None:
            print("Empty!!!")
        while current is not None:
            print("<=>", current.data, end=" ")
            current = current.prev
    def delete_from_beginning(self):
        if self.head is None:
            print("List is Empty")
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
    def delete_from_end(self):
        if self.head is None:
            print("List is Empty")
        else:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
    def delete_from_position(self, pos):
        if self.head is None:
            print("List is Empty")
        elif pos == 0:
            self.delete_from_beginning()
        else:
            current = self.head
            i = 0
            while current is not None and pos != i:
                i += 1
                current = current.next
            if current is None and pos >= i:
                print("Invalid Position")
            elif current.next.next is None and i == pos - 1:
                current.next = None
                self.tail = current
            else:
                current.next.next.prev = current
                current.next = current.next.next
def main():
    linked_list = DoublyLinkedList()
    choice = 'y'
    while choice == 'y':
        print('''1. Insertion
2. Insert at beginning
3. Insert at end
4. Insert at position
5. Display list
6. Display in reverse order
7. Delete from beginning
8. Delete from end
9. Delete from position
10. EXIT''')
        option = int(input("Enter option: "))
        if option == 1:
            data = int(input("Enter data: "))
            linked_list.insert(data)
        elif option == 2:
            data = int(input("Enter data: "))
            linked_list.insert_at_beginning(data)
        elif option == 3:
            data = int(input("Enter data: "))
            linked_list.insert(data)
        elif option == 4:
            pos = int(input("Enter position (0 ......n): "))
            data = int(input("Enter data: "))
            linked_list.insert_at_position(pos, data)
        elif option == 5:
            linked_list.display()
        elif option == 6:
            linked_list.reverse_display()
        elif option == 7:
            linked_list.delete_from_beginning()
        elif option == 8:
            linked_list.delete_from_end()
        elif option == 9:
            pos = int(input("Enter position (0 ......n): "))
            linked_list.delete_from_position(pos)
        else:
            break
        choice = input("\nEnter 'y' to continue: ")
if __name__ == "__main__":
    main()