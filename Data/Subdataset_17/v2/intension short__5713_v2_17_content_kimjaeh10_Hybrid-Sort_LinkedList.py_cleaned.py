class Node:
    __slots__ = 'value', 'next_node'
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value
    def __repr__(self):
        return str(self.value)
def _insertion_wrapper(insertion_sort_func):
    def insertion_counter(self, *args, **kwargs):
        if self.size > 1:
            LinkedList._c += 1
        insertion_sort_func(self)
    return insertion_counter
class LinkedList:
    _c = 0
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0
        if data:
            for value in data:
                self.push_back(value)
    def __len__(self):
        return self.size
    def __eq__(self, other):
        if self.size != other.size:
            return False
        current_self = self.head
        current_other = other.head
        while current_self and current_other:
            if current_self != current_other:
                return False
            current_self = current_self.next_node
            current_other = current_other.next_node
        return current_self is None and current_other is None
    def __repr__(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next_node
        return str(values)
    def is_empty(self):
        return self.size == 0
    def front_value(self):
        return self.head.value if self.head else None
    def push_front(self, value):
        new_node = Node(value, self.head)
        if self.is_empty():
            self.tail = new_node
        self.head = new_node
        self.size += 1
    def push_back(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node
        self.size += 1
    def pop_front(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return value
    @_insertion_wrapper
    def insertion_sort(self):
        if self.is_empty() or self.head.next_node is None:
            return
        sorted_list = LinkedList()
        sorted_list.push_back(self.pop_front())
        while self.head:
            current_value = self.pop_front()
            if current_value >= sorted_list.tail.value:
                sorted_list.push_back(current_value)
            elif current_value <= sorted_list.head.value:
                sorted_list.push_front(current_value)
            else:
                current = sorted_list.head
                while current.next_node:
                    if current_value <= current.next_node.value:
                        new_node = Node(current_value, current.next_node)
                        current.next_node = new_node
                        sorted_list.size += 1
                        break
                    current = current.next_node
        self.head = sorted_list.head
        self.tail = sorted_list.tail
        self.size = sorted_list.size
if __name__ == "__main__":
    linked_list = LinkedList([6, 2, 3, 1, 4, 5])
    print("Before sorting:", linked_list)
    linked_list.insertion_sort()
    print("After sorting:", linked_list)