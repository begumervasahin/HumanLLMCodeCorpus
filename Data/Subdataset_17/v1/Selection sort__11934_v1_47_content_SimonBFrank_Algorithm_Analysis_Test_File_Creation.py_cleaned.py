import random
n = 100000
name = "Descending_100000"
numberList = list(range(n, 0, -1))
with open(name, "w+") as f:
    for number in numberList:
        f.write(str(number) + "\n")