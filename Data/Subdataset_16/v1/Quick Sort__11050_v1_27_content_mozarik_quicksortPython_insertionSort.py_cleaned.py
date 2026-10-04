from random import randint
def fonk1(b7):
    for index in range(1, len(b7)):
        b1 = b7[index]
        b2 = index
        while b2 > 0 and b7[b2 - 1] > b1:
            print("Swapped {} for {}".format(b7[b2], b7[b2 - 1]))
            b7[b2] = b7[b2 - 1]
            print(b7)
            print("===================================================================================================")
            b2 -= 1
        b7[b2] = b1
    return b7
def fonk2():
    b3 = []
    b4 = input("Banyaknya list: ")
    b5 = int(b4)
    while len(b3) < b5:
        b6 = randint(1, 100)
        if b6 not in b3:
            b3.append(b6)
    return b3
def fonk3():
    b7 = fonk2()
    print("List yang akan di sorted menggunakan metode INSERTION SORT adalah : {}".format(b7))
    b8 = fonk1(b7)
    print("Final Sorted List : {}".format(b8))
if b9 = = "__main__":
    fonk3()