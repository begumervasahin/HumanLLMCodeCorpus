
def fonk1(b1):
    if b1 = = 0:
        return 0
    elif b1 = = 1:
        return 1
    else:
        return fonk1(b1 - 2) + fonk1(b1 - 1)
def fonk2(b3):
    if b3 <= 0:
        print("Please enter a positive integer.")
        return
    print(f"The Fibonacci Sequence with {b3} elements is:")
    for k in range(b3):
        print(fonk1(k), b2 = " ")
    print()
def fonk3():
    while True:
        try:
            b3 = int(input('\nEnter a positive number to generate the Fibonacci Sequence with that number of elements: '))
            fonk2(b3)
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
if b4 = = '__main__':
    fonk3()