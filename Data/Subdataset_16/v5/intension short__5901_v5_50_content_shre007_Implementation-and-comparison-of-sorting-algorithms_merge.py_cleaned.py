def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = len(arr)
    b2 = fonk1(arr[:b1])
    b3 = fonk1(arr[b1:])
    return fonk2(b2, b3)
def fonk2(left, right):
    b4 = []
    left_index, b5 = 0, 0
    while left_index < len(left) and b5 < len(right):
        if left[left_index] < right[b5]:
            b4.append(left[left_index])
            left_index += 1
        else:
            b4.append(right[b5])
            b5 += 1
    b4.extend(left[left_index:])
    b4.extend(right[b5:])
    return b4
def fonk3():
    b6 = int(input("Enter the number of elements: "))
    return [int(input(f"Element {i+1}: ")) for i in range(b6)]
if b7 = = "__main__":
    b8 = fonk3()
    b9 = fonk1(b8)
    print("Sorted list:", b9)