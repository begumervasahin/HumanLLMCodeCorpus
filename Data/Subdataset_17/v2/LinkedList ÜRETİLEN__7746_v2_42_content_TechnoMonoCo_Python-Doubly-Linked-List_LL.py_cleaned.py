class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node
class LinkedList:
    def __init__(self, data=None):
        if data is not None:
            self.head = Node(data)
        else:
            self.head = None
    def remove(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                del current
                return 0
            current = current.next
        return -1
    def insert(self, data):
        new_node = Node(data)
        if self.head is None or data < self.head.data:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < data:
                current = current.next
            new_node.next = current.next
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
    def display(self):
        if self.head is None:
            print("Empty.")
        else:
            current = self.head
            elements = []
            while current is not None:
                elements.append(current.data)
                current = current.next
            print(", ".join(map(str, elements)))
def test():
    ll = LinkedList(0)
    print("Initial list:")
    ll.display()
    print("\nInserting 1...")
    ll.insert(1)
    print("List after inserting 1:")
    ll.display()
    print("\nInserting 5...")
    ll.insert(5)
    print("List after inserting 5:")
    ll.display()
    print("\nRemoving 1...")
    ll.remove(1)
    print("List after removing 1:")
    ll.display()
    print("\nRemoving 5...")
    ll.remove(5)
    print("List after removing 5:")
    ll.display()
    print("\nRemoving 0...")
    ll.remove(0)
    print("List after removing 0:")
    ll.display()
if __name__ == "__main__":
    test()