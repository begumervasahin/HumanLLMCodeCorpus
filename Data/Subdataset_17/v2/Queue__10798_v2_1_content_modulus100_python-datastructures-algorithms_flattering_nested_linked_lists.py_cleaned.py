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
            values.append(current.value)
            current = current.next
        return " -> ".join(map(str, values))
def merge(list1, list2):
    merged = LinkedList()
    current1 = list1.head if list1 else None
    current2 = list2.head if list2 else None
    while current1 or current2:
        if current1 is None:
            merged.append(current2.value)
            current2 = current2.next
        elif current2 is None:
            merged.append(current1.value)
            current1 = current1.next
        elif current1.value <= current2.value:
            merged.append(current1.value)
            current1 = current1.next
        else:
            merged.append(current2.value)
            current2 = current2.next
    return merged
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)
    def _flatten(self, node):
        if not node.next:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))
if __name__ == "__main__":
    linked_list1 = LinkedList(Node(1))
    linked_list1.append(3)
    linked_list1.append(5)
    print(f"Linked List 1: {linked_list1}")
    linked_list2 = LinkedList(Node(2))
    linked_list2.append(4)
    print(f"Linked List 2: {linked_list2}")
    merged_list = merge(linked_list1, linked_list2)
    print(f"Merged List: {merged_list}")
    merged_with_none = merge(None, linked_list1)
    print(f"Merged with None: {merged_with_none}")
    nested_list = NestedLinkedList(Node(linked_list1))
    nested_list.append(linked_list2)
    flattened_list = nested_list.flatten()
    print(f"Flattened Nested List: {flattened_list}")