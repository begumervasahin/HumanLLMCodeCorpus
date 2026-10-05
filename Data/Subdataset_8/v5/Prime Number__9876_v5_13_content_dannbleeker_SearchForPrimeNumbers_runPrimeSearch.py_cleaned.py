import datetime
import sys
from primeSearchServer import PrimeServer
from isPrimeSearch import check_for_prime6
def print_status(prime_server):
    print("Number of primes found: {:,}".format(prime_server.return_total_number_of_primes_found()))
    print("Biggest prime found: {:,}".format(prime_server.return_highest_prime_found()))
    print("Number of unfinished intervals: {:,}".format(prime_server.return_unfinished_intervals()))
def print_help():
    print("useIntervals forces to use any open intervals on the server")
    print("status gives a status from the server")
    print("follow command with a number, and that is the interval of primes being searched")
def main():
    prime_server = PrimeServer()
    search_interval = 1000
    force_use_of_incomplete_intervals = False
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.isnumeric() and int(arg) > 0:
            search_interval = int(arg)
        elif arg == "status":
            print_status(prime_server)
            return
        elif arg == "-?":
            print_help()
            return
        elif arg == "useIntervals":
            force_use_of_incomplete_intervals = True
    start_search_at, end_search_at = prime_server.return_search_interval(search_interval, force_use_of_incomplete_intervals)
    prime_counter = 0
    start_time = datetime.datetime.now()
    print("Search for prime numbers")
    print("Starting at:", start_time.strftime("%Y-%m-%d %H:%M:%S"), "\n")
    print("Searching from {} to {} (interval: {})".format(
        "{:,}".format(start_search_at), "{:,}".format(end_search_at), "{:,}".format(end_search_at - start_search_at)))
    completion_rate = 0
    sys.stdout.write("\r{}% completed".format(completion_rate))
    sys.stdout.flush()
    current_number = start_search_at
    while current_number <= end_search_at:
        if check_for_prime6(current_number):
            prime_counter += 1
            prime_server.return_prime_found(current_number)
            current_number += 2
        else:
            current_number += 1
        new_completion_rate = int(round(((current_number - start_search_at) / (end_search_at - start_search_at)) * 100, 0))
        if completion_rate < new_completion_rate:
            completion_rate = new_completion_rate
            sys.stdout.write("\r{}% completed".format(completion_rate))
            sys.stdout.flush()
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
    prime_server.return_searched_interval(start_search_at, end_search_at)
    del prime_server
    end_time = datetime.datetime.now()
    print("\n\nStarting at:", start_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at:", end_time.strftime("%Y-%m-%d %H:%M:%S"))
    timedelta = end_time - start_time
    print("Running time: {} minutes {} seconds".format(int(timedelta.seconds / 60), (timedelta.seconds % 60)))
    print("Searched from {} to {} (interval: {})".format(
        "{:,}".format(start_search_at), "{:,}".format(end_search_at), "{:,}".format(end_search_at - start_search_at)))
    print("Number of primes: {} ({}%)".format(
        "{:,}".format(prime_counter), round(prime_counter / (end_search_at - start_search_at), 5)))
    if prime_counter > 0:
        print("Seconds per prime: {}".format(round(timedelta.seconds / prime_counter, 6)))
if __name__ == "__main__":
    main()