import time
import sort_numbers
b1 = open("NUM.txt", "r")
b2 = b1.read()
b3 = b2.split(" ")
b4 = len(b3)
for i in range(b4):
	b3[i] = int(b3[i])
b5 = b3
b6 = time.clock()
sort_numbers.bubble_sort(b3)
b7 = time.clock()
b8 = b7 - b6
b9 = time.clock()
sort_numbers.insertion_sort(b5)
b10 = time.clock()
b11 = b10 - b9
b12 = open("BUBBLE_SORTED.txt", "w")
b13 = open("INSERTION_SORTED.txt", "w")
for x in range(b4):
	b12.write(str(b3[x]))
	if x < b4-1:
		b12.write(" ")
	else:
		b12.write("\n")
b14 = "Running time: " + str( b8 ) + "Seconds"
b12.write(b14)
for x in range(b4):
	b13.write(str(b5[x]))
	if x < b4-1:
		b13.write(" ")
	else:
		b13.write("\n")
b15 = "Running time: " + str( b11 ) + "Seconds"
b13.write(b15)