import random
def fonk1(b5):
    if not isinstance(b5, list):
        raise TypeError('Input must be a list containing numbers.')
    for b6 in range(1, len(b5)):
        b1 = b5[b6]
        b2 = b6 - 1
        while b2 >= 0 and b5[b2] > b1:
            b5[b2 + 1] = b5[b2]
            b2 -= 1
        b5[b2 + 1] = b1
    return b5
def fonk2(b5, b7, b8, pivot_type):
    b3 = {
        'first': b7,
        'last': b8,
        'middle': (b7 + b8)
        'random': random.randint(b7, b8)
    }
    b4 = b3.get(pivot_type, b7)
    b5[b4], b5[b8] = b5[b8], b5[b4]
    return b5[b8], b5
def fonk3(b5, b7, b8, pivot_type):
    pivot, b5 = fonk2(b5, b7, b8, pivot_type)
    b6 = b7 - 1
    for b2 in range(b7, b8):
        if b5[b2] <= pivot:
            b6 += 1
            b5[b6], b5[b2] = b5[b2], b5[b6]
    b5[b6 + 1], b5[b8] = b5[b8], b5[b6 + 1]
    return b6 + 1
def fonk4(b5, b7 = 0, b8=None, pivot_type='last', use_insertion_sort=False, threshold=10):
    if not isinstance(b5, list):
        raise TypeError('Input must be a list containing numbers.')
    if b8 is None:
        b8 = len(b5) - 1
    if b7 < b8:
        if use_insertion_sort and (b8 - b7) < threshold:
            b5[b7:b8 + 1] = fonk1(b5[b7:b8 + 1])
        else:
            b4 = fonk3(b5, b7, b8, pivot_type)
            fonk4(b5, b7, b4 - 1, pivot_type, use_insertion_sort, threshold)
            fonk4(b5, b4 + 1, b8, pivot_type, use_insertion_sort, threshold)
    return b5