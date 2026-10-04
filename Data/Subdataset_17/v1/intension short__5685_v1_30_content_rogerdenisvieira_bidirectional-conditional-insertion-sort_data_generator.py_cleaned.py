import numpy as np
import csv
TEST_SIZE = 7000
STEP = 1
DATA_FILENAME = 'distributions.csv'
FIELDNAMES = ['uniform', 'binominal', 'poisson', 'normal']
def generate_distributions(test_size):
    uniform_dist = np.random.uniform(-1, 1, test_size)
    binominal_dist = np.random.binomial(1000, 0.5, test_size)
    poisson_dist = np.random.poisson(1000, test_size)
    normal_dist = np.random.normal(0, 0.1, test_size)
    return uniform_dist, binominal_dist, poisson_dist, normal_dist
def prepare_data(uniform_dist, binominal_dist, poisson_dist, normal_dist, step):
    distributions_list = []
    for i in range(0, len(uniform_dist) - 1, step):
        distributions = {
            'uniform': uniform_dist[i],
            'binominal': binominal_dist[i],
            'poisson': poisson_dist[i],
            'normal': normal_dist[i]
        }
        distributions_list.append(distributions)
    return distributions_list
def write_data_to_csv(data, filename, fieldnames):
    print('Writing data...')
    with open(filename, 'w', newline='') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)
def main():
    uniform_dist, binominal_dist, poisson_dist, normal_dist = generate_distributions(TEST_SIZE)
    data = prepare_data(uniform_dist, binominal_dist, poisson_dist, normal_dist, STEP)
    write_data_to_csv(data, DATA_FILENAME, FIELDNAMES)
if __name__ == "__main__":
    main()