class Hedgehog:
    def __init__(self, number):
        self.number = number
        self.next = None
class HedgehogList:
    def __init__(self):
        self.head = None
    def add_first(self, number):
        new_hedgehog = Hedgehog(number)
        new_hedgehog.next = self.head
        self.head = new_hedgehog
    def add_last(self, number):
        current = self.head
        if current is None:
            self.head = Hedgehog(number)
            return
        while current.next:
            current = current.next
        current.next = Hedgehog(number)
    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    def is_empty(self):
        return self.head is None
    def find_max(self):
        if self.is_empty():
            return None
        current = self.head
        max_value = current.number
        while current:
            if current.number > max_value:
                max_value = current.number
            current = current.next
        return max_value
    def remove(self, number):
        if self.is_empty():
            return None
        if self.head.number == number:
            removed = self.head
            self.head = self.head.next
            return removed
        current = self.head
        while current.next:
            if current.next.number == number:
                removed = current.next
                current.next = current.next.next
                return removed
            current = current.next
        return None
def test_list(actual, expected):
    item_index = 1
    actual_item = actual
    for item in expected:
        actual_value = actual_item.number if actual_item else None
        err_msg = f"Element number {item_index} should have the value of {item}, got {actual_value}"
        assert actual_item and item == actual_item.number, err_msg
        actual_item = actual_item.next
        item_index += 1
def test_length(linked_list, expected_length):
    assert linked_list.get_length() == expected_length, f"Length should be {expected_length}, got {linked_list.get_length()}"
def test_value(actual, expected, msg=""):
    assert actual == expected, f"{msg} should be {expected}, got {actual}"
def test_max(linked_list, expected):
    max_value = linked_list.find_max()
    test_value(max_value, expected, "Wrong maximum")
def create_list(numbers):
    hedgehog_list = HedgehogList()
    for number in numbers:
        hedgehog_list.add_last(number)
    return hedgehog_list
if __name__ == "__main__":
    first = Hedgehog(4)
    first.next = Hedgehog(1)
    first.next.next = Hedgehog(7)
    test_list(first, [4, 1, 7])
    print("Test 1: Hedgehog class passed")
    my_list = HedgehogList()
    my_list.add_first(6)
    my_list.add_first(4)
    my_list.add_first(2)
    test_list(my_list.head, [2, 4, 6])
    print("Test 2: add first & HedgehogList class passed")
    my_list2 = HedgehogList()
    my_list2.add_last(6)
    my_list2.add_last(4)
    my_list2.add_last(2)
    test_list(my_list2.head, [6, 4, 2])
    print("Test 3: add last passed")
    my_list = HedgehogList()
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
    test_value(removed.number, 4)
    test_list(my_list.head, [2, 6, 8])
    test_length(my_list, 3)
    removed = my_list.remove(2)
    test_value(removed.number, 2)
    test_list(my_list.head, [6, 8])
    test_length(my_list, 2)
    removed = my_list.remove(8)
    test_value(removed.number, 8)
    test_list(my_list.head, [6])
    test_length(my_list, 1)
    removed = my_list.remove(6)
    test_value(removed.number, 6)
    test_length(my_list, 0)
    assert my_list.is_empty(), "List should be empty"
    print("Test 5: remove passed")
    test_list(create_list([1,4,3,2]).head, [1,4,3,2])
    test_max(create_list([1,4,3,2]), 4)
    test_max(create_list([9,4,3,2]), 9)
    test_max(create_list([1,4,3,8]), 8)
    test_max(create_list([1]), 1)
    print("Test 6: find max passed")
    test_list(create_list([1,4,3,2]).head, [1,4,3,2])
    test_list(create_list([1,4,3,2]).head, [1,4,3,2])
    test_list(create_list([9,4,3,2]).head, [9,4,3,2])
    test_list(create_list([1,4,3,8]).head, [1,4,3,8])
    test_list(create_list([1]).head, [1])
    print("Test 7: Ninja - create linked list from list passed")