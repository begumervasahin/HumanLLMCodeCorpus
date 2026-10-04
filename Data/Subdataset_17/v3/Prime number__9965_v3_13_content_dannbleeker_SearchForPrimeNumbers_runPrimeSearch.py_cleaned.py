import datetime
import primeSearchServer
import isPrimeSearch
import sys
def display_status(prime_server):
    print(f"Number of primes found: {prime_server.returnTotalNumberOfPrimesFound():,d}".replace(",", "."))
    print(f"Biggest prime found: {prime_server.returnHighestPrimeFound():,d}".replace(",", "."))
    print(f"Number of unfinished intervals: {prime_server.returnUnfinishedIntervals():,d}".replace(",", "."))
def display_help():
    print("useIntervals forces to use any open intervals on the server")
    print("status gives a status from the server")
    print("follow command with a number, and that is the interval of primes being searched")
def parse_arguments():
    search_interval = 1000
    force_use_of_incomplete_intervals = False
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.isnumeric() and int(arg) > 0:
            search_interval = int(arg)
        elif arg == "status":
            return "status", search_interval, force_use_of_incomplete_intervals
        elif arg == "-?":
            return "help", search_interval, force_use_of_incomplete_intervals
        elif arg == "useIntervals":
            force_use_of_incomplete_intervals = True
    return "search", search_interval, force_use_of_incomplete_intervals
def search_primes(prime_server, search_interval, force_use_of_incomplete_intervals):
    start_search_at, end_search_at = prime_server.returnSearchInterval(search_interval, force_use_of_incomplete_intervals)
    prime_counter = 0
    start_time = datetime.datetime.now()
    print("Search for prime numbers")
    print(f"Starting at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Searching from {start_search_at:,d}".replace(",", ".") +
          f" to {end_search_at:,d}".replace(",", ".") +
          f" (interval: {(end_search_at - start_search_at):,d}".replace(",", ".") + ")")
    completion_rate = 0
    sys.stdout.write(f"\r{completion_rate}% completed")
    sys.stdout.flush()
    current_number = start_search_at
    while current_number <= end_search_at:
        if isPrimeSearch.checkForPrime6(current_number):
            prime_counter += 1
            prime_server.returnPrimeFound(current_number)
            current_number += 2
        else:
            current_number += 1
        new_completion_rate = int(round(((current_number - start_search_at) / (end_search_at - start_search_at)) * 100))
        if completion_rate < new_completion_rate:
            completion_rate = new_completion_rate
            sys.stdout.write(f"\r{completion_rate}% completed")
            sys.stdout.flush()
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
    prime_server.returnSearchedInterval(start_search_at, end_search_at)
    end_time = datetime.datetime.now()
    time_delta = end_time - start_time
    print("\n\n")
    print(f"Starting at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Ending at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Running time: {time_delta.seconds
    print(f"Searched from {start_search_at:,d}".replace(",", ".") +
          f" to {end_search_at:,d}".replace(",", ".") +
          f" (interval: {(end_search_at - start_search_at):,d}".replace(",", ".") + ")")
    print(f"Number of primes: {prime_counter:,d}".replace(",", ".") +
          f" ({round(prime_counter / (end_search_at - start_search_at), 5)}%)")
    if prime_counter > 0:
        print(f"Seconds per prime: {round(time_delta.seconds / prime_counter, 6)}")
def main():
    prime_server = primeSearchServer.primeServer()
    command, search_interval, force_use_of_incomplete_intervals = parse_arguments()
    if command == "status":
        display_status(prime_server)
    elif command == "help":
        display_help()
    else:
        search_primes(prime_server, search_interval, force_use_of_incomplete_intervals)
    del prime_server
if __name__ == "__main__":
    main()