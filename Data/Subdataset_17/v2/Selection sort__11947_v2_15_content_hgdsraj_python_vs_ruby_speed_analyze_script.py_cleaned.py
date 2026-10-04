
with open('pyt_res.txt') as file:
    lines = file.readlines()
values = []
for line in lines:
    if "real" in line:
        values.append(line[9:12])
total_sum = 0
for value in values:
    total_sum += float(value) / 1000
average = total_sum / len(values)
print("The average was:")
print(f"{average} seconds")