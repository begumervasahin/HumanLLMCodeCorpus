def fonk1(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
b1 = input('Enter a list of numbers separated by spaces: ')
b2 = b1.split()
b2 = [int(x) for x in b2]
b3 = int(input('Enter the number to search for: '))
b4 = fonk1(b2, b3)
if b4 < 0:
    print('{} was not found in the list.'.format(b3))
else:
    print('{} was found at index {}.'.format(b3, b4))