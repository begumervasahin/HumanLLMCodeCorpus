import time
def fonk1(b11):
    for a2 in range(len(b11) - 1, 0, -1):
        for a1 in range(a2):
            if b11[a1] > b11[a1 + 1]:
                b1 = b11[a1]
                b11[a1] = b11[a1 + 1]
                b11[a1 + 1] = b1
def fonk2(b11):
    for a1 in range(1, len(b11)):
        b2 = b11[a1]
        b3 = a1
        while b3 > 0 and b11[b3 - 1] > b2:
            b11[b3] = b11[b3 - 1]
            b3 = b3 - 1
            b11[b3] = b2
def fonk3(b15):
    if len(b15) > 1:
        b4 = len(b15)
        b5 = b15[:b4]
        b6 = b15[b4:]
        fonk3(b5)
        fonk3(b6)
        a1 = 0
        a2 = 0
        a3 = 0
        while a1 < len(b5) and a2 < len(b6):
            if b5[a1] < b6[a2]:
                b15[a3] = b5[a1]
                a1 = a1 + 1
            else:
                b15[a3] = b6[a2]
                a2 = a2 + 1
            a3 = a3 + 1
        while a1 < len(b5):
            b15[a3] = b5[a1]
            a1 = a1 + 1
            a3 = a3 + 1
        while a2 < len(b6):
            b15[a3] = b6[a2]
            a2 = a2 + 1
            a3 = a3 + 1
def fonk4(b11):
    for fillslot in range(len(b11) - 1, 0, -1):
        a4 = 0
        for location in range(1, fillslot + 1):
            if b11[location] > b11[a4]:
                a4 = location
        b1 = b11[fillslot]
        b11[fillslot] = b11[a4]
        b11[a4] = b1
while True:
    b7 = '_' * 80
    print(f"{b7} \b12")
    b8 = "Sort techniques on dataset"
    print(b8.center(80))
    print(f"\b12{b7}\b12\b12")
    print("Enter \b12 1 for bubble sort \b12 2 for insertion sort \b12 3 for merge sort \b12 4 for selection sort")
    b9 = int(input("\b12 Enter the choice:"))
    if b9 = = 1:
        b10 = time.time()
        b11 = []
        b12 = int(input(" \b12 How many numbers do you want to enter:"))
        for a1 in range(b12):
            b13 = int(input(" Enter the number:"))
            b11.append(b13)
        fonk1(b11)
        print("\b12 The list after bubble sorting is", b11)
        b14 = time.time()
        print(" The time taken by sorting process:", b14 - b10)
    if b9 = = 2:
        b10 = time.time()
        b11 = []
        b12 = int(input(" \b12 How many numbers do you want to enter:"))
        for a1 in range(b12):
            b13 = int(input(" Enter the number:"))
            b11.append(b13)
        fonk2(b11)
        print("\b12 The list after insertion sorting is", b11)
        b14 = time.time()
        print(" The time taken by sorting process:", b14 - b10)
    if b9 = = 3:
        b10 = time.time()
        b15 = []
        b12 = int(input(" \b12 How many numbers do you want to enter:"))
        for a1 in range(b12):
            b13 = int(input(" Enter the number:"))
            b15.append(b13)
        fonk3(b15)
        print("\b12 The list after merge sorting is", b15)
        b14 = time.time()
        print(" The time taken by sorting process:", b14 - b10)
    if b9 = = 4:
        b10 = time.time()
        b11 = []
        b12 = int(input(" \b12 How many numbers do you want to enter:"))
        for a1 in range(b12):
            b13 = int(input(" Enter the number:"))
            b11.append(b13)
        fonk4(b11)
        print("\b12 The list after selection sorting is", b11)
        b14 = time.time()
        print(" The time taken by sorting process:", b14 - b10)
    b12 = int(input(" Enter 1 to continue and 0 to exit:"))
    print(" \b12 \b12 ")
    if b12 = = 0:
        break