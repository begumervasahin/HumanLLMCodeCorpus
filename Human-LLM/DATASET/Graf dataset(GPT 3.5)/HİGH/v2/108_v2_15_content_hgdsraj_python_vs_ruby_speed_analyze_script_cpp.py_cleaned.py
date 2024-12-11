
with open('cpp_res.txt') as file:
    b1 = file.readlines()
b2 = []
for line in b1:
    if "real" in line:
        b3 = float(line.split()[1])
        b2.append(b3)
b4 = sum(b2) / len(b2)
print("The average time was:")
print(b4)
print("seconds")