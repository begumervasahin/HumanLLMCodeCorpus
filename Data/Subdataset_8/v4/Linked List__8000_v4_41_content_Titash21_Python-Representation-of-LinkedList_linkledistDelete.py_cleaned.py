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
    def delete_value_linked_list(self, data):
        if self.head is None:
            print("You are trying to delete from an empty list")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            prev = self.head
            while temp.next is not None and temp.data != data:
                prev = temp
                temp = temp.next
            if temp.data != data and temp.next is None:
                print("The data you want to delete is not in the list")
            prev.next = temp.next
            temp = None
    def prints(self):
        if self.head is None:
            print("Empty linked list")
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next
def main():
    print("OPTIONS FOR THIS PROGRAM")
    print("1. To insert at front")
    print("2. Delete a particular node")
    print("3. Print contents of the linked list")
    choice = int(input("Enter now: "))
    if choice > 3:
        print("Wrong input! Exiting..........")
    else:
        driver_function(choice)
def driver_function(choice):
    objects = LinkedList()
    if choice == 1:
        value = int(input("Enter data to add in front: "))
        objects.insert_at_front(value)
        objects.prints()
    elif choice == 2:
        value = int(input("Enter data to delete: "))
        objects.delete_value_linked_list(value)
        objects.prints()
    elif choice == 3:
        objects.prints()
    loops = int(input("Want to enter again? Then print 1 or 0: "))
    if loops == 1:
        main()
    else:
        objects.prints()
main()