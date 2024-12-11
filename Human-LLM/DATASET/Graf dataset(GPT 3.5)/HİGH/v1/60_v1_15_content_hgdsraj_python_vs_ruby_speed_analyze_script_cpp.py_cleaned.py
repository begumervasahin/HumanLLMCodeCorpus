with open('cpp_res.txt') as f:
    b1 = f.readlines()
b2 = []
for line in b1:
    if "real" in line:
        b2.append(float(line.split()[1]))
b3 = sum(b2) / len(b2)
print("The average was")
print(b3)
print("seconds")