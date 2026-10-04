from Student import Student
a1 = 0
a2 = 0
def fonk1(arr):
  global a1, a2
  b1 = False
  for row in range(len(arr)-b3):
    a1 += b3
    if int(arr[row].rating) < int(arr[row+b3].rating):
      a2 += b3
      b2 = arr[row]
      arr[row] = arr[row+b3]
      arr[row+b3] = b2
      b1 = True
  if b1:
    fonk1(arr)
  else:
    print("BubbleSort  \nComparasion times: ", a1, "\nSwap times: ", a2)
    a1 = 0
    a2 = 0
def fonk2(b4, b6, end_element, arr):
  global a2, a1
  arr[b4], arr[b6] = arr[b6], arr[b4]
  if b6+b3 = = end_element:
    a1 += b3
    if int(arr[b6].growth) > int(arr[end_element-b3].growth):
      arr[end_element], arr[b6] = arr[b6], arr[end_element]
      a2 += b3
  if(b6 < end_element):
    if b4 != b6:
        fonk3(b4, b6, arr)
    if b6+b3 != end_element:
      fonk3(b6+b3, end_element, arr)
def fonk3(start_element, end_element, arr):
  global a2, a1
  b4 = start_element
  b5 = start_element
  b6 = start_element
  for column in range(start_element, end_element):
    a1 += b3
    if int(arr[column].growth) < int(arr[b4].growth):
      b6 = column
    else:
      b7 = column
      if b5 = = start_element:
        b5 = b7
    if b6 > b7 & b7 != start_element:
      arr[b5], arr[b6] = arr[b6], arr[b5]
      b6 = b5
      b5 = b6 +b3
      a2 += b3
  fonk2(b4, b6, end_element, arr)