import time
def fonk1():
    print('_' * 80)
def fonk2(string):
    fonk1()
    print(string.center(80))
    fonk1()
def fonk3(b9):
    for a2 in range(len(b9) - 1, 0, -1):
        for a1 in range(a2):
            if b9[a1] > b9[a1 + 1]:
                b1 = b9[a1]
                b9[a1] = b9[a1 + 1]
                b9[a1 + 1] = b1
def fonk4(b9):
    for a1 in range(1, len(b9)):
        b2 = b9[a1]
        b3 = a1
        while b3 > 0 and b9[b3 - 1] > b2:
            b9[b3] = b9[b3 - 1]
            b3 = b3 - 1
        b9[b3] = b2
def fonk5(alist):
    if len(alist) > 1:
        b4 = len(alist)
        b5 = alist[:b4]
        b6 = alist[b4:]
        fonk5(b5)
        fonk5(b6)
        a1 = 0
        a2 = 0
        a3 = 0
        while a1 < len(b5) and a2 < len(b6):
            if b5[a1] < b6[a2]:
                alist[a3] = b5[a1]
                a1 = a1 + 1
            else:
                alist[a3] = b6[a2]
                a2 = a2 + 1
            a3 = a3 + 1
        while a1 < len(b5):
            alist[a3] = b5[a1]
            a1 = a1 + 1
            a3 = a3 + 1
        while a2 < len(b6):
            alist[a3] = b6[a2]
            a2 = a2 + 1
            a3 = a3 + 1
def fonk6(b9):
    for fillslot in range(len(b9) - 1, 0, -1):
        a4 = 0
        for location in range(1, fillslot + 1):
            if b9[location] > b9[a4]:
                a4 = location
        b1 = b9[fillslot]
        b9[fillslot] = b9[a4]
        b9[a4] = b1
fonk1()
print()
fonk2("Sort techniques on dataset")
while True:
    print("Enter:")
    print("1 for bubble sort")
    print("2 for insertion sort")
    print("3 for merge sort")
    print("4 for selection sort")
    b7 = int(input("\nEnter your b7: "))
    b8 = time.time()
    b9 = []
    b10 = int(input("\nHow many numbers do you want to enter: "))
    for a1 in range(b10):
        b11 = int(input("Enter the number: "))
        b9.append(b11)
    if b7 = = 1:
        fonk3(b9)
        print("\nThe list after bubble sorting is:", b9)
    elif b7 = = 2:
        fonk4(b9)
        print("\nThe list after insertion sorting is:", b9)
    elif b7 = = 3:
        fonk5(b9)
        print("\nThe list after merge sorting is:", b9)
    elif b7 = = 4:
        fonk6(b9)
        print("\nThe list after selection sorting is:", b9)
    b12 = time.time()
    print("The time taken by sorting process:", b12 - b8)
    b13 = int(input("\nEnter 1 to continue and 0 to exit: "))
    print("\b10\b10")
    if b13 = = 0:
        break