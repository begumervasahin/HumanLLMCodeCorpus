import time
def fonk1(b9):
    b1 = len(b9)
    for j in range(b1 - 1, 0, -1):
        for b7 in range(j):
            if b9[b7] > b9[b7 + 1]:
                b9[b7], b9[b7 + 1] = b9[b7 + 1], b9[b7]
def fonk2(b9):
    for b7 in range(1, len(b9)):
        b2 = b9[b7]
        b3 = b7
        while b3 > 0 and b9[b3 - 1] > b2:
            b9[b3] = b9[b3 - 1]
            b3 -= 1
        b9[b3] = b2
def fonk3(b9):
    if len(b9) > 1:
        b4 = len(b9)
        b5 = b9[:b4]
        b6 = b9[b4:]
        fonk3(b5)
        fonk3(b6)
        b7 = j = k = 0
        while b7 < len(b5) and j < len(b6):
            if b5[b7] < b6[j]:
                b9[k] = b5[b7]
                b7 += 1
            else:
                b9[k] = b6[j]
                j += 1
            k += 1
        while b7 < len(b5):
            b9[k] = b5[b7]
            b7 += 1
            k += 1
        while j < len(b6):
            b9[k] = b6[j]
            j += 1
            k += 1
def fonk4(b9):
    for fillslot in range(len(b9) - 1, 0, -1):
        a1 = 0
        for location in range(1, fillslot + 1):
            if b9[location] > b9[a1]:
                a1 = location
        b9[fillslot], b9[a1] = b9[a1], b9[fillslot]
def fonk5():
    print("Enter the number corresponding to the sorting algorithm:")
    print(" 1. Bubble Sort")
    print(" 2. Insertion Sort")
    print(" 3. Merge Sort")
    print(" 4. Selection Sort")
    while True:
        try:
            b8 = int(input("\nEnter your b8: "))
            if b8 in {1, 2, 3, 4}:
                return b8
            else:
                print("Invalid b8. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def fonk6():
    while True:
        try:
            b1 = int(input("\nHow many b12 do you want to enter? "))
            if b1 > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    b9 = []
    for _ in range(b1):
        while True:
            try:
                b10 = int(input("Enter a number: "))
                b9.append(b10)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return b9
def fonk7():
    b11 = '_' * 80
    print(f"{b11}\b1")
    print("Sort techniques on dataset".center(80))
    print(f"\b1{b11}\b1\b1")
    while True:
        b8 = fonk5()
        b12 = fonk6()
        b13 = time.time()
        if b8 = = 1:
            fonk1(b12)
            print("\nThe list after bubble sorting is {}".format(b12))
        elif b8 = = 2:
            fonk2(b12)
            print("\nThe list after insertion sorting is {}".format(b12))
        elif b8 = = 3:
            fonk3(b12)
            print("\nThe list after merge sorting is {}".format(b12))
        elif b8 = = 4:
            fonk4(b12)
            print("\nThe list after selection sorting is {}".format(b12))
        b14 = time.time()
        print("The time taken by the sorting process: {:.5f} seconds".format(b14 - b13))
        b15 = input("Enter 'y' to continue or any other key to exit: ").strip().lower()
        if b15 != 'y':
            break
if b16 = = "__main__":
    fonk7()