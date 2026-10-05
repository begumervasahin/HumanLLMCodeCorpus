def read_input_file(filename):
    with open(filename, "r") as file:
        return file.readline().lower()
def build_frequency_table(string):
    return {char: string.count(char) for char in set(string)}
def sort_frequency_table(freq_table):
    return dict(sorted(freq_table.items(), key=lambda item: item[1], reverse=True))
def huffman_encoding(freq_table):
    encoder = {}
    sorted_chars = list(freq_table.keys())
    while len(freq_table) > 1:
        char1, freq1 = freq_table.popitem()
        char2, freq2 = freq_table.popitem()
        total_freq = freq1 + freq2
        merged_char = char1 + char2
        for char in char1:
            encoder[char] = '0' + encoder.get(char, '')
        for char in char2:
            encoder[char] = '1' + encoder.get(char, '')
        freq_table[merged_char] = total_freq
        freq_table = sort_frequency_table(freq_table)
    return encoder
def encode_string(string, encoder):
    return ''.join(encoder[char] for char in string)
def write_encoded_string(filename, encoded_string):
    with open(filename, "w") as file:
        file.write(encoded_string)
def write_dictionary(filename, encoder):
    with open(filename, "w") as file:
        for char, code in encoder.items():
            file.write(f"{char}={code}\n")
def main():
    input_filename = "input.txt"
    output_filename = "output.txt"
    dictionary_filename = "dictionary.txt"
    original_string = read_input_file(input_filename)
    print("Original String:", original_string)
    frequency_table = build_frequency_table(original_string)
    print("Frequency Table:", frequency_table)
    encoder = huffman_encoding(frequency_table)
    print("Encoder:", encoder)
    encoded_string = encode_string(original_string, encoder)
    print("Encoded String:", encoded_string)
    write_encoded_string(output_filename, encoded_string)
    write_dictionary(dictionary_filename, encoder)
if __name__ == "__main__":
    main()