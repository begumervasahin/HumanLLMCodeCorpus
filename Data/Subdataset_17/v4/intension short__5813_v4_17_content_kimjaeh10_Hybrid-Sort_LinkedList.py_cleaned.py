class Node:
    __slots__ = 'value', 'next_node'
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def __eq__(self, other):
        return other is not None and self.value == other.value
    def __repr__(self):
        return str(self.value)
def _insertion_wrapper(insertion_sort):
    def insertion_counter(self, *args, **kwargs):
        if self.size > 1:
            LinkedList._c += 1
        insertion_sort(self)
    return insertion_counter
class LinkedList:
    _c = 0
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0
        if data:
            for item in data:
                self.push_back(item)
    def __len__(self):
        return self.size
    def __eq__(self, other):
        if self.size != other.size:
            return False
        node_self, node_other = self.head, other.head
        while node_self and node_other:
            if node_self != node_other:
                return False
            node_self, node_other = node_self.next_node, node_other.next_node
        return node_self is None and node_other is None
    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next_node
        return str(values)
    def is_empty(self):
        return self.size == 0
    def front_value(self):
        return self.head.value if self.head else None
    def push_front(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1
    def push_back(self, val):
        new_node = Node(val)
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
        if self.is_empty():
            return
        sorted_list = LinkedList()
        sorted_list.push_back(self.pop_front())
        while self.head:
            current_value = self.pop_front()
            if current_value <= sorted_list.head.value:
                sorted_list.push_front(current_value)
            elif current_value >= sorted_list.tail.value:
                sorted_list.push_back(current_value)
            else:
                current = sorted_list.head
                while current.next_node and current.next_node.value < current_value:
                    current = current.next_node
                new_node = Node(current_value, current.next_node)
                current.next_node = new_node
                sorted_list.size += 1
        self.head, self.tail, self.size = sorted_list.head, sorted_list.tail, sorted_list.size
list5 = LinkedList([6, 2, 3, 1, 4, 5])
print(list5)
list5.insertion_sort()
print(list5)