class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node
    def __str__(self):
        return f'Node [{self.value}]'
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    def insert(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        elif self.last == self.first:
            self.last = Node(value)
            self.first.next = self.last
        else:
            current = Node(value)
            self.last.next = current
            self.last = current
    def __str__(self):
        if self.first:
            current = self.first
            out = f'LinkedList [\n{current.value}\n'
            while current.next:
                current = current.next
                out += f'{current.value}\n'
            return out + ']'
        return 'LinkedList []'
    def clear(self):
        self.__init__()