def build_frequency_table(s):
    s = s.lower()
    unique_chars = list(set(s))
    freq_table = [s.count(char) for char in unique_chars]
    return unique_chars, freq_table
def sort_by_frequency(chars, freqs):
    combined = sorted(zip(freqs, chars), reverse=True)
    sorted_freqs, sorted_chars = zip(*combined)
    return list(sorted_chars), list(sorted_freqs)
def huffman_encoding(chars, freqs):
    encoder = [""] * len(chars)
    binary_tree = list(freqs)
    string_tree = list(chars)
    while len(binary_tree) > 1:
        right_idx = binary_tree.index(min(binary_tree))
        right_freq = binary_tree.pop(right_idx)
        right_str = string_tree.pop(right_idx)
        left_idx = binary_tree.index(min(binary_tree))
        left_freq = binary_tree.pop(left_idx)
        left_str = string_tree.pop(left_idx)
        for char in right_str:
            encoder[chars.index(char)] = "0" + encoder[chars.index(char)]
        for char in left_str:
            encoder[chars.index(char)] = "1" + encoder[chars.index(char)]
        binary_tree.insert(0, left_freq + right_freq)
        string_tree.insert(0, left_str + right_str)
    return encoder
def encode_string(s, chars, encoder):
    return ''.join(encoder[chars.index(char)] for char in s)
def save_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
def main():
    with open("input.txt", "r") as file:
        input_string = file.readline().strip()
    chars, freqs = build_frequency_table(input_string)
    print("Original String:", input_string)
    print("Character List:", chars)
    print("Frequency Table (Unsorted):", freqs)
    sorted_chars, sorted_freqs = sort_by_frequency(chars, freqs)
    print("Frequency Table (Sorted):", sorted_freqs)
    print("Sorted Character List:", sorted_chars)
    encoder = huffman_encoding(sorted_chars, sorted_freqs)
    print("Huffman Encoder:", encoder)
    encoded_string = encode_string(input_string, sorted_chars, encoder)
    print("Encoded String:", encoded_string)
    save_to_file("output.txt", encoded_string)
    dictionary_content = "\n".join(f"{char}={encoder[i]}" for i, char in enumerate(sorted_chars))
    save_to_file("dictionary.txt", dictionary_content)
    print("Huffman encoding dictionary saved to dictionary.txt")
if __name__ == "__main__":
    main()