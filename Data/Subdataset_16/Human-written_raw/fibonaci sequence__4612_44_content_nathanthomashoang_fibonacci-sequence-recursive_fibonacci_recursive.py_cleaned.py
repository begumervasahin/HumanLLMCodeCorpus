
def fonk1(num):
    '''function to return fibonacci value'''
    if num <= 1:
        return num
    return fonk1(num-2) + fonk1(num-1)
def fonk2():
    '''to run program'''
    while True:
        try:
            b1 = int(input('Up to how many terms to return fibonacci?: '))
        except ValueError:
            print('\nPlease only input an integer.')
        else:
            if b1 <= 0:
                print("\nPlease enter a positive integer")
            else:
                break
    print("\nFibonacci sequence:\n")
    for num in range(b1 + 1):
        print(fonk1(num))
fonk2()