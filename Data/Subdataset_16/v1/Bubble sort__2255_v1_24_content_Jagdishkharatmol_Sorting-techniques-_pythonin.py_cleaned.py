import time
def fonk1(b9):
    for a2 in range(len(b9) - 1, 0, -1):
        for a1 in range(a2):
            if b9[a1] > b9[a1 + 1]:
                b9[a1], b9[a1 + 1] = b9[a1 + 1], b9[a1]
def fonk2(b9):
    for a1 in range(1, len(b9)):
        b1 = b9[a1]
        b2 = a1
        while b2 > 0 and b9[b2 - 1] > b1:
            b9[b2] = b9[b2 - 1]
            b2 = b2 - 1
        b9[b2] = b1
def fonk3(alist):
    if len(alist) > 1:
        b3 = len(alist)
        b4 = alist[:b3]
        b5 = alist[b3:]
        fonk3(b4)
        fonk3(b5)
        a1 = 0
        a2 = 0
        a3 = 0
        while a1 < len(b4) and a2 < len(b5):
            if b4[a1] < b5[a2]:
                alist[a3] = b4[a1]
                a1 = a1 + 1
            else:
                alist[a3] = b5[a2]
                a2 = a2 + 1
            a3 = a3 + 1
        while a1 < len(b4):
            alist[a3] = b4[a1]
            a1 = a1 + 1
            a3 = a3 + 1
        while a2 < len(b5):
            alist[a3] = b5[a2]
            a2 = a2 + 1
            a3 = a3 + 1
def fonk4(b9):
    for fillslot in range(len(b9) - 1, 0, -1):
        a4 = 0
        for location in range(1, fillslot + 1):
            if b9[location] > b9[a4]:
                a4 = location
        b9[fillslot], b9[a4] = b9[a4], b9[fillslot]
def fonk5():
    b6 = '_' * 80
    print(f"{b6}\b10")
    b7 = "Sort techniques on dataset"
    print(b7.center(80))
    print(f"\b10{b6}\b10\b10")
    while True:
        print("Enter \b10 1 for Bubble Sort \b10 2 for Insertion Sort \b10 3 for Merge Sort \b10 4 for Selection Sort")
        b8 = int(input("\nEnter your choice: "))
        b9 = []
        b10 = int(input("\nHow many numbers do you want to enter: "))
        for a1 in range(b10):
            b11 = int(input("Enter the number: "))
            b9.append(b11)
        if b8 = = 1:
            b12 = time.time()
            fonk1(b9)
            b13 = time.time()
            print("\nThe list after Bubble Sorting is: {}".format(b9))
            print("The time taken by the sorting process: {:.6f} seconds".format(b13 - b12))
        elif b8 = = 2:
            b12 = time.time()
            fonk2(b9)
            b13 = time.time()
            print("\nThe list after Insertion Sorting is: {}".format(b9))
            print("The time taken by the sorting process: {:.6f} seconds".format(b13 - b12))
        elif b8 = = 3:
            b12 = time.time()
            fonk3(b9)
            b13 = time.time()
            print("\nThe list after Merge Sorting is: {}".format(b9))
            print("The time taken by the sorting process: {:.6f} seconds".format(b13 - b12))
        elif b8 = = 4:
            b12 = time.time()
            fonk4(b9)
            b13 = time.time()
            print("\nThe list after Selection Sorting is: {}".format(b9))
            print("The time taken by the sorting process: {:.6f} seconds".format(b13 - b12))
        else:
            print("Invalid choice! Please enter a valid option.")
        b10 = int(input("\nEnter 1 to continue and 0 to exit: "))
        if b10 = = 0:
            break
if b14 = = "__main__":
    fonk5()