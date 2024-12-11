def fonk1(alist, key):
    for i, b1 in enumerate(alist):
        if b1 = = key:
            return i
    return -1
b2 = input('Enter a list of numbers separated by spaces: ')
b3 = [int(x) for x in b2.split()]
b4 = int(input('Enter the number to search for: '))
b5 = fonk1(b3, b4)
if b5 < 0:
    print(f'{b4} was not found in the list.')
else:
    print(f'{b4} was found at index {b5}.')