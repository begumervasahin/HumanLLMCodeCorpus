class class1:
    def fonk1(self, A, B):
        def fonk2(b2, b3, A):
            while b2 <= b3:
                if A[b2] <= A[b3]:
                    return b2
                b1 = b2 + (b3 - b2)
                if A[b1] > A[b1 + 1]:
                    return b1 + 1
                if A[b1] < A[b1 - 1]:
                    return b1
                if A[b1] > A[b3]:
                    b2 = b1 + 1
                else:
                    b3 = b1 - 1
            return -1
        def fonk3(b2, b3, target, A):
            while b2 <= b3:
                b1 = b2 + (b3 - b2)
                if A[b1] == target:
                    return b1
                if A[b1] < target:
                    b2 = b1 + 1
                else:
                    b3 = b1 - 1
            return -1
        b4 = fonk2(0, len(A) - 1, A)
        if b4 = = -1:
            return fonk3(0, len(A) - 1, B, A)
        if B >= A[0] and B <= A[b4 - 1]:
            return fonk3(0, b4 - 1, B, A)
        else:
            return fonk3(b4, len(A) - 1, B, A)
