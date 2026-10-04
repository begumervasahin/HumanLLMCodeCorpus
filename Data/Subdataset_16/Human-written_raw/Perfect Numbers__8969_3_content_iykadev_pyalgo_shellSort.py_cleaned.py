def fonk1(b4):
    b1 = len(b4)
    while b1 > 0:
      for startposition in range(b1):
        fonk2(b4,startposition,b1)
      print("After increments of size",b1,
                                   "The list is",b4)
      b1 = b1
def fonk2(b4,start,gap):
    for i in range(start+gap,len(b4),gap):
        b2 = b4[i]
        b3 = i
        while b3>=gap and b4[b3-gap]>b2:
            b4[b3]=b4[b3-gap]
            b3 = b3-gap
        b4[b3]=b2
b4 = [54,26,93,17,77,31,44,55,20]
fonk1(b4)
print(b4)