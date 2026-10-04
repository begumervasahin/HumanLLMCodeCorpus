def fonk1(b2):
    for i in range(len(b2)):
        b1 = i
        print(f"Current minimum is: {b2[b1]}")
        for j in range(i + 1, len(b2)):
            if b2[j] < b2[b1]:
                b1 = j
        b2[i], b2[b1] = b2[b1], b2[i]
        print(f"New minimum is: {b2[i]}")
        print(b2)
        print()
def fonk2():
    b2 = []
    b3 = int(input("Number of elements in the list: "))
    for i in range(b3):
        b4 = int(input("Enter an b4: "))
        b2.append(b4)
    print("List before sorting:", b2)
    fonk1(b2)
    print("List after sorting:", b2)
if b5 = = "__main__":
    fonk2()