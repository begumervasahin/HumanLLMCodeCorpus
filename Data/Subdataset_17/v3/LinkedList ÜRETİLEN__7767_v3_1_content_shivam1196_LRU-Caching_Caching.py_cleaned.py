class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def enter_value(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node
    def access_node(self, node):
        if node == self.tail:
            return
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = None
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
    def get_head_node(self):
        return self.head
    def replace_node(self, key, value):
        old_head = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        new_node = Node(key, value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node
    def print_list(self):
        current = self.head
        while current:
            print(f"Key: {current.key}, Value: {current.value}")
            current = current.next
class Caching:
    def __init__(self, capacity):
        self.cache_dict = {}
        self.capacity = capacity
        self.current_size = 0
        self.dll = DoublyLinkedList()
    def get(self, key):
        if key in self.cache_dict:
            self.dll.access_node(self.cache_dict[key])
            return self.cache_dict[key].value
        else:
            return -1
    def set(self, key, value):
        if key in self.cache_dict:
            self.cache_dict[key].value = value
            self.dll.access_node(self.cache_dict[key])
        else:
            if self.current_size < self.capacity:
                new_node = self.dll.enter_value(key, value)
                self.cache_dict[key] = new_node
                self.current_size += 1
            else:
                head_node = self.dll.get_head_node()
                del self.cache_dict[head_node.key]
                new_node = self.dll.replace_node(key, value)
                self.cache_dict[key] = new_node
    def print_all_entries(self):
        self.dll.print_list()
if __name__ == "__main__":
    caching = Caching(5)
    caching.set(1, 1)
    caching.set(2, 2)
    caching.set(3, 3)
    caching.set(4, 4)
    caching.set(5, 5)
    caching.get(1)
    caching.set(6, 6)
    caching.set(7, 7)
    caching.get(11)
    caching.print_all_entries()