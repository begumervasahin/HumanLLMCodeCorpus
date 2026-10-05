class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def insert_tail_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    def insert_head_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_specific_position(self, data, position):
        if position == 0:
            self.insert_head_node(data)
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
    def delete(self, position):
        if position == 0:
            if self.head is None:
                return
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return
            current = current.next
        if current is None or current.next is None:
            return
        temp = current.next
        current.next = current.next.next
        temp.next = None
        return temp
    def print_reverse_iterative(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        while stack:
            print(stack.pop(), end=" ")
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
    llist.insert_head_node(1)
    llist.insert_specific_position(2, 1)
    llist.insert_specific_position(3, 2)
    llist.insert_tail_node(4)
    print("Linked list:")
    llist.print_list()
    print("\nReverse linked list:")
    llist.reverse()
    llist.print_list()