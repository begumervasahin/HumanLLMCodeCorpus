class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)
def merge_linked_lists(list1, list2):
    merged = LinkedList()
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None and list2_elt is not None:
        if list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    while list1_elt is not None:
        merged.append(list1_elt)
        list1_elt = list1_elt.next
    while list2_elt is not None:
        merged.append(list2_elt)
        list2_elt = list2_elt.next
    return merged
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)
    def _flatten(self, node):
        if node.next is None:
            return merge_linked_lists(node.value, None)
        return merge_linked_lists(node.value, self._flatten(node.next))
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)
nested_linked_list = NestedLinkedList(Node(linked_list))
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)
nested_linked_list.append(Node(second_linked_list))
merged = merge_linked_lists(linked_list, second_linked_list)
node = merged.head
print("Merged Linked Lists:")
while node is not None:
    print(node.value)
    node = node.next
merged = merge_linked_lists(None, linked_list)
node = merged.head
print("Merged None and Linked List:")
while node is not None:
    print(node.value)
    node = node.next
nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()
node = flattened.head
print("Flattened Nested Linked List:")
while node is not None:
    print(node.value)
    node = node.next