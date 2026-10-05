import numpy as np
import statistics as stat
import Cipher
def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def check_even(number):
    return number % 2 == 0
def reduce_number(number):
    new_number = 0
    num_str = str(number)
    for digit in num_str:
        new_number += int(digit) ** 3
    if new_number < 1000:
        return new_number * len(num_str)
    else:
        return reduce_number(new_number)
def generate_text():
    return "Hi there."
def random_generator(seeds):
    np.random.seed(seeds)
    random_numbers = np.random.rand(seeds).tolist()
    for i in range(seeds):
        temp = int((random_numbers[i] * 100000) / 37)
        if check_prime(temp):
            if check_even(temp):
                temp = temp ** 2
            else:
                temp = (temp ** 2) / ((seeds - 1) * 100)
        else:
            if check_even(temp):
                temp = temp * (100 - seeds) / (seeds ** 2)
            else:
                temp = temp * (temp ** 0.5) / ((seeds - 1) ** 2)
        random_numbers[i] = int(temp)
    mean_value = round(stat.mean(random_numbers))
    ciphered_text = Cipher.chiper(generate_text(), mean_value)
    deciphered_text = Cipher.dechiper(ciphered_text, mean_value)
    print("Ciphered Text:", ciphered_text)
    print("Deciphered Text:", deciphered_text)
random_generator(10)