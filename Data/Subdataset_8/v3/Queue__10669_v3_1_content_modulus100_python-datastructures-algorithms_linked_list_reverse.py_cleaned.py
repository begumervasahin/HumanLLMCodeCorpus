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
            return
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
def reverse_linked_list(linked_list):
    reversed_llist = LinkedList()
    node = None
    for value in linked_list:
        if node is None:
            node = Node(value)
        else:
            new_node = Node(value)
            new_node.next = node
            node = new_node
    reversed_llist.head = node
    return reversed_llist
llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)
reversed_llist = reverse_linked_list(llist)
is_correct = list(reversed_llist) == [0, -3, 1, 5, 2, 4] and list(llist) == list(reverse_linked_list(reversed_llist))
print("Pass" if is_correct else "Fail")