from sorters import BCIS, IS
from timeit import default_timer as timer
import pandas as pd
import csv
TEST_SIZE = 7000
STEP = 10
REPORT_FILENAME = 'ratios.csv'
DISTRIBUTIONS_FILENAME = 'distributions.csv'
distributions = pd.read_csv(DISTRIBUTIONS_FILENAME)
uniform_dist = distributions['uniform']
binomial_dist = distributions['binomial']
poisson_dist = distributions['poisson']
normal_dist = distributions['normal']
real_dist = distributions['real']
bcis_sorter = BCIS()
is_sorter = IS()
def write_report(values):
    filename = REPORT_FILENAME
    fieldnames = [
        'array_size',
        'uniform_bcis', 'uniform_is',
        'binomial_bcis', 'binomial_is',
        'poisson_bcis', 'poisson_is',
        'normal_bcis', 'normal_is',
        'real_bcis', 'real_is'
    ]
    print('Writing report...')
    with open(filename, 'w', newline='') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(values)
def calc_execution_elapsed_times(sorter, distribution, dist_name):
    start_time = timer()
    sorter.sort(distribution)
    end_time = timer()
    elapsed_time = end_time - start_time
    print(f"{sorter.__class__.__name__} for size {len(distribution)} took {elapsed_time} seconds for {dist_name}")
    return elapsed_time
try:
    final_results = []
    for i in range(STEP, TEST_SIZE + 1, STEP):
        print("Array size:", i)
        partial_result = {
            'array_size': i,
            'uniform_bcis': calc_execution_elapsed_times(bcis_sorter, uniform_dist[:i], "uniform"),
            'uniform_is': calc_execution_elapsed_times(is_sorter, uniform_dist[:i], "uniform"),
            'binomial_bcis': calc_execution_elapsed_times(bcis_sorter, binomial_dist[:i], "binomial"),
            'binomial_is': calc_execution_elapsed_times(is_sorter, binomial_dist[:i], "binomial"),
            'poisson_bcis': calc_execution_elapsed_times(bcis_sorter, poisson_dist[:i], "poisson"),
            'poisson_is': calc_execution_elapsed_times(is_sorter, poisson_dist[:i], "poisson"),
            'normal_bcis': calc_execution_elapsed_times(bcis_sorter, normal_dist[:i], "normal"),
            'normal_is': calc_execution_elapsed_times(is_sorter, normal_dist[:i], "normal"),
            'real_bcis': calc_execution_elapsed_times(bcis_sorter, real_dist[:i], "real"),
            'real_is': calc_execution_elapsed_times(is_sorter, real_dist[:i], "real")
        }
        final_results.append(partial_result)
except Exception as e:
    print("An error occurred:", e)
finally:
    write_report(final_results)