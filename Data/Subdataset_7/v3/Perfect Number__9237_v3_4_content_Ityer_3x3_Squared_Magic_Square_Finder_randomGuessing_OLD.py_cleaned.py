import random
import pickle
b1 = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: []
}
a1 = 15
a2 = 100
a3 = 0
def fonk1():
    print("One (may contain duplicates):")
    print(len(b1[1]))
    for i in range(2, 8):
        print(f"{i}:")
        print(len(b1[i]))
        print(b1[i])
    print("Win:")
    print(len(b1[8]))
    print(b1[8])
    print(f"{a3} Duplicates Removed")
def fonk2():
    with open("Win.txt", 'wb') as f:
        pickle.dump(b1[8], f)
    for i in range(2, 8):
        b2 = f"{i}.txt"
        with open(b2, 'wb') as f:
            pickle.dump(b1[i], f)
    with open("Fail.txt", 'wb') as f:
        pickle.dump(b1[1], f)
def fonk3(b11, b5):
    b3 = b11.count(max(b11, key=b11.count))
    b1[b3].append(b5)
    print(sum(len(b1[i]) for i in range(1, 9)))
def fonk4():
    global a3
    for _ in range(a2):
        b4 = False
        b5 = []
        for _ in range(9):
            while not b4:
                b6 = random.randint((a1 * -1), a1)
                if (b6 not in b5) and (b6 < a1):
                    b5.append(b6)
                    b4 = True
            b4 = False
        if b5 not in b1.values():
            b7 = [b6 ** 2 for b6 in b5]
            b8 = [sum(b7[i:i+3]) for i in range(0, len(b7), 3)]
            b9 = [sum(b7[i::3]) for i in range(3)]
            b10 = [sum(b7[::4]), sum(b7[2:7:2])]
            b11 = b8 + b9 + b10
            fonk3(b11, b5)
        else:
            print("Duplicate Found")
            a3 += 1
if b12 = = "__main__":
    fonk4()
    fonk1()
    fonk2()