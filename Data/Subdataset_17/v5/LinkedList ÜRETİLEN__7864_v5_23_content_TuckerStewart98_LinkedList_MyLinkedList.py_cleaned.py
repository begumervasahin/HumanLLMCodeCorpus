class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    def __str__(self):
        return str(self.data)
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.last.next_node = new_node
        self.last = new_node
        self.size += 1
    def get(self, index):
        if index >= self.size or index < 0:
            raise IndexError('Index out of bounds')
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node
        return current_node.data
    def __len__(self):
        return self.size
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next_node
    def __str__(self):
        elements = [str(node) for node in self]
        return " -> ".join(elements)
if __name__ == "__main__":
    linked_list = MyLinkedList()
    linked_list.add(1)
    linked_list.add(5)
    linked_list.add(-7)
    print(f"Linked list elements: {linked_list}")
    print(f"Size of linked list: {len(linked_list)}")
    print(f"Element at index 1: {linked_list.get(1)}")