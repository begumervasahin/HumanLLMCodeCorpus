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
def fonk3(b11):
    if len(b11) > 1:
        b3 = len(b11)
        b4 = b11[:b3]
        b5 = b11[b3:]
        fonk3(b4)
        fonk3(b5)
        b6 = j = k = 0
        while b6 < len(b4) and j < len(b5):
            if b4[b6] < b5[j]:
                b11[k] = b4[b6]
                b6 += 1
            else:
                b11[k] = b5[j]
                j += 1
            k += 1
        while b6 < len(b4):
            b11[k] = b4[b6]
            b6 += 1
            k += 1
        while j < len(b5):
            b11[k] = b5[j]
            j += 1
            k += 1
def fonk4(b10):
    for fill_slot in range(len(b10) - 1, 0, -1):
        a1 = 0
        for location in range(1, fill_slot + 1):
            if b10[location] > b10[a1]:
                a1 = location
        b10[fill_slot], b10[a1] = b10[a1], b10[fill_slot]
while True:
    b7 = '_' * 80
    print(f"\n{b7}\n{'Sort techniques on dataset'.center(80)}\n{b7}\n")
    print("Enter:\n1 for Bubble Sort\n2 for Insertion Sort\n3 for Merge Sort\n4 for Selection Sort")
    b8 = int(input("\nEnter your b8: "))
    if b8 = = 1:
        b9 = time.time()
        b10 = [int(input("Enter a number: ")) for _ in range(int(input("How many numbers do you want to enter: ")))]
        fonk1(b10)
        print(f"The list after Bubble Sort: {b10}")
        print(f"Time taken: {time.time() - b9} seconds")
    elif b8 = = 2:
        b9 = time.time()
        b10 = [int(input("Enter a number: ")) for _ in range(int(input("How many numbers do you want to enter: ")))]
        fonk2(b10)
        print(f"The list after Insertion Sort: {b10}")
        print(f"Time taken: {time.time() - b9} seconds")
    elif b8 = = 3:
        b9 = time.time()
        b11 = [int(input("Enter a number: ")) for _ in range(int(input("How many numbers do you want to enter: ")))]
        fonk3(b11)
        print(f"The list after Merge Sort: {b11}")
        print(f"Time taken: {time.time() - b9} seconds")
    elif b8 = = 4:
        b9 = time.time()
        b10 = [int(input("Enter a number: ")) for _ in range(int(input("How many numbers do you want to enter: ")))]
        fonk4(b10)
        print(f"The list after Selection Sort: {b10}")
        print(f"Time taken: {time.time() - b9} seconds")
    else:
        print("Invalid b8!")
    b12 = int(input("\nEnter 1 to continue and 0 to exit: "))
    if b12 = = 0:
        break