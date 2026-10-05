def extract_average_time_from_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    times = []
    for line in lines:
        if "real" in line:
            time_str = line[9:12]
            times.append(float(time_str))
    total_time = sum(times)
    average_time = total_time / len(times)
    return average_time
if __name__ == "__main__":
    file_path = 'cpp_res.txt'
    average_time = extract_average_time_from_file(file_path)
    print("The average time was:")
    print(average_time, "seconds")