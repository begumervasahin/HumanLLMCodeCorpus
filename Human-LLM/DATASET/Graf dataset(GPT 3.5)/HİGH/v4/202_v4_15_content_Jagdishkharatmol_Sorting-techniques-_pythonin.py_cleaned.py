import time
b1 = '_' * 80
b2 = "Sort techniques on dataset"
print(b1)
print(b2.center(80))
print(b1 + "\n\n")
while True:
    print("Enter \n 1 for bubble sort \n 2 for insertion sort \n 3 for merge sort \n 4 for selection sort")
    b3 = int(input("\nEnter your b3: "))
    if b3 = = 1:
        b4 = time.time()
        def fonk1(b6):
            for j in range(len(b6) - 1, 0, -1):
                for b15 in range(j):
                    if b6[b15] > b6[b15 + 1]:
                        b5 = b6[b15]
                        b6[b15] = b6[b15 + 1]
                        b6[b15 + 1] = b5
        b6 = []
        b7 = int(input("\nHow many numbers do you want to enter? "))
        for b15 in range(b7):
            b8 = int(input("Enter the number: "))
            b6.append(b8)
        fonk1(b6)
        print("\nThe list after bubble sorting is:", b6)
        b9 = time.time()
        print("The time taken by sorting process:", b9 - b4)
    elif b3 = = 2:
        b4 = time.time()
        def fonk2(b6):
            for b15 in range(1, len(b6)):
                b10 = b6[b15]
                b11 = b15
                while b11 > 0 and b6[b11 - 1] > b10:
                    b6[b11] = b6[b11 - 1]
                    b11 -= 1
                b6[b11] = b10
        b6 = []
        b7 = int(input("\nHow many numbers do you want to enter? "))
        for b15 in range(b7):
            b8 = int(input("Enter the number: "))
            b6.append(b8)
        fonk2(b6)
        print("\nThe list after insertion sorting is:", b6)
        b9 = time.time()
        print("The time taken by sorting process:", b9 - b4)
    elif b3 = = 3:
        b4 = time.time()
        def fonk3(b16):
            if len(b16) > 1:
                b12 = len(b16)
                b13 = b16[:b12]
                b14 = b16[b12:]
                fonk3(b13)
                fonk3(b14)
                b15 = j = k = 0
                while b15 < len(b13) and j < len(b14):
                    if b13[b15] < b14[j]:
                        b16[k] = b13[b15]
                        b15 += 1
                    else:
                        b16[k] = b14[j]
                        j += 1
                    k += 1
                while b15 < len(b13):
                    b16[k] = b13[b15]
                    b15 += 1
                    k += 1
                while j < len(b14):
                    b16[k] = b14[j]
                    j += 1
                    k += 1
        b16 = []
        b7 = int(input("\nHow many numbers do you want to enter? "))
        for b15 in range(b7):
            b8 = int(input("Enter the number: "))
            b16.append(b8)
        fonk3(b16)
        print("\nThe list after merge sorting is:", b16)
        b9 = time.time()
        print("The time taken by sorting process:", b9 - b4)
    elif b3 = = 4:
        b4 = time.time()
        def fonk4(b6):
            for fillslot in range(len(b6) - 1, 0, -1):
                a1 = 0
                for location in range(1, fillslot + 1):
                    if b6[location] > b6[a1]:
                        a1 = location
                b5 = b6[fillslot]
                b6[fillslot] = b6[a1]
                b6[a1] = b5
        b6 = []
        b7 = int(input("\nHow many numbers do you want to enter? "))
        for b15 in range(b7):
            b8 = int(input("Enter the number: "))
            b6.append(b8)
        fonk4(b6)
        print("\nThe list after selection sorting is:", b6)
        b9 = time.time()
        print("The time taken by sorting process:", b9 - b4)
    b17 = int(input("\nEnter 1 to continue and 0 to exit: "))
    print("\n\n")
    if b17 = = 0:
        break