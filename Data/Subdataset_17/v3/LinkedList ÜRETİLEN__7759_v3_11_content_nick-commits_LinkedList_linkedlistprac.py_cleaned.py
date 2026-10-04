class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def length(self):
        current = self.head
        total_nodes = 0
        while current.next:
            total_nodes += 1
            current = current.next
        return total_nodes
    def display(self):
        elements = []
        current = self.head
        while current.next:
            current = current.next
            elements.append(current.data)
        print(elements)
    def get(self, index):
        if index >= self.length():
            print('Index out of bounds')
            return None
        current = self.head.next
        current_idx = 0
        while current:
            if current_idx == index:
                return current.data
            current = current.next
            current_idx += 1
    def erase(self, index):
        if index >= self.length():
            print('Index out of bounds')
            return
        current = self.head
        current_idx = 0
        while current.next:
            last_node = current
            current = current.next
            if current_idx == index:
                last_node.next = current.next
                return
            current_idx += 1
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(2)
    my_list.append(1)
    my_list.erase(1)
    my_list.display()