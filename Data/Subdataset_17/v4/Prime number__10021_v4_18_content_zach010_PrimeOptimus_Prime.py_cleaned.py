import sys
import os
import struct
import time
from mpmath import mp
import multiprocessing
def progress_bar(total, progress):
    bar_length = 10
    progress = float(progress) / float(total)
    if progress >= 1.0:
        progress = 1
        status = "\r\n"
    else:
        status = ""
    block = int(round(bar_length * progress))
    text = "\rProgress: [{}] {:.0f}/10 {}".format(
        chr(9632) * block + chr(9633) * (bar_length - block),
        round(progress * 10, 0), status
    )
    sys.stdout.write(text)
    sys.stdout.flush()
def prime_multiprocess(n_range, number, q):
    start, end = n_range
    for i in range(start, end):
        if number % i == 0:
            q.put(0)
            return
    q.put(1)
def segregate(number, precision):
    mp.dps = precision
    sqrt_num = int(mp.floor(mp.sqrt(number)) + 1)
    cores = min(multiprocessing.cpu_count(), sqrt_num - 1)
    segment_size = sqrt_num
    segments = [segment_size] * cores
    for i in range(sqrt_num % cores):
        segments[i] += 1
    ranges = []
    start = 2
    for size in segments:
        end = start + size
        ranges.append((start, end))
        start = end
    return ranges, cores
def initialize(segments, cores, number):
    queues = [multiprocessing.Queue() for _ in range(cores)]
    processes = [
        multiprocessing.Process(target=prime_multiprocess, args=(segments[i], number, queues[i]))
        for i in range(cores)
    ]
    for p in processes:
        p.start()
    print('\rCalculating...')
    start_time = time.time()
    results = [0] * cores
    while True:
        for i in range(cores):
            if not queues[i].empty():
                results[i] = queues[i].get()
                progress_bar(cores, sum(results))
                if results[i] == 0:
                    print('\rProgress: [' + chr(9632) * 10 + '] 10/10')
                    for p in processes:
                        p.terminate()
                    print_result(number, False, time.time() - start_time)
                    return
                if sum(results) == cores:
                    print_result(number, True, time.time() - start_time)
                    return
def print_result(number, is_prime, elapsed_time):
    number_length = len(str(number))
    if elapsed_time < 60:
        print(f"\rFinished processing in {elapsed_time:.1f} seconds.")
    else:
        minutes = int(elapsed_time
        seconds = elapsed_time % 60
        print(f"\rFinished processing in {minutes} minute{'s' if minutes > 1 else ''} and {seconds:.1f} seconds.")
    print(f"Number: {number}\nPrime: {'Yes' if is_prime else 'No'}\nLength: {number_length}")
def start_program():
    while True:
        response = input('Do you want to calculate if another number is Prime? (y/n): ').lower()
        if response == 'y':
            try:
                number = int(input('Enter number for Prime test: '))
                if number == 1:
                    print("The number 1 is not considered Prime because it is a square of which all are not Prime.")
                    continue
                precision = len(str(number)) + 4
                segments, cores = segregate(number, precision)
                initialize(segments, cores, number)
            except ValueError:
                print("Invalid Input.")
        elif response == 'n':
            print("Program Exit.")
            sys.exit()
        else:
            print("Invalid Input.")
if __name__ == '__main__':
    processor_count = multiprocessing.cpu_count()
    print(f"Python version {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} "
          f"({8 * struct.calcsize('P')}-bit)")
    print(f"\nThis computer-system has ({processor_count}) logical processors initialized for this Prime task.")
    start_program()