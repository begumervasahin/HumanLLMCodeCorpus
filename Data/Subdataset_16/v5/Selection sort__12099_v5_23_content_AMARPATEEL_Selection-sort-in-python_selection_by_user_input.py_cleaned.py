def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = i
        print(f"Current minimum is: {b3[i]}")
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
        print(f"New minimum is: {b3[i]}")
        print(b3)
        print()
def fonk2():
    b3 = []
    b4 = int(input("Number of elements in the list: "))
    for _ in range(b4):
        b5 = int(input("Enter an b5: "))
        b3.append(b5)
    print("List before sorting:", b3)
    fonk1(b3)
    print("List after sorting:", b3)
if b6 = = "__main__":
    fonk2()