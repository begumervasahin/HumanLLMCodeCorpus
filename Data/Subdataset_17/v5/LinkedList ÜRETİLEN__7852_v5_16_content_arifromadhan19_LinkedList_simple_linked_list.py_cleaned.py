class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    def insert_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_head(data)
        else:
            new_node = Node(data)
            current = self.head
            current_position = 1
            while current and current_position < position:
                current = current.next
                current_position += 1
            if current:
                new_node.next = current.next
                current.next = new_node
            else:
                print("Position out of bounds")
    def delete(self, position):
        if not self.head:
            return
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                if not current.next:
                    print("Position out of bounds")
                    return
                current = current.next
            if current.next:
                current.next = current.next.next
    def print_reverse_iterative(self):
        stack = []
        current = self.head
        while current:
            stack.append(current)
            current = current.next
        while stack:
            node = stack.pop()
            print(node.data, end=" ")
        print()
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_head(1)
    llist.insert_at_position(2, 1)
    llist.insert_at_position(3, 2)
    llist.insert_tail(4)
    print("Linked list:")
    llist.print_list()
    print("Reversed linked list:")
    llist.reverse()
    llist.print_list()