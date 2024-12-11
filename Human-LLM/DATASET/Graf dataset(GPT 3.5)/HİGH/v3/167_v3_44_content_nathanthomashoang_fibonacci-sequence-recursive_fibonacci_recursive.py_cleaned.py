def fonk1(index):
    '''Calculate the Fibonacci value recursively.'''
    if index <= 1:
        return index
    return fonk1(index - 2) + fonk1(index - 1)
def fonk2(b2):
    '''Generate the Fibonacci sequence up to the given number of terms.'''
    b1 = []
    for index in range(b2 + 1):
        b1.append(fonk1(index))
    return b1
def fonk3():
    '''Run the Fibonacci program.'''
    while True:
        try:
            b2 = int(input('How many Fibonacci terms would you like to generate?: '))
        except ValueError:
            print('\nPlease enter an integer.')
        else:
            if b2 <= 0:
                print("\nPlease enter a positive integer.")
            else:
                break
    print("\nGenerated Fibonacci sequence:\n")
    b1 = fonk2(b2)
    for term in b1:
        print(term)
if b3 = = "__main__":
    fonk3()