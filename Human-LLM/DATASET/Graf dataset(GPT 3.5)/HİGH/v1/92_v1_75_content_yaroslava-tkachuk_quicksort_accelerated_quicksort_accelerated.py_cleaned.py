import random
def fonk1(b6):
    '''Insertion sort.
    Compares all the elements preceding the chosen element in the list. All the elements greater than the chosen element are moved after it.
    The operation is repeated for each element from the list.'''
    if type(b6) == list:
        b1 = len(b6)
        if b1 < 2:
            return b6
        else:
            for b7 in range(1, b1):
                b2 = b6[b7]
                b3 = b7 - 1
                try:
                    while b3 >= 0 and b6[b3] > b2:
                        b6[b3 + 1] = b6[b3]
                        b3 -= 1
                    b6[b3 + 1] = b2
                except TypeError:
                    print('The list must contain numbers.')
                    return None
            return b6
    else:
        raise TypeError('The function argument must be a list containing numbers.')
def fonk2(b6, l, h, pi):
    '''Chooses the reference element and moves it on the last place in the list.
    Options: first, last, middle, random.'''
    b4 = {'first': l, 'last': h, 'middle': (l + h)
    b5 = b6[b4[pi]]
    b6[b4[pi]], b6[h] = b6[h], b6[b4[pi]]
    return b5, b6
def fonk3(b6, l, h, pi):
    '''Places the reference element on its right place in the sorted list.'''
    b5, b6 = fonk2(b6, l, h, pi)
    b7 = l - 1
    for b3 in range(l, h):
        if b6[b3] <= b5:
            b7 += 1
            b6[b7], b6[b3] = b6[b3], b6[b7]
    b6[b7 + 1], b6[h] = b6[h], b6[b7 + 1]
    return b7 + 1
def fonk4(b6, l, h, pi, b8 = False, mod_len=10):
    '''Sorts the list elements with the use of recursive version of quicksort algorithm.
    Places the reference element (b5) on its right place in the sorted list. Repeats the operation until the whole list is sorted'''
    if type(b6) == list:
        if len(b6) < 2:
            return b6
        else:
            try:
                if l < h:
                    if b8 and ((h - l) < mod_len):
                        b6 = fonk1(b6[l:h + 1])
                    else:
                        try:
                            b9 = fonk3(b6, l, h, pi)
                        except KeyError:
                            print('Pivot options: first, last, middle, random.')
                            return None
                        if b8 and ((b9 - l) < mod_len):
                            fonk1(b6[l:b9])
                        else:
                            fonk4(b6, l, b9 - 1, pi)
                        if b8 and ((h - b9) < mod_len):
                            fonk1(b6[b9 + 1: h + 1])
                        else:
                            fonk4(b6, b9 + 1, h, pi)
                return b6
            except TypeError:
                print('The list must contain numbers.')
                return None
    else:
        raise TypeError('The function argument must be a list containing numbers.')
if b10 = = "__main__":
    b11 = [3, 1, 7, 2, 9, 5, 4, 8, 6]
    print("Original list:", b11)
    b12 = fonk4(b11, 0, len(b11) - 1, 'first')
    print("Sorted list using Quicksort:", b12)