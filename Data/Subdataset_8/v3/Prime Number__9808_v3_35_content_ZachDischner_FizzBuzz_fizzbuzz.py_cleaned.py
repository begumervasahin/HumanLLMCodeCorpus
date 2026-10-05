from __future__ import print_function
import sys
import argparse
def is_prime(x):
    assert isinstance(x, int), "is_prime requires integer type, provided {}".format(type(x))
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for possibility in range(3, int(x ** 0.5 + 1), 2):
        if x % possibility == 0:
            return False
    return True
def generate_fibonacci_sequence():
    one_ago, two_ago = 0, 1
    while True:
        yield one_ago
        one_ago, two_ago = two_ago, one_ago + two_ago
def fizz_buzzify(x):
    if is_prime(x):
        return "BuzzFizz"
    divisible_by_3 = "" if x % 3 else "Buzz"
    divisible_by_5 = "" if x % 5 else "Fizz"
    return (divisible_by_5 + divisible_by_3) or x
def generate_fizz_buzz_sequence(N, debug=False):
    for index, fib_number in enumerate(generate_fibonacci_sequence()):
        if index > N:
            break
        fizzbuzzed = fizz_buzzify(fib_number)
        if debug:
            print("F[{}] ==> {} ==> {}".format(index, fib_number, fizzbuzzed))
        else:
            print(fizzbuzzed)
def test_generate_fibonacci_sequence():
    fib_gen = generate_fibonacci_sequence()
    fib_5 = [next(fib_gen) for _ in range(5)]
    truth = [0, 1, 1, 2, 3]
    assert fib_5 == truth, "Fibonacci sequence generator failed, {} should == {}".format(fib_5, truth)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fizz-Buzzify a Fibonacci sequence',
                                     epilog='Example of use: python fizzbuzz.py 5')
    parser.add_argument('N', type=int, help="Length of Fibonacci Sequence to produce")
    parser.add_argument('--debug', action='store_true', help="Print extra info illustrating the fizzbuzzification")
    args = parser.parse_args()
    N = args.N
    debug = args.debug
    print("Generating a Fibonacci sequence of length {N} for fizz-buzzifying".format(N=N))
    generate_fizz_buzz_sequence(N, debug=debug)
    sys.exit(0)