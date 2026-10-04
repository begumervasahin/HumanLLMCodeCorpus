def fonk1(A):
    try:
        b2, b1 = A[0], 0
        for i in range(1, len(A)):
            if (A[i] < b2):
                b2 = A[i]
                b1 = i
        return (b2, b1)
    except:
        print("List expected. Got : ", A)
        exit(1)
def fonk2(A):
    try:
        b3, b1 = A[0], 0
        for i in range(1, len(A)):
            if (A[i] > b3):
                b3 = A[i]
                b1 = i
        return (b3, b1)
    except:
        print("List expected. Got : ", A)
        exit(1)
def fonk3(b5, b6):
    b4 = b5
    b5 = b6
    b6 = b4
    return(b5, b6)