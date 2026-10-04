import timeit
use_log_file = True
logfile = open('log.txt', 'a') if use_log_file else None
start_number = 0
end_number = 100_000_000
def log_message(message):
    print(message)
    if use_log_file:
        print(message, file=logfile)
search_range_message = (
    f"Searching from {start_number:,d}".replace(",", ".") +
    f" to {end_number:,d}".replace(",", ".") +
    f" (interval: {(end_number - start_number):,d}".replace(",", ".") + ")"
)
log_message(search_range_message)
for current_prime_search in range(6, 7):
    test_code_wsa2 = f'''
import isPrimeSearch
prime_counter = 0
current_number = {start_number}
while current_number <= {end_number}:
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        prime_counter += 1
    current_number += 2 if current_number > 2 else 1
'''
    time_to_run_wsa2 = round(timeit.timeit(stmt=test_code_wsa2, number=1), 4)
    log_message(f"CheckForPrime{current_prime_search} (wsa2): {time_to_run_wsa2}")
    test_code_for1 = f'''
import isPrimeSearch
prime_counter = 0
for current_number in range({start_number}, {end_number}):
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        prime_counter += 1
'''
    time_to_run_for1 = round(timeit.timeit(stmt=test_code_for1, number=1), 4)
    log_message(f"CheckForPrime{current_prime_search} (for1): {time_to_run_for1}")
if use_log_file:
    logfile.close()