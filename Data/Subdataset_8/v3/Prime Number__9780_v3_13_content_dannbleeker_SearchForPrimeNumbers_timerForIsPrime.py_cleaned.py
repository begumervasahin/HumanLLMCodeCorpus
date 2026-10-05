import timeit
import isPrimeSearch
def search_for_primes(start_number, end_number, prime_search_function, loop_type):
    print(f"Searching from {start_number:,} to {end_number:,} (interval: {end_number - start_number:,})")
    for current_prime_search in prime_search_function:
        test_code = f'''
import isPrimeSearch
prime_counter = 0
{loop_type}
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        prime_counter += 1
'''
        time_to_run = round(timeit.timeit(stmt=test_code, number=1), 4)
        print(f"CheckForPrime{current_prime_search} ({loop_type}): {time_to_run}")
start_number = 0
end_number = 100_000_000
use_log_file = True
if use_log_file:
    log_file = open('log.txt', 'a')
prime_search_function = range(6, 7)
loop_types = ["while", "for"]
for loop_type in loop_types:
    search_for_primes(start_number, end_number, prime_search_function, loop_type)
if use_log_file:
    log_file.close()