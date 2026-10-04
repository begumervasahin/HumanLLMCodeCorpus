
from __future__ import print_function
import sys
import argparse
def is_prime(x):
    """Determine if a number is prime or not
    Algo:
        Less than 2 is not prime
        2 is prime
        Evens greater than 2 are not prime
        Otherwise check to see if any number up to sqrt(x) goes into x evenly
    Note that under this definition, 0 and 1 are _NOT_ prime numbers. 0 has infinitely many
    divisors, and 1 fails the logic of "a number is prime if it's only two divisors are 1
    and itself". http:
    not considered primes, though that definition varies and an abs() pretty easily changes
    this assumption.
    Args:
        x:  (integer) number to test for primeness
    Returns:
        _   (bool) Boolean indicator of primeness
    Examples:
        >>> is_prime(-1)
        False
        >>> is_prime(0)
        False
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(6)
        False
        >>> is_prime(9)
        False
        >>> is_prime(49)
        False
    """
    assert type(x) is int, "is_prime requires integer type, provided {}".format(type(x))
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for possibility in range(3, int(x**0.5 + 1), 2):
        if x % possibility == 0:
            return False
    return True
def fib():
    """Memory efficient Fibonacci sequence generator
    Note that the definition chosen here is that 0 is the first element in the Fibonacci sequence
    F_0=0, F_1=1, F_2=1, F_3=2...
    See https:
    Returns:
        _   (generator) Fibonacci number generator
    Examples:
        for ix, fn in enumerate(fizzbuzz.fib()):
            print("Fib sequence number F({}) ==> {}".format(ix, fn))
            if ix > 10:
                break
    Determined modified fizz-buzz representation of number `x`
    Rules:
        * if x is prime ==> "BuzzFizz"
        * if x is divisible by 15 ==> "FizzBuzz"
        * if x is divisible by 3 ==> "Fizz"
        * if x is divisible by 5 ==> "Buzz"
        * x ==> x otherwise
    Note 1. Order of precedence:
        The number 3 is prime as well as divisible by 3. But here we choose to return
        prime representation first. Logic follows that if prime didn't take precedence, then
        x%15 wouldn't take precedence either and then we'd be stuck without ever having that
        occurrence and trying to figure out if "Fizz" or "Buzz" is the correct implementation.
    Note 2: 0 treatment
        The number 0 is an odd one in that it is sometimes prime depending on your definition
        (_not_ in this implementation though), and it is divisible by everything. So I'm keeping
        with program logic which says that 0 % 3 == 0 *and* 0 % 5 == 0 (which means 0 % 15 == 0)
        so the fizzbuzzification of 0 will result in "FizzBuzz"
    Examples:
        >>> fizz_buzzify(0)
        'FizzBuzz'
        >>> fizz_buzzify(10)
        'Buzz'
        >>> fizz_buzzify(11)
        'BuzzFizz'
        >>> fizz_buzzify(12)
        'Fizz'
        >>> fizz_buzzify(15)
        'FizzBuzz'
        >>> fizz_buzzify(16)
        16
    """
    if is_prime(x):
        return "BuzzFizz"
    divis_3 = ""
    divis_5 = ""
    if x % 3 == 0:
        divis_3 += "Fizz"
    if x % 5 == 0:
        divis_5 += "Buzz"
    return (divis_5 + divis_3) or x
def generate_fizz_buzz(N, debug=False):
    for index, fib_number in enumerate(fib()):
        if index > N:
            break
        fizzbuzzed = fizz_buzzify(fib_number)
        if debug:
            print("F[{}] ==> {} ==> {}".format(index, fib_number, fizzbuzzed))
        else:
            print(fizzbuzzed)
def test_fib():
    fibgen = fib()
    fib5 = [next(fibgen) for ix in range(5)]
    truth = [0, 1, 1, 2, 3]
    assert fib5 == truth, "Fibonacci sequence generator failed, {} should == {}".format(fib5, truth)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fizz-Buzzify a Fibonacci sequence',
                                     epilog='Example of use: python fizzbuzz.py 5')
    parser.add_argument('N', type=int, help="Length of Fibonacci Sequence to produce")
    parser.add_argument('--debug', action='store_true', help="Printout extra info illustrating the fizzbuzzification")
    args = parser.parse_args()
    N = args.N
    debug = args.debug
    print("Generating a Fibonacci sequence of length {N} for fizz-buzzifying".format(N=N))
    generate_fizz_buzz(N, debug=debug)
    sys.exit(0)