'''
Created on Dec 16th, 2017
@author: Lok
'''
class Node:
    def __init__(self, data):
        if isinstance(data, int) or data is None:
            self.data = data
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
        return result.rstrip() + ")"
    def add_to_front(self, data):
        if isinstance(data, int):
            new_node = Node(data)
            first_real_node = self.first.next
            self.first.next = new_node
            new_node.previous = self.first
            new_node.next = first_real_node
            first_real_node.previous = new_node
            self._size += 1
        else:
            raise TypeError("Input must be an int")
    def add_to_back(self, data):
        if isinstance(data, int):
            new_node = Node(data)
            last_real_node = self.last.previous
            last_real_node.next = new_node
            new_node.previous = last_real_node
            new_node.next = self.last
            self.last.previous = new_node
            self._size += 1
        else:
            raise TypeError("Input must be an int")
    def remove_front(self):
        if self._size == 0:
            raise IndexError("List is empty")
        first_real_node = self.first.next
        self.first.next = first_real_node.next
        first_real_node.next.previous = self.first
        self._size -= 1
        return first_real_node.data
    def remove_last(self):
        if self._size == 0:
            raise IndexError("List is empty")
        last_real_node = self.last.previous
        self.last.previous = last_real_node.previous
        last_real_node.previous.next = self.last
        self._size -= 1
        return last_real_node.data
    def size(self):
        return self._size
    def front(self):
        if self._size == 0:
            raise IndexError("List is empty")
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
        current = self.first.next
        for _ in range(pos):
            current = current.next
        new_node = Node(data)
        previous_node = current.previous
        previous_node.next = new_node
        new_node.previous = previous_node
        new_node.next = current
        current.previous = new_node
        self._size += 1
    def remove(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an int")
        if pos < 0 or pos >= self._size:
            raise IndexError("Position out of range")
        current = self.first.next
        for _ in range(pos):
            current = current.next
        previous_node = current.previous
        next_node = current.next
        previous_node.next = next_node
        next_node.previous = previous_node
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
