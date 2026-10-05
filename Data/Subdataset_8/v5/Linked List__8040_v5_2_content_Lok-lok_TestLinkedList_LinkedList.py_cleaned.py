class Node:
    def __init__(self, data):
        if isinstance(data, int) or data is None:
            self.data = data
            self.previous = None
            self.next = None
        else:
            raise TypeError("Data must be an integer or None")
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.size = 0
    def __str__(self):
        result = "("
        current = self.head.next
        while current != self.tail:
            result += str(current.data) + " "
            current = current.next
        result += ")"
        return result
    def add_to_front(self, data):
        if not isinstance(data, int):
            raise TypeError("Data must be an integer")
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.previous = self.head
        self.head.next.previous = new_node
        self.head.next = new_node
        self.size += 1
    def add_to_back(self, data):
        if not isinstance(data, int):
            raise TypeError("Data must be an integer")
        new_node = Node(data)
        new_node.next = self.tail
        new_node.previous = self.tail.previous
        self.tail.previous.next = new_node
        self.tail.previous = new_node
        self.size += 1
    def remove_front(self):
        if self.size == 0:
            raise Exception("Cannot remove from an empty list")
        node = self.head.next
        self.head.next = node.next
        node.next.previous = self.head
        self.size -= 1
        return node.data
    def remove_last(self):
        if self.size == 0:
            raise Exception("Cannot remove from an empty list")
        node = self.tail.previous
        self.tail.previous = node.previous
        node.previous.next = self.tail
        self.size -= 1
        return node.data
    def get_size(self):
        return self.size
    def get_front(self):
        if self.size == 0:
            raise Exception("List is empty")
        return self.head.next.data
    def get(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer")
        if not 0 <= pos < self.size:
            raise IndexError("Position out of range")
        current = self.head.next
        for _ in range(pos):
            current = current.next
        return current.data
    def insert(self, data, pos):
        if not isinstance(data, int) or not isinstance(pos, int):
            raise TypeError("Data and position must be integers")
        if not 0 <= pos <= self.size:
            raise IndexError("Position out of range")
        current = self.head
        for _ in range(pos):
            current = current.next
        new_node = Node(data)
        new_node.next = current.next
        new_node.previous = current
        current.next.previous = new_node
        current.next = new_node
        self.size += 1
    def remove(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer")
        if not 0 <= pos < self.size:
            raise IndexError("Position out of range")
        current = self.head
        for _ in range(pos):
            current = current.next
        node_to_remove = current.next
        current.next = node_to_remove.next
        node_to_remove.next.previous = current
        self.size -= 1
        return node_to_remove.data
    def contains(self, data):
        count = 0
        current = self.head.next
        while current != self.tail:
            if current.data == data:
                count += 1
            current = current.next
        return count
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_to_back(5)
    linked_list.add_to_front(10)
    linked_list.add_to_back(12)
    linked_list.insert(7, 1)
    linked_list.insert(6, 1)
    print(linked_list.get(2))
    print(linked_list.remove(2))
    print(linked_list)
    print(linked_list.get_size())
    print(linked_list.contains(10))
    print(linked_list.remove_front())
    print(linked_list.remove_front())
    print(linked_list.remove_last())
    print(linked_list.get_size())