import datetime
import primeSearchServer
import isPrimeSearch
import sys
def main():
    PrimeServerConnection = primeSearchServer.primeServer()
    searchInterval = 1000
    forceUseOfIncompleteIntervals = False
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.isnumeric() and int(arg) > 0:
            searchInterval = int(arg)
        elif arg == "status":
            print_status(PrimeServerConnection)
            return
        elif arg == "-?":
            print_help()
            return
        elif arg == "useIntervals":
            forceUseOfIncompleteIntervals = True
    startSearchAt, endSearchAt = PrimeServerConnection.returnSearchInterval(
        searchInterval, forceUseOfIncompleteIntervals)
    primeCounter = 0
    startTime = datetime.datetime.now()
    print_start_search_message(startTime, startSearchAt, endSearchAt)
    completionRate = 0
    currentNumber = startSearchAt
    while currentNumber <= endSearchAt:
        if isPrimeSearch.checkForPrime6(currentNumber):
            primeCounter += 1
            PrimeServerConnection.returnPrimeFound(currentNumber)
            currentNumber += 2
        else:
            currentNumber += 1
        new_completion_rate = int(round(
            ((currentNumber - startSearchAt) / (endSearchAt - startSearchAt)) * 100, 0))
        if completionRate < new_completion_rate:
            completionRate = new_completion_rate
            print_progress(completionRate)
    print_completion()
    PrimeServerConnection.returnSearchedInterval(startSearchAt, endSearchAt)
    del PrimeServerConnection
    endTime = datetime.datetime.now()
    print_end_search_message(startTime, endTime, startSearchAt, endSearchAt, primeCounter)
def print_status(PrimeServerConnection):
    print("Number of primes found: %s" % (
        f"{PrimeServerConnection.returnTotalNumberOfPrimesFound():,d}".replace(",", ".")))
    print("Biggest prime found: %s" % (
        f"{PrimeServerConnection.returnHighestPrimeFound():,d}".replace(",", ".")))
    print("Number of unfinished intervals: %s" % (
        f"{PrimeServerConnection.returnUnfinishedIntervals():,d}".replace(",", ".")))
def print_help():
    print("useIntervals forces to use any open intervals on the server")
    print("status gives a status from the server")
    print("follow command with a number, and that is the interval of primes being searched")
def print_start_search_message(startTime, startSearchAt, endSearchAt):
    print("Search for prime numbers\nStarting at: %s\n" % startTime.strftime("%Y-%m-%d %H:%M:%S"))
    print("Searching from %s to %s (interval: %s)" % (
        f"{startSearchAt:,d}".replace(",", "."), f"{endSearchAt:,d}".replace(",", "."),
        f"{(endSearchAt - startSearchAt):,d}".replace(",", ".")))
def print_progress(completionRate):
    sys.stdout.write("\r" + str(completionRate) + "% completed")
    sys.stdout.flush()
def print_completion():
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
def print_end_search_message(startTime, endTime, startSearchAt, endSearchAt, primeCounter):
    timedelta = endTime - startTime
    print("\n\nStarting at: %s" % startTime.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at: %s" % endTime.strftime("%Y-%m-%d %H:%M:%S"))
    print("Running time: %s minutes %s seconds" % (
        int(timedelta.seconds / 60), (timedelta.seconds % 60)))
    print("Searched from %s to %s (interval: %s)" % (
        f"{startSearchAt:,d}".replace(",", "."), f"{endSearchAt:,d}".replace(",", "."),
        f"{(endSearchAt - startSearchAt):,d}".replace(",", ".")))
    print("Number of primes: %s (%s%%)" % (
        f"{primeCounter:,d}".replace(",", "."), round(primeCounter / (endSearchAt - startSearchAt), 5)))
    if primeCounter > 0:
        print("Seconds per prime: %s" % round(timedelta.seconds / primeCounter, 6))
if __name__ == "__main__":
    main()