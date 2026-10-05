import random
def generate_configuration(algorithm, size, length):
    configurations = []
    for _ in range(length):
        array = random.sample(range(1000000000, 9999999999), size)
        configurations.append(array)
    filename = f'conf{size}Inicial{algorithm}.txt'
    with open(filename, 'a') as file:
        for config in configurations:
            file.write(str(config) + '\n')
    return configurations
def main():
    algorithms = ['A', 'B', 'C', 'D', 'E', 'F']
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    lengths = [100000, 10000, 1000, 100, 10, 1]
    for algorithm, size, length in zip(algorithms, sizes, lengths):
        generate_configuration(algorithm, size, length)
        print(f'Configuration {algorithm} generated.')
if __name__ == "__main__":
    main()