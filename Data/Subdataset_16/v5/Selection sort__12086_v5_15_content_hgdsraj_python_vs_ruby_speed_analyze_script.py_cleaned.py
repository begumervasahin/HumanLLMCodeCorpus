
with open('pyt_res.txt') as file:
    b1 = file.readlines()
b2 = []
for line in b1:
    if "real" in line:
        b3 = line.split()[1][:-1]
        b4 = float(b3) / 1000
        b2.append(b4)
b5 = sum(b2) / len(b2) if b2 else 0
print("The average time was")
print(f"{b5:.3f} seconds")