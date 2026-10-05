class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def insertTailNode(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    def insertHeadNode(self, data):
        current = Node(data)
        current.next = self.head
        self.head = current
    def insertSpecificPosition(self, data, position):
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
    def delete(self, position):
        temp = self.head
        if position == 0:
            return temp.next
        while position - 1 > 0:
            self.head = self.head.next
            position -= 1
        self.head.next = self.head.next.next
        return temp
    def printReverseIterative(self):
        if self.head:
            stack = [self.head]
            while stack[-1].next:
                node = stack[-1]
                stack.append(node.next)
            while stack:
                node = stack.pop()
                print(node.data, end=" ")
        print()
    def reverse(self):
        current = self.head
        previous = None
        next_node = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
if __name__ == '__main__':
    llist = LinkedList()
    llist.insertHeadNode(1)
    llist.insertSpecificPosition(2, 1)
    llist.insertSpecificPosition(3, 2)
    llist.insertTailNode(4)
    print("Linked list:")
    llist.printList()
    print("\nReverse linked list:")
    llist.reverse()
    llist.printList()