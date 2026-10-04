from sorters import BCIS, QS, IS
from timeit import default_timer as timer
import numpy as np
import pandas as pd
import sys
import csv
TEST_SIZE = 7000
STEP = 10
REPORT_FILENAME = 'ratios.csv'
DISTRIBUTIONS_FILENAME = 'distributions.csv'
distributions = pd.read_csv(DISTRIBUTIONS_FILENAME)
uniform_dist = distributions['uniform'].to_numpy()
binomial_dist = distributions['binominal'].to_numpy()
poisson_dist = distributions['poisson'].to_numpy()
normal_dist = distributions['normal'].to_numpy()
real_dist = distributions['real'].to_numpy()
bcis_sorter = BCIS()
is_sorter = IS()
qs_sorter = QS()
sys.setrecursionlimit(TEST_SIZE + 100)
def write_report(values):
    fieldnames = [
        'array_size', 'uniform_bcis', 'uniform_qs', 'uniform_is', 'uniform_bcis/qs', 'uniform_bcis/is',
        'binomial_bcis', 'binomial_qs', 'binomial_is', 'binomial_bcis/qs', 'binomial_bcis/is',
        'poisson_bcis', 'poisson_qs', 'poisson_is', 'poisson_bcis/qs', 'poisson_bcis/is',
        'normal_bcis', 'normal_qs', 'normal_is', 'normal_bcis/qs', 'normal_bcis/is',
        'real_bcis', 'real_qs', 'real_is', 'real_bcis/qs', 'real_bcis/is'
    ]
    with open(REPORT_FILENAME, 'w', newline='') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(values)
    print("Report written to", REPORT_FILENAME)
def calc_execution_elapsed_times(distribution, dist_name):
    times = {}
    start = timer()
    bcis_sorter.sort(distribution.copy(), 0, len(distribution) - 1)
    times['bcis'] = timer() - start
    print(f"BCIS for size: {len(distribution)} took {times['bcis']:.6f} seconds for {dist_name}")
    start = timer()
    qs_sorter.sort(distribution.copy())
    times['qs'] = timer() - start
    print(f"QS for size: {len(distribution)} took {times['qs']:.6f} seconds for {dist_name}")
    start = timer()
    is_sorter.sort(distribution.copy())
    times['is'] = timer() - start
    print(f"IS for size: {len(distribution)} took {times['is']:.6f} seconds for {dist_name}")
    times['bcis/qs'] = times['bcis'] / times['qs']
    times['bcis/is'] = times['bcis'] / times['is']
    return times
final_results = []
try:
    for i in range(STEP, TEST_SIZE + 1, STEP):
        print(f"Processing array size: {i}")
        uniform_res = calc_execution_elapsed_times(uniform_dist[:i], "uniform")
        binomial_res = calc_execution_elapsed_times(binomial_dist[:i], "binomial")
        poisson_res = calc_execution_elapsed_times(poisson_dist[:i], "poisson")
        normal_res = calc_execution_elapsed_times(normal_dist[:i], "normal")
        real_res = calc_execution_elapsed_times(real_dist[:i], "real")
        partial_result = {
            'array_size': i,
            'uniform_bcis': uniform_res['bcis'],
            'uniform_qs': uniform_res['qs'],
            'uniform_is': uniform_res['is'],
            'uniform_bcis/qs': uniform_res['bcis/qs'],
            'uniform_bcis/is': uniform_res['bcis/is'],
            'binomial_bcis': binomial_res['bcis'],
            'binomial_qs': binomial_res['qs'],
            'binomial_is': binomial_res['is'],
            'binomial_bcis/qs': binomial_res['bcis/qs'],
            'binomial_bcis/is': binomial_res['bcis/is'],
            'poisson_bcis': poisson_res['bcis'],
            'poisson_qs': poisson_res['qs'],
            'poisson_is': poisson_res['is'],
            'poisson_bcis/qs': poisson_res['bcis/qs'],
            'poisson_bcis/is': poisson_res['bcis/is'],
            'normal_bcis': normal_res['bcis'],
            'normal_qs': normal_res['qs'],
            'normal_is': normal_res['is'],
            'normal_bcis/qs': normal_res['bcis/qs'],
            'normal_bcis/is': normal_res['bcis/is'],
            'real_bcis': real_res['bcis'],
            'real_qs': real_res['qs'],
            'real_is': real_res['is'],
            'real_bcis/qs': real_res['bcis/qs'],
            'real_bcis/is': real_res['bcis/is'],
        }
        final_results.append(partial_result)
except Exception as e:
    print(f"An error has occurred: {e}")
finally:
    write_report(final_results)