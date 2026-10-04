from caching.doublylinkedlist.DoublyLinkedList import DoublyLinkedList
from caching.node.HashNode import HashNode
class Cache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.total_entries = 0
        self.doubly_linked_list = DoublyLinkedList()
    def get(self, key):
        if key in self.cache:
            self.doubly_linked_list.access_node(self.cache[key])
            return self.cache[key].value
        else:
            print(-1)
            return -1
    def set(self, key, value):
        if self.total_entries < self.capacity:
            self.cache[key] = self.doubly_linked_list.add_node(key, value)
            self.total_entries += 1
        else:
            lru_node = self.doubly_linked_list.get_head_node()
            del self.cache[lru_node.key]
            self.cache[key] = self.doubly_linked_list.replace_node(lru_node, key, value)
    def hash_of_key(self, key):
        return key % self.capacity
    def get_total_entries(self):
        return self.total_entries
    def print_all_entries(self):
        self.doubly_linked_list.print_list()
if __name__ == "__main__":
    cache = Cache(5)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    cache.set(5, 5)
    cache.get(1)
    cache.set(6, 6)
    cache.set(7, 7)
    cache.get(11)
    cache.print_all_entries()