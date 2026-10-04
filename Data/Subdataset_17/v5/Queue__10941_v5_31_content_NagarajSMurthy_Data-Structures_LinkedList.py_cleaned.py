class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.data_set = set()
    def insert_node(self, data):
        self.size += 1
        self.data_set.add(data)
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def get_size(self):
        return self.size
    def calculate_size(self):
        actual_node = self.head
        size = 0
        while actual_node is not None:
            size += 1
            actual_node = actual_node.next_node
        return size
    def insert_end(self, data):
        self.size += 1
        self.data_set.add(data)
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            actual_node.next_node = new_node
    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node
    def remove_node(self, data):
        if not self.head:
            print('The list is empty.')
            return
        if data not in self.data_set:
            print('Data not in the linked list')
            return
        self.size -= 1
        self.data_set.remove(data)
        current_node = self.head
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node
        if current_node:
            if previous_node:
                previous_node.next_node = current_node.next_node
            else:
                self.head = current_node.next_node
def main():
    my_list = LinkedList()
    my_list.insert_node(10)
    my_list.insert_node(35)
    my_list.insert_node(67)
    my_list.insert_node(89)
    my_list.insert_node(341)
    print(f"Size (tracked): {my_list.get_size()}")
    print(f"Size (calculated): {my_list.calculate_size()}")
    my_list.insert_end(671)
    print(f"Size after inserting at end: {my_list.calculate_size()}")
    my_list.traverse_list()
    my_list.remove_node(20)
    print(f"Size after removing a node: {my_list.calculate_size()}")
    my_list.traverse_list()
if __name__ == "__main__":
    main()