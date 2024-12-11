def fonk1(lst, target):
    for index, b1 in enumerate(lst):
        if b1 = = target:
            return index
    return -1
b2 = input('Enter a list of numbers separated by spaces: ')
b3 = [int(x) for x in b2.split()]
b4 = int(input('Enter the number to search for: '))
b5 = fonk1(b3, b4)
if b5 < 0:
    print(f'The number {b4} was not found in the list.')
else:
    print(f'The number {b4} was found at index {b5}.')