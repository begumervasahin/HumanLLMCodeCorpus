def fonk1(b7, b1 = 0, desc=False):
    def fonk2(low, high):
        b2 = b7[low]
        b3 = low + 1
        b4 = high
        while True:
            while b3 <= b4 and b7[b3] <= b2:
                b3 += 1
            while b3 <= b4 and b7[b4] > b2:
                b4 -= 1
            if b3 <= b4:
                b7[b3], b7[b4] = b7[b4], b7[b3]
                if b1 = = 2:
                    print(f"  sub: b2 = {b2}, b3={b3}, b4={b4} :: {b7}")
            else:
                break
        b7[low], b7[b4] = b7[b4], b7[low]
        return b4
    def fonk3(low, high):
        if low < high:
            b5 = fonk2(low, high)
            if b1:
                print(f"iter: b5 = {b5}, low={low}, high={high} :: {b7}")
            fonk3(low, b5 - 1)
            fonk3(b5 + 1, high)
    fonk3(0, len(b7) - 1)
    if desc:
        b7.reverse()
    return b7
if b6 = = "__main__":
    b7 = [24, 3, 45, 12, 56, 18, 39, 17, 8]
    b8 = fonk1(b7, b1=1, desc=False)
    print("Sorted array:", b8)