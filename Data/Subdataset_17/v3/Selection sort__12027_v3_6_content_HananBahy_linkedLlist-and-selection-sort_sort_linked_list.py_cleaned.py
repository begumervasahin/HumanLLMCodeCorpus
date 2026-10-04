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
def main():
    my_list = LinkedList()
    elements = [100, 500, 70, 1, -1, 8, 40, 70, 5, -1]
    for element in elements:
        my_list.add(element)
    print("Original list:")
    my_list.print_list()
    my_list.selection_sort()
    print("Sorted list:")
    my_list.print_list()
if __name__ == "__main__":
    main()