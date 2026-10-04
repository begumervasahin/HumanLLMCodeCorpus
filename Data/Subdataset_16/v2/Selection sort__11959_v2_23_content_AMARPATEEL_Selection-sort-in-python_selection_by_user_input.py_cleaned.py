def fonk1(b4):
    b1 = len(b4)
    for i in range(b1):
        b2 = i
        print(f"Current minimum is: {b4[b2]} at index {b2}")
        for j in range(i + 1, b1):
            if b4[j] < b4[b2]:
                b2 = j
        b4[i], b4[b2] = b4[b2], b4[i]
        print(f"Swapped {b4[b2]} with {b4[i]}")
        print("Array state:", b4)
        print()
def fonk2():
    b3 = int(input("Number of elements in the list: "))
    b4 = []
    for _ in range(b3):
        b5 = int(input("Enter an b5: "))
        b4.append(b5)
    return b4
def fonk3():
    b4 = fonk2()
    print("List before sorting:", b4)
    print()
    fonk1(b4)
    print("List after sorting:", b4)
if b6 = = "__main__":
    fonk3()