
def fonk1(b1):
    if b1 = = 0:
        return 0
    elif b1 = = 1:
        return 1
    else:
        return (fonk1(b1 - 2) + fonk1(b1 - 1))
def fonk2(number):
    if number <= 0:
        return print("Please enter a positive integer")
    else:
        print("The Fibonacci Sequence with", number, "elements is:")
        for k in range(number):
            print(fonk1(k),"",b2 = "")
def fonk3():
    while True:
        fonk2(int(input('\nEnter a positive number to generate the Fibonacci Sequence with that amount of elements: ')))
if b3 = = '__main__':
    fonk3()