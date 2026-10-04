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
            print(current.data, end=' ')
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
        if position < 0:
            print("Position must be a non-negative integer.")
            return
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            current_position = 0
            while current and current_position < position - 1:
                current = current.next
                current_position += 1
            if current is None:
                print("Position out of bounds")
            else:
                new_node.next = current.next
                current.next = new_node
    def delete_node(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position < 0:
            print("Position must be a non-negative integer.")
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
        else:
            current = self.head
            for i in range(position - 1):
                if current.next is None:
                    print("Position out of bounds")
                    return
                current = current.next
            if current.next is None:
                print("Position out of bounds")
                return
            next_node = current.next.next
            current.next = None
            current.next = next_node
    def print_reverse(self):
        stack = []
        current = self.head
        while current:
            stack.append(current)
            current = current.next
        while stack:
            node = stack.pop()
            print(node.data, end=' ')
        print()
    def reverse(self):
        current = self.head
        previous = None
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