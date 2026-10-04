import random
n = 100000
name = "Descending_100000"
f = open(name, "w+")
for i in range(n):
	inputStr = str(numberList[i]) + "\n"
	f.write(inputStr)
f.close()