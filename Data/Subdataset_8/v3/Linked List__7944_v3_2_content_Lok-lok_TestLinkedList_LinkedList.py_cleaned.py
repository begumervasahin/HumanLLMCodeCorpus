class Node:
    def __init__(self, data):
        if isinstance(data, int) or data is None:
            self.data = data
            self.previous = None
            self.next = None
        else:
            raise TypeError("Data must be an integer or None.")
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
        if isinstance(data, int):
            new_node = Node(data)
            successor = self.head.next
            new_node.previous = self.head
            new_node.next = successor
            self.head.next = new_node
            successor.previous = new_node
            self.size += 1
        else:
            raise TypeError("Data must be an integer.")
    def add_to_back(self, data):
        if isinstance(data, int):
            new_node = Node(data)
            predecessor = self.tail.previous
            predecessor.next = new_node
            new_node.previous = predecessor
            new_node.next = self.tail
            self.tail.previous = new_node
            self.size += 1
        else:
            raise TypeError("Data must be an integer.")
    def remove_front(self):
        if self.size == 0:
            raise IndexError("Cannot remove from an empty list.")
        node_to_remove = self.head.next
        successor = node_to_remove.next
        self.head.next = successor
        successor.previous = self.head
        self.size -= 1
        return node_to_remove.data
    def remove_back(self):
        if self.size == 0:
            raise IndexError("Cannot remove from an empty list.")
        node_to_remove = self.tail.previous
        predecessor = node_to_remove.previous
        predecessor.next = self.tail
        self.tail.previous = predecessor
        self.size -= 1
        return node_to_remove.data
    def get_size(self):
        return self.size
    def front(self):
        if self.size == 0:
            raise IndexError("List is empty.")
        return self.head.next.data
    def get(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer.")
        if not 0 <= pos < self.size:
            raise IndexError("Position out of range.")
        current = self.head.next
        for _ in range(pos):
            current = current.next
        return current.data
    def insert(self, data, pos):
        if not isinstance(data, int):
            raise TypeError("Data must be an integer.")
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer.")
        if not 0 <= pos <= self.size:
            raise IndexError("Position out of range.")
        current = self.head
        for _ in range(pos):
            current = current.next
        new_node = Node(data)
        successor = current.next
        current.next = new_node
        new_node.previous = current
        new_node.next = successor
        successor.previous = new_node
        self.size += 1
    def remove(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer.")
        if not 0 <= pos < self.size:
            raise IndexError("Position out of range.")
        current = self.head
        for _ in range(pos):
            current = current.next
        node_to_remove = current.next
        successor = node_to_remove.next
        current.next = successor
        successor.previous = current
        self.size -= 1
        return node_to_remove.data
    def contains(self, data):
        current = self.head.next
        while current != self.tail:
            if current.data == data:
                return True
            current = current.next
        return False
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_to_back(5)
    linked_list.add_to_front(10)
    linked_list.add_to_back(12)
    linked_list.insert(7, 1)
    linked_list.insert(6, 1)
    print("Data at position 2:", linked_list.get(2))
    print("Removed data at position 2:", linked_list.remove(2))
    print("Linked list:", linked_list)
    print("Size of linked list:", linked_list.get_size())
    print("Does linked list contain 10?", linked_list.contains(10))
    print("Removed front node data:", linked_list.remove_front())
    print("Removed front node data:", linked_list.remove_front())
    print("Removed back node data:", linked_list.remove_back())
    print("Size of linked list:", linked_list.get_size())