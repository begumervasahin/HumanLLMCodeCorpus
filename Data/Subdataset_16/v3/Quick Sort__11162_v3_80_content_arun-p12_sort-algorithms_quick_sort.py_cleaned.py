def fonk1(arr, b1 = 0, desc=0):
    def fonk2(x, y):
        return y, x
    def fonk3(low, high):
        b2 = arr[low]
        b3 = low
        b4 = high
        while b3 < b4:
            while b3 < high and arr[b3] <= b2:
                b3 += 1
            while b4 > low and arr[b4] > b2:
                b4 -= 1
            if b3 < b4:
                arr[b3], arr[b4] = fonk2(arr[b3], arr[b4])
            if b1 = = 2:
                print("  sub:", b2, b3, b4, " :: ", arr)
        arr[low], arr[b4] = fonk2(arr[low], arr[b4])
        return b4
    def fonk4(low, high):
        if low < high:
            b5 = fonk3(low, high)
            if b1 >= 1:
                print("iter:", b5, low, high, "::", arr)
            fonk4(low, b5 - 1)
            fonk4(b5 + 1, high)
    fonk4(0, len(arr) - 1)
    if desc:
        arr.reverse()
    return arr
if b6 = = "__main__":
    b7 = [3, 6, 8, 10, 1, 2, 1]
    b8 = fonk1(b7, b1=1, desc=0)
    print("Sorted list:", b8)