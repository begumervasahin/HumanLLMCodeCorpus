
import numpy.random as rand
import sys
ACGT = "acgt"
BITS = "01"
def get_random_acgt(length, delta=None):
    x = "".join([ACGT[rand.randint(0, len(ACGT))] for _ in range(length)])
    if delta is None:
        return x, x
    delta_idx = rand.permutation(len(x))[:delta]
    y = "".join(
        [ACGT[rand.randint(0, len(ACGT))] if i in delta_idx else x[i] for i in range(len(x))]
    )
    return x, y
def get_random_bits(length, delta=None):
    x = "".join([BITS[rand.randint(0, len(BITS))] for _ in range(length)])
    if delta is None:
        return x, x
    delta_idx = rand.permutation(len(x))[:delta]
    y = "".join(
        [BITS[rand.randint(0, len(BITS))] if i in delta_idx else x[i] for i in range(len(x))]
    )
    return x, y
functions = {
    "bits": get_random_bits,
    "acgt": get_random_acgt
}
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: python {__file__} acgt/bits N")
        print("acgt - generate sequences of acgt")
        print("bits - generate sequences of binary digits")
        print("N - length of the random strings to generate")
    else:
        seq_type = sys.argv[1]
        size = int(sys.argv[2])
        delta = round(size * 0.3)
        if seq_type in functions:
            x, y = functions[seq_type](size, delta)
            with open(f"{seq_type}.txt", 'w') as f:
                f.write(f"{x}\n{y}")
        else:
            print("Unknown type. Please specify a valid type (acgt/bits).")