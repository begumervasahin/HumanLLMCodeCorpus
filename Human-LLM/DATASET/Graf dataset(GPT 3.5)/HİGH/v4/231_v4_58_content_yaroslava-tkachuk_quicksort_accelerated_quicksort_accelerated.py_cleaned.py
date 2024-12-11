import random
def fonk1(b6):
    if not isinstance(b6, list):
        raise TypeError('The input must be a list.')
    b1 = len(b6)
    if b1 < 2:
        return b6
    for b7 in range(1, b1):
        b2 = b6[b7]
        b3 = b7 - 1
        while b3 >= 0 and b6[b3] > b2:
            b6[b3 + 1] = b6[b3]
            b3 -= 1
        b6[b3 + 1] = b2
    return b6
def fonk2(b6, low, high, pivot_type):
    b4 = {'first': low, 'last': high, 'middle': (low + high)
    b5 = b6[b4[pivot_type]]
    b6[b4[pivot_type]], b6[high] = b6[high], b6[b4[pivot_type]]
    return b5, b6
def fonk3(b6, low, high, pivot_type):
    b5, b6 = fonk2(b6, low, high, pivot_type)
    b7 = low - 1
    for b3 in range(low, high):
        if b6[b3] <= b5:
            b7 += 1
            b6[b7], b6[b3] = b6[b3], b6[b7]
    b6[b7 + 1], b6[high] = b6[high], b6[b7 + 1]
    return b7 + 1
def fonk4(b6, low, high, pivot_type, b8 = False, modify_length=10):
    if not isinstance(b6, list):
        raise TypeError('Input must be a list.')
    if len(b6) < 2:
        return b6
    try:
        if low < high:
            if b8 and (high - low) < modify_length:
                b6 = fonk1(b6[low:high + 1])
            else:
                b9 = fonk3(b6, low, high, pivot_type)
                if b8 and (b9 - low) < modify_length:
                    fonk1(b6[low:b9])
                else:
                    fonk4(b6, low, b9 - 1, pivot_type)
                if b8 and (high - b9) < modify_length:
                    fonk1(b6[b9 + 1: high + 1])
                else:
                    fonk4(b6, b9 + 1, high, pivot_type)
        return b6
    except TypeError:
        print('List must contain only numbers.')
        return None