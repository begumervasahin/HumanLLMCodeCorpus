def fonk1(b2):
   for ultimaPos in range(len(b2)-1,0,-1):
       a1 = 0
       for pos in range(1,ultimaPos+1):
           if b2[pos]>b2[a1]:
               a1 = pos
       b1 = b2[ultimaPos]
       b2[ultimaPos] = b2[a1]
       b2[a1] = b1
b2 = [54,26,93,17,77,31,44,55,20]
fonk1(b2)
print(b2)