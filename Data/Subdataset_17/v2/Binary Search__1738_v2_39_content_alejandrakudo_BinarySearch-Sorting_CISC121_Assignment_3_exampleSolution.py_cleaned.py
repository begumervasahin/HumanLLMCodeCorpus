
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
def print_linked_list(linked_list):
    current = linked_list
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next
def get_length(linked_list):
    length = 0
    current = linked_list
    while current:
        length += 1
        current = current.next
    return length
def is_in_list(linked_list, value):
    current = linked_list
    while current:
        if current.data == value:
            return True
        current = current.next
    return False
def pop_first(linked_list):
    if not linked_list:
        return None, None
    value = linked_list.data
    linked_list = linked_list.next
    return value, linked_list
def get_element(linked_list, index):
    if not linked_list or index >= get_length(linked_list):
        return None
    current = linked_list
    for _ in range(index):
        current = current.next
    return current.data
def pop_last(linked_list):
    if not linked_list:
        return None, None
    if not linked_list.next:
        return linked_list.data, None
    current = linked_list
    while current.next.next:
        current = current.next
    value = current.next.data
    current.next = None
    return value, linked_list
def sum_sequence(n):
    if n == 0:
        return 0
    return n + sum_sequence(n - 1)
def binary_to_decimal(binary_str):
    if len(binary_str) == 1:
        return int(binary_str)
    return int(binary_str[0]) * (2 ** (len(binary_str) - 1)) + binary_to_decimal(binary_str[1:])
if __name__ == "__main__":
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    print("Original Linked List:")
    print_linked_list(linked_list)
    value_to_check = 3
    print(f"\nIs {value_to_check} in the list? {'Yes' if is_in_list(linked_list, value_to_check) else 'No'}")
    first_value, linked_list = pop_first(linked_list)
    print(f"\nPopped first value: {first_value}")
    print("Linked List after popping the first element:")
    print_linked_list(linked_list)
    index = 2
    print(f"\nElement at index {index}: {get_element(linked_list, index)}")
    last_value, linked_list = pop_last(linked_list)
    print(f"\nPopped last value: {last_value}")
    print("Linked List after popping the last element:")
    print_linked_list(linked_list)
    n = 5
    print(f"\nSum of numbers from {n} to 0: {sum_sequence(n)}")
    binary_str = "1101"
    print(f"\nBinary string '{binary_str}' to decimal: {binary_to_decimal(binary_str)}")