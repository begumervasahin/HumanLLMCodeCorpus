from sorters import BCIS, QS, IS
from timeit import default_timer as timer
import pandas as pd
import sys
import csv
TEST_SIZE = 7000
STEP = 10
REPORT_FILENAME = 'ratios.csv'
DISTRIBUTIONS_FILENAME = 'distributions.csv'
distributions = pd.read_csv(DISTRIBUTIONS_FILENAME)
distribution_types = {
    "uniform": distributions['uniform'].to_numpy(),
    "binomial": distributions['binominal'].to_numpy(),
    "poisson": distributions['poisson'].to_numpy(),
    "normal": distributions['normal'].to_numpy(),
    "real": distributions['real'].to_numpy()
}
bcis_sorter = BCIS()
qs_sorter = QS()
is_sorter = IS()
sys.setrecursionlimit(TEST_SIZE + 100)
def write_report(results, filename=REPORT_FILENAME):
    fieldnames = [
        'array_size', 'uniform_bcis', 'uniform_qs', 'uniform_is', 'uniform_bcis/qs', 'uniform_bcis/is',
        'binomial_bcis', 'binomial_qs', 'binomial_is', 'binomial_bcis/qs', 'binomial_bcis/is',
        'poisson_bcis', 'poisson_qs', 'poisson_is', 'poisson_bcis/qs', 'poisson_bcis/is',
        'normal_bcis', 'normal_qs', 'normal_is', 'normal_bcis/qs', 'normal_bcis/is',
        'real_bcis', 'real_qs', 'real_is', 'real_bcis/qs', 'real_bcis/is'
    ]
    with open(filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"Report successfully written to {filename}")
def measure_sort_times(distribution, name):
    times = {}
    for sorter_name, sorter in [("bcis", bcis_sorter), ("qs", qs_sorter), ("is", is_sorter)]:
        start_time = timer()
        sorter.sort(distribution.copy())
        elapsed_time = timer() - start_time
        times[sorter_name] = elapsed_time
        print(f"{sorter_name.upper()} for {name} of size {len(distribution)} took {elapsed_time:.6f} seconds")
    times['bcis/qs'] = times['bcis'] / times['qs']
    times['bcis/is'] = times['bcis'] / times['is']
    return times
def main():
    final_results = []
    try:
        for size in range(STEP, TEST_SIZE + 1, STEP):
            print(f"Processing distributions of size: {size}")
            result = {'array_size': size}
            for name, distribution in distribution_types.items():
                sort_times = measure_sort_times(distribution[:size], name)
                result.update({
                    f"{name}_bcis": sort_times['bcis'],
                    f"{name}_qs": sort_times['qs'],
                    f"{name}_is": sort_times['is'],
                    f"{name}_bcis/qs": sort_times['bcis/qs'],
                    f"{name}_bcis/is": sort_times['bcis/is']
                })
            final_results.append(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        write_report(final_results)
if __name__ == "__main__":
    main()