from math import floor, ceil
from sys import stdout as so
from bisect import bisect
def encode(x, p):
    precision = 32
    one = int(2 ** precision - 1)
    quarter = int(ceil(one / 4))
    half = 2 * quarter
    threequarters = 3 * quarter
    p = {a: p[a] for a in p if p[a] > 0}
    f = [0]
    for a in p:
        f.append(p[a] + f[-1])
    f.pop()
    f = {a: mf for a, mf in zip(p, f)}
    y = []
    lo, hi = 0, one
    straddle = 0
    for k in range(len(x)):
        if k % 100 == 0:
            so.write(f'Arithmetic encoded {floor(k / len(x) * 100)}%    \r')
            so.flush()
        lohi_range = (hi - lo) + 1
        lo = int(ceil(lo + (f[x[k]] * lohi_range)))
        hi = int(floor(lo + (p[x[k]] * lohi_range)))
        if lo == hi:
            raise ValueError('Zero interval!')
        while True:
            if hi < half:
                y.append(0)
                y.extend([1] * straddle)
                straddle = 0
            elif lo >= half:
                y.append(1)
                y.extend([0] * straddle)
                straddle = 0
                lo -= half
                hi -= half
            elif lo >= quarter and hi < threequarters:
                straddle += 1
                lo -= quarter
                hi -= quarter
            else:
                break
            lo *= 2
            hi = (2 * hi) + 1
    straddle += 1
    if lo < quarter:
        y.append(0)
        y.extend([1] * straddle)
    else:
        y.append(1)
        y.extend([0] * straddle)
    return y
def decode(y, p, n):
    precision = 32
    one = int(2 ** precision - 1)
    quarter = int(ceil(one / 4))
    half = 2 * quarter
    threequarters = 3 * quarter
    p = {a: p[a] for a in p if p[a] > 0}
    alphabet = list(p)
    f = [0]
    for a in p:
        f.append(f[-1] + p[a])
    f.pop()
    p = list(p.values())
    y.extend([0] * precision)
    x = [0] * n
    value = int(''.join(map(str, y[:precision])), 2)
    y_position = precision
    lo, hi = 0, one
    x_position = 0
    while x_position < n:
        if x_position % 100 == 0:
            so.write(f'Arithmetic decoded {floor(x_position / n * 100)}%    \r')
            so.flush()
        lohi_range = hi - lo + 1
        a = bisect(f, (value - lo) / lohi_range) - 1
        x[x_position] = alphabet[a]
        lo = lo + int(ceil(f[a] * lohi_range))
        hi = lo + int(floor(p[a] * lohi_range))
        if lo == hi:
            raise ValueError('Zero interval!')
        while True:
            if hi < half:
                pass
            elif lo >= half:
                lo -= half
                hi -= half
                value -= half
            elif lo >= quarter and hi < threequarters:
                lo -= quarter
                hi -= quarter
                value -= quarter
            else:
                break
            lo *= 2
            hi = (2 * hi) + 1
            value = (2 * value) + y[y_position]
            y_position += 1
            if y_position == len(y):
                break
        x_position += 1
    return x
if __name__ == "__main__":
    probabilities = {'a': 0.1, 'b': 0.2, 'c': 0.3, 'd': 0.4}
    sequence = ['a', 'b', 'c', 'd', 'a', 'c', 'b', 'd']
    encoded_sequence = encode(sequence, probabilities)
    print("Encoded sequence:", encoded_sequence)
    decoded_sequence = decode(encoded_sequence, probabilities, len(sequence))
    print("Decoded sequence:", decoded_sequence)