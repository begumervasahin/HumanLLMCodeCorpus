import random
def fonk1(b5):
    '''Insertion sort algorithm.'''
    if not isinstance(b5, list):
        raise TypeError('The function argument must be a list containing numbers.')
    if len(b5) < 2:
        return b5
    for b6 in range(1, len(b5)):
        b1 = b5[b6]
        b2 = b6 - 1
        while b2 >= 0 and b5[b2] > b1:
            b5[b2 + 1] = b5[b2]
            b2 -= 1
        b5[b2 + 1] = b1
    return b5
def fonk2(b5, low, high, pivot_choice):
    '''Chooses the reference element and moves it to the last place in the list.'''
    b3 = {'first': low, 'last': high, 'middle': (low + high)
    b4 = b5[b3[pivot_choice]]
    b5[b3[pivot_choice]], b5[high] = b5[high], b5[b3[pivot_choice]]
    return b4, b5
def fonk3(b5, low, high, pivot_choice):
    '''Places the reference element in its correct position in the sorted list.'''
    b4, b5 = fonk2(b5, low, high, pivot_choice)
    b6 = low - 1
    for b2 in range(low, high):
        if b5[b2] <= b4:
            b6 += 1
            b5[b6], b5[b2] = b5[b2], b5[b6]
    b5[b6 + 1], b5[high] = b5[high], b5[b6 + 1]
    return b6 + 1
def fonk4(b5, low, high, pivot_choice, b7 = False, mod_length=10):
    '''Recursive version of the Quicksort algorithm.'''
    if not isinstance(b5, list):
        raise TypeError('The function argument must be a list containing numbers.')
    if len(b5) < 2:
        return b5
    if low < high:
        if b7 and ((high - low) < mod_length):
            b5[low:high + 1] = fonk1(b5[low:high + 1])
        else:
            try:
                b8 = fonk3(b5, low, high, pivot_choice)
            except KeyError:
                print('Pivot options: first, last, middle, random.')
                return None
            if b7 and ((b8 - low) < mod_length):
                b5[low:b8] = fonk1(b5[low:b8])
            else:
                fonk4(b5, low, b8 - 1, pivot_choice, b7, mod_length)
            if b7 and ((high - b8) < mod_length):
                b5[b8 + 1:high + 1] = fonk1(b5[b8 + 1:high + 1])
            else:
                fonk4(b5, b8 + 1, high, pivot_choice, b7, mod_length)
    return b5