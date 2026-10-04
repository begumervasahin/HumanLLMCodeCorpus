import random
def fonk1(lst):
    if not isinstance(lst, list):
        raise TypeError('The function argument must be a list containing numbers.')
    b1 = len(lst)
    if b1 < 2:
        return lst
    for b7 in range(1, b1):
        b2 = lst[b7]
        b3 = b7 - 1
        while b3 >= 0 and lst[b3] > b2:
            lst[b3 + 1] = lst[b3]
            b3 -= 1
        lst[b3 + 1] = b2
    return lst
def fonk2(lst, l, h, strategy):
    b4 = {'first': l, 'last': h, 'middle': (l + h)
    if strategy not in b4:
        raise ValueError("Pivot options: 'first', 'last', 'middle', 'random'.")
    b5 = b4[strategy]
    lst[b5], lst[h] = lst[h], lst[b5]
    return lst[h]
def fonk3(lst, l, h, strategy):
    b6 = fonk2(lst, l, h, strategy)
    b7 = l - 1
    for b3 in range(l, h):
        if lst[b3] <= b6:
            b7 += 1
            lst[b7], lst[b3] = lst[b3], lst[b7]
    lst[b7 + 1], lst[h] = lst[h], lst[b7 + 1]
    return b7 + 1
def fonk4(lst, l, h, strategy, b8 = False, threshold=10):
    if not isinstance(lst, list):
        raise TypeError('The function argument must be a list containing numbers.')
    if len(lst) < 2:
        return lst
    if l < h:
        if b8 and (h - l) < threshold:
            lst[l:h + 1] = fonk1(lst[l:h + 1])
        else:
            b5 = fonk3(lst, l, h, strategy)
            if b8 and (b5 - l) < threshold:
                lst[l:b5] = fonk1(lst[l:b5])
            else:
                fonk4(lst, l, b5 - 1, strategy, b8, threshold)
            if b8 and (h - b5) < threshold:
                lst[b5 + 1:h + 1] = fonk1(lst[b5 + 1:h + 1])
            else:
                fonk4(lst, b5 + 1, h, strategy, b8, threshold)
    return lst