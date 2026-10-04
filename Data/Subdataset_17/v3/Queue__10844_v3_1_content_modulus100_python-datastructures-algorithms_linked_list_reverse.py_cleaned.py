class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
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
values_to_add = [4, 2, 5, 1, -3, 0]
for value in values_to_add:
    llist.append(value)
reversed_ll = reverse(llist)
is_correct = list(reversed_ll) == list(reversed(values_to_add)) and list(llist) == values_to_add
print("Pass" if is_correct else "Fail")