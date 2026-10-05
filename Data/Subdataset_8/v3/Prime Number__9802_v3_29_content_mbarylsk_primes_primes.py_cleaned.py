import os
import numpy
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import math
kernel = SourceModule()
class Primes:
    def __init__(self, cache_results):
        self.caching_primality_results = cache_results
        self.primes = set()
        self.primes_to_be_excluded = set()
        self.twin_primes = set()
        self.non_primes = set()
        self.sorted_primes = []
        self.sorted_twin_primes = []
        self.sorted_non_primes = []
        self.used_primes = []
    def initialize_set(self, filename, number_type):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.replace('[', '').replace(']', '')
                    numbers = line.split(',')
                    for number in numbers:
                        self.add_to_set(int(number), number_type)
    def add_to_set(self, n, number_type):
        if number_type == 1:
            self.primes.add(n)
        elif number_type == 2:
            self.twin_primes.add(n)
        elif number_type == 3:
            self.non_primes.add(n)
    def sort_set(self, set_type):
        if set_type == "primes":
            self.sorted_primes = sorted(self.primes)
        elif set_type == "twinprimes":
            self.sorted_twin_primes = sorted(self.twin_primes)
        elif set_type == "nonprimes":
            self.sorted_non_primes = sorted(self.non_primes)
    def is_in_set(self, n, set_type):
        if set_type == "primes":
            return n in self.primes
        elif set_type == "primes_to_be_excluded":
            return n in self.primes_to_be_excluded
        elif set_type == "twinprimes":
            return n in self.twin_primes
        elif set_type == "nonprimes":
            return n in self.non_primes
    def add_to_excluded_set(self, n):
        self.primes_to_be_excluded.add(n)
    def is_prime(self, n):
        if self.is_in_set(n, "primes_to_be_excluded"):
            return False
        if n < 2:
            return False
        elif n in (2, 3):
            return True
        elif self.is_in_set(n, "primes"):
            return True
        elif self.is_in_set(n, "nonprimes"):
            return False
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        if self.caching_primality_results:
            if n not in self.primes:
                self.primes.add(n)
            else:
                self.non_primes.add(n)
        return True
    def is_twin_prime(self, n):
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
                self.twin_primes.add(n)
            else:
                self.non_primes.add(n)
        return result
    def is_lesser_twin_prime(self, n):
        return self.is_prime(n) and self.is_prime(n + 2)
    def is_greater_twin_prime(self, n):
        return self.is_prime(n) and self.is_prime(n - 2)
    def is_prime_cuda(self, n):
        def min2(list, bound=0):
            for item in list:
                if item > bound:
                    return item
            return None
        first_factor = kernel.get_function('first_factor')
        if n == 1:
            return False
        if n in (2, 3):
            return True
        all_primes = [2, 3]
        num_primes = len(all_primes)
        num_threads = 384
        result = numpy.zeros(num_primes, numpy.int32)
        primes = numpy.copy(all_primes).astype(numpy.int32)
        while True:
            first_factor(numpy.int64(n), cuda.InOut(result), cuda.In(primes), block=(num_threads, 1, 1))
            prime = min2(result, 1)
            if prime is None:
                break
            return False
        return True
    def get_ith_prime(self, i):
        max_known_index = len(self.sorted_primes)
        if i < max_known_index:
            return self.sorted_primes[i]
        else:
            n = self.sorted_primes[-1] if max_known_index > 0 else 2
            primes_to_find = i - max_known_index
            while primes_to_find > 0:
                n += 1
                if self.is_prime(n):
                    primes_to_find -= 1
        return n
    def get_ith_twinprime(self, i):
        max_known_index = len(self.sorted_twin_primes)
        if i < max_known_index:
            return self.sorted_twin_primes[i]
        else:
            n = self.sorted_twin_primes[-1] if max_known_index > 0 else 3
            twin_primes_to_find = i - max_known_index
            while twin_primes_to_find > 0:
                n += 1
                if self.is_twin_prime(n):
                    twin_primes_to_find -= 1
        return n
    def get_ith_composite(self, i):
        max_known_index = len(self.sorted_non_primes)
        if i < max_known_index:
            return self.sorted_non_primes[i]
        else:
            n = self.sorted_non_primes[-1] if max_known_index > 0 else 4
            composites_to_find = i - max_known_index
            while composites_to_find > 0:
                n += 1
                if not self.is_prime(n):
                    composites_to_find -= 1
        return n
    def get_all_primes_leq(self, n):
        count = 0
        for i in range(n + 1):
            if self.is_prime(i):
                count += 1
        return count
    def factorize(self, n):
        if n <= 1:
            return []
        factors = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n
            else:
                i += 1
        if n > 1:
            factors.append(n)
        return factors
    def is_symmetric_prime(self, n, distance):
        k1 = n - distance
        k2 = n + distance
        return self.is_prime(k1) and self.is_prime(k2), k1, k2
    def is_6km1(self, n):
        return self.is_prime(n) and (n > 3) and (n % 6 == 5)
    def is_6kp1(self, n):
        return self.is_prime(n) and (n > 3) and (n % 6 == 1)
    def find_unique_prime_in_sum(self, n):
        is_prime_lower_than_current_sum = True
        k = 1
        while is_prime_lower_than_current_sum:
            q = self.get_ith_prime(k)
            if 2 <= n - q and q not in self.used_primes:
                self.used_primes.append(q)
                self.find_unique_prime_in_sum(n - q)
            elif 2 <= n - q:
                k += 1
            else:
                self.used_primes.append(q)
                is_prime_lower_than_current_sum = False