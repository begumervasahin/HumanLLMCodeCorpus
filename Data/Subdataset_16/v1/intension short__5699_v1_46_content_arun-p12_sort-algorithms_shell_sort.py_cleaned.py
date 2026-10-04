def fonk1(A, b1 = 0, desc=0):
    def fonk2(b4, start):
        for i in range(start + b4, len(A), b4):
            b2 = A[i]
            b3 = i
            while b3 >= b4 and A[b3 - b4] > b2:
                A[b3] = A[b3 - b4]
                b3 -= b4
            A[b3] = b2
    b4 = len(A)
    while b4 > 0:
        if b1:
            print(f"Current b4: {b4}")
        for start_position in range(b4):
            fonk2(b4, start_position)
        b4
    if desc:
        A.reverse()
    return A
if b5 = = "__main__":
    b6 = [19, 2, 31, 45, 6, 11, 121, 27]
    b7 = fonk1(b6, b1=1)
    print("Sorted array:", b7)