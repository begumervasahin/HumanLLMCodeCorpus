class DoublyLinkedList:
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def append(self, key, value):
        new_node = self.Node(key, value)
        self._add_to_tail(new_node)
        return new_node
    def move_to_end(self, node):
        self._remove_node(node)
        self._add_to_tail(node)
    def _replace_tail(self, key, value):
        new_node = self.Node(key, value)
        self._remove_from_head()
        self._add_to_tail(new_node)
        return new_node
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def _add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    def _remove_from_head(self):
        if self.head.next != self.tail:
            removed_node = self.head.next
            self._remove_node(removed_node)
            return removed_node
    def get_head_node(self):
        if self.head.next != self.tail:
            return self.head.next
    def print_list(self):
        current = self.head.next
        while current != self.tail:
            print(f"({current.key}, {current.value})")
            current = current.next
class Caching:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.dll = DoublyLinkedList()
    def get(self, key):
        if key in self.cache:
            self.dll.move_to_end(self.cache[key])
            print(self.cache[key].value)
        else:
            print(-1)
    def set(self, key, value):
        if key in self.cache:
            self.dll.move_to_end(self.cache[key])
            self.cache[key].value = value
        else:
            if self.size >= self.capacity:
                del self.cache[self.dll._remove_from_head().key]
                self.size -= 1
            self.cache[key] = self.dll.append(key, value)
            self.size += 1
    def print_cache(self):
        self.dll.print_list()
if __name__ == "__main__":
    cache = Caching(5)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    cache.set(5, 5)
    cache.get(1)
    cache.set(6, 6)
    cache.set(7, 7)
    cache.get(11)
    cache.print_cache()