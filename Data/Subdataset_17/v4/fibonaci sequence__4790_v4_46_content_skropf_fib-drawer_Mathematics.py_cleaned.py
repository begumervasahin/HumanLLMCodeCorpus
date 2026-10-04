
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
CHARACTER_MAP = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
    17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
    25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W',
    33: 'X', 34: 'Y', 35: 'Z'
}
HEBREW_ALPHABET = {
    1: ['alef', '\u05D0', ''], 2: ['bet', '\u05D1', 'B'], 3: ['gimel', '\u05D2', 'G'],
    4: ['dalet', '\u05D3', 'D'], 5: ['he', '\u05D4', 'H'], 6: ['vav', '\u05D5', 'V'],
    7: ['zayin', '\u05D6', 'Z'], 8: ['het', '\u05D7', 'H'], 9: ['tet', '\u05D8', 'T'],
    10: ['yud', '\u05D9', 'Y'], 20: ['kaf', '\u05DB', 'K'], 30: ['lamed', '\u05DC', 'L'],
    40: ['mem', '\u05DE', 'M'], 50: ['nun', '\u05E0', 'N'], 60: ['samekh', '\u05E1', 'S'],
    70: ['ayin', '\u05E2', ''], 80: ['pe', '\u05E4', 'P'], 90: ['tsadi', '\u05E6', 'TS'],
    100: ['kuf', '\u05E7', 'K'], 200: ['resh', '\u05E8', 'R'],
    300: ['shin', '\u05E9', 'SH'], 400: ['tav', '\u05EA', 'T']
}
HEBREW_ALPHABET_FINALS = {
    20: ['final kaf', '\u05DA'], 40: ['final mem', '\u05DD'],
    50: ['final nun', '\u05DF'], 80: ['final pe', '\u05E3'],
    90: ['final tsadi', '\u05E5']
}
def get_doubling_sequence(start, base):
    while True:
        yield convert_decimal_to_base(start, base)
        start *= 2
def convert_decimal_to_base(number, base, converted=''):
    if number == 0:
        return converted or '0'
    if 2 <= base <= 36:
        return convert_decimal_to_base(number
    return convert_decimal_to_base(number
def convert_base_to_decimal(number, base, converted=0, power=0):
    number = str(number)
    if not number:
        return converted
    if 2 <= base <= 36:
        return convert_base_to_decimal(number[:-1], base, converted + CHARACTER_MAP.index(number[-1]) * (base ** power), power + 1)
    integer_part, fractional_part = number.split('.') if '.' in number else (number, '')
    return convert_base_to_decimal(integer_part, base, converted + int(fractional_part) * (base ** power), power + 1)
def get_digital_root(number, base):
    decimal_value = convert_base_to_decimal(number, base)
    if decimal_value < base:
        return number
    if 2 <= base <= 36:
        return get_digital_root(convert_decimal_to_base(sum(CHARACTER_MAP.index(elem) for elem in str(number)), base), base)
    return get_digital_root(convert_decimal_to_base(sum(int(elem) for elem in str(number).split('.')), base), base)
if __name__ == "__main__":
    base = 10
    start_value = 1
    sequence_generator = get_doubling_sequence(start_value, base)
    for _ in range(10):
        print(next(sequence_generator))