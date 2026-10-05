def fonk1(lst, target):
    for index, b1 in enumerate(lst):
        if b1 = = target:
            return index
    return -1
def fonk2():
    b2 = input('Enter a list of numbers separated by spaces: ')
    return [int(x) for x in b2.split()]
def fonk3():
    b3 = fonk2()
    b4 = int(input('Enter the number to search for: '))
    b5 = fonk1(b3, b4)
    if b5 < 0:
        print('{} was not found in the list.'.format(b4))
    else:
        print('{} was found at index {}.'.format(b4, b5))
if b6 = = "__main__":
    fonk3()