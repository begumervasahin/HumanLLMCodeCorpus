class class1:
    def fonk1(self, A, B):
       def fonk2(start,end,A):
          b1 = start + (end-start)
          if len(A) <3:
            return start
          if A[b1] < A[b1-1] and A[b1] < A[b1+1]:
            return b1
          elif A[b1] > A[b1-1] and A[b1] > A[b1+1]:
            return b1
          elif A[b1] > A[len(A)-1]:
            return fonk2(b1,len(A),A)
          elif A[b1] < A[0]:
            return fonk2(start,b1,A)
          else:
            return -1
       def fonk3(start,end,b2,A):
          b1 = start + (end-start)
          if b2 = = A[b1]:
            return b1
          if end-start < 3:
            if b2 = = A[start]:
              return start
            elif b2 = = A[end]:
      	      return end
      	    else:
      	       return -1
      	  elif b2 > A[b1]:
      	      return fonk3(b1,end,b2,A)
          else:
      	    return fonk3(start,b1,b2,A)
       b2 = B
       b3 = fonk2(0,len(A)-1,A)
       if b3 = = -1:
           return fonk3(0,len(A)-1,b2,A)
       else:
           b4 = fonk3(0,b3-1,b2,A)
           if b4 != -1:
               return b4
           else:
               b4 = fonk3(b3,len(A)-1,b2,A)
               return b4