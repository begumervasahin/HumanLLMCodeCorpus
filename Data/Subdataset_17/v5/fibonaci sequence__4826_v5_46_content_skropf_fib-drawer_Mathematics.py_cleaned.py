
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
CHARACTER_MAP = {i: c for i, c in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
HEBREW_ALPHABET = {
    1: ['alef', '\u05D0', ''], 2: ['bet', '\u05D1', 'B'], 3: ['gimel', '\u05D2', 'G'],
    4: ['dalet', '\u05D3', 'D'], 5: ['he', '\u05D4', 'H'], 6: ['vav', '\u05D5', 'V'],
    7: ['zayin', '\u05D6', 'Z'], 8: ['het', '\u05D7', 'H'], 9: ['tet', '\u05D8', 'T'],
    10: ['yud', '\u05D9', 'Y'], 20: ['kaf', '\u05DB', 'K'], 30: ['lamed', '\u05DC', 'L'],
    40: ['mem', '\u05DE', 'M'], 50: ['nun', '\u05E0', 'N'], 60: ['samekh', '\u05E1', 'S'],
    70: ['ayin', '\u05E2', ''], 80: ['pe', '\u05E4', 'P'], 90: ['tsadi', '\u05E6', 'TS'],
    100: ['kuf', '\u05E7', 'K'], 200: ['resh', '\u05E8', 'R'], 300: ['shin', '\u05E9', 'SH'], 400: ['tav', '\u05EA', 'T']
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
    if not number:
        return converted
    if 2 <= base <= 36:
        return convert_base_to_decimal(number[:-1], base, converted + CHARACTER_MAP.index(number[-1]) * (base ** power), power + 1)
    integer_part, fractional_part = (number.split('.') + [''])[:2]
    return convert_base_to_decimal(integer_part, base, converted + int(fractional_part) * (base ** power), power + 1)
def get_digital_root(number, base):
    decimal_value = convert_base_to_decimal(number, base)
    if decimal_value < base:
        return number
    if 2 <= base <= 36:
        return get_digital_root(convert_decimal_to_base(sum(CHARACTER_MAP.index(c) for c in number), base), base)
    return get_digital_root(convert_decimal_to_base(sum(int(c) for c in number.split('.')), base), base)
if __name__ == "__main__":
    base = 10
    start_value = 1
    sequence_generator = get_doubling_sequence(start_value, base)
    for _ in range(10):
        print(next(sequence_generator))