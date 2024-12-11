import time
b1 = '_' * 80
print(f"{b1} \n")
b2 = "Sort Techniques on Dataset"
print(b2.center(80))
print(f"\n{b1}\n\n")
def fonk1(b11):
    for j in range(len(b11) - 1, 0, -1):
        for i in range(j):
            if b11[i] > b11[i + 1]:
                b11[i], b11[i + 1] = b11[i + 1], b11[i]
def fonk2(b11):
    for i in range(1, len(b11)):
        b3 = b11[i]
        b4 = i
        while b4 > 0 and b11[b4 - 1] > b3:
            b11[b4] = b11[b4 - 1]
            b4 -= 1
        b11[b4] = b3
def fonk3(b11):
    def fonk4(left, right):
        b5 = []
        while left and right:
            b5.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        return b5 + left + right
    if len(b11) <= 1:
        return b11
    b6 = len(b11)
    b7 = fonk3(b11[:b6])
    b8 = fonk3(b11[b6:])
    return fonk4(b7, b8)
def fonk5(b11):
    for fill_slot in range(len(b11) - 1, 0, -1):
        a1 = 0
        for location in range(1, fill_slot + 1):
            if b11[location] > b11[a1]:
                a1 = location
        b11[fill_slot], b11[a1] = b11[a1], b11[fill_slot]
while True:
    print("Enter:")
    print("1 for Bubble Sort")
    print("2 for Insertion Sort")
    print("3 for Merge Sort")
    print("4 for Selection Sort")
    b9 = int(input("\nEnter your b9: "))
    if b9 = = 1:
        b10 = time.time()
        b11 = [int(input("Enter the number: ")) for _ in range(int(input("\nHow many numbers do you want to enter? ")))]
        fonk1(b11)
        print("\nThe list after Bubble Sort is:", b11)
        print("The time taken by sorting process:", time.time() - b10)
    elif b9 = = 2:
        b10 = time.time()
        b11 = [int(input("Enter the number: ")) for _ in range(int(input("\nHow many numbers do you want to enter? ")))]
        fonk2(b11)
        print("\nThe list after Insertion Sort is:", b11)
        print("The time taken by sorting process:", time.time() - b10)
    elif b9 = = 3:
        b10 = time.time()
        b11 = [int(input("Enter the number: ")) for _ in range(int(input("\nHow many numbers do you want to enter? ")))]
        b11 = fonk3(b11)
        print("\nThe list after Merge Sort is:", b11)
        print("The time taken by sorting process:", time.time() - b10)
    elif b9 = = 4:
        b10 = time.time()
        b11 = [int(input("Enter the number: ")) for _ in range(int(input("\nHow many numbers do you want to enter? ")))]
        fonk5(b11)
        print("\nThe list after Selection Sort is:", b11)
        print("The time taken by sorting process:", time.time() - b10)
    b12 = int(input("\nEnter 1 to continue and 0 to exit: "))
    print("\n\n")
    if b12 = = 0:
        break