def fonk1(b2):
   for fillslot in range(len(b2) - 1 , 0 , -1):
       a1 = 0
       for location in range(1 , fillslot + 1):
           if b2[location] > b2[a1]:
               a1 = location
       b1 = b2[fillslot]
       b2[fillslot] = b2[a1]
       b2[a1] = b1
b2 = [54,26,93,17,77,31,44,55,20]
fonk1(b2)
print("Sorted array is:")
for elements in b2:
    print(elements)