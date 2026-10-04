def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = len(arr)
    b2 = fonk1(arr[:b1])
    b3 = fonk1(arr[b1:])
    return fonk2(b2, b3)
def fonk2(left, right):
    b4 = []
    b5 = j = 0
    while b5 < len(left) and j < len(right):
        if left[b5] < right[j]:
            b4.append(left[b5])
            b5 += 1
        else:
            b4.append(right[j])
            j += 1
    b4.extend(left[b5:])
    b4.extend(right[j:])
    return b4
if b6 = = "__main__":
    b7 = int(input("Enter the number of elements: "))
    b8 = [int(input(f"Element {b5+1}: ")) for b5 in range(b7)]
    b4 = fonk1(b8)
    print("Sorted list:", b4)