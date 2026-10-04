import time
import math
def fonk1(lst, b3):
    if len(lst) == 0:
        return False
    else:
        b1 = len(lst)
        if lst[b1] == b3:
            return True
        else:
            if lst[b1] < b3:
                return fonk1(lst[b1+1:], b3)
            else:
                return fonk1(lst[:b1], b3)
def fonk2(lst, b3):
    a1 = 0
    b2 = len(lst) - 1
    while a1 <= b2:
        b1 = (a1 + b2)
        if lst[b1] == b3:
            return b1
        elif lst[b1] < b3:
            a1 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(lst, b3):
    for i in range(len(lst)):
        if b3 = = lst[i]:
            return i
    return None
def fonk4():
    for i in range(10, 19):
        b4 = range(int(math.pow(10, i)))
        b5 = int(math.pow(10, i)) - 3
        b6 = ""
        b6 += str(len(b4))
        b6 += ";"
        print("")
        b7 = '-> Quantity: %s (10 to the power of %s)' % (b5 + 3, i)
        print(b7)
        print("Linear search: ", "null")
        b6 += "null"
        b6 += ";"
        b8 = time.time()
        print(fonk2(b4, b5))
        b9 = time.time() - b8
        print("Binary search: ", b9)
        b6 += str(b9)
        b6 += ";"
        b8 = time.time()
        print(fonk1(b4, b5))
        b9 = time.time() - b8
        print("Recursive binary search: ", b9)
        b6 += str(b9)
        with open("data.csv", "a") as file:
            file.write(b6 + "\n")
fonk4()