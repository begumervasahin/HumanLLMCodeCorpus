def fonk1(num):
    '''Calculate the Fibonacci value recursively.'''
    if num <= 1:
        return num
    return fonk1(num - 2) + fonk1(num - 1)
def fonk2():
    '''Run the Fibonacci program.'''
    while True:
        try:
            b1 = int(input('How many Fibonacci terms would you like to generate?: '))
        except ValueError:
            print('\nPlease enter an integer.')
        else:
            if b1 <= 0:
                print("\nPlease enter a positive integer.")
            else:
                break
    print("\nGenerated Fibonacci sequence:\n")
    for num in range(b1 + 1):
        print(fonk1(num))
if b2 = = "__main__":
    fonk2()