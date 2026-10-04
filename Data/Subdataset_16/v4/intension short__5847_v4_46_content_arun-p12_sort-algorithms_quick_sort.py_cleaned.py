def fonk1(A, b1 = 0, desc=0):
    def fonk2(low, high):
        b2 = A[low]
        b3 = low + 1
        b4 = high
        while True:
            while b3 <= b4 and A[b3] <= b2:
                b3 += 1
            while b3 <= b4 and A[b4] > b2:
                b4 -= 1
            if b3 <= b4:
                A[b3], A[b4] = A[b4], A[b3]
                if b1 = = 2:
                    print("  sub:", b2, b3, b4, " :: ", A)
            else:
                break
        A[low], A[b4] = A[b4], A[low]
        return b4
    def fonk3(low, high):
        if low < high:
            b5 = fonk2(low, high)
            if b1:
                print("iter :", b5, low, high, " :: ", A)
            fonk3(low, b5 - 1)
            fonk3(b5 + 1, high)
    fonk3(0, len(A) - 1)
    if desc:
        A.reverse()
    return A