import numpy.random as rand
import sys
ACGT_CHARS = "acgt"
BITS_CHARS = "01"
def generate_random_sequence(chars, length):
    return "".join([chars[rand.randint(0, len(chars))] for _ in range(length)])
def get_random_sequence(chars, length, delta=None):
    x = generate_random_sequence(chars, length)
    if delta is None:
        return x, x
    delta_idx = rand.permutation(len(x))[:delta]
    y = "".join([chars[rand.randint(0, len(chars))] if i in delta_idx else x[i] for i in range(len(x))])
    return x, y
def get_random_acgt(length, delta=None):
    return get_random_sequence(ACGT_CHARS, length, delta)
def get_random_bits(length, delta=None):
    return get_random_sequence(BITS_CHARS, length, delta)
FUNCTIONS = {
    "bits": get_random_bits,
    "acgt": get_random_acgt
}
def main():
    if len(sys.argv) < 3:
        print("Usage: python " + __file__ + " acgt/bits N")
        print("acgt - generate sequences of acgt")
        print("bits - generate sequences of binary digits")
        print("N - length of the random strings to generate")
        return
    sequence_type = sys.argv[1]
    length = int(sys.argv[2])
    delta = round(length * 0.3)
    if sequence_type in FUNCTIONS:
        x, y = FUNCTIONS[sequence_type](length, delta)
        with open(sequence_type + ".txt", 'w') as f:
            f.write(x + "\n" + y)
    else:
        print("Unknown type, please specify a valid type (acgt/bits)")
if __name__ == "__main__":
    main()