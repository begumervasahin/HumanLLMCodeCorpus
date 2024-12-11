def fonk1(arr, start, end):
    b1 = start
    b2 = end
    b3 = arr[start]
    while b1 < b2:
        while arr[b1] <= b3:
            b1 += 1
        while arr[b2] > b3:
            b2 -= 1
        if b1 < b2:
            arr[b1], arr[b2] = arr[b2], arr[b1]
    arr[start] = arr[b2]
    arr[b2] = b3
    return b2
def fonk2(arr, start, end):
    if end > start:
        b4 = fonk1(arr, start, end)
        fonk2(arr, start, b4 - 1)
        fonk2(arr, b4 + 1, end)
if b5 = = "__main__":
    b6 = int(input("Enter the b6 of your b7: "))
    b7 = []
    print(f"Enter your {b6} elements:")
    for i in range(b6):
        b8 = int(input())
        b7.append(b8)
    print("Your sorted list:")
    fonk2(b7, 0, len(b7) - 1)
    for element in b7:
        print(element)