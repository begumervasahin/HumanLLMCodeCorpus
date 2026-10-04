
def fonk1(num):
    if num <= 1:
        return num
    return fonk1(num - 2) + fonk1(num - 1)
def fonk2():
    while True:
        try:
            b1 = int(input('Up to how many terms to return Fibonacci?: '))
            if b1 <= 0:
                print("\nPlease enter a positive integer.")
            else:
                break
        except ValueError:
            print('\nPlease only input an integer.')
    print("\nFibonacci sequence:\n")
    for num in range(b1 + 1):
        print(fonk1(num))
if b2 = = "__main__":
    fonk2()