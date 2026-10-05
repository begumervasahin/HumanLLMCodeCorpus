from sorters import BCIS, IS
from timeit import default_timer as timer
import pandas as pd
import csv
TEST_SIZE = 7000
STEP = 10
REPORT_FILENAME = 'ratios.csv'
DISTRIBUTIONS_FILENAME = 'distributions.csv'
distributions = pd.read_csv(DISTRIBUTIONS_FILENAME)
distribution_names = ['uniform', 'binominal', 'poisson', 'normal', 'real']
distributions_data = {name: distributions[name] for name in distribution_names}
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
def calc_execution_elapsed_times(sorter, distribution, dist_name):
    start_time = timer()
    sorter.sort(distribution)
    end_time = timer()
    elapsed_time = end_time - start_time
    print(f"{sorter.__class__.__name__} for size: {len(distribution)} took {elapsed_time} for {dist_name}")
    return elapsed_time
final_results = []
try:
    for i in range(STEP, TEST_SIZE, STEP):
        print(f"Array size: {i}")
        partial_result = {'array_size': i}
        for dist_name, dist_data in distributions_data.items():
            elapsed_time_bcis = calc_execution_elapsed_times(bcis_sorter, dist_data[:i], dist_name)
            elapsed_time_is = calc_execution_elapsed_times(is_sorter, dist_data[:i], dist_name)
            partial_result[f'{dist_name}_bcis'] = elapsed_time_bcis
            partial_result[f'{dist_name}_qs'] = None
            partial_result[f'{dist_name}_is'] = elapsed_time_is
            partial_result[f'{dist_name}_bcis/qs'] = None
            partial_result[f'{dist_name}_bcis/is'] = elapsed_time_bcis / elapsed_time_is
        final_results.append(partial_result)
except Exception as e:
    print("An error occurred:", e)
finally:
    write_report(final_results)