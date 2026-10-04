def fonk1(arr, b1 = 0, descending=False):
    def fonk2(low, high):
        b2 = arr[low]
        b3 = low + 1
        b4 = high
        while True:
            while b3 <= b4 and arr[b3] <= b2:
                b3 += 1
            while b3 <= b4 and arr[b4] > b2:
                b4 -= 1
            if b3 <= b4:
                arr[b3], arr[b4] = arr[b4], arr[b3]
                if b1 = = 2:
                    print(f"Sub-array after swap: b2 = {b2}, b3={b3}, b4={b4} :: {arr}")
            else:
                break
        arr[low], arr[b4] = arr[b4], arr[low]
        return b4
    def fonk3(low, high):
        if low < high:
            b5 = fonk2(low, high)
            if b1:
                print(f"Partition b6 = {b5}, low={low}, high={high} :: {arr}")
            fonk3(low, b5 - 1)
            fonk3(b5 + 1, high)
    fonk3(0, len(arr) - 1)
    if descending:
        arr.reverse()
    return arr
if b7 = = "__main__":
    b8 = [24, 3, 45, 12, 56, 18, 39, 17, 8]
    b9 = fonk1(b8, b1=1, descending=False)
    print("Sorted array:", b9)