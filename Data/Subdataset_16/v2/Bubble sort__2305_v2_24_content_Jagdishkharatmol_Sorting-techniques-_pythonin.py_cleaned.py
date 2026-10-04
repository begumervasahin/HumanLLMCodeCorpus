import time
def fonk1(b10):
    for j in range(len(b10) - 1, 0, -1):
        for b6 in range(j):
            if b10[b6] > b10[b6 + 1]:
                b10[b6], b10[b6 + 1] = b10[b6 + 1], b10[b6]
def fonk2(b10):
    for b6 in range(1, len(b10)):
        b1 = b10[b6]
        b2 = b6
        while b2 > 0 and b10[b2 - 1] > b1:
            b10[b2] = b10[b2 - 1]
            b2 -= 1
        b10[b2] = b1
def fonk3(b10):
    if len(b10) > 1:
        b3 = len(b10)
        b4 = b10[:b3]
        b5 = b10[b3:]
        fonk3(b4)
        fonk3(b5)
        b6 = j = k = 0
        while b6 < len(b4) and j < len(b5):
            if b4[b6] < b5[j]:
                b10[k] = b4[b6]
                b6 += 1
            else:
                b10[k] = b5[j]
                j += 1
            k += 1
        while b6 < len(b4):
            b10[k] = b4[b6]
            b6 += 1
            k += 1
        while j < len(b5):
            b10[k] = b5[j]
            j += 1
            k += 1
def fonk4(b10):
    for fill_slot in range(len(b10) - 1, 0, -1):
        a1 = 0
        for location in range(1, fill_slot + 1):
            if b10[location] > b10[a1]:
                a1 = location
        b10[fill_slot], b10[a1] = b10[a1], b10[fill_slot]
def fonk5():
    b7 = '_' * 80
    print(f"{b7}\b11")
    b8 = "Sort Techniques on Dataset"
    print(b8.center(80))
    print(f"\b11{b7}\b11\b11")
    while True:
        print("Enter \b11 1 for Bubble Sort \b11 2 for Insertion Sort \b11 3 for Merge Sort \b11 4 for Selection Sort")
        b9 = int(input("\nEnter your b9: "))
        b10 = []
        b11 = int(input("\nHow many numbers do you want to enter: "))
        for b6 in range(b11):
            b12 = int(input("Enter the number: "))
            b10.append(b12)
        if b9 = = 1:
            b13 = time.time()
            fonk1(b10)
            b14 = time.time()
            print("\nThe list after Bubble Sorting is: {}".format(b10))
            print("The time taken by the sorting process: {:.6f} seconds".format(b14 - b13))
        elif b9 = = 2:
            b13 = time.time()
            fonk2(b10)
            b14 = time.time()
            print("\nThe list after Insertion Sorting is: {}".format(b10))
            print("The time taken by the sorting process: {:.6f} seconds".format(b14 - b13))
        elif b9 = = 3:
            b13 = time.time()
            fonk3(b10)
            b14 = time.time()
            print("\nThe list after Merge Sorting is: {}".format(b10))
            print("The time taken by the sorting process: {:.6f} seconds".format(b14 - b13))
        elif b9 = = 4:
            b13 = time.time()
            fonk4(b10)
            b14 = time.time()
            print("\nThe list after Selection Sorting is: {}".format(b10))
            print("The time taken by the sorting process: {:.6f} seconds".format(b14 - b13))
        else:
            print("Invalid b9! Please enter a valid option.")
        b15 = int(input("\nEnter 1 to continue and 0 to exit: "))
        if b15 = = 0:
            break
if b16 = = "__main__":
    fonk5()