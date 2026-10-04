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
            b2.append(float(line[9:12]) / 1000)
    return b2
def fonk2(b2):
    if not b2:
        return 0.0
    b3 = sum(b2)
    return b3 / len(b2)
b2 = fonk1('pyt_res.txt')
b4 = fonk2(b2)
print("The b4 was:")
print(f"{b4:.3f} seconds")