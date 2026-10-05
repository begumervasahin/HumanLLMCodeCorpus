
with open('cpp_res.txt') as file:
    lines = file.readlines()
times = []
for line in lines:
    if "real" in line:
        time_value = float(line.split()[1])
        times.append(time_value)
average_time = sum(times) / len(times)
print(f"The average time was: {average_time} seconds")