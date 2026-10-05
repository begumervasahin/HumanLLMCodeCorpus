from caching.doublylinkedlist.DoublyLinkedList import DoublyLinkedList
from caching.node.HashNode import HashNode
class Caching:
    def __init__(self, capacity):
        self.cache_map = {}
        self.capacity = capacity
        self.size = 0
        self.doubly_linked_list = DoublyLinkedList()
    def get(self, key):
        if key in self.cache_map:
            self.doubly_linked_list.access_a_node(self.cache_map[key])
        else:
            print(-1)
    def set(self, key, value):
        if self.size < self.capacity:
            self.cache_map[key] = self.doubly_linked_list.enter_value(key, value)
            self.size += 1
        else:
            node = self.doubly_linked_list.get_head_node()
            del self.cache_map[node.key]
            self.cache_map[key] = self.doubly_linked_list.replace_a_node(key, value)
    def hash_of_set(self, key):
        index = key % self.capacity
        return index
    def get_total_entries(self):
        return self.size
    def print_all_entries(self):
        self.doubly_linked_list.print_doubly_linked_list()
if __name__ == "__main__":
    caching = Caching(5)
    for i in range(1, 6):
        caching.set(i, i)
    caching.get(1)
    caching.set(6, 6)
    caching.set(7, 7)
    caching.get(11)
    caching.print_all_entries()