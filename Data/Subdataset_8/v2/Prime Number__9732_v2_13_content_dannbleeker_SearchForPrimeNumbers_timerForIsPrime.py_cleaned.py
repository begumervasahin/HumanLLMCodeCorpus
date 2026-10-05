import timeit
import isPrimeSearch
use_log_file = True
if use_log_file:
    log_file = open('log.txt', 'a')
start_number = 0
end_number = 100000000
print("Searching from {:,d} to {:,d} (interval: {:,d})".format(start_number, end_number, end_number - start_number))
if use_log_file:
    print("Searching from {:,d} to {:,d} (interval: {:,d})".format(start_number, end_number, end_number - start_number),
          file=log_file)
for current_prime_search in range(6, 7):
    test_code_while = f'''
import isPrimeSearch
prime_counter = 0
current_number = {start_number}
while current_number <= {end_number}:
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        prime_counter += 1
    current_number += 2
'''
    time_to_run_while = round(timeit.timeit(stmt=test_code_while, number=1), 4)
    print(f"CheckForPrime{current_prime_search} (wsa2): {time_to_run_while}")
    if use_log_file:
        print(f"CheckForPrime{current_prime_search} (wsa2): {time_to_run_while}", file=log_file)
for current_prime_search in range(6, 7):
    test_code_for = f'''
import isPrimeSearch
prime_counter = 0
for current_number in range({start_number}, {end_number}):
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        prime_counter += 1
'''
    time_to_run_for = round(timeit.timeit(stmt=test_code_for, number=1), 4)
    print(f"CheckForPrime{current_prime_search} (for1): {time_to_run_for}")
    if use_log_file:
        print(f"CheckForPrime{current_prime_search} (for1): {time_to_run_for}", file=log_file)
if use_log_file:
    log_file.close()