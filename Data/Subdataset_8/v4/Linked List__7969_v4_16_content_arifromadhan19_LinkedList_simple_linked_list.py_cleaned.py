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
    def insert_tail_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        return self.head
    def insert_head_node(self, data):
        current = Node(data)
        current.next = self.head
        self.head = current
    def insert_specific_position(self, data, position):
        if position != 0:
            current = self.head
            current_position = 1
            while position - current_position > 0:
                current = current.next
                current_position += 1
            if current.next is None:
                current.next = Node(data, None)
            else:
                prev = current.next
                current.next = Node(data, prev)
        else:
            self.head = Node(data, self.head)
        return self.head
    def delete(self, position):
        temp = self.head
        if position == 0:
            return temp.next
        while position - 1 > 0:
            self.head = self.head.next
            position -= 1
        self.head.next = self.head.next.next
        return temp
    def print_reverse_iterative(self):
        if self.head:
            stack = [self.head]
            while stack[-1].next:
                node = stack[-1]
                stack.append(node.next)
            while stack:
                node = stack.pop()
                print(node.data, end=" ")
    def reverse(self):
        current = self.head
        previous = None
        next_node = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
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