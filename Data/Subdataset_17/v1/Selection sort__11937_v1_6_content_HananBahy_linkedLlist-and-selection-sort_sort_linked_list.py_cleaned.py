class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedListUno:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print_linked2(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def selectionsort(self):
        current = self.head
        while current:
            smallest = current
            next_node = current.next
            while next_node:
                if next_node.data < smallest.data:
                    smallest = next_node
                next_node = next_node.next
            current.data, smallest.data = smallest.data, current.data
            current = current.next
if __name__ == "__main__":
    mylist = LinkedListUno()
    mylist.add(100)
    mylist.add(500)
    mylist.add(70)
    mylist.add(1)
    mylist.add(-1)
    mylist.add(8)
    mylist.add(40)
    mylist.add(70)
    mylist.add(5)
    mylist.add(-1)
    print("Original list:")
    mylist.print_linked2()
    mylist.selectionsort()
    print("After sorting:")
    mylist.print_linked2()