def fonk1(b1):
    '''
    Sorts a list of numbers using the Bubble Sort algorithm.
    '''
    for i in range(len(b1) - 1, 0, -1):
        for j in range(i):
            if b1[j] > b1[j + 1]:
                b1[j], b1[j + 1] = b1[j + 1], b1[j]
        print(b1)
b1 = [5, 3, 8, 6, 7, 2]
print("Unsorted b2 = ", b1)
fonk1(b1)
print("Sorted b2 = ", b1)