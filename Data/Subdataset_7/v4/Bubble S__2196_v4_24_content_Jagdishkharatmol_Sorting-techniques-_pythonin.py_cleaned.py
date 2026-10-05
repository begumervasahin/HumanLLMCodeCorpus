import time
b1 = '_' * 80
print(f"{b1} \b15")
b2 = "Sort techniques on dataset"
print(b2.center(80))
print(f"\b15{b1}\b15\b15")
def fonk1(b14):
    for b10 in range(len(b14)-1, 0, -1):
        for b9 in range(b10):
            if b14[b9] > b14[b9+1]:
                b3 = b14[b9]
                b14[b9] = b14[b9+1]
                b14[b9+1] = b3
def fonk2(b14):
    for b9 in range(1, len(b14)):
        b4 = b14[b9]
        b5 = b9
        while b5 > 0 and b14[b5-1] > b4:
            b14[b5] = b14[b5-1]
            b5 = b5 - 1
            b14[b5] = b4
def fonk3(b18):
    if len(b18) > 1:
        b6 = len(b18)
        b7 = b18[:b6]
        b8 = b18[b6:]
        fonk3(b7)
        fonk3(b8)
        b9 = b10 = b11 = 0
        while b9 < len(b7) and b10 < len(b8):
            if b7[b9] < b8[b10]:
                b18[b11] = b7[b9]
                b9 = b9 + 1
            else:
                b18[b11] = b8[b10]
                b10 = b10 + 1
            b11 = b11 + 1
        while b9 < len(b7):
            b18[b11] = b7[b9]
            b9 = b9 + 1
            b11 = b11 + 1
        while b10 < len(b8):
            b18[b11] = b8[b10]
            b10 = b10 + 1
            b11 = b11 + 1
def fonk4(b14):
    for fillslot in range(len(b14)-1, 0, -1):
        a1 = 0
        for location in range(1, fillslot+1):
            if b14[location] > b14[a1]:
                a1 = location
        b3 = b14[fillslot]
        b14[fillslot] = b14[a1]
        b14[a1] = b3
while True:
    print("Enter:")
    print("1 for bubble sort")
    print("2 for insertion sort")
    print("3 for merge sort")
    print("4 for selection sort")
    b12 = int(input("\nEnter your choice: "))
    if b12 = = 1:
        b13 = time.time()
        b14 = []
        b15 = int(input("\nHow many numbers do you want to enter? "))
        for b9 in range(b15):
            b16 = int(input("Enter the number: "))
            b14.append(b16)
        fonk1(b14)
        print("\nThe list after bubble sorting is", b14)
        b17 = time.time()
        print("The time taken by sorting process:", b17 - b13)
    elif b12 = = 2:
        b13 = time.time()
        b14 = []
        b15 = int(input("\nHow many numbers do you want to enter? "))
        for b9 in range(b15):
            b16 = int(input("Enter the number: "))
            b14.append(b16)
        fonk2(b14)
        print("\nThe list after insertion sorting is", b14)
        b17 = time.time()
        print("The time taken by sorting process:", b17 - b13)
    elif b12 = = 3:
        b13 = time.time()
        b18 = []
        b15 = int(input("\nHow many numbers do you want to enter? "))
        for b9 in range(b15):
            b16 = int(input("Enter the number: "))
            b18.append(b16)
        fonk3(b18)
        print("\nThe list after merge sorting is", b18)
        b17 = time.time()
        print("The time taken by sorting process:", b17 - b13)
    elif b12 = = 4:
        b13 = time.time()
        b14 = []
        b15 = int(input("\nHow many numbers do you want to enter? "))
        for b9 in range(b15):
            b16 = int(input("Enter the number: "))
            b14.append(b16)
        fonk4(b14)
        print("\nThe list after selection sorting is", b14)
        b17 = time.time()
        print("The time taken by sorting process:", b17 - b13)
    b15 = int(input("\nEnter 1 to continue and 0 to exit: "))
    print("\b15\b15")
    if b15 = = 0:
        break