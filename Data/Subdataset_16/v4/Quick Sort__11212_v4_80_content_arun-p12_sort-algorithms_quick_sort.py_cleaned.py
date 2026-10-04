import common as c
def fonk1(arr, b1 = 0, desc=0):
    def fonk2(low, high):
        b2 = arr[low]
        b3 = low
        b4 = high
        while b3 < b4:
            while b3 < high and arr[b3] <= b2:
                b3 += 1
            while b4 > low and arr[b4] > b2:
                b4 -= 1
            if b3 < b4:
                arr[b3], arr[b4] = c.swap(arr[b3], arr[b4])
            if b1 = = 2:
                print("  sub:", b2, b3, b4, " :: ", arr)
        arr[low], arr[b4] = c.swap(arr[low], arr[b4])
        return b4
    def fonk3(low, high):
        if low < high:
            b5 = fonk2(low, high)
            if b1:
                print("iter :", b5, low, high, " :: ", arr)
            fonk3(low, b5 - 1)
            fonk3(b5 + 1, high)
    fonk3(0, len(arr) - 1)
    if desc:
        arr.reverse()
    return arr