import random
import pickle
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []
b8 = []
a1 = 15
a2 = 100
a3 = 0
def fonk1():
    print("One (may contain duplicates):")
    print(len(b1))
    print("Two:")
    print(len(b2))
    print("Three:")
    print(len(b3))
    print("Four:")
    print(len(b4))
    print("Five:")
    print(len(b5))
    print(b5)
    print("Six:")
    print(len(b6))
    print(b6)
    print("Seven:")
    print(len(b7))
    print(b7)
    print("Win:")
    print(len(b8))
    print(b8)
    print(a3, "/", a2, "Duplicates Removed")
    with open("Win.txt", 'wb') as f:
        pickle.dump(b8, f)
    with open("Two.txt", 'wb') as f:
        pickle.dump(b2, f)
    with open("Three.txt", 'wb') as f:
        pickle.dump(b3, f)
    with open("Four.txt", 'wb') as f:
        pickle.dump(b4, f)
    with open("Five.txt", 'wb') as f:
        pickle.dump(b5, f)
    with open("Six.txt", 'wb') as f:
        pickle.dump(b6, f)
    with open("Seven.txt", 'wb') as f:
        pickle.dump(b7, f)
    with open("Fail.txt", 'wb') as f:
        pickle.dump(b1, f)
def fonk2(lst, lstt):
    a4 = 0
    b9 = max(set(lst), key=lst.count)
    for b10 in lst:
        if b10 = = b9:
            a4 += 1
    if a4 = = 1:
        b1.append(lstt)
    elif a4 = = 2:
        b2.append(lstt)
    elif a4 = = 3:
        b3.append(lstt)
    elif a4 = = 4:
        b4.append(lstt)
    elif a4 = = 5:
        b5.append(lstt)
    elif a4 = = 6:
        b6.append(lstt)
    elif a4 = = 7:
        b7.append(lstt)
    elif a4 = = 8:
        b8.append(lstt)
    print((len(b1)) + (len(b2)) + (len(b3)) + (len(b4)) + (len(b5)) + (len(b6)) + (len(b7)) + (len(b8)))
for _ in range(a2):
    b11 = False
    b12 = []
    for x in ["a", "b", "c", "d", "e", "f", "g", "h", "b10"]:
        while not b11:
            globals()[x] = random.randint((a1 * -1), a1)
            if ((globals()[x] in b12) == False) and ((globals()[x]) < a1):
                b12.append(globals()[x])
                b11 = True
        b11 = False
    if ((([a, b, c, d, e, f, g, h, b10] in b2) == False) and (([a, b, c, d, e, f, g, h, b10] in b3) == False) and (
            ([a, b, c, d, e, f, g, h, b10] in b4) == False) and (([a, b, c, d, e, f, g, h, b10] in b5) == False) and (
            ([a, b, c, d, e, f, g, h, b10] in b6) == False) and (([a, b, c, d, e, f, g, h, b10] in b7) == False) and (
            ([a, b, c, d, e, f, g, h, b10] in b8) == False)):
        b13 = a * a
        b14 = b * b
        b15 = c * c
        b16 = d * d
        b17 = e * e
        b18 = f * f
        b19 = g * g
        b20 = h * h
        b21 = b10 * b10
        b22 = b13 + b14 + b15
        b23 = b16 + b17 + b18
        b24 = b19 + b20 + b21
        b25 = b13 + b16 + b19
        b26 = b14 + b17 + b20
        b27 = b15 + b18 + b21
        b28 = b13 + b17 + b21
        b29 = b19 + b17 + b15
        b30 = [a, b, c, d, e, f, g, h, b10]
        b31 = [b22, b23, b24, b25, b26, b27, b28, b29]
        fonk2(b31, b30)
    else:
        print("Duplicate Found")
        a3 += 1
fonk1()