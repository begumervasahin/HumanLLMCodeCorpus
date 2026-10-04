import random
import time
import copy
import numpy as np
def fonk1(my_list, start, finish):
  assert type(start) is int, "Starting index must be an integer."
  assert type(finish) is int, "Ending index must be an integer."
  assert finish > start, "Ending index must be greater than starting index."
  assert type(my_list) is list, "List parameter must be a list."
  b1 = start
  b2 = start
  while b1 != finish:
    if my_list[b1] <= my_list[finish]:
      my_list[b1], my_list[b2] = \
        my_list[b2], my_list[b1]
      b2 += 1
    b1 += 1
  my_list[b2], my_list[finish] = my_list[finish], my_list[b2]
  if start < b2 - 1:
    fonk1(my_list, start, b2 - 1)
  if b2 + 1 < finish:
    fonk1(my_list, b2 + 1, finish)
a1 = 0
a2 = 0
a3 = 0
b3 = "Invalid number entered. Please try again.\n"
while True:
  a1 = raw_input(str("\nEnter the length of the list of random " +
                             "numbers to be generated.\n"))
  if a1.isdigit():
    a1 = int(a1)
    break
  else:
    print b3
while True:
  a2 = raw_input(str("\nEnter the smallest number in the range of " +
                              "random numbers to be generated.\n"))
  if a2.isdigit():
    a2 = int(a2)
    break
  else:
    print b3
while True:
  a3 = raw_input(str("\nEnter the largest number in the range of " +
                             "random numbers to be generated.\n"))
  if a3.isdigit():
    a3 = int(a3)
    break
  else:
    print b3
print "\nGenerating a list of random numbers of length " , a1, ", "
print "with numbers between ", a2, " and " , a3 , ".\n"
b4 = []
for i in range(0,a1):
  b4.append(random.randrange(a2, a3))
b5 = copy.deepcopy(b4)
b6 = copy.deepcopy(b4)
b7 = copy.deepcopy(b4)
b8 = open("generatedLists.txt", "w")
b9 = "=================================================================\n"
b8.write(b9)
b8.write("randList unsorted is:\n")
b8.write(b9)
for item in b4:
  b8.write("%s\n" % item)
for item in b4:
  b8.write("%s\n" % item)
print "Beginning quicksort...\n"
b10 = time.clock()
b11 = random.randrange(0, len(b4) - 1)
b5[b11], b5[len(b5) - 1] = \
  b5[len(b4) - 1], b5[b11]
fonk1(b5, 0, len(b5) - 1)
b12 = time.clock()
print "Total elapsed quicksort time is: %.3fs" % (b12 - b10) , "\n"
b8.write(b9)
b8.write("randList after quicksort sorting is:\n")
b8.write(b9)
for item in b5:
  b8.write("%s\n" % item)
b10 = time.clock()
b6 = b6.sort()
b12 = time.clock()
print "Total elapsed built-in Python sorter is: %.3fs" % (b12 - b10) \
  , "\n"
b10 = time.clock()
b7 = np.sort(b7)
b12 = time.clock()
print "Total elapsed time for np sorter is: %.3fs" % (b12 - b10) \
  , "\n"