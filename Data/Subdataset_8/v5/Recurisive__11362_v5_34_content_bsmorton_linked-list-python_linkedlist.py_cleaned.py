class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
def length_iterative(ll):
    count = 0
    while ll is not None:
        count += 1
        ll = ll.next
    return count
def length_recursive(ll):
    if ll is None:
        return 0
    return 1 + length_recursive(ll.next)
def sum_iterative(ll):
    total = 0
    while ll is not None:
        total += ll.value
        ll = ll.next
    return total
if __name__ == '__main__':
    linked_list = list_to_ll([1, 2, 3, 4, 5, 6])
    linked_list.next.next.value = 9
    linked_list.next.next.next = ListNode(9)
    print(linked_list.next.next.next)
