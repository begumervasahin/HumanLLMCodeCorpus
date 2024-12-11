import random
import time
def fonk1(b17, b6):
    random.seed(0)
    with open(b17, 'w') as f:
        for _ in range(b6):
            f.write(str(random.randrange(0, 100)) + "\b6")
def fonk2(b4, b5):
    b1 = []
    left_index, b2 = 0, 0
    while left_index < len(b4) and b2 < len(b5):
        if b4[left_index] < b5[b2]:
            b1.append(b4[left_index])
            left_index += 1
        else:
            b1.append(b5[b2])
            b2 += 1
    b1.extend(b4[left_index:])
    b1.extend(b5[b2:])
    return b1
def fonk3(aList):
    if len(aList) <= 1:
        return aList
    else:
        b3 = len(aList)
        b4 = fonk3(aList[:b3])
        b5 = fonk3(aList[b3:])
        return fonk2(b4, b5)
def fonk4(aList):
    b6 = len(aList)
    for i in range(b6 - 1):
        b7 = i
        for j in range(i + 1, b6):
            if aList[j] < aList[b7]:
                b7 = j
        aList[i], aList[b7] = aList[b7], aList[i]
    return aList
def fonk5(inputfile, b18):
    b8 = time.time()
    with open(inputfile, 'r') as f:
        b9 = [int(line.strip()) for line in f]
    b10 = time.time()
    b11 = time.time()
    b12 = fonk3(b9)
    b13 = time.time()
    b14 = time.time()
    with open(b18, 'w') as f:
        for num in b12:
            f.write(str(num) + "\b6")
    b15 = time.time()
    b16 = b15 - b8
    print(f"It took {b10 - b8:.6f} seconds to input values from file {inputfile}")
    print(f"It took {b13 - b11:.6f} seconds to sort {len(b9)} values using merge sort")
    print(f"It took {b15 - b14:.6f} seconds to output {len(b12)} sorted values to file {b18}")
    print(f"Total time the program took is {b16:.6f} seconds\b6")
def fonk6(inputfile, b18):
    b8 = time.time()
    with open(inputfile, 'r') as f:
        b9 = [int(line.strip()) for line in f]
    b10 = time.time()
    b11 = time.time()
    b12 = fonk4(b9)
    b13 = time.time()
    b14 = time.time()
    with open(b18, 'w') as f:
        for num in b12:
            f.write(str(num) + "\b6")
    b15 = time.time()
    b16 = b15 - b8
    print(f"It took {b10 - b8:.6f} seconds to input values from file {inputfile}")
    print(f"It took {b13 - b11:.6f} seconds to sort {len(b9)} values using selection sort")
    print(f"It took {b15 - b14:.6f} seconds to output {len(b12)} sorted values to file {b18}")
    print(f"Total time the program took is {b16:.6f} seconds\b6")
def fonk7():
    b17 = input("Enter the b17: ")
    b6 = int(input("Enter number of values: "))
    fonk1(b17, b6)
    b18 = input("Please enter output file name: ")
    fonk5(b17, b18)
    fonk6(b17, b18)
if b19 = = "__main__":
    fonk7()