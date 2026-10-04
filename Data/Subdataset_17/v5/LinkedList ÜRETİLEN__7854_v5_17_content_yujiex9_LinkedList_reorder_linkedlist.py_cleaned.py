from LinkedList import Node, LinkedList
def locate_middle_node(ll):
    slow = ll.head
    fast = ll.head
    prev_slow = None
    while fast and fast.next_node:
        prev_slow = slow
        slow = slow.next_node
        fast = fast.next_node.next_node
    if prev_slow:
        prev_slow.next_node = None
    return slow
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next_node
        current.next_node = prev
        prev = current
        current = next_node
    return prev
def reorder_original_list(ll, second_half_head):
    first_half_head = ll.head
    second_half_current = second_half_head
    while first_half_head and second_half_current:
        tmp_first = first_half_head.next_node
        tmp_second = second_half_current.next_node
        first_half_head.next_node = second_half_current
        if not tmp_first:
            break
        second_half_current.next_node = tmp_first
        first_half_head = tmp_first
        second_half_current = tmp_second
def reorder_linked_list(ll):
    if not ll.head or not ll.head.next_node:
        return
    middle_node = locate_middle_node(ll)
    second_half_head = reverse_linked_list(middle_node)
    reorder_original_list(ll, second_half_head)
ll = LinkedList()
ll.add_to_end(1)
ll.add_to_end(2)
ll.add_to_end(3)
ll.add_to_end(4)
ll.add_to_end(5)
print("Original list:")
ll.display()
reorder_linked_list(ll)
print("Reordered list:")
ll.display()