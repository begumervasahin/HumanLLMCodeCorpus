def fonk1(alist, b2):
    for i in range(len(alist)):
        if alist[i] == b2:
            return i
    return -1
b1 = input('Enter the list of numbers: ')
b1 = b1.split()
b1 = [int(x) for x in alist]
b2 = int(input('The number to search for: '))
b3 = fonk1(b1, b2)
if b3 < 0:
    print('{} was not found.'.format(b2))
else:
    print('{} was found at b3 {}.'.format(b2, b3))