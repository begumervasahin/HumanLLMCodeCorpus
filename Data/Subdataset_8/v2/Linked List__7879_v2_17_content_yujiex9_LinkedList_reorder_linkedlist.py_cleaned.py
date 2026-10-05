from LinkedList import Node, LinkedList
def locate_middle_node(linked_list):
    slow_cursor = linked_list.head
    fast_cursor = linked_list.head
    while fast_cursor and fast_cursor.next_node:
        slow_cursor = slow_cursor.next_node
        fast_cursor = fast_cursor.next_node.next_node
    return slow_cursor
def reverse_second_half(middle_node):
    current = middle_node
    previous = None
    next_node = None
    while current:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node
    return previous
def reorder_original_list(head_of_second_half):
    cursor1 = ll.head
    cursor2 = head_of_second_half
    while cursor1.next_node:
        tmp_node = cursor1.next_node
        cursor1.next_node = cursor2
        cursor1 = tmp_node
        tmp_node = cursor2.next_node
        cursor2.next_node = cursor1
        cursor2 = tmp_node
    cursor1.next_node = cursor2
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    middle_node = locate_middle_node(ll)
    head_of_second_half = reverse_second_half(middle_node)
    reorder_original_list(head_of_second_half)
    ll.printList()