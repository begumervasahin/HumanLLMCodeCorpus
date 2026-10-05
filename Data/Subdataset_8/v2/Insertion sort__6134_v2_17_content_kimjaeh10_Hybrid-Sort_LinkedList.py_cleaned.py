
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value
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
            [self.push_back(i) for i in data]
    def __len__(self):
        return self.size
    def __eq__(self, other):
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self != temp_other:
                return False
            temp_self = temp_self.next_node
            temp_other = temp_other.next_node
        return True
    def __repr__(self):
        values = []
        temp_node = self.head
        while temp_node:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)
    def length(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def front_value(self):
        return self.head.value if self.head else None
    def push_front(self, val):
        new_node = Node(val, self.head)
        if self.is_empty():
            self.tail = new_node
        self.head = new_node
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
        val = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return val
    @_insertion_wrapper
    def insertion_sort(self):
        if self.head is None:
            return
        pointer = self.head.next_node
        sorted_list = LinkedList()
        sorted_list.push_back(self.pop_front())
        h = self.pop_front()
        while pointer is not None:
            if h >= sorted_list.tail.value:
                sorted_list.push_back(h)
            elif h <= sorted_list.head.value:
                sorted_list.push_front(h)
            else:
                new_head = sorted_list.head
                while new_head.next_node is not None:
                    if h <= new_head.next_node.value and h > new_head.value:
                        temp = Node(h, new_head.next_node)
                        new_head.next_node = temp
                        sorted_list.size += 1
                        new_head = new_head.next_node
                    else:
                        new_head = new_head.next_node
            h = self.pop_front()
            pointer = pointer.next_node
        self.head = sorted_list.head
        self.tail = sorted_list.tail
        self.size = sorted_list.size
list5 = LinkedList()
list5.push_back(6)
list5.push_back(2)
list5.push_back(3)
list5.push_back(1)
list5.push_back(4)
list5.push_back(5)
print(list5)
list5.insertion_sort()
print(list5)