import numpy as np
import csv
TEST_SIZE = 7000
STEP = 1
OUTPUT_FILENAME = 'distributions.csv'
CSV_FIELDS = ['uniform', 'binomial', 'poisson', 'normal']
def generate_random_distributions(size):
    uniform_dist = np.random.uniform(-1, 1, size)
    binomial_dist = np.random.binomial(1000, 0.5, size)
    poisson_dist = np.random.poisson(1000, size)
    normal_dist = np.random.normal(0, 0.1, size)
    return uniform_dist, binomial_dist, poisson_dist, normal_dist
def organize_data_for_csv(uniform, binomial, poisson, normal, step):
    data_records = []
    for i in range(0, len(uniform) - 1, step):
        record = {
            'uniform': uniform[i],
            'binomial': binomial[i],
            'poisson': poisson[i],
            'normal': normal[i]
        }
        data_records.append(record)
    return data_records
def write_data_to_csv(data, filename, fieldnames):
    print('Writing data to CSV...')
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
def main():
    uniform, binomial, poisson, normal = generate_random_distributions(TEST_SIZE)
    data_for_csv = organize_data_for_csv(uniform, binomial, poisson, normal, STEP)
    write_data_to_csv(data_for_csv, OUTPUT_FILENAME, CSV_FIELDS)
if __name__ == "__main__":
    main()