def selectionSort(ar):
   for fillslot in range(len(ar) - 1 , 0 , -1):
       positionOfMax = 0
       for location in range(1 , fillslot + 1):
           if ar[location] > ar[positionOfMax]:
               positionOfMax = location
       temp = ar[fillslot]
       ar[fillslot] = ar[positionOfMax]
       ar[positionOfMax] = temp
ar = [54,26,93,17,77,31,44,55,20]
selectionSort(ar)
print("Sorted array is:")
for elements in ar:
    print(elements)