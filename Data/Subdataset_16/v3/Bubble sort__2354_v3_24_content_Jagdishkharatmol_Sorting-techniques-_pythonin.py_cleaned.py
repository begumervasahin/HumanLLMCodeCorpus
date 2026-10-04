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
    b1 = len(b9)
    for fill_slot in range(b1 - 1, 0, -1):
        a1 = 0
        for location in range(1, fill_slot + 1):
            if b9[location] > b9[a1]:
                a1 = location
        b9[fill_slot], b9[a1] = b9[a1], b9[fill_slot]
def fonk5():
    print("Enter \b1 1 for Bubble Sort \b1 2 for Insertion Sort \b1 3 for Merge Sort \b1 4 for Selection Sort")
    while True:
        try:
            b8 = int(input("\nEnter your b8: "))
            if b8 in {1, 2, 3, 4}:
                return b8
            else:
                print("Invalid b8! Please enter a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")
def fonk6():
    b9 = []
    while True:
        try:
            b1 = int(input("\nHow many numbers do you want to enter: "))
            for _ in range(b1):
                b10 = int(input("Enter the number: "))
                b9.append(b10)
            return b9
        except ValueError:
            print("Invalid input! Please enter a number.")
def fonk7(b8, b9):
    if b8 = = 1:
        fonk1(b9)
    elif b8 = = 2:
        fonk2(b9)
    elif b8 = = 3:
        fonk3(b9)
    elif b8 = = 4:
        fonk4(b9)
    return b9
def fonk8():
    b11 = '_' * 80
    b12 = "Sort Techniques on Dataset"
    print(f"{b11}\b1{b12.center(80)}\b1{b11}\b1")
    while True:
        b8 = fonk5()
        b9 = fonk6()
        b13 = time.time()
        b14 = fonk7(b8, b9)
        b15 = time.time()
        b16 = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"][b8 - 1]
        print(f"\nThe list after {b16} is: {b14}")
        print(f"The time taken by the sorting process: {b15 - b13:.6f} seconds")
        try:
            b17 = int(input("\nEnter 1 to continue and 0 to exit: "))
            if b17 = = 0:
                break
        except ValueError:
            print("Invalid input! Exiting the program.")
            break
if b18 = = "__main__":
    fonk8()