from LinkedList import Node, LinkedList
def locate_middle_node(linked_list):
    slow_cursor = linked_list.head
    fast_cursor = linked_list.head
    while fast_cursor and fast_cursor.next_node:
        prev_slow_cursor = slow_cursor
        slow_cursor = slow_cursor.next_node
        fast_cursor = fast_cursor.next_node.next_node
    prev_slow_cursor.next_node = None
    return slow_cursor
def reverse_second_half(middle_node):
    cursor = middle_node
    prev_node = None
    while cursor:
        next_node = cursor.next_node
        cursor.next_node = prev_node
        prev_node = cursor
        cursor = next_node
    return prev_node
def reorder_original_list(head_of_second_half):
    cursor1 = ll.head
    cursor2 = head_of_second_half
    while cursor1.next_node:
        next_cursor1 = cursor1.next_node
        cursor1.next_node = cursor2
        cursor1 = next_cursor1
        next_cursor2 = cursor2.next_node
        cursor2.next_node = cursor1
        cursor2 = next_cursor2
    cursor1.next_node = cursor2
if __name__ == '__main__':
    ll = LinkedList()
    middle_node = locate_middle_node(ll)
    head_of_second_half = reverse_second_half(middle_node)
    reorder_original_list(head_of_second_half)