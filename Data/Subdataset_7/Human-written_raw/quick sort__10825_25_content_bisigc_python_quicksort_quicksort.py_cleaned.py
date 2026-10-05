def fonk1(A,l,r):
	if l < r:
		b1 = A[l]
		b2 = l
		for i in range(l+1, r):
			if A[i] < b1:
				b2 = b2 + 1
				A[b2], A[i] = A[i], A[b2]
		A[l], A[b2] = A[b2], A[l]
		fonk1(A, l, b2 - 1)
		fonk1(A, b2 + 1, r)