import binary
def fonk1(b1):
    print(b1)
    if b1 > 0:
        fonk1(b1 - 1)
def fonk2(b1):
    if b1 = = 0:
        return 1
    return b1 * fonk2(b1 - 1)
def fonk3(b1, b2 = 1):
    if b1 = = 0:
        return b2
    return fonk3(b1 - 1, b2 * b1)
b3 = binary.Node(0)
b4 = binary.Node(1)
b5 = binary.Node(2)
b6 = binary.Node(3)
b7 = binary.Node(4)
b8 = binary.Node(5)
b3.addLeft(b4)
b3.addRight(b5)
b4.addLeft(b6)
b5.addLeft(b7)
b5.addRight(b8)
def fonk4(root):
    print(root.b9)
    if root.l:
        print("Left")
        fonk4(root.l)
    if root.r:
        print("Right")
        fonk4(root.r)
    print("Up")
def fonk5(root, val):
    if root.b9 = = val:
        print("Found")
        return True
    b10 = False
    if root.l:
        b10 = fonk5(root.l, val)
    if not b10 and root.r:
        b10 = fonk5(root.r, val)
    return b10
def fonk6(b1):
    if len(b1) < 2:
        return b1
    b11 = len(b1)
    b12 = fonk6(b1[:b11])
    b13 = fonk6(b1[b11:])
    return fonk7(b12, b13)
def fonk7(b12, b13):
    b14 = []
    b15 = j = 0
    while b15 < len(b12) and j < len(b13):
        if b12[b15] < b13[j]:
            b14.append(b12[b15])
            b15 += 1
        else:
            b14.append(b13[j])
            j += 1
    b14.extend(b12[b15:])
    b14.extend(b13[j:])
    return b14
if b16 = = "__main__":
    print("Countdown from 5:")
    fonk1(5)
    print()
    print("Factorial of 5:")
    print(fonk2(5))
    print()
    print("Tail factorial of 5:")
    print(fonk3(5))
    print()
    print("Tree traversal:")
    fonk4(b3)
    print()
    print("Search for value 4 in the tree:")
    b10 = fonk5(b3, 4)
    if not b10:
        print("Not Found")
    print()
    b17 = [38, 27, 43, 3, 9, 82, 10]
    print("Merge sort:")
    b18 = fonk6(b17)
    print(f"Unsorted list: {b17}")
    print(f"Sorted list: {b18}")