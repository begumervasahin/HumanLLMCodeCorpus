class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
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
def sum_recursive(ll):
    if ll is None:
        return 0
    return ll.value + sum_recursive(ll.next)
def to_string_iterative(ll):
    result = ''
    while ll is not None:
        result += str(ll.value) + '->'
        ll = ll.next
    return result + 'None'
def to_string_recursive(ll):
    if ll is None:
        return 'None'
    return str(ll.value) + '->' + to_string_recursive(ll.next)
def list_to_linked_list_iterative(lst):
    if not lst:
        return None
    front = rear = ListNode(lst[0])
    for value in lst[1:]:
        rear.next = ListNode(value)
        rear = rear.next
    return front
def list_to_linked_list_recursive(lst):
    if not lst:
        return None
    return ListNode(lst[0], list_to_linked_list_recursive(lst[1:]))
def find_iterative(ll, value):
    while ll is not None:
        if ll.value == value:
            return ll
        ll = ll.next
    return None
def find_recursive(ll, value):
    if ll is None:
        return None
    if ll.value == value:
        return ll
    return find_recursive(ll.next, value)
def copy_iterative(ll):
    if ll is None:
        return None
    front = rear = ListNode(ll.value)
    while ll.next is not None:
        ll = ll.next
        rear.next = ListNode(ll.value)
        rear = rear.next
    return front
def copy_recursive(ll):
    if ll is None:
        return None
    return ListNode(ll.value, copy_recursive(ll.next))
def linked_list_iterator(ll):
    while ll is not None:
        yield ll.value
        ll = ll.next
def append_iterative(ll, value):
    if ll is None:
        return ListNode(value)
    front = ll
    while ll.next is not None:
        ll = ll.next
    ll.next = ListNode(value)
    return front
def append_recursive(ll, value):
    if ll is None:
        return ListNode(value)
    ll.next = append_recursive(ll.next, value)
    return ll
def add_after(ll, value):
    ll.next = ListNode(value, ll.next)
def remove_after(ll):
    if ll.next is not None:
        ll.next = ll.next.next
if __name__ == '__main__':
    linked_list = list_to_linked_list_iterative([1, 2, 3, 4, 5, 6])
    linked_list.next.next.value = 9
    linked_list.next.next = ListNode(9)
    print(to_string_iterative(linked_list))
