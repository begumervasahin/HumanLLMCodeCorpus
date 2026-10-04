def fonk1(b4, b6, b7):
    b1 = []
    for num in b4:
        b2 = sum(1 for divisor in b6 if num % divisor == 0)
        if b2 >= b7:
            b1.append(num)
    b1 = list(set(b1))
    print(b1)
def fonk2():
    b3 = input("Enter a list of numbers separated by a space: ")
    b4 = list(map(int, b3.split()))
    b5 = input("Enter a list of numbers separated by a space: ")
    b6 = list(map(int, b5.split()))
    b7 = len(b6)
    fonk1(b4, b6, b7)
    input("Press any key to exit ")
if b8 = = "__main__":
    fonk2()