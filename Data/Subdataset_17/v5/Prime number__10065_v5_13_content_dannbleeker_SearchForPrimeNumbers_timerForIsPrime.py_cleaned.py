import timeit
def log_message(message, use_log_file, logfile=None):
    print(message)
    if use_log_file and logfile:
        print(message, file=logfile)
def format_number(number):
    return f"{number:,d}".replace(",", ".")
def run_prime_search(start_number, end_number, current_prime_search, use_log_file, logfile, search_type):
    if search_type == "while":
        test_code = f'''
import isPrimeSearch
prime_counter = 0
current_number = {start_number}
while current_number <= {end_number}:
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        prime_counter += 1
        current_number += 2
    else:
        current_number += 1
'''
    elif search_type == "for":
        test_code = f'''
import isPrimeSearch
prime_counter = 0
for current_number in range({start_number}, {end_number}):
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        prime_counter += 1
'''
    time_to_run = round(timeit.timeit(stmt=test_code, number=1), 4)
    log_message(f"CheckForPrime{current_prime_search} ({search_type}): {time_to_run}", use_log_file, logfile)
def main():
    use_log_file = True
    start_number = 0
    end_number = 100_000_000
    logfile = open('log.txt', 'a') if use_log_file else None
    search_range_msg = f"Searching from {format_number(start_number)} to {format_number(end_number)} " \
                       f"(interval: {format_number(end_number - start_number)})"
    log_message(search_range_msg, use_log_file, logfile)
    for current_prime_search in range(6, 7):
        run_prime_search(start_number, end_number, current_prime_search, use_log_file, logfile, "while")
    for current_prime_search in range(6, 7):
        run_prime_search(start_number, end_number, current_prime_search, use_log_file, logfile, "for")
    if use_log_file and logfile:
        logfile.close()
if __name__ == '__main__':
    main()