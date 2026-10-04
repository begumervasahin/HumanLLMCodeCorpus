
with open('pyt_res.txt') as file:
    lines = file.readlines()
times = []
for line in lines:
    if "real" in line:
        time_str = line.split()[1][:-1]
        time_value = float(time_str) / 1000
        times.append(time_value)
average_time = sum(times) / len(times) if times else 0
print("The average time was")
print(f"{average_time:.3f} seconds")