def fonk1(b1):
    if b1 = = 0:
        return 0
    elif b1 = = 1:
        return 1
    else:
        return fonk1(b1 - 1) + fonk1(b1 - 2)
def fonk2(b3):
    if b3 <= 0:
        print("Please enter a positive integer.")
    else:
        print("The Fibonacci sequence with", b3, "elements is:")
        for i in range(b3):
            print(fonk1(i), b2 = " ")
def fonk3():
    while True:
        try:
            b3 = int(input('\nEnter a positive number to generate the Fibonacci sequence with that number of elements: '))
            fonk2(b3)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
if b4 = = '__main__':
    fonk3()