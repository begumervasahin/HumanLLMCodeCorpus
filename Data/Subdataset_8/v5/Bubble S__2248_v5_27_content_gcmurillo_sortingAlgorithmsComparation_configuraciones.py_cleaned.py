import random
def generate_configurations(algorithm, size, num_arrays, file_prefix):
    configurations = []
    for _ in range(num_arrays):
        array = random.sample(range(1000000000, 9999999999), size)
        configurations.append(array)
    filename = f"{file_prefix}{algorithm}.txt"
    with open(filename, 'a') as file_created:
        for config in configurations:
            file_created.write(str(config) + '\n')
    return configurations
def confA(algorithm):
    return generate_configurations(algorithm, 10, 100000, 'confAInicial')
def confB(algorithm):
    return generate_configurations(algorithm, 100, 10000, 'confBInicial')
def confC(algorithm):
    return generate_configurations(algorithm, 1000, 1000, 'confCInicial')
def confD(algorithm):
    return generate_configurations(algorithm, 10000, 100, 'confDInicial')
def confE(algorithm):
    return generate_configurations(algorithm, 100000, 10, 'confEInicial')
def confF(algorithm):
    return generate_configurations(algorithm, 1000000, 1, 'confFInicial')
def main():
    algorithms = ['A', 'B', 'C', 'D', 'E', 'F']
    for algorithm in algorithms:
        confA(algorithm)
        confB(algorithm)
        confC(algorithm)
        confD(algorithm)
        confE(algorithm)
        confF(algorithm)
        print(f"Configurations generated for Algorithm {algorithm}")
if __name__ == "__main__":
    main()