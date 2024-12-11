
def fonk1(b1):
    if b1 = = 0:
        return 0
    elif b1 = = 1:
        return 1
    else:
        return fonk1(b1 - 2) + fonk1(b1 - 1)
def fonk2(b3):
    if b3 <= 0:
        print("Please enter a positive integer")
    else:
        print("The Fibonacci Sequence with", b3, "elements is:")
        for b1 in range(b3):
            print(fonk1(b1), "", b2 = "")
def fonk3():
    while True:
        try:
            b3 = int(input('\nEnter a positive number to generate the Fibonacci Sequence with that amount of elements: '))
            fonk2(b3)
            break
        except ValueError:
            print("Please enter a valid positive integer.")
if b4 = = '__main__':
    fonk3()