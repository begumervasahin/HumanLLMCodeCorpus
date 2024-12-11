from random import randint
def fonk1(b6):
    for index in range(1, len(b6)):
        b1 = b6[index]
        b2 = index
        while b2 > 0 and b6[b2 - 1] > b1:
            b6[b2] = b6[b2 - 1]
            b2 -= 1
        b6[b2] = b1
    return b6
def fonk2():
    b3 = []
    b4 = int(input("Enter the number of elements: "))
    for _ in range(b4):
        b5 = randint(1, 100)
        if b5 not in b3:
            b3.append(b5)
    return b3
def fonk3():
    b6 = fonk2()
    print("List to be sorted using INSERTION SORT:", b6)
    b7 = fonk1(b6.copy())
    print("Final Sorted List:", b7)
if b8 = = "__main__":
    fonk3()