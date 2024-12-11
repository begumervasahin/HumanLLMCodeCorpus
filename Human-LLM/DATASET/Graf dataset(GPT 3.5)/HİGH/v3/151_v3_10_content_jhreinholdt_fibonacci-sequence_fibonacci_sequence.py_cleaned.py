def fonk1(b1):
    if b1 = = 0:
        return 0
    elif b1 = = 1:
        return 1
    else:
        return fonk1(b1 - 2) + fonk1(b1 - 1)
def fonk2(b4):
    if b4 <= 0:
        print("Please enter a positive integer.")
        return
    print("The Fibonacci Sequence with", b4, "elements is:")
    for b1 in range(b4):
        print(fonk1(b1), b2 = " ")
def fonk3(prompt):
    while True:
        try:
            b3 = int(input(prompt))
            if b3 <= 0:
                print("Please enter a positive integer.")
            else:
                return b3
        except ValueError:
            print("Please enter a valid positive integer.")
def fonk4():
    b4 = fonk3('\nEnter a positive number to generate the Fibonacci Sequence with that amount of elements: ')
    fonk2(b4)
if b5 = = '__main__':
    fonk4()