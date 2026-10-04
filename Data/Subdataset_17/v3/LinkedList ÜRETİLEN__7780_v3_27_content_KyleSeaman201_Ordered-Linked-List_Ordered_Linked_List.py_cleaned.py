class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
    __repr__ = __str__
class OrderedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        elif value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        elif value > self.tail.value:
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next
            if current.next is None:
                self.tail = current
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    def pop(self):
        if not self.head:
            return None
        if self.head == self.tail:
            value = self.head.value
            self.head = self.tail = None
            return value
        current = self.head
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        return value
    def is_empty(self):
        return self.head is None
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')
if __name__ == "__main__":
    oll = OrderedLinkedList()
    oll.add(3)
    oll.add(1)
    oll.add(4)
    oll.add(2)
    print("List after adding elements:")
    oll.print_list()
    print("Size of list:", oll.size())
    oll.delete(3)
    print("List after deleting 3:")
    oll.print_list()
    print("Searching for 4:", oll.search(4))
    print("Searching for 3:", oll.search(3))
    print("Popping the last element:", oll.pop())
    print("List after popping the last element:")
    oll.print_list()
    print("Is the list empty?", oll.is_empty())
    print("Size of list:", oll.size())