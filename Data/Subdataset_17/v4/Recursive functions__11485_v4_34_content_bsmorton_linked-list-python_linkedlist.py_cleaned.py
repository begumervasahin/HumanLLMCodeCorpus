class LN:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def len_ll(ll):
    count = 0
    while ll is not None:
        count += 1
        ll = ll.next
    return count
def len_ll_r(ll):
    if ll is None:
        return 0
    else:
        return 1 + len_ll_r(ll.next)
def sum_ll(ll):
    total = 0
    while ll is not None:
        total += ll.value
        ll = ll.next
    return total
def sum_ll_r(ll):
    if ll is None:
        return 0
    else:
        return ll.value + sum_ll_r(ll.next)
def str_ll(ll):
    answer = ''
    while ll is not None:
        answer += str(ll.value) + '->'
        ll = ll.next
    return answer + 'None'
def str_ll_r(ll):
    if ll is None:
        return 'None'
    else:
        return str(ll.value) + '->' + str_ll_r(ll.next)
def list_to_ll(l):
    if not l:
        return None
    front = rear = LN(l[0])
    for v in l[1:]:
        rear.next = LN(v)
        rear = rear.next
    return front
def list_to_ll_r(l):
    if not l:
        return None
    else:
        return LN(l[0], list_to_ll_r(l[1:]))
def find_ll(ll, avalue):
    while ll is not None:
        if ll.value == avalue:
            return ll
        ll = ll.next
    return None
def find_ll_r(ll, avalue):
    if ll is None:
        return None
    elif ll.value == avalue:
        return ll
    else:
        return find_ll_r(ll.next, avalue)
def copy_ll(ll):
    if ll is None:
        return None
    front = rear = LN(ll.value)
    while ll.next is not None:
        ll = ll.next
        rear.next = LN(ll.value)
        rear = rear.next
    return front
def copy_ll_r(ll):
    if ll is None:
        return None
    else:
        return LN(ll.value, copy_ll_r(ll.next))
def iterator(ll):
    while ll is not None:
        yield ll.value
        ll = ll.next
def append_ll(ll, value):
    if ll is None:
        return LN(value)
    front = ll
    while ll.next is not None:
        ll = ll.next
    ll.next = LN(value)
    return front
def append_ll_r(ll, value):
    if ll is None:
        return LN(value)
    else:
        ll.next = append_ll_r(ll.next, value)
        return ll
def add_after_ll(ll, value):
    ll.next = LN(value, ll.next)
def remove_after_ll(ll):
    if ll.next is not None:
        ll.next = ll.next.next
if __name__ == '__main__':
    l = list_to_ll([1, 2, 3, 4, 5, 6])
    l.next.next.value = 9
    l.next.next = LN(9)
    print(l.next.next.next)
