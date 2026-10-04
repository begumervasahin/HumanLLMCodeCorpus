
with open('pyt_res.txt') as f:
    b1 = f.readlines()
b2 = []
for line in b1:
    if "real" in line:
        b3 = float(line.split()[1][:-1]) / 1000
        b2.append(b3)
b4 = sum(b2) / len(b2)
print("The average was")
print(f"{b4:.3f} seconds")