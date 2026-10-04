class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
    def __repr__(self):
        return str([value for value in self])
def reverse(linked_list):
    reversed_llist = LinkedList()
    previous_node = None
    for value in linked_list:
        new_node = Node(value)
        new_node.next = previous_node
        previous_node = new_node
    reversed_llist.head = previous_node
    return reversed_llist
llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)
flipped = reverse(llist)
is_correct = list(flipped) == [0, -3, 1, 5, 2, 4] and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")