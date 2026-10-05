import timeit
use_log_file = True
if use_log_file:
    logfile = open('log.txt', 'a')
start_number = 0
end_number = 100000000
print("Searching from %s to %s (interval: %s)" % (
    f"{start_number:,d}".replace(",", "."), f"{end_number:,d}".replace(",", "."),
    f"{(end_number - start_number):,d}".replace(",", ".")
))
if use_log_file:
    print("Searching from %s to %s (interval: %s)" % (
        f"{start_number:,d}".replace(",", "."), f"{end_number:,d}".replace(",", "."),
        f"{(end_number - start_number):,d}".replace(",", ".")
    ), file=logfile)
for current_prime_search in range(6, 7):
    test_code = '''
import isPrimeSearch
prime_counter = 0
current_number = %s
while current_number <= %s:
    if isPrimeSearch.checkForPrime%s(current_number) == True:
        prime_counter +=  1
        current_number += 2
    else:
        current_number += 1
''' % (start_number, end_number, current_prime_search)
    time_to_run = round(timeit.timeit(stmt=test_code, number=1), 4)
    print("CheckForPrime%s (wsa2): %s" % (current_prime_search, time_to_run))
    if use_log_file:
        print("CheckForPrime%s (wsa2): %s" % (current_prime_search, time_to_run),
              file=logfile)
for current_prime_search in range(6, 7):
    test_code = '''
import isPrimeSearch
prime_counter = 0
for current_number in range(%s, %s):
    if isPrimeSearch.checkForPrime%s(current_number) == True:
        prime_counter +=  1
''' % (start_number, end_number, current_prime_search)
    time_to_run = round(timeit.timeit(stmt=test_code, number=1), 4)
    print("CheckForPrime%s (for1): %s" % (current_prime_search, time_to_run))
    if use_log_file:
        print("CheckForPrime%s (for1): %s" % (current_prime_search, time_to_run),
              file=logfile)
if use_log_file:
    logfile.close()