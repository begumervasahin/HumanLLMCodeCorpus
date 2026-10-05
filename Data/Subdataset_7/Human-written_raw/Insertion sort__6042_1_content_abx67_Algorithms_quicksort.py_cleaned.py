def fonk1(A,left,right):
    if left>=right:
        return right
    else:
        b1 = left
        b2 = A[right]
        print("b2",b2)
        for i in range(left,right+1):
            print("i",i)
            if A[i]<=b2 :
                if i!=b1 :
                    b3 = A[i]
                    A[i]=A[b1]
                    A[b1]=b3
                b1 = b1+1
        return b1-1
def fonk2(A,left,right):
    if right!=left:
        b1 = fonk1(A,left,right)
        print("b1:",b1,"left",left,"right",right)
        print("A",A)
        if b1 >= left + 1:
            fonk2(A,left,b1-1)
        if b1 <= right - 1:
            fonk2(A,b1+1,right)
    else:
        return