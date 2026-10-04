class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def remove(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                if current == self.tail:
                    self.tail = previous
                return
            previous = current
            current = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.display()
    print("Size:", linked_list.size())
    print("Search 2:", linked_list.search(2))
    print("Search 5:", linked_list.search(5))
    linked_list.remove(2)
    linked_list.display()
