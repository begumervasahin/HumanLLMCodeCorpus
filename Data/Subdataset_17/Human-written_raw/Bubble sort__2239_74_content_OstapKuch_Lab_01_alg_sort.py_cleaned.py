from Student import Student
comparasion_times = 0
swap_times = 0
def buble_sort(arr):
  global comparasion_times, swap_times
  bool_ckeck = False
  for row in range(len(arr)-1):
    comparasion_times += 1
    if int(arr[row].rating) < int(arr[row+1].rating):
      swap_times += 1
      temporary = arr[row]
      arr[row] = arr[row+1]
      arr[row+1] = temporary
      bool_ckeck = True
  if bool_ckeck:
    buble_sort(arr)
  else:
    print("BubbleSort  \nComparasion times: ", comparasion_times, "\nSwap times: ", swap_times)
    comparasion_times = 0
    swap_times = 0
def partitioning(pivot_index, smaller_element, end_element, arr):
  global swap_times, comparasion_times
  arr[pivot_index], arr[smaller_element] = arr[smaller_element], arr[pivot_index]
  if smaller_element+1 == end_element:
    comparasion_times += 1
    if int(arr[smaller_element].growth) > int(arr[end_element-1].growth):
      arr[end_element], arr[smaller_element] = arr[smaller_element], arr[end_element]
      swap_times += 1
  if(smaller_element < end_element):
    if pivot_index != smaller_element:
        quick_sort(pivot_index, smaller_element, arr)
    if smaller_element+1 != end_element:
      quick_sort(smaller_element+1, end_element, arr)
def quick_sort(start_element, end_element, arr):
  global swap_times, comparasion_times
  pivot_index=start_element
  swap_index = start_element
  smaller_element = start_element
  for column in range(start_element, end_element):
    comparasion_times += 1
    if int(arr[column].growth) < int(arr[pivot_index].growth):
      smaller_element = column
    else:
      larger_element = column
      if swap_index == start_element:
        swap_index = larger_element
    if smaller_element > larger_element & larger_element != start_element:
      arr[swap_index], arr[smaller_element] = arr[smaller_element], arr[swap_index]
      smaller_element = swap_index
      swap_index = smaller_element +1
      swap_times += 1
  partitioning(pivot_index, smaller_element, end_element, arr)