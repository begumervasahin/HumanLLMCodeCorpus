import numpy as np
import statistics as stat
import Cipher
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def is_even(num):
    return num % 2 == 0
def reduce_seeds(seeds):
    new_number = 0
    seeds_str = str(seeds)
    for digit in seeds_str:
        new_number += int(digit) ** 3
    if new_number < 1000:
        return new_number * len(seeds_str)
    else:
        return reduce_seeds(new_number)
def generate_text():
    return "Hi there."
def random_generator(seeds):
    np.random.seed(seeds)
    random_nums = np.random.rand(seeds).tolist()
    for i in range(seeds):
        temp = int((random_nums[i] * 100000) / 37)
        if is_prime(temp):
            if is_even(temp):
                temp = temp ** 2
            else:
                temp = (temp ** 2) / ((seeds - 1) * 100)
        else:
            if is_even(temp):
                temp = temp * (100 - seeds) / (seeds ** 2)
            else:
                temp = temp * (temp ** (0.5)) / ((seeds - 1) ** 2)
        random_nums[i] = int(temp)
    mean_val = round(stat.mean(random_nums))
    ciphered_text = Cipher.chiper(generate_text(), mean_val)
    deciphered_text = Cipher.dechiper(ciphered_text, mean_val)
    print("Ciphered Text:", ciphered_text)
    print("Deciphered Text:", deciphered_text)
random_generator(10)