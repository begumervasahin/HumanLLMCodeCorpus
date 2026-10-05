class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
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
        else:
            self.last.next = new_node
            self.last = new_node
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
        self.first = None
        self.last = None
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    print(linked_list)
    linked_list.clear()
    print(linked_list)