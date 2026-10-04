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
            index = 0
            while current is not None and index < pos - 1:
                index += 1
                current = current.next
            if current is None:
                print("Invalid position")
            else:
                new_node.next = current.next
                new_node.prev = current
                if current.next is not None:
                    current.next.prev = new_node
                current.next = new_node
                if new_node.next is None:
                    self.tail = new_node
    def display(self):
        current = self.head
        print("Doubly Linked List:", end=" ")
        if current is None:
            print("Empty!")
        while current is not None:
            print("<=>", current.data, end=" ")
            current = current.next
        print()
    def display_reverse(self):
        current = self.tail
        if current is None:
            print("List is empty")
        else:
            while current is not None:
                print("<=>", current.data, end=" ")
                current = current.prev
            print()
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
    def delete_from_position(self, pos):
        if self.head is None:
            print("List is empty")
        elif pos == 0:
            self.delete_from_beginning()
        else:
            current = self.head
            index = 0
            while current is not None and index < pos - 1:
                index += 1
                current = current.next
            if current is None or current.next is None:
                print("Invalid position")
            else:
                to_delete = current.next
                current.next = to_delete.next
                if to_delete.next is not None:
                    to_delete.next.prev = current
                if to_delete == self.tail:
                    self.tail = current
def main():
    dll = DoublyLinkedList()
    ch = 'y'
    while ch == 'y':
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
            dll.insert(data)
        elif option == 2:
            data = int(input("Enter data: "))
            dll.insert_at_beginning(data)
        elif option == 3:
            data = int(input("Enter data: "))
            dll.insert(data)
        elif option == 4:
            pos = int(input("Enter position (0 ......n): "))
            data = int(input("Enter data: "))
            dll.insert_at_position(pos, data)
        elif option == 5:
            dll.display()
        elif option == 6:
            print("List in reverse order is:", end=" ")
            dll.display_reverse()
        elif option == 7:
            dll.delete_from_beginning()
        elif option == 8:
            dll.delete_from_end()
        elif option == 9:
            pos = int(input("Enter position (0 ......n): "))
            dll.delete_from_position(pos)
        else:
            break
        ch = input("Enter y to continue program: ")
if __name__ == "__main__":
    main()