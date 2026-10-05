from math import floor, ceil
from sys import stdout as so
from bisect import bisect
def encode(sequence, probabilities):
    precision = 32
    one = int(2 ** precision - 1)
    quarter = int(ceil(one / 4))
    half = 2 * quarter
    threequarters = 3 * quarter
    probabilities = {a: probabilities[a] for a in probabilities if probabilities[a] > 0}
    cumulative_probabilities = [0]
    for symbol in probabilities:
        cumulative_probabilities.append(probabilities[symbol] + cumulative_probabilities[-1])
    cumulative_probabilities.pop()
    cumulative_probabilities = {symbol: cumulative_prob for symbol, cumulative_prob in zip(probabilities, cumulative_probabilities)}
    encoded_sequence = []
    lo, hi = 0, one
    straddle = 0
    for k in range(len(sequence)):
        if k % 100 == 0:
            so.write('Arithmetic encoded %d%%    \r' % int(floor(k / len(sequence) * 100)))
            so.flush()
        lohi_range = (hi - lo) + 1
        lo = int(ceil(lo + (cumulative_probabilities[sequence[k]] * lohi_range)))
        hi = int(floor(lo + (probabilities[sequence[k]] * lohi_range)))
        if lo == hi:
            raise ValueError('Zero interval!')
        while True:
            if hi < half:
                encoded_sequence.append(0)
                for i in range(straddle):
                    encoded_sequence.append(1)
                straddle = 0
            elif lo >= half:
                encoded_sequence.append(1)
                for i in range(straddle):
                    encoded_sequence.append(0)
                straddle = 0
                lo = lo - half
                hi = hi - half
            elif lo >= quarter and hi < threequarters:
                straddle += 1
                lo = lo - quarter
                hi = hi - quarter
            else:
                break
            lo *= 2
            hi = (2 * hi) + 1
    straddle += 1
    if lo < quarter:
        encoded_sequence.append(0)
        for i in range(straddle):
            encoded_sequence.append(1)
    else:
        encoded_sequence.append(1)
        for i in range(straddle):
            encoded_sequence.append(0)
    return encoded_sequence
def decode(encoded_sequence, probabilities, n):
    precision = 32
    one = int(2 ** precision - 1)
    quarter = int(ceil(one / 4))
    half = 2 * quarter
    threequarters = 3 * quarter
    probabilities = {a: probabilities[a] for a in probabilities if probabilities[a] > 0}
    alphabet = list(probabilities)
    cumulative_probabilities = [0]
    for symbol in probabilities:
        cumulative_probabilities.append(cumulative_probabilities[-1] + probabilities[symbol])
    cumulative_probabilities.pop()
    probabilities = list(probabilities.values())
    encoded_sequence.extend(precision * [0])
    decoded_sequence = n * [0]
    value = int(''.join(str(bit) for bit in encoded_sequence[0:precision]), 2)
    encoded_sequence_position = precision
    lo, hi = 0, one
    decoded_sequence_position = 0
    while 1:
        if decoded_sequence_position % 100 == 0:
            so.write('Arithmetic decoded %d%%    \r' % int(floor(decoded_sequence_position / n * 100)))
            so.flush()
        lohi_range = hi - lo + 1
        symbol = bisect(cumulative_probabilities, (value - lo) / lohi_range) - 1
        decoded_sequence[decoded_sequence_position] = alphabet[symbol]
        lo = lo + int(ceil(cumulative_probabilities[symbol] * lohi_range))
        hi = lo + int(floor(probabilities[symbol] * lohi_range))
        if lo == hi:
            raise ValueError('Zero interval!')
        while True:
            if hi < half:
                pass
            elif lo >= half:
                lo = lo - half
                hi = hi - half
                value = value - half
            elif lo >= quarter and hi < threequarters:
                lo = lo - quarter
                hi = hi - quarter
                value = value - quarter
            else:
                break
            lo = 2 * lo
            hi = 2 * hi + 1
            value = 2 * value + encoded_sequence[encoded_sequence_position]
            encoded_sequence_position += 1
            if encoded_sequence_position == len(encoded_sequence):
                break
        decoded_sequence_position += 1
        if decoded_sequence_position == n or encoded_sequence_position == len(encoded_sequence):
            break
    return decoded_sequence
if __name__ == "__main__":
    input_sequence = [0, 1, 0, 1, 0, 1, 0, 1]
    probabilities = {0: 0.5, 1: 0.5}
    encoded_sequence = encode(input_sequence, probabilities)
    print("Encoded sequence:", encoded_sequence)
    decoded_sequence = decode(encoded_sequence, probabilities, len(input_sequence))
    print("Decoded sequence:", decoded_sequence)