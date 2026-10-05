import random
import time
import copy
import numpy as np
def quicksort(my_list, start, finish):
  assert type(start) is int, "Starting index must be an integer."
  assert type(finish) is int, "Ending index must be an integer."
  assert finish > start, "Ending index must be greater than starting index."
  assert type(my_list) is list, "List parameter must be a list."
  comparisonIndex = start
  swapIndex = start
  while comparisonIndex != finish:
    if my_list[comparisonIndex] <= my_list[finish]:
      my_list[comparisonIndex], my_list[swapIndex] = \
        my_list[swapIndex], my_list[comparisonIndex]
      swapIndex += 1
    comparisonIndex += 1
  my_list[swapIndex], my_list[finish] = my_list[finish], my_list[swapIndex]
  if start < swapIndex - 1:
    quicksort(my_list, start, swapIndex - 1)
  if swapIndex + 1 < finish:
    quicksort(my_list, swapIndex + 1, finish)
listLength = 0
firstNumber = 0
lastNumber = 0
errorMessage = "Invalid number entered. Please try again.\n"
while True:
  listLength = raw_input(str("\nEnter the length of the list of random " +
                             "numbers to be generated.\n"))
  if listLength.isdigit():
    listLength = int(listLength)
    break
  else:
    print errorMessage
while True:
  firstNumber = raw_input(str("\nEnter the smallest number in the range of " +
                              "random numbers to be generated.\n"))
  if firstNumber.isdigit():
    firstNumber = int(firstNumber)
    break
  else:
    print errorMessage
while True:
  lastNumber = raw_input(str("\nEnter the largest number in the range of " +
                             "random numbers to be generated.\n"))
  if lastNumber.isdigit():
    lastNumber = int(lastNumber)
    break
  else:
    print errorMessage
print "\nGenerating a list of random numbers of length " , listLength, ", "
print "with numbers between ", firstNumber, " and " , lastNumber , ".\n"
randList1 = []
for i in range(0,listLength):
  randList1.append(random.randrange(firstNumber, lastNumber))
randList2 = copy.deepcopy(randList1)
randList3 = copy.deepcopy(randList1)
randList4 = copy.deepcopy(randList1)
my_file = open("generatedLists.txt", "w")
banner = "=================================================================\n"
my_file.write(banner)
my_file.write("randList unsorted is:\n")
my_file.write(banner)
for item in randList1:
  my_file.write("%s\n" % item)
for item in randList1:
  my_file.write("%s\n" % item)
print "Beginning quicksort...\n"
startTime = time.clock()
randomIndex = random.randrange(0, len(randList1) - 1)
randList2[randomIndex], randList2[len(randList2) - 1] = \
  randList2[len(randList1) - 1], randList2[randomIndex]
quicksort(randList2, 0, len(randList2) - 1)
endTime = time.clock()
print "Total elapsed quicksort time is: %.3fs" % (endTime - startTime) , "\n"
my_file.write(banner)
my_file.write("randList after quicksort sorting is:\n")
my_file.write(banner)
for item in randList2:
  my_file.write("%s\n" % item)
startTime = time.clock()
randList3 = randList3.sort()
endTime = time.clock()
print "Total elapsed built-in Python sorter is: %.3fs" % (endTime - startTime) \
  , "\n"
startTime = time.clock()
randList4 = np.sort(randList4)
endTime = time.clock()
print "Total elapsed time for np sorter is: %.3fs" % (endTime - startTime) \
  , "\n"