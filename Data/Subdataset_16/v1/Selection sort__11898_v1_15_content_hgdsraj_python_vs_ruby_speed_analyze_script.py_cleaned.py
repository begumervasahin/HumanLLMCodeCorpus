
with open('pyt_res.txt') as f:
    b1 = f.readlines()
b2 = []
for line in b1:
    if "real" in line:
        b2.append(line[9:12])
a1 = 0
for value in b2:
    a1 += float(value) / 1000
b3 = a1 / 40
print("The b3 was")
print(b3)
print("seconds")