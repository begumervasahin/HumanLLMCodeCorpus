
import numpy as np
import csv
TEST_SIZE = 7000
DATA_FILENAME = 'distributions.csv'
def write_data(values):
    fieldnames = ['uniform', 'binomial', 'poisson', 'normal']
    print('Writing data...')
    with open(DATA_FILENAME, 'w', newline='') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(values)
    print('Data written successfully.')
def generate_distributions(size):
    uniform_dist = np.random.uniform(-1, 1, size)
    binomial_dist = np.random.binomial(1000, 0.5, size)
    poisson_dist = np.random.poisson(1000, size)
    normal_dist = np.random.normal(0, 0.1, size)
    distributions_list = []
    for i in range(size):
        distributions_list.append({
            'uniform': uniform_dist[i],
            'binomial': binomial_dist[i],
            'poisson': poisson_dist[i],
            'normal': normal_dist[i]
        })
    return distributions_list
def main():
    distributions_list = generate_distributions(TEST_SIZE)
    write_data(distributions_list)
if __name__ == "__main__":
    main()