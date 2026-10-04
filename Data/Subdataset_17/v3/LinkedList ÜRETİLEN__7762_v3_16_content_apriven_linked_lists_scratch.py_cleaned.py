class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.length = 0
        if values:
            for value in values:
                self.add_last(value)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    def add_last(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
    def get_length(self):
        return self.length
    def is_empty(self):
        return self.head is None
    def find_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
    def remove(self, value):
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if not previous:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.length -= 1
                return current
            previous = current
            current = current.next
        return None
def test_list(actual, expected):
    current = actual
    for index, value in enumerate(expected):
        assert current is not None and current.value == value, f"Element number {index + 1} should be {value}, got {current.value if current else 'None'}"
        current = current.next
def test_length(linked_list, expected_length):
    assert linked_list.get_length() == expected_length, f"Length should be {expected_length}, got {linked_list.get_length()}"
def test_value(actual, expected, msg=""):
    assert actual == expected, f"{msg} should be {expected}, got {actual}"
def test_max(linked_list, expected):
    max_val = linked_list.find_max()
    test_value(max_val, expected, "Wrong maximum")
def create_list(values):
    return LinkedList(values)
if __name__ == "__main__":
    first = Node(4)
    first.next = Node(1)
    first.next.next = Node(7)
    test_list(first, [4, 1, 7])
    print("Test 1: Node class passed")
    my_list = LinkedList()
    my_list.add_first(6)
    my_list.add_first(4)
    my_list.add_first(2)
    test_list(my_list.head, [2, 4, 6])
    test_length(my_list, 3)
    print("Test 2: add_first & LinkedList class passed")
    my_list2 = LinkedList()
    my_list2.add_last(6)
    my_list2.add_last(4)
    my_list2.add_last(2)
    test_list(my_list2.head, [6, 4, 2])
    test_length(my_list2, 3)
    print("Test 3: add_last passed")
    my_list = LinkedList()
    test_length(my_list, 0)
    my_list.add_first(6)
    test_list(my_list.head, [6])
    test_length(my_list, 1)
    my_list.add_first(4)
    test_list(my_list.head, [4, 6])
    test_length(my_list, 2)
    my_list.add_last(8)
    test_list(my_list.head, [4, 6, 8])
    test_length(my_list, 3)
    print("Test 4: length passed")
    my_list = create_list([2, 4, 6, 8])
    removed = my_list.remove(3)
    test_value(removed, None)
    removed = my_list.remove(4)
    test_value(removed.value, 4)
    test_list(my_list.head, [2, 6, 8])
    test_length(my_list, 3)
    removed = my_list.remove(2)
    test_value(removed.value, 2)
    test_list(my_list.head, [6, 8])
    test_length(my_list, 2)
    removed = my_list.remove(8)
    test_value(removed.value, 8)
    test_list(my_list.head, [6])
    test_length(my_list, 1)
    removed = my_list.remove(6)
    test_value(removed.value, 6)
    test_length(my_list, 0)
    assert my_list.is_empty() is True, "List should be empty"
    print("Test 5: remove passed")
    test_max(create_list([1, 4, 3, 2]), 4)
    test_max(create_list([9, 4, 3, 2]), 9)
    test_max(create_list([1, 4, 3, 8]), 8)
    test_max(create_list([1]), 1)
    print("Test 6: find max passed")
    test_list(create_list([1, 4, 3, 2]).head, [1, 4, 3, 2])
    test_list(create_list([9, 4, 3, 2]).head, [9, 4, 3, 2])
    test_list(create_list([1, 4, 3, 8]).head, [1, 4, 3, 8])
    test_list(create_list([1]).head, [1])
    print("Test 7: Create linked list from list passed")