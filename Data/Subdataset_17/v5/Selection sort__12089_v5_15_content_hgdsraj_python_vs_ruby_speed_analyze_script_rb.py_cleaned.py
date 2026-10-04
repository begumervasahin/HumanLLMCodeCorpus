def read_and_extract_times(filename):
    """
    Reads the file and extracts time values from lines containing "real".
    Parameters:
    filename (str): The name of the file to be read.
    Returns:
    list: A list of extracted time values in seconds.
    """
    with open(filename) as file:
        lines = file.readlines()
    times = []
    for line in lines:
        if "real" in line:
            time_value = float(line.split()[1][:-1]) / 1000
            times.append(time_value)
    return times
def calculate_average(times):
    return sum(times) / len(times) if times else 0
def main():
    times = read_and_extract_times('ruby_res.txt')
    average_time = calculate_average(times)
    print("The average time was")
    print(f"{average_time:.3f} seconds")
if __name__ == "__main__":
    main()