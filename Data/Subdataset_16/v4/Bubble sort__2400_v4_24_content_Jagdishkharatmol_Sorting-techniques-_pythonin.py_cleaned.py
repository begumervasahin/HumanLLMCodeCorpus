import time
def fonk1(b9):
    for j in range(len(b9)-1, 0, -1):
        for b6 in range(j):
            if b9[b6] > b9[b6+1]:
                b9[b6], b9[b6+1] = b9[b6+1], b9[b6]
def fonk2(b9):
    for b6 in range(1, len(b9)):
        b1 = b9[b6]
        b2 = b6
        while b2 > 0 and b9[b2-1] > b1:
            b9[b2] = b9[b2-1]
            b2 -= 1
        b9[b2] = b1
def fonk3(alist):
    if len(alist) > 1:
        b3 = len(alist)
        b4 = alist[:b3]
        b5 = alist[b3:]
        fonk3(b4)
        fonk3(b5)
        b6 = j = k = 0
        while b6 < len(b4) and j < len(b5):
            if b4[b6] < b5[j]:
                alist[k] = b4[b6]
                b6 += 1
            else:
                alist[k] = b5[j]
                j += 1
            k += 1
        while b6 < len(b4):
            alist[k] = b4[b6]
            b6 += 1
            k += 1
        while j < len(b5):
            alist[k] = b5[j]
            j += 1
            k += 1
def fonk4(b9):
    for fillslot in range(len(b9)-1, 0, -1):
        a1 = 0
        for location in range(1, fillslot+1):
            if b9[location] > b9[a1]:
                a1 = location
        b9[fillslot], b9[a1] = b9[a1], b9[fillslot]
def fonk5():
    b7 = '_' * 80
    print(f"{b7}\b10")
    print("Sort techniques on dataset".center(80))
    print(f"\b10{b7}\b10\b10")
    while True:
        print("Enter \b10 1 for bubble sort \b10 2 for insertion sort \b10 3 for merge sort \b10 4 for selection sort")
        b8 = int(input("\b10 Enter the b8: "))
        if b8 in {1, 2, 3, 4}:
            b9 = []
            b10 = int(input("\b10 How many numbers do you want to enter: "))
            for _ in range(b10):
                b11 = int(input(" Enter the number: "))
                b9.append(b11)
            b12 = time.time()
            if b8 = = 1:
                fonk1(b9)
                print("\b10 The list after bubble sorting is {}".format(b9))
            elif b8 = = 2:
                fonk2(b9)
                print("\b10 The list after insertion sorting is {}".format(b9))
            elif b8 = = 3:
                fonk3(b9)
                print("\b10 The list after merge sorting is {}".format(b9))
            elif b8 = = 4:
                fonk4(b9)
                print("\b10 The list after selection sorting is {}".format(b9))
            b13 = time.time()
            print(" The time taken by sorting process: {:.5f} seconds".format(b13 - b12))
        else:
            print("Invalid b8. Please try again.")
        b14 = int(input(" Enter 1 to continue and 0 to exit: "))
        if b14 = = 0:
            break
if b15 = = "__main__":
    fonk5()