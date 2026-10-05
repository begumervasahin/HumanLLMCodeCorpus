class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
def length_linked_list(ll):
    count = 0
    while ll:
        count += 1
        ll = ll.next
    return count
def length_linked_list_recursive(ll):
    if not ll:
        return 0
    return 1 + length_linked_list_recursive(ll.next)
def sum_linked_list(ll):
    total = 0
    while ll:
        total += ll.value
        ll = ll.next
    return total
def sum_linked_list_recursive(ll):
    if not ll:
        return 0
    return ll.value + sum_linked_list_recursive(ll.next)
def stringify_linked_list(ll):
    answer = ''
    while ll:
        answer += str(ll.value) + '->'
        ll = ll.next
    return answer + 'None'
def stringify_linked_list_recursive(ll):
    if not ll:
        return 'None'
    return str(ll.value) + '->' + stringify_linked_list_recursive(ll.next)
def list_to_linked_list(lst):
    if not lst:
        return None
    head = current = ListNode(lst[0])
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
def list_to_linked_list_recursive(lst):
    if not lst:
        return None
    return ListNode(lst[0], list_to_linked_list_recursive(lst[1:]))
if __name__ == '__main__':
    l = list_to_linked_list([1, 2, 3, 4, 5, 6])
    l.next.next.value = 9
    l.next.next = ListNode(9)
    print(l.next.next.next)