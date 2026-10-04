import random
def fonk1(b6):
    if not isinstance(b6, list):
        raise TypeError('The function argument must be a list containing numbers.')
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
    b4 = {
        'first': low,
        'last': high,
        'middle': (low + high)
        'random': random.randint(low, high)
    }
    if pivot_type not in b4:
        raise ValueError('Pivot options: first, last, middle, random.')
    b5 = b4[pivot_type]
    b6[b5], b6[high] = b6[high], b6[b5]
    return b6[high], b6
def fonk3(b6, low, high, pivot_type):
    pivot, b6 = fonk2(b6, low, high, pivot_type)
    b7 = low - 1
    for b3 in range(low, high):
        if b6[b3] <= pivot:
            b7 += 1
            b6[b7], b6[b3] = b6[b3], b6[b7]
    b6[b7 + 1], b6[high] = b6[high], b6[b7 + 1]
    return b7 + 1
def fonk4(b6, low, high, pivot_type, b8 = False, threshold=10):
    if not isinstance(b6, list):
        raise TypeError('The function argument must be a list containing numbers.')
    if len(b6) < 2:
        return b6
    if low < high:
        if b8 and (high - low) < threshold:
            b6[low:high + 1] = fonk1(b6[low:high + 1])
        else:
            b5 = fonk3(b6, low, high, pivot_type)
            fonk4(b6, low, b5 - 1, pivot_type, b8, threshold)
            fonk4(b6, b5 + 1, high, pivot_type, b8, threshold)
    return b6
if b9 = = "__main__":
    b10 = [3, 6, 8, 10, 1, 2, 1]
    b11 = fonk4(b10, 0, len(b10) - 1, 'middle', b8=True, threshold=10)
    print(b11)