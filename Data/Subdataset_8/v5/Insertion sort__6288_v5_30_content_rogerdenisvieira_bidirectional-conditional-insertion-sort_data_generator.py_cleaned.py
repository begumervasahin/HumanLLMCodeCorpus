import numpy as np
import csv
TEST_SIZE = 7000
STEP = 1
DATA_FILENAME = 'distributions.csv'
def write_data_to_csv(data, filename):
    fieldnames = ['uniform', 'binomial', 'poisson', 'normal']
    print('Writing data to CSV...')
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        print(f"Error writing to file: {e}")
uniform_dist = np.random.uniform(-1, 1, TEST_SIZE)
binomial_dist = np.random.binomial(1000, 0.5, TEST_SIZE)
poisson_dist = np.random.poisson(1000, TEST_SIZE)
normal_dist = np.random.normal(0, 0.1, TEST_SIZE)
distributions_list = []
for i in range(0, TEST_SIZE - 1, STEP):
    distribution = {
        'uniform': uniform_dist[i],
        'binomial': binomial_dist[i],
        'poisson': poisson_dist[i],
        'normal': normal_dist[i]
    }
    distributions_list.append(distribution)
write_data_to_csv(distributions_list, DATA_FILENAME)