
with open('cpp_res.txt') as f:
    b1 = f.readlines()
b2 = []
for line in b1:
    if "real" in line:
        b3 = line[9:12]
        b2.append(float(b3))
b4 = sum(b2)
b5 = b4 / len(b2)
print("The average time was:")
print(b5, "seconds")