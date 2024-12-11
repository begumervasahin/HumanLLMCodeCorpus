import time
b1 = '_' * 80
b2 = "Sort Techniques on Dataset"
def fonk1(b10):
    for j in range(len(b10) - 1, 0, -1):
        for b8 in range(j):
            if b10[b8] > b10[b8 + 1]:
                b10[b8], b10[b8 + 1] = b10[b8 + 1], b10[b8]
def fonk2(b10):
    for b8 in range(1, len(b10)):
        b3 = b10[b8]
        b4 = b8
        while b4 > 0 and b10[b4 - 1] > b3:
            b10[b4] = b10[b4 - 1]
            b4 -= 1
        b10[b4] = b3
def fonk3(alist):
    if len(alist) > 1:
        b5 = len(alist)
        b6 = alist[:b5]
        b7 = alist[b5:]
        fonk3(b6)
        fonk3(b7)
        b8 = j = k = 0
        while b8 < len(b6) and j < len(b7):
            if b6[b8] < b7[j]:
                alist[k] = b6[b8]
                b8 += 1
            else:
                alist[k] = b7[j]
                j += 1
            k += 1
        while b8 < len(b6):
            alist[k] = b6[b8]
            b8 += 1
            k += 1
        while j < len(b7):
            alist[k] = b7[j]
            j += 1
            k += 1
def fonk4(b10):
    for fillslot in range(len(b10) - 1, 0, -1):
        a1 = 0
        for location in range(1, fillslot + 1):
            if b10[location] > b10[a1]:
                a1 = location
        b10[fillslot], b10[a1] = b10[a1], b10[fillslot]
def fonk5():
    print("Enter:")
    print("1 for Bubble Sort")
    print("2 for Insertion Sort")
    print("3 for Merge Sort")
    print("4 for Selection Sort")
def fonk6():
    print(b1)
    print(b2.center(80))
    print(b1 + "\n\n")
    while True:
        fonk5()
        b9 = int(input("\nEnter your b9: "))
        if b9 not in [1, 2, 3, 4]:
            print("Invalid b9. Please select again.")
            continue
        b10 = []
        b11 = int(input("\nHow many numbers do you want to enter? "))
        for b8 in range(b11):
            b12 = int(input("Enter the number: "))
            b10.append(b12)
        b13 = time.time()
        if b9 = = 1:
            fonk1(b10)
            print("\nThe list after Bubble Sort is:", b10)
        elif b9 = = 2:
            fonk2(b10)
            print("\nThe list after Insertion Sort is:", b10)
        elif b9 = = 3:
            fonk3(b10)
            print("\nThe list after Merge Sort is:", b10)
        elif b9 = = 4:
            fonk4(b10)
            print("\nThe list after Selection Sort is:", b10)
        b14 = time.time()
        print("The time taken by sorting process:", b14 - b13)
        b15 = input("\nEnter 1 to continue and 0 to exit: ")
        if b15 != '1':
            break
        print("\n\n")
if b16 = = "__main__":
    fonk6()