def read_and_process_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    times = []
    for line in lines:
        if "real" in line:
            time_value = float(line.split()[1]) / 1000
            times.append(time_value)
    return times
def calculate_average(times):
    return sum(times) / len(times)
def main():
    times = read_and_process_file('cpp_res.txt')
    average_time = calculate_average(times)
    print("The average was")
    print(f"{average_time:.3f} seconds")
if __name__ == "__main__":
    main()