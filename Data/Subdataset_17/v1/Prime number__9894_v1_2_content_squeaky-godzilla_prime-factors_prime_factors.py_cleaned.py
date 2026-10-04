
import sys
import time
import json
import argparse
def init_archive(archive_file_path):
    with open(archive_file_path, 'w') as archive_file:
        pass
def load_archive(archive_file_path):
    with open(archive_file_path, 'r') as archive_file:
        try:
            archive_dict = json.load(archive_file)
        except json.JSONDecodeError:
            print('Error: archive JSON cannot be decoded')
            sys.exit(1)
    return archive_dict
def validate_number(number):
    try:
        number = int(number)
    except ValueError:
        raise Exception('not a valid integer')
    if number < 0:
        raise Exception('not a natural number')
    return number
def get_prime_factors(number):
    start_time = time.time()
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number
            factors.append(i)
    if number > 1:
        factors.append(number)
    return number, factors, time.time() - start_time
def record_result(number, factors, record_dict, archive_file_path):
    record_dict[number] = factors
    with open(archive_file_path, 'w') as archive_file:
        json.dump(record_dict, archive_file)
def main():
    parser = argparse.ArgumentParser(
        usage='Enter the integer number to find prime factors and archive JSON file to store performed computations, -h for help'
    )
    parser.add_argument('-n', type=str, help='integer number', required=True, dest='number')
    parser.add_argument('-a', type=str, help='archive JSON file', default='archive.json', dest='archive_file')
    parser.add_argument('-t', action='store_true', dest='testing', default=False, help='flag for testing output format')
    arguments = parser.parse_args()
    archive_file = arguments.archive_file
    testing = arguments.testing
    number = validate_number(arguments.number)
    try:
        record_dict = load_archive(archive_file)
    except FileNotFoundError:
        init_archive(archive_file)
        record_dict = {}
    if str(number) in record_dict.keys():
        prime_factors = record_dict[str(number)]
        compute_time = 0
    else:
        _, prime_factors, compute_time = get_prime_factors(number)
        record_result(number, prime_factors, record_dict, archive_file)
    if testing:
        print(json.dumps({number: prime_factors, "compute_time": compute_time}))
    else:
        print(f'Prime factors of {number} are {", ".join(map(str, prime_factors))} - found in: {compute_time:.6f} sec')
if __name__ == '__main__':
    main()