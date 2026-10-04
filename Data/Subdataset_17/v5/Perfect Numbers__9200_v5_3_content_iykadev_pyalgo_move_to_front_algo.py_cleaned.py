from string import ascii_lowercase
SYMBOL_TABLE = list(ascii_lowercase)
def move_to_front_encode(string, symbol_table):
    sequence = []
    pad = symbol_table[:]
    for char in string:
        index = pad.index(char)
        sequence.append(index)
        pad = [pad.pop(index)] + pad
    return sequence
def move_to_front_decode(sequence, symbol_table):
    chars = []
    pad = symbol_table[:]
    for index in sequence:
        char = pad[index]
        chars.append(char)
        pad = [pad.pop(index)] + pad
    return ''.join(chars)
def main():
    test_strings = ['broood', 'bananaaa', 'hiphophiphop']
    for s in test_strings:
        encoded = move_to_front_encode(s, SYMBOL_TABLE)
        decoded = move_to_front_decode(encoded, SYMBOL_TABLE)
        print(f'{s:14} encodes to {encoded}, which decodes back to {decoded}')
if __name__ == '__main__':
    main()