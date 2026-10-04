import random
n = 100000
filename = "Descending_100000"
number_list = list(range(n, 0, -1))
with open(filename, "w") as f:
    for number in number_list:
        f.write(f"{number}\n")