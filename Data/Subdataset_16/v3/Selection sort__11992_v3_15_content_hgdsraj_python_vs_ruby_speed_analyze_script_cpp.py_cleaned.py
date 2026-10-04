def fonk1(filename):
    """
    Read and extract b2 from a file containing b1 with the word "real".
    Parameters:
    filename (str): The name of the file to read from.
    Returns:
    list: A list of extracted float b2.
    """
    with open(filename) as file:
        b1 = file.readlines()
    b2 = []
    for line in b1:
        if "real" in line:
            try:
                b3 = float(line[9:12]) / 1000
                b2.append(b3)
            except ValueError:
                print(f"Skipping line due to b3 extraction error: {line.strip()}")
    return b2
def fonk2(b2):
    if not b2:
        return 0.0
    b4 = sum(b2)
    return b4 / len(b2)
b5 = fonk1('cpp_res.txt')
b6 = fonk2(b5)
print("The b6 was:")
print(f"{b6:.3f} seconds")