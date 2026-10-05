
with open('cpp_res.txt') as f:
    lines = f.readlines()
times = []
for line in lines:
    if "real" in line:
        time_str = line[9:12]
        times.append(float(time_str))
total_time = sum(times)
average_time = total_time / len(times)
print("The average time was:")
print(average_time, "seconds")