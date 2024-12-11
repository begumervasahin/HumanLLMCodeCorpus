from random import randint
import array
def fonk1(b8):
    for index in range(1, len(b8)):
        b1 = b8[index]
        b2 = index
        while b2 > 0 and b8[b2-1] > b1:
            print("Swapped {} for {}".format(b8[b2], b8[b2-1]))
            b8[b2] = b8[b2-1]
            print(b8)
            print("===================================================================================================")
            b2 -= 1
        b8[b2] = b1
    return b8
def fonk2():
    b3 = []
    b4 = input("Banyak nya list : ")
    b5 = int(b4)
    for x in range (b5):
        b6 = randint(1 , 100)
        if b6 in b3 :
            continue
        b7 = int(b6)
        b3.append(b7)
    b8 = b3
    return b8
b8 = fonk2()
print("List yang akan di sorted menggunakan metode INSERTION SORT adalah : {}".format(b8))
fonk1(b8)
print("Final Sorted List : {}".format(b8))