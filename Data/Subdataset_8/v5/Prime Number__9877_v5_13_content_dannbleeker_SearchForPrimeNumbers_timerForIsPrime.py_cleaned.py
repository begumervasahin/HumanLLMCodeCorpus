import timeit
def print_interval(start, end):
    print("Searching from {:,d} to {:,d} (interval: {:,d})".format(start, end, end - start))
def log_interval(start, end, logfile):
    print("Searching from {:,d} to {:,d} (interval: {:,d})".format(start, end, end - start), file=logfile)
def run_prime_search(start, end, current_prime_search):
    test_code = f'''
import isPrimeSearch
prime_counter = 0
current_number = {start}
while current_number <= {end}:
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        prime_counter += 1
        current_number += 2
    else:
        current_number += 1
'''
    return round(timeit.timeit(stmt=test_code, number=1), 4)
def run_prime_search_for(start, end, current_prime_search):
    test_code = f'''
import isPrimeSearch
prime_counter = 0
for current_number in range({start}, {end}):
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        prime_counter += 1
'''
    return round(timeit.timeit(stmt=test_code, number=1), 4)
def main():
    start_number = 0
    end_number = 100_000_000
    use_log_file = True
    if use_log_file:
        with open('log.txt', 'a') as logfile:
            print_interval(start_number, end_number)
            log_interval(start_number, end_number, logfile)
            for current_prime_search in range(6, 7):
                time_to_run = run_prime_search(start_number, end_number, current_prime_search)
                print("CheckForPrime{} (wsa2): {}".format(current_prime_search, time_to_run))
                print("CheckForPrime{} (wsa2): {}".format(current_prime_search, time_to_run), file=logfile)
            for current_prime_search in range(6, 7):
                time_to_run = run_prime_search_for(start_number, end_number, current_prime_search)
                print("CheckForPrime{} (for1): {}".format(current_prime_search, time_to_run))
                print("CheckForPrime{} (for1): {}".format(current_prime_search, time_to_run), file=logfile)
if __name__ == "__main__":
    main()