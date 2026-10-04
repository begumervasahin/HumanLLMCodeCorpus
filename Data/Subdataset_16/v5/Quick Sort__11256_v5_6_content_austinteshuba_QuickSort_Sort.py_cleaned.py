def fonk1(arr, start, end):
    b1 = arr[start]
    b2 = start + 1
    b3 = end
    b4 = False
    while not b4:
        while b2 <= b3 and arr[b2] <= b1:
            b2 += 1
        while b3 >= b2 and arr[b3] >= b1:
            b3 -= 1
        if b3 < b2:
            b4 = True
        else:
            arr[b2], arr[b3] = arr[b3], arr[b2]
    arr[start], arr[b3] = arr[b3], arr[start]
    return b3
def fonk2(arr, start, end):
    global a1
    if start < end:
        a1 += end - start
        b5 = fonk1(arr, start, end)
        a1 += abs(start - (b5 - 1))
        fonk2(arr, start, b5 - 1)
        a1 += abs((b5 + 1) - end)
        fonk2(arr, b5 + 1, end)
    return arr
def fonk3(b6):
    with open(b6, "r") as file:
        return [int(line.strip()) for line in file]
def fonk4():
    b6 = "list.txt"
    b7 = fonk3(b6)
    b8 = fonk2(b7, 0, len(b7) - 1)
    print("Sorted List:", b8)
    print("Total Operations:", a1)
if b9 = = "__main__":
    a1 = 0
    fonk4()