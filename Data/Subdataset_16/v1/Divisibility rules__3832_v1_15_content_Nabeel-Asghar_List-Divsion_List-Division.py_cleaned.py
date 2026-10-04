def fonk1(b4, b6, b7):
    b1 = []
    for i in b4:
        a1 = 0
        for b2 in b6:
            if i % b2 = = 0:
                a1 += 1
        if a1 >= b7:
            b1.append(i)
    b1 = set(b1)
    print(b1)
b3 = input("Enter a list of numbers separated by a space: ")
b4 = list(map(int, b3.split()))
b5 = input("Enter a list of numbers separated by a space: ")
b6 = list(map(int, b5.split()))
b7 = len(b6)
fonk1(b4, b6, b7)
input("Press any key to exit ")