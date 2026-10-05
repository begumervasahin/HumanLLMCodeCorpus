def read_estimated_data(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        g = float(lines[-2].strip().split("=")[1])
        b = float(lines[-1].strip().split("=")[1])
    return g, b
def estimate_real(g, b, x):
    return b * (g ** x)
def estimate_fastest(x):
    return (210 * (x ** 2) + 1060 * x - 1410) * (10 ** -9)
def estimate_slowest(x):
    return (2650 * (x ** 3) + 1060 * x - 1410) * (10 ** -9)
def write_quantum_data(file_path, all_times_real, all_times_fastest, all_times_slowest):
    with open(file_path, "w") as file:
        file.write("estimated_extended_data=[{\n")
        file.write("".join(['"bits":' + str(x) + ',\n"time":' + str(all_times_real[x]) + "\n},{\n" for x in range(4, highest + 4, 4)])[:-3])
        file.write("];\n")
        file.write("fastest_data=[{\n")
        file.write("".join(['"bits":' + str(x) + ',\n"time":' + str(all_times_fastest[x]) + "\n},{\n" for x in range(4, highest + 4, 4)])[:-3])
        file.write("];\n")
        file.write("slowest_data=[{\n")
        file.write("".join(['"bits":' + str(x) + ',\n"time":' + str(all_times_slowest[x]) + "\n},{\n" for x in range(4, highest + 4, 4)])[:-3])
        file.write("];\n")
def main():
    RESULT_FILE_PATH = "results/estimated_datafile.js"
    OUTPUT_FILE_PATH = "results/quantum_datafile.js"
    HIGHEST_BIT_SIZE = 2048
    g, b = read_estimated_data(RESULT_FILE_PATH)
    all_times_real = {x: estimate_real(g, b, x) for x in range(4, HIGHEST_BIT_SIZE + 4, 4)}
    all_times_fastest = {x: estimate_fastest(x) for x in range(4, HIGHEST_BIT_SIZE + 4, 4)}
    all_times_slowest = {x: estimate_slowest(x) for x in range(4, HIGHEST_BIT_SIZE + 4, 4)}
    write_quantum_data(OUTPUT_FILE_PATH, all_times_real, all_times_fastest, all_times_slowest)
if __name__ == "__main__":
    main()