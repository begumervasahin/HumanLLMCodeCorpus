def fonk1(b2):
   for fillslot in range(len(b2)-1,0,-1):
       a1 = 0
       for location in range(1,fillslot+1):
           if b2[location]>b2[a1]:
               a1 = location
       b1 = b2[fillslot]
       b2[fillslot] = b2[a1]
       b2[a1] = b1
b2 = [54,45,67,12,34,98,66]
fonk1(b2)
print(b2)