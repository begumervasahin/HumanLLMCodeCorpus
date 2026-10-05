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
            result = f'LinkedList [\n{current.value}\n'
            while current.next:
                current = current.next
                result += f'{current.value}\n'
            return result + ']'
        return 'LinkedList []'
    def clear(self):
        self.head = None
        self.tail = None
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    print(linked_list)
    linked_list.clear()
    print(linked_list)