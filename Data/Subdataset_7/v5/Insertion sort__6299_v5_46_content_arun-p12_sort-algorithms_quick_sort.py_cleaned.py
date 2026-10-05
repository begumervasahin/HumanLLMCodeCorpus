def fonk1(b5, b1 = 0, desc=0):
    def fonk2(left, right):
        b2 = b5[left]
        start, b3 = left, right
        while start < b3:
            while start < right and b5[start] <= b2:
                start += 1
            while b3 > left and b5[b3] > b2:
                b3 -= 1
            if start < b3:
                b5[start], b5[b3] = b5[b3], b5[start]
                if b1 = = 2:
                    print("Swapping:", start, b3, "::", b5)
        b5[left], b5[b3] = b5[b3], b5[left]
        return b3
    def fonk3(left, right):
        if left < right:
            b4 = fonk2(left, right)
            if b1:
                print("Pivot index:", b4, "Left:", left, "Right:", right, "::", b5)
            fonk3(left, b4 - 1)
            fonk3(b4 + 1, right)
    fonk3(0, len(b5) - 1)
    if desc:
        b5 = b5[::-1]
    return b5