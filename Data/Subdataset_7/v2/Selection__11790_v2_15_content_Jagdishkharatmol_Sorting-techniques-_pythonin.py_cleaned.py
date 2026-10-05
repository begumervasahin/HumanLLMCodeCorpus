import time
def fonk1():
    print('_' * 80)
def fonk2(string):
    fonk1()
    print(string.center(80))
    fonk1()
def fonk3(b9):
    for j in range(len(b9) - 1, 0, -1):
        for b6 in range(j):
            if b9[b6] > b9[b6 + 1]:
                b9[b6], b9[b6 + 1] = b9[b6 + 1], b9[b6]
def fonk4(b9):
    for b6 in range(1, len(b9)):
        b1 = b9[b6]
        b2 = b6
        while b2 > 0 and b9[b2 - 1] > b1:
            b9[b2] = b9[b2 - 1]
            b2 -= 1
        b9[b2] = b1
def fonk5(alist):
    if len(alist) > 1:
        b3 = len(alist)
        b4 = alist[:b3]
        b5 = alist[b3:]
        fonk5(b4)
        fonk5(b5)
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
def fonk6(b9):
    for fillslot in range(len(b9) - 1, 0, -1):
        a1 = 0
        for location in range(1, fillslot + 1):
            if b9[location] > b9[a1]:
                a1 = location
        b9[fillslot], b9[a1] = b9[a1], b9[fillslot]
fonk1()
print()
fonk2("Sorting Techniques on Dataset")
while True:
    print("Enter:")
    print("1 for Bubble Sort")
    print("2 for Insertion Sort")
    print("3 for Merge Sort")
    print("4 for Selection Sort")
    b7 = int(input("\nEnter your b7: "))
    b8 = time.time()
    b9 = []
    b10 = int(input("\nHow many numbers do you want to enter: "))
    for b6 in range(b10):
        b11 = int(input("Enter the number: "))
        b9.append(b11)
    if b7 = = 1:
        fonk3(b9)
        print("\nThe list after Bubble Sorting is:", b9)
    elif b7 = = 2:
        fonk4(b9)
        print("\nThe list after Insertion Sorting is:", b9)
    elif b7 = = 3:
        fonk5(b9)
        print("\nThe list after Merge Sorting is:", b9)
    elif b7 = = 4:
        fonk6(b9)
        print("\nThe list after Selection Sorting is:", b9)
    b12 = time.time()
    print("Time taken by the sorting process:", b12 - b8)
    b13 = int(input("\nEnter 1 to continue and 0 to exit: "))
    print("\b10\b10")
    if b13 = = 0:
        break