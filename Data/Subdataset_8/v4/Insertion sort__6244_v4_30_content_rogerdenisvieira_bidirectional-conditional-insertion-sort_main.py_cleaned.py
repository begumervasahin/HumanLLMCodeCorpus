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
binominal_dist = distributions['binominal']
poisson_dist = distributions['poisson']
normal_dist = distributions['normal']
real_dist = distributions['real']
bcis_sorter = BCIS()
is_sorter = IS()
def write_report(values):
    filename = REPORT_FILENAME
    fieldnames = [
        'array_size',
        'uniform_bcis', 'uniform_qs', 'uniform_is', 'uniform_bcis/qs', 'uniform_bcis/is',
        'binomial_bcis', 'binomial_qs', 'binomial_is', 'binomial_bcis/qs', 'binomial_bcis/is',
        'poisson_bcis', 'poisson_qs', 'poisson_is', 'poisson_bcis/qs', 'poisson_bcis/is',
        'normal_bcis', 'normal_qs', 'normal_is', 'normal_bcis/qs', 'normal_bcis/is',
        'real_bcis', 'real_qs', 'real_is', 'real_bcis/qs', 'real_bcis/is'
    ]
    print('Writing report...')
    with open(filename, 'w', newline='') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(values)
def calc_execution_elapsed_times(distribution, dist_name):
    start_time_bcis = timer()
    bcis_sorter.sort(distribution, 0, len(distribution)-1)
    end_time_bcis = timer()
    elapsed_time_bcis = end_time_bcis - start_time_bcis
    start_time_is = timer()
    is_sorter.sort(distribution)
    end_time_is = timer()
    elapsed_time_is = end_time_is - start_time_is
    print(f"BCIS for size: {len(distribution)} took {elapsed_time_bcis} for {dist_name}")
    print(f"IS for size: {len(distribution)} took {elapsed_time_is} for {dist_name}")
    return {
        'bcis': elapsed_time_bcis,
        'is': elapsed_time_is,
        'bcis/is': (elapsed_time_bcis / elapsed_time_is)
    }
final_results = []
try:
    for i in range(STEP, TEST_SIZE, STEP):
        print(f"Array size: {i}")
        uniform_res = calc_execution_elapsed_times(uniform_dist[0:i], "uniform")
        binominal_res = calc_execution_elapsed_times(binominal_dist[0:i], "binominal")
        poisson_res = calc_execution_elapsed_times(poisson_dist[0:i], "poisson")
        normal_res = calc_execution_elapsed_times(normal_dist[0:i], "normal")
        real_res = calc_execution_elapsed_times(real_dist[0:i], "real")
        partial_result = {
            'array_size': i,
            'uniform_bcis': uniform_res['bcis'],
            'uniform_qs': None,
            'uniform_is': uniform_res['is'],
            'uniform_bcis/qs': None,
            'uniform_bcis/is': uniform_res['bcis/is'],
            'binomial_bcis': binominal_res['bcis'],
            'binomial_qs': None,
            'binomial_is': binominal_res['is'],
            'binomial_bcis/qs': None,
            'binomial_bcis/is': binominal_res['bcis/is'],
            'poisson_bcis': poisson_res['bcis'],
            'poisson_qs': None,
            'poisson_is': poisson_res['is'],
            'poisson_bcis/qs': None,
            'poisson_bcis/is': poisson_res['bcis/is'],
            'normal_bcis': normal_res['bcis'],
            'normal_qs': None,
            'normal_is': normal_res['is'],
            'normal_bcis/qs': None,
            'normal_bcis/is': normal_res['bcis/is'],
            'real_bcis': real_res['bcis'],
            'real_qs': None,
            'real_is': real_res['is'],
            'real_bcis/qs': None,
            'real_bcis/is': real_res['bcis/is']
        }
        final_results.append(partial_result)
except Exception as e:
    print("An error occurred:", e)
finally:
    write_report(final_results)