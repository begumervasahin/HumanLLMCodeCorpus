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
    with open("Win.txt", 'rb') as f:
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
    for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "b13"]:
        b10 = False
        while not b10:
            b11 = random.randint((a1 * -1), a1)
            if (b11 not in b9) and (b11 < a1):
                b9.append(b11)
                b10 = True
    return b9
def fonk3(answers, b22, b24, b2, b3, b4, b5, b6, b7, b8, goal):
    a3 = 0
    b12 = max(set(answers), key=answers.count)
    for b13 in answers:
        if b13 = = b12:
            a3 += 1
    if a3 = = 1:
        b24.append(b22)
    elif a3 = = 2:
        b2.append(b22)
    elif a3 = = 3:
        b3.append(b22)
    elif a3 = = 4:
        b4.append(b22)
    elif a3 = = 5:
        b5.append(b22)
    elif a3 = = 6:
        b6.append(b22)
    elif a3 = = 7:
        b7.append(b22)
    elif a3 = = 8:
        b8.append(b22)
    print(((len(b24)) + (len(b2)) + (len(b3)) + (len(b4)) + (len(b5)) + (len(b6)) + (len(b7)) + (len(b8))), "/", goal)
    return b24, b2, b3, b4, b5, b6, b7, b8
def fonk4(b24, b2, b3, b4, b5, b6, b7, b8, *b22, goal):
    b14 = [b11 ** 2 for b11 in b22]
    b15 = [b14[0] + b14[1] + b14[2], b14[3] + b14[4] + b14[5], b14[6] + b14[7] + b14[8]]
    b16 = [b14[0] + b14[3] + b14[6], b14[1] + b14[4] + b14[7], b14[2] + b14[5] + b14[8]]
    b17 = [b14[0] + b14[4] + b14[8], b14[6] + b14[4] + b14[2]]
    b24, b2, b3, b4, b5, b6, b7, b8 = fonk3(b15 + b16 + b17, b22, b24, b2, b3, b4, b5, b6, b7, b8, goal)
    return b24, b2, b3, b4, b5, b6, b7, b8
def fonk5(lst):
    if lst:
        lst.sort()
        b18 = lst[-1]
        for b13 in range(len(lst) - 2, -1, -1):
            if b18 = = lst[b13]:
                del lst[b13]
            else:
                b18 = lst[b13]
    return lst
def fonk6(b24, b2, b3, b4, b5, b6, b7, b8):
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
    print(a2, "Duplicates Removed")
    print("Saving Results")
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
b24, b2, b3, b4, b5, b6, b7, b8 = fonk1()
b19 = ((len(b24)) + (len(b2)) + (len(b3)) + (len(b4)) + (len(b5)) + (len(b6)) + (len(b7)) + (len(b8)))
print("Don't run too many tests at once, as b24 are only saved at the end")
b20 = (int(input("There are %s current tests. How many more? " % ("{:,d}".format(b19))))) + b19
b21 = b20 - b19
while ((len(b24)) + (len(b2)) + (len(b3)) + (len(b4)) + (len(b5)) + (len(b6)) + (len(b7)) + (len(b8))) < b20:
    b22 = fonk2(a1)
    b24, b2, b3, b4, b5, b6, b7, b8 = fonk4(b24, b2, b3, b4, b5, b6, b7, b8, *b22, goal=b20)
b23 = ((len(b24)) + (len(b2)) + (len(b3)) + (len(b4)) + (len(b5)) + (len(b6)) + (len(b7)) + (len(b8)))
print("Before purification:", "{:,d}".format(b23))
b24 = []
b2 = fonk5(b2)
b3 = fonk5(b3)
b4 = fonk5(b4)
b5 = fonk5(b5)
b6 = fonk5(b6)
b7 = fonk5(b7)
b8 = fonk5(b8)
b25 = ((len(b24)) + (len(b2)) + (len(b3)) + (len(b4)) + (len(b5)) + (len(b6)) + (len(b7)) + (len(b8)))
print("After purification:", "{:,d}".format(b25))
fonk6(b24, b2, b3, b4, b5, b6, b7, b8)
input("Press enter to close")