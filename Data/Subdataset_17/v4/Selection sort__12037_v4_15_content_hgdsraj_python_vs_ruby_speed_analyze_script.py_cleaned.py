
with open('pyt_res.txt') as f:
    lines = f.readlines()
times = []
for line in lines:
    if "real" in line:
        time_value = float(line.split()[1][:-1]) / 1000
        times.append(time_value)
average_time = sum(times) / len(times)
print("The average was")
print(f"{average_time:.3f} seconds")