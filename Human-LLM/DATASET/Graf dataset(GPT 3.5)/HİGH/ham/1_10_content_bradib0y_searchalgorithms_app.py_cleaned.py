import time
import math
def fonk1(list, b3):
    if len(list) == 0:
        return False
    else:
        b1 = (len(list))
        if list[b1] == b3:
            return True
        else:
            if list[b1] < b3:
                return fonk1(list[b1+1:], b3)
            else:
                return fonk1(list[:b1], b3)
def fonk2(list, b3):
    a1 = 0
    b2 = len(list) -1
    while a1 <= b2:
        b1 = (a1 + b2)
        if list[b1] == b3:
            return b1
        elif list[b1]<b3:
            a1 = b1 +1
        else:
            b2 = b1 -1
    return None
def fonk3(list, b3):
    for i in range(0, len(list)):
        if b3 = = list[i]:
            return i
    return None
def fonk4():
    for i in range(10, 19):
        b4 = range(0, int(math.pow(10, i)))
        b5 = (int(math.pow(10, i)) - 3)
        b6 = ""
        b6 += (str)(len(b4))
        b6 += ";"
        print("")
        b7 = '-> Quantity: %s (10 to the power of %s)' % (b5 + 3, i)
        print(b7)
        print("Linear search: " , "null")
        b6 += "null"
        b6 += ";"
        b8 = time.time()
        print(fonk2(b4, b5))
        b9 = time.time() - b8
        print("Binary search: " , b9)
        b6 += (str)(b9)
        b6 += ";"
        b8 = time.time()
        print(fonk1(b4, b5))
        b9 = time.time() - b8
        print("Recursive binary search: " , b9)
        b6 += (str)(b9)
        b10 = open("data.csv", "a")
        b10.write(b6 + "\n")
        b10.close()
fonk4()