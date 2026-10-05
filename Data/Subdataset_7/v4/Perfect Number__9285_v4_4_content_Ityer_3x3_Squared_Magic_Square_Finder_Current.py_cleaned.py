import random
import pickle
a1 = 30
a2 = 0
def fonk1():
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    with open("b8.txt", 'rb') as f:
        b8 = pickle.load(f)
    with open("Two.txt", 'rb') as f:
        b2 = pickle.load(f)
    with open("Three.txt", 'rb') as f:
        b3 = pickle.load(f)
    with open("Four.txt", 'rb') as f:
        b4 = pickle.load(f)
    with open("Five.txt", 'rb') as f:
        b5 = pickle.load(f)
    with open("Six.txt", 'rb') as f:
        b6 = pickle.load(f)
    with open("Seven.txt", 'rb') as f:
        b7 = pickle.load(f)
    return b1, b2, b3, b4, b5, b6, b7, b8
def fonk2(a1):
    b9 = []
    for x in ["a","b","c","d","e","f","g","h","b12"]:
        b10 = False
        while b10 = = False:
            globals()[x] = random.randint((a1 * -1), a1)
            if ((globals()[x] in b9) == False) and ((globals()[x] < a1)):
                b9.append(globals()[x])
                b10 = True
    return a, b, c, d, e, f, g, h, b12
def fonk3(lst, lstt, b1, b2, b3, b4, b5, b6, b7, b8, goal):
    a3 = 0
    b11 = max(set(lst), key=lst.count)
    for b12 in lst:
        if b12 = = b11:
            a3 += 1
    if a3 = = 1:
        b1.append(lstt)
    elif a3 = = 2:
        b2.append(lstt)
    elif a3 = = 3:
        b3.append(lstt)
    elif a3 = = 4:
        b4.append(lstt)
    elif a3 = = 5:
        b5.append(lstt)
    elif a3 = = 6:
        b6.append(lstt)
    elif a3 = = 7:
        b7.append(lstt)
    elif a3 = = 8:
        b8.append(lstt)
    print(((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8))), "/", goal)
    return b1, b2, b3, b4, b5, b6, b7, b8
def fonk4(b1, b2, b3, b4, b5, b6, b7, b8, a, b, c, d, e, f, g, h, b12, goal):
    b13 = a * a
    b14 = b * b
    b15 = c * c
    b16 = d * d
    b17 = e * e
    b18 = f * f
    b19 = g * g
    b20 = h * h
    b21 = b12 * b12
    b22 = b13 + b14 + b15
    b23 = b16 + b17 + b18
    b24 = b19 + b20 + b21
    b25 = b13 + b16 + b19
    b26 = b14 + b17 + b20
    b27 = b15 + b18 + b21
    b28 = b13 + b17 + b21
    b29 = b19 + b17 + b15
    b30 = [a, b, c, d, e, f, g, h, b12]
    b31 = [b22, b23, b24, b25, b26, b27, b28, b29]
    b1, b2, b3, b4, b5, b6, b7, b8 = fonk3(b31, b30, b1, b2, b3, b4, b5, b6, b7, b8, goal)
    return b1, b2, b3, b4, b5, b6, b7, b8
def fonk5(b1, b2, b3, b4, b5, b6, b7, b8):
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
    print("b8:")
    print(len(b8))
    print(b8)
    print(a2, "Where dupes")
    print("Saving Results")
    with open("b8.txt", 'wb') as f:
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
def fonk6(L):
    if L:
       L.sort()
       b32 = L[-1]
       for b12 in range(len(L)-2, -1, -1):
           if b32 = = L[b12]:
               del L[b12]
           else:
               b32 = L[b12]
    return L
b1, b2, b3, b4, b5, b6, b7, b8 = fonk1()
b33 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("Don't run too many tests at once, as results are only saved at the end")
b34 = (int(input("There are %s current tests. How many more? " % ("{:,d}".format(b33))))) + b33
b35 = b34 - b33
while ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8))) < b34:
    a, b, c, d, e, f, g, h, b12 = fonk2(a1)
    b1, b2, b3, b4, b5, b6, b7, b8 = fonk4(b1, b2, b3, b4, b5, b6, b7, b8, a, b, c, d, e, f, g, h, b12, b34)
b36 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("Before purification:", "{:,d}".format(b36))
print("Removing squares with 0 matching rows")
b1 = []
b37 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("{:,d}".format(b36 - b37), " Removed")
print("Removing duplicates 1/7")
b2 = fonk6(b2)
b38 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("{:,d}".format(b37 - b38), " Removed")
print("Removing duplicates 2/7")
b3 = fonk6(b3)
b39 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("{:,d}".format(b38 - b39), " Removed")
print("Removing duplicates 3/7")
b4 = fonk6(b4)
b40 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("{:,d}".format(b39 - b40), " Removed")
print("Removing duplicates 4/7")
b5 = fonk6(b5)
b41 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("{:,d}".format(b40 - b41), " Removed")
print("Removing duplicates 5/7")
b6 = fonk6(b6)
b42 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("{:,d}".format(b41 - b42), " Removed")
print("Removing duplicates 6/7")
b7 = fonk6(b7)
b43 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("{:,d}".format(b42 - b43), " Removed")
print("Removing duplicates 7/7")
b8 = fonk6(b8)
b44 = ((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8)))
print("{:,d}".format(b43 - b44), " Removed")
print("Removing duplicates complete")
print("After purification:", "{:,d}".format((len(b1))+(len(b2))+(len(b3))+(len(b4))+(len(b5))+(len(b6))+(len(b7))+(len(b8))))
fonk5(b1, b2, b3, b4, b5, b6, b7, b8)
input("Press enter to close")