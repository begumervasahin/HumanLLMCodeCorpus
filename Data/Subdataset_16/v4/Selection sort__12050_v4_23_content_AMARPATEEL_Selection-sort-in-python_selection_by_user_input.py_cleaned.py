def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = i
        print(f"Current minimum is: {b3[i]}")
        for j in range(i + 1, b1):
            if b3[b2] > b3[j]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
        print(f"New minimum is: {b3[i]}")
        print(b3)
        print()
def fonk2():
    b3 = []
    b4 = int(input("Number of elements in the list: "))
    for _ in range(b4):
        b1 = int(input("Enter an element: "))
        b3.append(b1)
    print("List before sorting:", b3)
    fonk1(b3)
    print("List after sorting:", b3)
if b5 = = "__main__":
    fonk2()