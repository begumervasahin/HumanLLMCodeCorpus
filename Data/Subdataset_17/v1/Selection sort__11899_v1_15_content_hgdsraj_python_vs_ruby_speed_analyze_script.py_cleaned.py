
with open('pyt_res.txt') as f:
    lines = f.readlines()
x = []
for line in lines:
    if "real" in line:
        x.append(line[9:12])
y = 0
for value in x:
    y += float(value) / 1000
average = y / 40
print("The average was")
print(average)
print("seconds")