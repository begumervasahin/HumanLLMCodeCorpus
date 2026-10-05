class Node:
    def __init__(self, data, next_node):
        self._data = data
        self._next = next_node
    def get_data(self):
        return self._data
    def get_next(self):
        return self._next
    def set_next(self, next_node):
        self._next = next_node
    def to_string(self):
        return "{}".format(self._data)
class MyLinkedList:
    def __init__(self):
        self._head_node = None
        self._last_node = None
        self._size = 0
    def size(self):
        return self._size
    def add(self, data):
        new_node = Node(data, None)
        if self._head_node is None:
            self._head_node = new_node
            self._last_node = new_node
        else:
            self._last_node.set_next(new_node)
            self._last_node = new_node
        self._size += 1
    def get(self, index):
        if index >= self._size or index < 0:
            raise IndexError('Index out of bounds')
        data_node = self._head_node
        for i in range(index):
            data_node = data_node.get_next()
        return data_node.get_data()
list1 = MyLinkedList()
list1.add(1)
list1.add(5)
list1.add(-7)
for i in range(list1.size()):
    print(list1.get(i))