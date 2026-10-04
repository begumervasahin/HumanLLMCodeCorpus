class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    def __repr__(self):
        return str([value for value in self])
def reverse(linked_list):
    reversed_ll = LinkedList()
    current = None
    for value in linked_list:
        new_node = Node(value)
        new_node.next = current
        current = new_node
    reversed_ll.head = current
    return reversed_ll
llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)
reversed_ll = reverse(llist)
is_correct = list(reversed_ll) == [0, -3, 1, 5, 2, 4] and list(llist) == list(reverse(reversed_ll))
print("Pass" if is_correct else "Fail")