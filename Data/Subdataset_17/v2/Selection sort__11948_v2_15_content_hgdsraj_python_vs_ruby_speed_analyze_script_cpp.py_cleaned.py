
with open('cpp_res.txt') as file:
    lines = file.readlines()
extracted_values = []
for line in lines:
    if "real" in line:
        extracted_values.append(line[9:12])
total_sum = 0
for value in extracted_values:
    total_sum += float(value) / 1000
average = total_sum / len(extracted_values)
print("The average was:")
print(f"{average} seconds")