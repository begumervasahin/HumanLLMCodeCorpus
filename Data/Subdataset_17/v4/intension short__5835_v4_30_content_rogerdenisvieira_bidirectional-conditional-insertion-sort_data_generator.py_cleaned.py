import numpy as np
import csv
TEST_SIZE = 7000
STEP = 1
DATA_FILENAME = 'distributions.csv'
def write_data(values, filename):
    fieldnames = ['uniform', 'binomial', 'poisson', 'normal']
    print('Writing data to file...')
    with open(filename, 'w', newline='') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(values)
    print('Data writing complete.')
def generate_distributions(test_size):
    uniform_dist = np.random.uniform(-1, 1, test_size)
    binomial_dist = np.random.binomial(1000, 0.5, test_size)
    poisson_dist = np.random.poisson(1000, test_size)
    normal_dist = np.random.normal(0, 0.1, test_size)
    distributions_list = [
        {
            'uniform': uniform_dist[i],
            'binomial': binomial_dist[i],
            'poisson': poisson_dist[i],
            'normal': normal_dist[i]
        }
        for i in range(0, test_size, STEP)
    ]
    return distributions_list
if __name__ == "__main__":
    distributions = generate_distributions(TEST_SIZE)
    write_data(distributions, DATA_FILENAME)