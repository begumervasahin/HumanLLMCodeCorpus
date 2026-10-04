def fonk1(b6):
    if len(b6) <= 1:
        return
    b1 = len(b6)
    b2 = b6[:b1]
    b3 = b6[b1:]
    fonk1(b2)
    fonk1(b3)
    fonk2(b6, b2, b3)
def fonk2(b6, left, right):
    b4 = j = k = 0
    while b4 < len(left) and j < len(right):
        if left[b4] < right[j]:
            b6[k] = left[b4]
            b4 += 1
        else:
            b6[k] = right[j]
            j += 1
        k += 1
    while b4 < len(left):
        b6[k] = left[b4]
        b4 += 1
        k += 1
    while j < len(right):
        b6[k] = right[j]
        j += 1
        k += 1
def fonk3():
    b5 = int(input("How many elements do you want in the list? "))
    b6 = [int(input(f"Enter element {b4 + 1}: ")) for b4 in range(b5)]
    fonk1(b6)
    print("Sorted list is:", b6)
if b7 = = "__main__":
    fonk3()