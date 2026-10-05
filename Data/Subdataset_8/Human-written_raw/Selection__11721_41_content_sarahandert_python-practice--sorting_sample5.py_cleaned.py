
import random
import time
def generate_nums(filename, n):
    random.seed(0)
    f = open(filename, 'w')
    counter = 0
    while counter < n:
        f.write(str(random.randrange(0,100)) + "\n")
        counter += 1
    f.close()
def merge( left, right ):
    aList = []
    lt = 0
    rt = 0
    while lt < len( left ) and rt < len( right ):
        if left[ lt ] < right[ rt ]:
            aList.append( left[ lt ]  )
            lt += 1
        else:
            aList.append( right[ rt ] )
            rt += 1
    while lt < len(left):
        aList.append( left[ lt ] )
        lt += 1
    while rt < len( right ):
        aList.append( right[ rt ] )
        rt += 1
    return aList
def merge_sort( aList ):
    if len( aList ) <= 1:
        return aList
    else:
        mid = len( aList )
        left = merge_sort( aList[ :mid ] )
        right = merge_sort( aList[mid:] )
        return merge( left, right )
def selection_sort( aList ):
  n = len( aList )
  for i in range( n - 1 ):
    smallNdx = i
    for j in range( i + 1, n ):
      if aList[ j ] < aList[ smallNdx ] :
        smallNdx = j
    tmp = aList[ i ]
    aList[ i ] = aList[ smallNdx ]
    aList[ smallNdx ] = tmp
  return aList
def analyze_mergesort(inputfile, outputfile):
    t = time.time()
    f = open(inputfile, 'r')
    lst = f.readlines()
    f.close()
    t1 = time.time()
    time_difference1 = t1 - t
    print("It took", round(time_difference1, 6), "seconds to input values from file", inputfile)
    t = time.time()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    sorted_lst = merge_sort(lst)
    t1 = time.time()
    time_difference2 = t1 - t
    print("It took", round(time_difference2, 6), "seconds to sort", n, "values using merge sort")
    t = time.time()
    f = open(outputfile, 'w')
    for i in range(len(sorted_lst)):
        sorted_lst[i] = str(sorted_lst[i])
        f.write(sorted_lst[i] + "\n")
    f.close()
    t1 = time.time()
    time_difference3 = t1 - t
    print("It took", round(time_difference3, 6), "seconds to output", n, "sorted values to file", outputfile)
    print("Total time the program took is", round((time_difference1 + time_difference2 + time_difference3), 6), "seconds")
    print()
def analyze_selection(inputfile, outputfile):
    t = time.time()
    f = open(inputfile, 'r')
    lst = f.readlines()
    f.close()
    t1 = time.time()
    time_difference1 = t1 - t
    print("It took", round(time_difference1, 6), "seconds to input values from file", inputfile)
    t = time.time()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    sorted_lst = selection_sort(lst)
    t1 = time.time()
    time_difference2 = t1 - t
    print("It took", round(time_difference2, 6), "seconds to sort", n, "values using selection sort")
    t = time.time()
    f = open(outputfile, 'w')
    for i in range(len(sorted_lst)):
        sorted_lst[i] = str(sorted_lst[i])
        f.write(sorted_lst[i] + "\n")
    f.close()
    t1 = time.time()
    time_difference3 = t1 - t
    print("It took", round(time_difference3, 6), "seconds to output", n, "sorted values to file", outputfile)
    print("Total time the program took is", round((time_difference1 + time_difference2 + time_difference3), 6), "seconds")
filename = input('Enter the filename: ')
n = int(input('Enter number of values: '))
generate_nums(filename, n)
inputfile = filename
outputfile = input('Please enter output file name: ')
analyze_mergesort(inputfile, outputfile)
analyze_selection(inputfile, outputfile)