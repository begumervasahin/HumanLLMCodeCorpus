import time
def fonk1(b9):
    for j in range(len(b9) - 1, 0, -1):
        for b6 in range(j):
            if b9[b6] > b9[b6 + 1]:
                b9[b6], b9[b6 + 1] = b9[b6 + 1], b9[b6]
def fonk2(b9):
    for b6 in range(1, len(b9)):
        b1 = b9[b6]
        b2 = b6
        while b2 > 0 and b9[b2 - 1] > b1:
            b9[b2] = b9[b2 - 1]
            b2 -= 1
        b9[b2] = b1
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
def fonk4(b9):
    for fill_slot in range(len(b9) - 1, 0, -1):
        a1 = 0
        for location in range(1, fill_slot + 1):
            if b9[location] > b9[a1]:
                a1 = location
        b9[fill_slot], b9[a1] = b9[a1], b9[fill_slot]
def fonk5(prompt):
    while True:
        try:
            b7 = int(input(prompt))
            return b7
        except ValueError:
            print("Please enter a valid integer.")
def fonk6():
    while True:
        print("_" * 80)
        print("Sort techniques on dataset".center(80))
        print("_" * 80)
        print("Enter:")
        print("1 for Bubble Sort")
        print("2 for Insertion Sort")
        print("3 for Merge Sort")
        print("4 for Selection Sort")
        b8 = fonk5("\nEnter your b8: ")
        if b8 = = 1:
            b9 = [fonk5("Enter a number: ") for _ in range(fonk5("How many numbers do you want to enter: "))]
            b10 = time.time()
            fonk1(b9)
            print(f"The list after Bubble Sort: {b9}")
            print(f"Time taken: {time.time() - b10} seconds")
        elif b8 = = 2:
            b9 = [fonk5("Enter a number: ") for _ in range(fonk5("How many numbers do you want to enter: "))]
            b10 = time.time()
            fonk2(b9)
            print(f"The list after Insertion Sort: {b9}")
            print(f"Time taken: {time.time() - b10} seconds")
        elif b8 = = 3:
            b11 = [fonk5("Enter a number: ") for _ in range(fonk5("How many numbers do you want to enter: "))]
            b10 = time.time()
            fonk3(b11)
            print(f"The list after Merge Sort: {b11}")
            print(f"Time taken: {time.time() - b10} seconds")
        elif b8 = = 4:
            b9 = [fonk5("Enter a number: ") for _ in range(fonk5("How many numbers do you want to enter: "))]
            b10 = time.time()
            fonk4(b9)
            print(f"The list after Selection Sort: {b9}")
            print(f"Time taken: {time.time() - b10} seconds")
        else:
            print("Invalid b8!")
        b12 = fonk5("\nEnter 1 to continue and 0 to exit: ")
        if b12 = = 0:
            break
if b13 = = "__main__":
    fonk6()