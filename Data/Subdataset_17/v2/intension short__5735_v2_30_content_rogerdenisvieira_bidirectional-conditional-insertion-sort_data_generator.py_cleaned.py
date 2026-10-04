import numpy as np
import csv
TEST_SIZE = 7000
STEP = 1
DATA_FILENAME = 'distributions.csv'
FIELDNAMES = ['uniform', 'binominal', 'poisson', 'normal']
def generate_distributions(size):
    uniform = np.random.uniform(-1, 1, size)
    binominal = np.random.binomial(1000, 0.5, size)
    poisson = np.random.poisson(1000, size)
    normal = np.random.normal(0, 0.1, size)
    return uniform, binominal, poisson, normal
def assemble_data(uniform, binominal, poisson, normal, step):
    data = []
    for i in range(0, len(uniform) - 1, step):
        data.append({
            'uniform': uniform[i],
            'binominal': binominal[i],
            'poisson': poisson[i],
            'normal': normal[i]
        })
    return data
def write_to_csv(data, filename, fieldnames):
    print('Writing data to CSV...')
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
def main():
    uniform, binominal, poisson, normal = generate_distributions(TEST_SIZE)
    data = assemble_data(uniform, binominal, poisson, normal, STEP)
    write_to_csv(data, DATA_FILENAME, FIELDNAMES)
if __name__ == "__main__":
    main()