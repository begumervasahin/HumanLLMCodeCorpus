def fonk1(b2):
    '''
    Sorts a list of numbers using the Bubble Sort algorithm.
    '''
    b1 = len(b2)
    for i in range(b1 - 1, 0, -1):
        for j in range(i):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
        print(b2)
def fonk2():
    b2 = [5, 3, 8, 6, 7, 2]
    print("Unsorted b3 = ", b2)
    fonk1(b2)
    print("Sorted b3 = ", b2)
if b4 = = "__main__":
    fonk2()