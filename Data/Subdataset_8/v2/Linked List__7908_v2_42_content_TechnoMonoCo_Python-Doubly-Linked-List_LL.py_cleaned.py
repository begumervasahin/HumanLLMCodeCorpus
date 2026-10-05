class LinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
class LinkedList:
    def __init__(self, data=None):
        self.head = LinkedListNode(data) if data is not None else None
    def remove(self, data):
        if self.head is None:
            return -1
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return 0
            prev = current
            current = current.next
        return -1
    def insert(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        elif data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
    def contains(self):
        if self.head is None:
            print("Empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=", ")
                current = current.next
            print()
def test():
    linked_list = LinkedList()
    print("contains...")
    linked_list.contains()
    print()
    print("inserting 1...")
    linked_list.insert(1)
    print("contains:")
    linked_list.contains()
    print()
    print("inserting 5...")
    linked_list.insert(5)
    print("contains:")
    linked_list.contains()
    print()
    print("removing 1...")
    linked_list.remove(1)
    print("contains:")
    linked_list.contains()
    print()
    print("removing 5...")
    linked_list.remove(5)
    print("contains...")
    linked_list.contains()
    print()
    print("removing 0...")
    linked_list.remove(0)
    print("contains:")
    linked_list.contains()
    print()
if __name__ == "__main__":
    test()