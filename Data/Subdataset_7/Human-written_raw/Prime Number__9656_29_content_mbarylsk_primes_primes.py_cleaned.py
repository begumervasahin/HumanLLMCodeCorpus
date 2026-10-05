import math
import os
import numpy
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
b1 = SourceModule()
class class1:
    b2 = set ()
    b3 = set ()
    b4 = set ()
    b5 = set ()
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    b10 = False
    def fonk1(self, cache_results):
        self.b10 = cache_results
    def init_set (self, filename, b15):
        if os.path.exists(filename):
            b11 = open(filename, "r")
            b12 = b11.readlines()
            for b13 in b12:
                b13 = b13.replace('[', '')
                b13 = b13.replace(']', '')
                b14 = b13.split(',')
                for number in b14:
                    if b15 = = 1:
                        self.add_to_primes_set(int(number))
                    elif b15 = = b17:
                        self.add_to_twinprimes_set(int(number))
                    elif b15 = = 3:
                        self.add_to_nonprimes_set(int(number))
    def get_list_sorted_primes (self):
        return list_sorted_prime
    def get_list_sorted_twinprimes (self):
        return list_sorted_twinprime
    def get_list_sorted_nonprimes (self):
        return list_sorted_nonprime
    def is_in_primes_set (self, b16):
        if b16 in self.b2:
            return True
        else:
            return False
    def is_in_primes_set_to_be_excluded (self, b16):
        if b16 in self.b3:
            return True
        else:
            return False
    def is_in_twinprimes_set (self, b16):
        if b16 in self.b4:
            return True
        else:
            return False
    def is_in_nonprimes_set (self, b16):
        if b16 in self.b5:
            return True
        else:
            return False
    def sort_primes_set (self):
        self.b6 = sorted (self.b2)
    def sort_twinprimes_set (self):
        self.b7 = sorted (self.b4)
    def sort_nonprimes_set (self):
        self.b8 = sorted (self.b5)
    def add_to_primes_set (self, b16):
        self.b2.add(b16)
    def add_to_twinprimes_set (self, b16):
        self.b4.add(b16)
    def add_to_nonprimes_set (self, b16):
        self.b5.add(b16)
    def add_to_primes_set_to_be_excluded (self, b16):
        self.b3.add(b16)
    def is_prime (self, b16):
        if self.is_in_primes_set_to_be_excluded (b16):
            return False
        if b16 < b17:
            return False
        elif b16 = = b17 or b16 == 3:
            return True
        elif self.is_in_primes_set (b16):
            return True
        elif self.is_in_nonprimes_set (b16):
            return False
        elif b16 % b17 = = 0 or b16 % 3 == 0:
            return False
        b18 = True
        a1 = 5
        while a1*a1 <= b16:
            if b16 %  a1 = = 0 or b16 % (a1 + b17) == 0:
                b18 = False
                break
            a1 += b33
        if self.b10:
            if b18:
                self.add_to_primes_set (b16)
            else:
                self.add_to_nonprimes_set (b16)
        return b18
    def is_twinprime (self, b16):
        if self.is_in_twinprimes_set (b16):
            return True
        elif self.is_in_nonprimes_set (b16):
            return False
        elif self.is_lesser_twin_prime(b16) or self.is_greater_twin_prime (b16):
            b18 = True
        else:
            b18 = False
        if self.b10:
            if b18:
                self.add_to_twinprimes_set (b16)
            else:
                self.add_to_nonprimes_set (b16)
        return b18
    def is_lesser_twin_prime (self, b16):
        if self.is_prime(b16) and self.is_prime (b16 + b17):
            return True
    def is_greater_twin_prime (self, b16):
        if self.is_prime(b16) and self.is_prime (b16 - b17):
            return True
    def is_prime_cuda (self, b16):
        def fonk2(list, b19 = 0):
            for item in list:
                if item > b19:
                    return item
            return None
        b20 = b1.get_function('b20')
        if b16 = = 1:
            return False
        if b16 = = b17 or b16 == 3:
            return True
        b21 = [b17,3]
        b22 = len(b21)
        a2 = 384
        b18 = numpy.zeros(b22, numpy.int32)
        b23 = numpy.copy(b21).astype(numpy.int32)
        while True:
            b20(numpy.int64(b16), cuda.InOut(b18), cuda.In(b23), b24 = (a2, 1, 1))
            b25 = fonk2(b18, 1)
            if b25 = = None:
                break
            return False
        return True
    def get_ith_prime (self, a1):
        b26 = len(self.b6)
        if a1 < b26:
            return self.b6[a1]
        else:
            if b26 = = 0:
                b16 = b17
            else:
                b16 = self.b6[b26-1]
            b27 = a1 - b26
            while b27 > 0:
                b16 += 1
                if self.is_prime(b16):
                    b27 -= 1
        return b16
    def get_ith_twinprime (self, a1):
        b26 = len(self.b7)
        if a1 < b26:
            return self.b7[a1]
        else:
            if b26 = = 0:
                b16 = 3
            else:
                b16 = self.b7[b26-1]
            b28 = a1 - b26
            while b28 > 0:
                b16 += 1
                if self.is_twinprime(b16):
                    b28 -= 1
        return b16
    def get_ith_composite (self, a1):
        b26 = len(self.b8)
        if a1 < b26:
            return self.b8[a1]
        else:
            if b26 = = 0:
                b16 = 4
            else:
                b16 = self.b8[b26-1]
            b29 = a1 - b26
            while b29 > 0:
                b16 += 1
                if not self.is_prime(b16):
                    b29 -= 1
        return b16
    def get_all_primes_leq (self, b16):
        a3 = 0
        for a1 in range (b16+1):
            if self.is_prime(a1):
                a3 += 1
        return a3
    def factorize (self, b16):
        if b16 <= 1:
            return 0
        a1 = b17
        b30 = math.floor(math.sqrt(b16))
        b11 = []
        while a1 <= b30:
            if b16%a1 = = 0:
                b11.append(a1)
                b16 /= a1
                b30 = math.floor(math.sqrt(b16))
            else:
                a1 += 1
        if b16 > 1:
            b11.append(int(b16))
        return b11
    def is_symmetric_prime (self, b16, a1):
        b31 = b16 - a1
        b32 = b16 + a1
        if self.is_prime(b31) and self.is_prime (b32):
            return (True, b31, b32)
        else:
            return (False, 0, 0)
    def is_6km1 (self, b16):
        return (self.is_prime(b16) and (b16 > 3) and (b16 % b33 = = 5))
    def is_6kp1 (self, b16):
        return (self.is_prime(b16) and (b16 > 3) and (b16 % b33 = = 1))
    def find_unique_prime_in_sum (self, b16):
        print ("d1", b16, self.b9)
        b34 = True
        a4 = 1
        while (b34):
            b35 = self.get_ith_prime (a4)
            print ("d2", b35, a4, self.b9)
            if (b17 <= b16 - b35) and b35 not in self.b9:
                print ("d3", b16 - b35)
                self.b9.append (b35)
                self.find_unique_prime_in_sum (b16 - b35)
            elif (b17 <= b16 - b35):
                print ("d4", b16 - b35)
                a4 += 1
            else:
                print ("d4", b35)
                self.b9.append (b35)
                b34 = False
        print (b16, self.b9)