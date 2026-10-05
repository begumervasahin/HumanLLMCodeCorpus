import numpy as np
import csv
TEST_SIZE = 7000
DATA_FILENAME = 'distributions.csv'
def write_data_to_csv(values, filename, fieldnames):
    print('Writing data to CSV...')
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(values)
    print('Data successfully written to', filename)
def generate_distribution_samples(sample_size):
    return {
        'uniform': np.random.uniform(-1, 1, sample_size),
        'binomial': np.random.binomial(1000, 0.5, sample_size),
        'poisson': np.random.poisson(1000, sample_size),
        'normal': np.random.normal(0, 0.1, sample_size)
    }
def compile_distributions_data(sample_size):
    distributions = generate_distribution_samples(sample_size)
    compiled_data = [
        {dist: distributions[dist][i] for dist in distributions}
        for i in range(sample_size)
    ]
    return compiled_data
def main():
    distribution_data = compile_distributions_data(TEST_SIZE)
    data_categories = ['uniform', 'binomial', 'poisson', 'normal']
    write_data_to_csv(distribution_data, DATA_FILENAME, data_categories)
if __name__ == "__main__":
    main()