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
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)
def merge(list1, list2):
    dummy = Node(0)
    current = dummy
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 if list1 else list2
    return LinkedList(dummy.next)
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)
    def _flatten(self, node):
        if not node.next:
            return node.value
        return merge(node.value, self._flatten(node.next))
if __name__ == '__main__':
    linked_list1 = LinkedList(Node(1))
    linked_list1.append(3)
    linked_list1.append(5)
    linked_list2 = LinkedList(Node(2))
    linked_list2.append(4)
    merged_list = merge(linked_list1.head, linked_list2.head)
    print("Merged Linked List:", merged_list)
    nested_linked_list = NestedLinkedList(Node(linked_list1))
    nested_linked_list.append(linked_list2)
    flattened_list = nested_linked_list.flatten()
    print("Flattened Nested Linked List:", flattened_list)