class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def length_linked_list(ll):
    count = 0
    while ll is not None:
        count += 1
        ll = ll.next
    return count
def length_linked_list_recursive(ll):
    if ll is None:
        return 0
    else:
        return 1 + length_linked_list_recursive(ll.next)
def sum_linked_list(ll):
    total = 0
    while ll is not None:
        total += ll.value
        ll = ll.next
    return total
def sum_linked_list_recursive(ll):
    if ll is None:
        return 0
    else:
        return ll.value + sum_linked_list_recursive(ll.next)
def stringify_linked_list(ll):
    answer = ''
    while ll is not None:
        answer += str(ll.value) + '->'
        ll = ll.next
    return answer + 'None'
def stringify_linked_list_recursive(ll):
    if ll is None:
        return 'None'
    else:
        return str(ll.value) + '->' + stringify_linked_list_recursive(ll.next)
def list_to_linked_list(l):
    if not l:
        return None
    front = rear = ListNode(l[0])
    for v in l[1:]:
        rear.next = ListNode(v)
        rear = rear.next
    return front
def list_to_linked_list_recursive(l):
    if not l:
        return None
    else:
        return ListNode(l[0], list_to_linked_list_recursive(l[1:]))
def find_in_linked_list(ll, value):
    while ll is not None:
        if ll.value == value:
            return ll
        ll = ll.next
    return None
def find_in_linked_list_recursive(ll, value):
    if ll is None:
        return None
    else:
        if ll.value == value:
            return ll
        else:
            return find_in_linked_list_recursive(ll.next, value)
def copy_linked_list(ll):
    if ll is None:
        return None
    front = rear = ListNode(ll.value)
    while ll.next is not None:
        ll = ll.next
        rear.next = ListNode(ll.value)
        rear = rear.next
    return front
def copy_linked_list_recursive(ll):
    if ll is None:
        return None
    else:
        return ListNode(ll.value, copy_linked_list_recursive(ll.next))
def linked_list_iterator(ll):
    while ll is not None:
        yield ll.value
        ll = ll.next
def append_to_linked_list(ll, value):
    if ll is None:
        return ListNode(value)
    front = ll
    while ll.next is not None:
        ll = ll.next
    ll.next = ListNode(value)
    return front
def append_to_linked_list_recursive(ll, value):
    if ll is None:
        return ListNode(value)
    else:
        ll.next = append_to_linked_list_recursive(ll.next, value)
        return ll
def add_after_in_linked_list(ll, value):
    ll.next = ListNode(value, ll.next)
def remove_after_in_linked_list(ll):
    ll.next = ll.next.next
if __name__ == '__main__':
    l = list_to_linked_list([1, 2, 3, 4, 5, 6])
    l.next.next.value = 9
    l.next.next = ListNode(9)
    print(l.next.next.next)