import os
import numpy
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
kernel = SourceModule()
class Primes:
    def __init__(self, cache_results):
        self.caching_primality_results = cache_results
        self.set_primes = set()
        self.set_primes_to_be_excluded = set()
        self.set_twinprimes = set()
        self.set_nonprimes = set()
        self.list_sorted_primes = []
        self.list_sorted_twinprimes = []
        self.list_sorted_nonprimes = []
        self.list_of_primes_used = []
    def init_set(self, filename, number_type):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.replace('[', '')
                    line = line.replace(']', '')
                    numbers = line.split(',')
                    for number in numbers:
                        self.add_to_set(number, number_type)
    def add_to_set(self, n, number_type):
        n = int(n)
        if number_type == 1:
            self.set_primes.add(n)
        elif number_type == 2:
            self.set_twinprimes.add(n)
        elif number_type == 3:
            self.set_nonprimes.add(n)
    def sort_set(self, set_type):
        if set_type == "primes":
            self.list_sorted_primes = sorted(self.set_primes)
        elif set_type == "twinprimes":
            self.list_sorted_twinprimes = sorted(self.set_twinprimes)
        elif set_type == "nonprimes":
            self.list_sorted_nonprimes = sorted(self.set_nonprimes)
    def is_in_set(self, n, set_type):
        if set_type == "primes":
            return n in self.set_primes
        elif set_type == "primes_to_be_excluded":
            return n in self.set_primes_to_be_excluded
        elif set_type == "twinprimes":
            return n in self.set_twinprimes
        elif set_type == "nonprimes":
            return n in self.set_nonprimes
    def add_to_set_to_be_excluded(self, n):
        self.set_primes_to_be_excluded.add(n)
    def is_prime(self, n):
        if self.is_in_set(n, "primes_to_be_excluded"):
            return False
        if n < 2:
            return False
        elif n == 2 or n == 3:
            return True
        elif self.is_in_set(n, "primes"):
            return True
        elif self.is_in_set(n, "nonprimes"):
            return False
        elif n % 2 == 0 or n % 3 == 0:
            return False
        result = True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                result = False
                break
            i += 6
        if self.caching_primality_results:
            if result:
                self.set_primes.add(n)
            else:
                self.set_nonprimes.add(n)
        return result
    def is_twinprime(self, n):
        if self.is_in_set(n, "twinprimes"):
            return True
        elif self.is_in_set(n, "nonprimes"):
            return False
        elif self.is_lesser_twin_prime(n) or self.is_greater_twin_prime(n):
            result = True
        else:
            result = False
        if self.caching_primality_results:
            if result:
                self.set_twinprimes.add(n)
            else:
                self.set_nonprimes.add(n)
        return result
    def is_lesser_twin_prime(self, n):
        if self.is_prime(n) and self.is_prime(n + 2):
            return True
    def is_greater_twin_prime(self, n):
        if self.is_prime(n) and self.is_prime(n - 2):
            return True
    def is_prime_cuda(self, n):
        def min2(list, bound=0):
            for item in list:
                if item > bound:
                    return item
            return None
        first_factor = kernel.get_function('first_factor')
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        allPrimes = [2, 3]
        numPrimes = len(allPrimes)
        numThreads = 384
        result = numpy.zeros(numPrimes, numpy.int32)
        primes = numpy.copy(allPrimes).astype(numpy.int32)
        while True:
            first_factor(numpy.int64(n), cuda.InOut(result), cuda.In(primes), block=(numThreads, 1, 1))
            prime = min2(result, 1)
            if prime is None:
                break
            return False
        return True
    def get_ith_prime(self, i):
        max_known_index = len(self.list_sorted_primes)
        if i < max_known_index:
            return self.list_sorted_primes[i]
        else:
            if max_known_index == 0:
                n = 2
            else:
                n = self.list_sorted_primes[max_known_index - 1]
            primes_to_be_found = i - max_known_index
            while primes_to_be_found > 0:
                n += 1
                if self.is_prime(n):
                    primes_to_be_found -= 1
        return n
    def get_ith_twinprime(self, i):
        max_known_index = len(self.list_sorted_twinprimes)
        if i < max_known_index:
            return self.list_sorted_twinprimes[i]
        else:
            if max_known_index == 0:
                n = 3
            else:
                n = self.list_sorted_twinprimes[max_known_index - 1]
            twinprimes_to_be_found = i - max_known_index
            while twinprimes_to_be_found > 0:
                n += 1
                if self.is_twinprime(n):
                    twinprimes_to_be_found -= 1
        return n
    def get_ith_composite(self, i):
        max_known_index = len(self.list_sorted_nonprimes)
        if i < max_known_index:
            return self.list_sorted_nonprimes[i]
        else:
            if max_known_index == 0:
                n = 4
            else:
                n = self.list_sorted_nonprimes[max_known_index - 1]
            composites_to_be_found = i - max_known_index
            while composites_to_be_found > 0:
                n += 1
                if not self.is_prime(n):
                    composites_to_be_found -= 1
        return n
    def get_all_primes_leq(self, n):
        counter = 0
        for i in range(n + 1):
            if self.is_prime(i):
                counter += 1
        return counter
    def factorize(self, n):
        if n <= 1:
            return 0
        i = 2
        e = math.floor(math.sqrt(n))
        f = []
        while i <= e:
            if n % i == 0:
                f.append(i)
                n /= i
                e = math.floor(math.sqrt(n))
            else:
                i += 1
        if n > 1:
            f.append(int(n))
        return f
    def is_symmetric_prime(self, n, i):
        k1 = n - i
        k2 = n + i
        if self.is_prime(k1) and self.is_prime(k2):
            return True, k1, k2
        else:
            return False, 0, 0
    def is_6km1(self, n):
        return self.is_prime(n) and (n > 3) and (n % 6 == 5)
    def is_6kp1(self, n):
        return self.is_prime(n) and (n > 3) and (n % 6 == 1)
    def find_unique_prime_in_sum(self, n):
        is_prime_lower_than_current_sum = True
        k = 1
        while is_prime_lower_than_current_sum:
            q = self.get_ith_prime(k)
            if 2 <= n - q and q not in self.list_of_primes_used:
                self.list_of_primes_used.append(q)
                self.find_unique_prime_in_sum(n - q)
            elif 2 <= n - q:
                k += 1
            else:
                self.list_of_primes_used.append(q)
                is_prime_lower_than_current_sum = False