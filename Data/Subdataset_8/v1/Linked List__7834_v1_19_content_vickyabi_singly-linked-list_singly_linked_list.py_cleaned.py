class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def insertbeg(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def insertpos(self, data, key):
        newnode = Node(data)
        if self.head is None:
            print("List is empty")
            return
        lastnode = self.head
        while lastnode:
            if lastnode.data == key:
                break
            lastnode = lastnode.next
        if lastnode is None:
            print("Key not found")
            return
        newnode.next = lastnode.next
        lastnode.next = newnode
    def insertend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = newnode
    def printlist(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.data)
            currentnode = currentnode.next
singlylinkedlist = SLL()
while True:
    print("1. Insert at beginning")
    print("2. Insert at position")
    print("3. Insert at end")
    print("4. Display list")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        data = input("Enter the element to insert: ")
        singlylinkedlist.insertbeg(data)
    elif ch == 2:
        data = input("Enter the element to insert: ")
        key = input("Enter the element after insertion: ")
        singlylinkedlist.insertpos(data, key)
    elif ch == 3:
        data = input("Enter the element to insert: ")
        singlylinkedlist.insertend(data)
    elif ch == 4:
        print("Linked List:")
        singlylinkedlist.printlist()
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid input. Please try again.")