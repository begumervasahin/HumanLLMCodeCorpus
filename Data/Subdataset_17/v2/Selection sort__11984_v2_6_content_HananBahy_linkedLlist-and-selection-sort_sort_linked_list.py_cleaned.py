class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def selection_sort(self):
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
    my_list = LinkedList()
    my_list.add(100)
    my_list.add(500)
    my_list.add(70)
    my_list.add(1)
    my_list.add(-1)
    my_list.add(8)
    my_list.add(40)
    my_list.add(70)
    my_list.add(5)
    my_list.add(-1)
    print("Original list:")
    my_list.print_list()
    my_list.selection_sort()
    print("Sorted list:")
    my_list.print_list()