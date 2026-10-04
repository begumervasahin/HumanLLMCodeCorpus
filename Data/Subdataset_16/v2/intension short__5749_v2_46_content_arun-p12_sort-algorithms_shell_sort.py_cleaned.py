def fonk1(A, b1 = 0, desc=0):
    def fonk2(A, b5):
        for i in range(b5, len(A)):
            b2 = A[i]
            b3 = i
            while b3 >= b5 and A[b3 - b5] > b2:
                A[b3] = A[b3 - b5]
                b3 -= b5
            A[b3] = b2
    b4 = len(A)
    b5 = b4
    while b5 > 0:
        if b1:
            print(f"Current b5: {b5}")
        fonk2(A, b5)
        b5
    if desc:
        A.reverse()
    return A
if b6 = = "__main__":
    b7 = [19, 2, 31, 45, 6, 11, 121, 27]
    b8 = fonk1(b7, b1=1)
    print("Sorted array:", b8)