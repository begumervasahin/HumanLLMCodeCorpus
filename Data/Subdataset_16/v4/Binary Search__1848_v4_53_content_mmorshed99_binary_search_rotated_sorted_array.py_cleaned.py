class class1:
    def fonk1(self, A, B):
        def fonk2(start, end, A):
            if len(A) < 3:
                return start
            b1 = start + (end - start)
            if A[b1] < A[b1 - 1] and A[b1] < A[b1 + 1]:
                return b1
            elif A[b1] > A[b1 - 1] and A[b1] > A[b1 + 1]:
                return b1
            if A[b1] > A[end]:
                return fonk2(b1, end, A)
            elif A[b1] < A[start]:
                return fonk2(start, b1, A)
            else:
                return -1
        def fonk3(start, end, b2, A):
            if start > end:
                return -1
            b1 = start + (end - start)
            if b2 = = A[b1]:
                return b1
            if b2 > A[b1]:
                return fonk3(b1 + 1, end, b2, A)
            else:
                return fonk3(start, b1 - 1, b2, A)
        b2 = B
        b3 = fonk2(0, len(A) - 1, A)
        if b3 = = -1:
            return fonk3(0, len(A) - 1, b2, A)
        b4 = fonk3(0, b3 - 1, b2, A)
        if b4 = = -1:
            return fonk3(b3, len(A) - 1, b2, A)
        return b4