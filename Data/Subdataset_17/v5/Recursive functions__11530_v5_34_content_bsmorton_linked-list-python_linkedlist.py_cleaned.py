class LN:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def len_ll(ll):
    count = 0
    while ll:
        count += 1
        ll = ll.next
    return count
def len_ll_r(ll):
    return 0 if ll is None else 1 + len_ll_r(ll.next)
def sum_ll(ll):
    total = 0
    while ll:
        total += ll.value
        ll = ll.next
    return total
def sum_ll_r(ll):
    return 0 if ll is None else ll.value + sum_ll_r(ll.next)
def str_ll(ll):
    result = ''
    while ll:
        result += f"{ll.value}->"
        ll = ll.next
    return result + 'None'
def str_ll_r(ll):
    return 'None' if ll is None else f"{ll.value}->" + str_ll_r(ll.next)
def list_to_ll(lst):
    if not lst:
        return None
    front = rear = LN(lst[0])
    for value in lst[1:]:
        rear.next = LN(value)
        rear = rear.next
    return front
def list_to_ll_r(lst):
    return None if not lst else LN(lst[0], list_to_ll_r(lst[1:]))
def find_ll(ll, value):
    while ll:
        if ll.value == value:
            return ll
        ll = ll.next
    return None
def find_ll_r(ll, value):
    if ll is None or ll.value == value:
        return ll
    return find_ll_r(ll.next, value)
def copy_ll(ll):
    if not ll:
        return None
    front = rear = LN(ll.value)
    while ll.next:
        ll = ll.next
        rear.next = LN(ll.value)
        rear = rear.next
    return front
def copy_ll_r(ll):
    return None if ll is None else LN(ll.value, copy_ll_r(ll.next))
def iterator(ll):
    while ll:
        yield ll.value
        ll = ll.next
def append_ll(ll, value):
    if not ll:
        return LN(value)
    front = ll
    while ll.next:
        ll = ll.next
    ll.next = LN(value)
    return front
def append_ll_r(ll, value):
    return LN(value) if ll is None else (ll.next := append_ll_r(ll.next, value)) or ll
def add_after_ll(ll, value):
    ll.next = LN(value, ll.next)
def remove_after_ll(ll):
    if ll.next:
        ll.next = ll.next.next
if __name__ == '__main__':
    l = list_to_ll([1, 2, 3, 4, 5, 6])
    l.next.next.value = 9
    l.next.next = LN(9)
    print(l.next.next.next)
