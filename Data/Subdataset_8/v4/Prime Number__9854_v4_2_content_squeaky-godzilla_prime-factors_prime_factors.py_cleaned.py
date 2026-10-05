import sys
import time
import json
import argparse
def init_archive(archive_file_path):
    with open(archive_file_path, 'w'):
        pass
def load_archive(archive_file_path):
    try:
        with open(archive_file_path, 'r') as archive_file:
            archive_dict = json.load(archive_file)
    except json.JSONDecodeError:
        print('Error: Unable to decode archive JSON')
        sys.exit(1)
    return archive_dict
def validate_number(number):
    try:
        number = int(number)
    except ValueError:
        raise ValueError('Invalid integer')
    if number < 0:
        raise ValueError('Not a natural number')
    return number
def get_prime_factors(number):
    start_time = time.time()
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number
    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number
    if number > 2:
        factors.append(number)
    return factors, time.time() - start_time
def record_result(number, factors, record_dict, archive_file_path):
    record_dict[str(number)] = factors
    with open(archive_file_path, 'w') as archive_file:
        json.dump(record_dict, archive_file)
def main():
    parser = argparse.ArgumentParser(
        usage='Enter an integer number to find its prime factors '
              'and an archive JSON file to store computations (-h for help)'
    )
    parser.add_argument('-n', type=str, help='Integer number', required=True, dest='number')
    parser.add_argument('-a', type=str, help='Archive JSON file', default='archive.json', dest='archive_file')
    parser.add_argument('-t', action='store_true', dest='testing', default=False,
                        help='Flag for testing output format')
    args = parser.parse_args()
    archive_file = args.archive_file
    testing = args.testing
    number = validate_number(args.number)
    try:
        record_dict = load_archive(archive_file)
    except FileNotFoundError:
        init_archive(archive_file)
        record_dict = {}
    if str(number) in record_dict:
        prime_factors = record_dict[str(number)]
        compute_time = 0
    else:
        prime_factors, compute_time = get_prime_factors(number)
        record_result(number, prime_factors, record_dict, archive_file)
    if testing:
        print('{"%d": [%s], "compute_time": %f}' %
              (number, ', '.join(map(str, prime_factors)), compute_time))
    else:
        print('Prime factors of %d are %s - found in: %f sec' %
              (number, ', '.join(map(str, prime_factors)), compute_time))
if __name__ == '__main__':
    main()