import random
def fonk1(b7):
    if not isinstance(b7, list):
        raise TypeError('The function argument must be a list containing numbers.')
    b1 = len(b7)
    if b1 < 2:
        return b7
    for b8 in range(1, b1):
        b2 = b7[b8]
        b3 = b8 - 1
        try:
            while b3 >= 0 and b7[b3] > b2:
                b7[b3 + 1] = b7[b3]
                b3 -= 1
            b7[b3 + 1] = b2
        except TypeError:
            print('The list must contain numbers.')
            return None
    return b7
def fonk2(b7, l, h, pi):
    b4 = {'first': l, 'last': h, 'middle': (l + h)
    if pi not in b4:
        raise ValueError("Pivot options: 'first', 'last', 'middle', 'random'.")
    b5 = b4[pi]
    b6 = b7[b5]
    b7[b5], b7[h] = b7[h], b7[b5]
    return b6, b7
def fonk3(b7, l, h, pi):
    b6, b7 = fonk2(b7, l, h, pi)
    b8 = l - 1
    for b3 in range(l, h):
        if b7[b3] <= b6:
            b8 += 1
            b7[b8], b7[b3] = b7[b3], b7[b8]
    b7[b8 + 1], b7[h] = b7[h], b7[b8 + 1]
    return b8 + 1
def fonk4(b7, l, h, pi, b9 = False, threshold=10):
    if not isinstance(b7, list):
        raise TypeError('The function argument must be a list containing numbers.')
    if len(b7) < 2:
        return b7
    if l < h:
        if b9 and (h - l) < threshold:
            b7[l:h + 1] = fonk1(b7[l:h + 1])
        else:
            try:
                b5 = fonk3(b7, l, h, pi)
            except ValueError as e:
                print(e)
                return None
            if b9 and (b5 - l) < threshold:
                b7[l:b5] = fonk1(b7[l:b5])
            else:
                fonk4(b7, l, b5 - 1, pi, b9, threshold)
            if b9 and (h - b5) < threshold:
                b7[b5 + 1:h + 1] = fonk1(b7[b5 + 1:h + 1])
            else:
                fonk4(b7, b5 + 1, h, pi, b9, threshold)
    return b7