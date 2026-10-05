
from linkedList_CISC121 import createList, printList, getLength
def is_value_in_linked_list(linked_list, value):
    current_node = linked_list
    while current_node is not None:
        if current_node['data'] == value:
            return True
        current_node = current_node['next']
    return False
def pop_first_element(linked_list):
    if linked_list is None:
        return None, None
    first_element = linked_list
    linked_list = linked_list['next']
    return first_element['data'], linked_list
def get_element_at_index(linked_list, index):
    if linked_list is None or index >= getLength(linked_list):
        return None
    current_node = linked_list
    for i in range(index):
        current_node = current_node['next']
    return current_node['data']
def pop_last_element(linked_list):
    if linked_list is None:
        return None, None
    if linked_list['next'] is None:
        return linked_list['data'], None
    if getLength(linked_list) == 2:
        value = linked_list['next']['data']
        linked_list['next'] = None
        return value, linked_list
    current_node = linked_list
    for i in range(getLength(linked_list)-2):
        current_node = current_node['next']
    last_value = current_node['next']['data']
    current_node['next'] = None
    return last_value, linked_list
def calculate_sum_sequence(n):
    if n == 0:
        return 0
    return n + calculate_sum_sequence(n-1)
def convert_binary_to_decimal(binary_string):
    if len(binary_string) == 1:
        return int(binary_string[0])
    first_digit = int(binary_string[0])
    remaining_digits = binary_string[1:]
    return 2**(len(remaining_digits)) * first_digit + convert_binary_to_decimal(remaining_digits)
if __name__ == "__main__":
    linked_list = createList([1, 2, 3, 4, 5])
    print("Linked List:")
    printList(linked_list)
    print("Is 3 in the linked list?", is_value_in_linked_list(linked_list, 3))
    print("Is 6 in the linked list?", is_value_in_linked_list(linked_list, 6))
    popped_value, linked_list = pop_first_element(linked_list)
    print("Popped value from the linked list:", popped_value)
    print("Linked List after popping first element:")
    printList(linked_list)
    print("Element at index 2 in the linked list:", get_element_at_index(linked_list, 2))
    popped_value, linked_list = pop_last_element(linked_list)
    print("Popped value from the end of the linked list:", popped_value)
    print("Linked List after popping last element:")
    printList(linked_list)
    print("Sum of sequence from 0 to 5:", calculate_sum_sequence(5))
    binary_number = "1011"
    print("Decimal representation of binary number", binary_number, "is:", convert_binary_to_decimal(binary_number))