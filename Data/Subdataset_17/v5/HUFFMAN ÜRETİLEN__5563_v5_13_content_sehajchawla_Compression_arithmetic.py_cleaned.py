from math import floor, ceil
from sys import stdout as so
from bisect import bisect
def encode(input_sequence, symbol_probabilities):
    precision = 32
    max_value = (1 << precision) - 1
    quarter = (max_value + 1)
    half = 2 * quarter
    three_quarters = 3 * quarter
    symbol_probabilities = {symbol: prob for symbol, prob in symbol_probabilities.items() if prob > 0}
    cumulative_freq = [0]
    for symbol in symbol_probabilities:
        cumulative_freq.append(cumulative_freq[-1] + symbol_probabilities[symbol])
    cumulative_freq.pop()
    cumulative_freq = {symbol: freq for symbol, freq in zip(symbol_probabilities, cumulative_freq)}
    encoded_bits = []
    lo, hi = 0, max_value
    straddle = 0
    for index, symbol in enumerate(input_sequence):
        if index % 100 == 0:
            so.write(f'Arithmetic encoded {int(floor(index / len(input_sequence) * 100))}%    \r')
            so.flush()
        lohi_range = hi - lo + 1
        lo = int(ceil(lo + cumulative_freq[symbol] * lohi_range))
        hi = int(floor(lo + symbol_probabilities[symbol] * lohi_range))
        if lo == hi:
            raise ValueError('Zero interval!')
        while True:
            if hi < half:
                encoded_bits.append(0)
                encoded_bits.extend([1] * straddle)
                straddle = 0
            elif lo >= half:
                encoded_bits.append(1)
                encoded_bits.extend([0] * straddle)
                straddle = 0
                lo -= half
                hi -= half
            elif quarter <= lo < three_quarters and quarter <= hi < three_quarters:
                straddle += 1
                lo -= quarter
                hi -= quarter
            else:
                break
            lo *= 2
            hi = 2 * hi + 1
    straddle += 1
    if lo < quarter:
        encoded_bits.append(0)
        encoded_bits.extend([1] * straddle)
    else:
        encoded_bits.append(1)
        encoded_bits.extend([0] * straddle)
    return encoded_bits
def decode(encoded_bits, symbol_probabilities, symbol_count):
    precision = 32
    max_value = (1 << precision) - 1
    quarter = (max_value + 1)
    half = 2 * quarter
    three_quarters = 3 * quarter
    symbol_probabilities = {symbol: prob for symbol, prob in symbol_probabilities.items() if prob > 0}
    alphabet = list(symbol_probabilities)
    cumulative_freq = [0]
    for symbol in symbol_probabilities:
        cumulative_freq.append(cumulative_freq[-1] + symbol_probabilities[symbol])
    cumulative_freq.pop()
    probabilities = list(symbol_probabilities.values())
    encoded_bits.extend([0] * precision)
    decoded_sequence = [0] * symbol_count
    value = int(''.join(map(str, encoded_bits[:precision])), 2)
    y_position = precision
    lo, hi = 0, max_value
    x_position = 0
    while x_position < symbol_count:
        if x_position % 100 == 0:
            so.write(f'Arithmetic decoded {int(floor(x_position / symbol_count * 100))}%    \r')
            so.flush()
        lohi_range = hi - lo + 1
        symbol_index = bisect(cumulative_freq, (value - lo) / lohi_range) - 1
        decoded_sequence[x_position] = alphabet[symbol_index]
        lo = int(ceil(lo + cumulative_freq[symbol_index] * lohi_range))
        hi = int(floor(lo + probabilities[symbol_index] * lohi_range))
        if lo == hi:
            raise ValueError('Zero interval!')
        while True:
            if hi < half:
                pass
            elif lo >= half:
                lo -= half
                hi -= half
                value -= half
            elif quarter <= lo < three_quarters and quarter <= hi < three_quarters:
                lo -= quarter
                hi -= quarter
                value -= quarter
            else:
                break
            lo *= 2
            hi = 2 * hi + 1
            value = 2 * value + encoded_bits[y_position]
            y_position += 1
        x_position += 1
    return decoded_sequence