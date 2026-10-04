class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        print(f"Value {data} not found in the list.")
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"
def reverse_list(input_list):
    linked_list = SinglyLinkedList()
    for item in input_list:
        linked_list.add(item)
    print("Input list:", linked_list)
    current = linked_list.head
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev
    return linked_list
if __name__ == "__main__":
    print('\nReverse and Deleting in Singly Linked List\n')
    test_cases = [
        (1, 2, 3, 4, 5),
        ('org', 'com', 'her', 'him', 'blah'),
        (1, 'com', 3, 'him', 5),
        (1, 'com', SinglyLinkedList(), 'him', 5),
        ('B',),
        ('B', 'B', 'B', 'B'),
        (),
    ]
    for idx, test_case in enumerate(test_cases):
        returned_list = reverse_list(test_case)
        print(f"Output list for test case {idx + 1}: {returned_list}")
        if test_case:
            print(f"Deleting '{test_case[0]}'")
            returned_list.delete(test_case[0])
            print(f"Output list after deleting '{test_case[0]}': {returned_list}")
        print('')