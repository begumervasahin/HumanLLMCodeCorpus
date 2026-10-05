class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node
    def __str__(self):
        return f'Node [{self.value}]'
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def __str__(self):
        if self.head:
            current = self.head
            output = f'LinkedList [\n{current.value}\n'
            while current.next:
                current = current.next
                output += f'{current.value}\n'
            return output + ']'
        return 'LinkedList []'
    def clear(self):
        self.head = None
        self.tail = None