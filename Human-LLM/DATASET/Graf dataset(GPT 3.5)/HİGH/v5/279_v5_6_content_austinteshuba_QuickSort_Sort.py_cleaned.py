def fonk1(arr, start, end):
    b1 = arr[start]
    b2 = start + 1
    b3 = end
    while True:
        while b2 <= b3 and arr[b2] <= b1:
            b2 += 1
        while arr[b3] >= b1 and b3 >= b2:
            b3 -= 1
        if b3 < b2:
            break
        else:
            arr[b2], arr[b3] = arr[b3], arr[b2]
    arr[start], arr[b3] = arr[b3], arr[start]
    return b3
def fonk2(arr, start, end):
    if start < end:
        b4 = fonk1(arr, start, end)
        fonk2(arr, start, b4 - 1)
        fonk2(arr, b4 + 1, end)
    return arr
def fonk3():
    with open("list.txt", "r") as file:
        b5 = [int(line.strip()) for line in file.readlines()]
    b6 = fonk2(b5, 0, len(b5) - 1)
    print(b6)
if b7 = = "__main__":
    fonk3()