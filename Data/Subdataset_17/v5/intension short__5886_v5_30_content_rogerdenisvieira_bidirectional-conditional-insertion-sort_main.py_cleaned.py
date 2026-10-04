import csv
import sys
import pandas as pd
from timeit import default_timer as timer
from sorters import BCIS, IS
TEST_SIZE = 7000
STEP = 10
REPORT_FILENAME = 'ratios.csv'
DISTRIBUTIONS_FILENAME = 'distributions.csv'
sys.setrecursionlimit(TEST_SIZE + 100)
distributions = pd.read_csv(DISTRIBUTIONS_FILENAME)
uniform_dist = distributions['uniform']
binomial_dist = distributions['binominal']
poisson_dist = distributions['poisson']
normal_dist = distributions['normal']
real_dist = distributions['real']
bcis_sorter = BCIS()
is_sorter = IS()
def calc_execution_times(distribution, dist_name):
    start = timer()
    bcis_sorter.sort(distribution, 0, len(distribution) - 1)
    bcis_time = timer() - start
    print(f"BCIS for size {len(distribution)} took {bcis_time:.5f} seconds for {dist_name}")
    start = timer()
    is_sorter.sort(distribution)
    is_time = timer() - start
    print(f"IS for size {len(distribution)} took {is_time:.5f} seconds for {dist_name}")
    return {
        'bcis': bcis_time,
        'is': is_time,
        'bcis/is': bcis_time / is_time if is_time != 0 else float('inf')
    }
def write_report(data, filename=REPORT_FILENAME):
    fieldnames = [
        'array_size',
        'uniform_bcis', 'uniform_is', 'uniform_bcis/is',
        'binomial_bcis', 'binomial_is', 'binomial_bcis/is',
        'poisson_bcis', 'poisson_is', 'poisson_bcis/is',
        'normal_bcis', 'normal_is', 'normal_bcis/is',
        'real_bcis', 'real_is', 'real_bcis/is'
    ]
    print('Writing report...')
    try:
        with open(filename, 'w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Failed to write report: {e}")
def main():
    final_results = []
    try:
        for i in range(STEP, TEST_SIZE, STEP):
            print(f"Processing array size: {i}")
            uniform_res = calc_execution_times(uniform_dist[:i], "uniform")
            binomial_res = calc_execution_times(binomial_dist[:i], "binomial")
            poisson_res = calc_execution_times(poisson_dist[:i], "poisson")
            normal_res = calc_execution_times(normal_dist[:i], "normal")
            real_res = calc_execution_times(real_dist[:i], "real")
            final_results.append({
                'array_size': i,
                'uniform_bcis': uniform_res['bcis'],
                'uniform_is': uniform_res['is'],
                'uniform_bcis/is': uniform_res['bcis/is'],
                'binomial_bcis': binomial_res['bcis'],
                'binomial_is': binomial_res['is'],
                'binomial_bcis/is': binomial_res['bcis/is'],
                'poisson_bcis': poisson_res['bcis'],
                'poisson_is': poisson_res['is'],
                'poisson_bcis/is': poisson_res['bcis/is'],
                'normal_bcis': normal_res['bcis'],
                'normal_is': normal_res['is'],
                'normal_bcis/is': normal_res['bcis/is'],
                'real_bcis': real_res['bcis'],
                'real_is': real_res['is'],
                'real_bcis/is': real_res['bcis/is']
            })
    except Exception as e:
        print(f"An error occurred during processing: {e}")
    finally:
        write_report(final_results)
if __name__ == "__main__":
    main()