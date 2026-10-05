from caching.doublylinkedlist.DoublyLinkedList import DoublyLinkedList
from caching.node.HashNode import HashNode
class Caching:
    def __init__(self, capacity):
        self.cache_array = {}
        self.array_size = capacity
        self.total_entries = 0
        self.doubly_linked_list = DoublyLinkedList()
    def get(self, key):
        if(key in self.cache_array):
            self.doubly_linked_list.access_a_node(self.cache_array[key])
        else :
            print -1
    def set(self, key, value):
        if self.total_entries < self.array_size:
            self.cache_array[key] = self.doubly_linked_list.enter_value(key, value)
            self.total_entries += 1
        else:
            node = self.doubly_linked_list.get_head_node()
            del(self.cache_array[node.key])
            self.cache_array[key] = self.doubly_linked_list.replace_a_node(key, value)
    def hash_of_set(self, key):
        index_number = key % self.array_size
        return index_number
    def get_total_entries(self):
        return self.total_entries
    def print_all_entries(self):
        self.doubly_linked_list.print_doubly_linked_list()
if __name__ == "__main__":
    caching = Caching(5)
    caching.set(1,1)
    caching.set(2,2)
    caching.set(3,3)
    caching.set(4,4)
    caching.set(5,5)
    caching.get(1)
    caching.set(6,6)
    caching.set(7,7)
    caching.get(11)
    caching.print_all_entries()