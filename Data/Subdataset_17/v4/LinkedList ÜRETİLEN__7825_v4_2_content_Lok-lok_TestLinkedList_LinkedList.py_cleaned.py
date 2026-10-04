
class Node:
    def __init__(self, data):
        if isinstance(data, int):
            self.data = data
            self.previous = None
            self.next = None
        elif data is None:
            self.data = None
            self.previous = None
            self.next = None
        else:
            raise TypeError("Input must be an int")
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.first = Node(None)
        self.last = Node(None)
        self.first.next = self.last
        self.last.previous = self.first
        self._size = 0
    def __str__(self):
        result = "("
        current = self.first.next
        while current != self.last:
            result += str(current.data) + " "
            current = current.next
        result = result.strip() + ")"
        return result
    def add_to_front(self, data):
        if isinstance(data, int):
            new_node = Node(data)
            new_node.next = self.first.next
            new_node.previous = self.first
            self.first.next.previous = new_node
            self.first.next = new_node
            self._size += 1
        else:
            raise TypeError("Input must be an int")
    def add_to_back(self, data):
        if isinstance(data, int):
            new_node = Node(data)
            new_node.previous = self.last.previous
            new_node.next = self.last
            self.last.previous.next = new_node
            self.last.previous = new_node
            self._size += 1
        else:
            raise TypeError("Input must be an int")
    def remove_front(self):
        if self.is_empty():
            raise IndexError("Remove from empty list")
        front_node = self.first.next
        self.first.next = front_node.next
        front_node.next.previous = self.first
        self._size -= 1
        return front_node.data
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Remove from empty list")
        last_node = self.last.previous
        self.last.previous = last_node.previous
        last_node.previous.next = self.last
        self._size -= 1
        return last_node.data
    def size(self):
        return self._size
    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty list")
        return self.first.next.data
    def get(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an int")
        if pos < 0 or pos >= self._size:
            raise IndexError("Position out of range")
        current = self.first.next
        for _ in range(pos):
            current = current.next
        return current.data
    def insert(self, data, pos):
        if not isinstance(data, int):
            raise TypeError("Input must be an int")
        if not isinstance(pos, int):
            raise TypeError("Position must be an int")
        if pos < 0 or pos > self._size:
            raise IndexError("Position out of range")
        current = self.first
        for _ in range(pos):
            current = current.next
        new_node = Node(data)
        new_node.previous = current
        new_node.next = current.next
        current.next.previous = new_node
        current.next = new_node
        self._size += 1
    def remove(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an int")
        if pos < 0 or pos >= self._size:
            raise IndexError("Position out of range")
        current = self.first.next
        for _ in range(pos):
            current = current.next
        current.previous.next = current.next
        current.next.previous = current.previous
        self._size -= 1
        return current.data
    def contains(self, data):
        if not isinstance(data, int):
            raise TypeError("Input must be an int")
        count = 0
        current = self.first.next
        while current != self.last:
            if current.data == data:
                count += 1
            current = current.next
        return count
    def is_empty(self):
        return self._size == 0
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
    print(linked_list.size())
    print(linked_list.contains(10))
    print(linked_list.remove_front())
    print(linked_list.remove_front())
    print(linked_list.remove_last())
    print(linked_list.size())