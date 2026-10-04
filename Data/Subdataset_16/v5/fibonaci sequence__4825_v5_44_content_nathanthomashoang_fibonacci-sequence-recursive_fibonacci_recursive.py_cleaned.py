
def fonk1(num):
    if num <= 1:
        return num
    return fonk1(num - 2) + fonk1(num - 1)
def fonk2(prompt):
    while True:
        try:
            b1 = int(input(prompt))
            if b1 > 0:
                return b1
            else:
                print("\nPlease enter a positive integer.")
        except ValueError:
            print("\nPlease only input an integer.")
def fonk3(b2):
    print("\nFibonacci sequence:")
    for num in range(b2 + 1):
        print(fonk1(num))
def fonk4():
    b2 = fonk2('Up to how many b2 to return Fibonacci?: ')
    fonk3(b2)
if b3 = = "__main__":
    fonk4()