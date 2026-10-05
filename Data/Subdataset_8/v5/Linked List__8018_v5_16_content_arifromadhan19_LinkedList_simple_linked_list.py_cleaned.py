class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
    def insert_tail_node(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        return self.head
    def insert_head_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_specific_position(self, data, position):
        if position == 0:
            self.insert_head_node(data)
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    break
                current = current.next
            if current is None:
                return self.head
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
        return self.head
    def delete(self, position):
        if position == 0:
            self.head = self.head.next
            return self.head
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return self.head
            current = current.next
        if current is None or current.next is None:
            return self.head
        current.next = current.next.next
        return self.head
    def print_reverse_iterative(self):
        stack = []
        current = self.head
        while current:
            stack.append(current)
            current = current.next
        while stack:
            node = stack.pop()
            print(node.data, end=" ")
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
        return self.head
if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_head_node(1)
    llist.insert_specific_position(2, 1)
    llist.insert_specific_position(3, 2)
    llist.insert_tail_node(4)
    print("\nLinked List:")
    llist.print_list()
    print("\nReverse Linked List:")
    llist.reverse()
    llist.print_list()