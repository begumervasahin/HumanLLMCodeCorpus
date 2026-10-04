from linkedList_CISC121 import createList, printList, getLength
def is_in_list(linked_list, value):
    current_node = linked_list
    while current_node is not None:
        if current_node['data'] == value:
            return True
        current_node = current_node['next']
    return False
def pop_first(linked_list):
    if linked_list is None:
        return None, None
    first_value = linked_list['data']
    new_head = linked_list['next']
    return first_value, new_head
def get_element(linked_list, index):
    if linked_list is None or index >= getLength(linked_list):
        return None
    current_node = linked_list
    for _ in range(index):
        current_node = current_node['next']
    return current_node['data']
def pop_last(linked_list):
    if linked_list is None:
        return None, None
    if linked_list['next'] is None:
        return linked_list['data'], None
    if getLength(linked_list) == 2:
        last_value = linked_list['next']['data']
        linked_list['next'] = None
        return last_value, linked_list
    current_node = linked_list
    for _ in range(getLength(linked_list) - 2):
        current_node = current_node['next']
    last_value = current_node['next']['data']
    current_node['next'] = None
    return last_value, linked_list
def sum_sequence(n):
    if n == 0:
        return 0
    return n + sum_sequence(n - 1)
def binary_to_decimal(binary_string):
    if len(binary_string) == 1:
        return int(binary_string[0])
    most_significant_bit = int(binary_string[0])
    remaining_bits = binary_string[1:]
    return (most_significant_bit * (2 ** len(remaining_bits))) + binary_to_decimal(remaining_bits)