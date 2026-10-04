def read_values_from_file(filename):
    """
    Read and extract values from a file containing lines with the word "real".
    Parameters:
    filename (str): The name of the file to read from.
    Returns:
    list: A list of extracted float values.
    """
    with open(filename) as file:
        lines = file.readlines()
    values = []
    for line in lines:
        if "real" in line:
            values.append(float(line[9:12]) / 1000)
    return values
def calculate_average(values):
    if not values:
        return 0.0
    total_sum = sum(values)
    return total_sum / len(values)
values = read_values_from_file('pyt_res.txt')
average = calculate_average(values)
print("The average was:")
print(f"{average:.3f} seconds")