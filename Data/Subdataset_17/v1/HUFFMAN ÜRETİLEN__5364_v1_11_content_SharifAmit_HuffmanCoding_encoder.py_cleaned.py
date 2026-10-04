def build_frequency_table(s):
    s = s.lower()
    unique_chars = list(set(s))
    freq_table = [0] * len(unique_chars)
    for char in s:
        idx = unique_chars.index(char)
        if freq_table[idx] == 0:
            freq_table[idx] = s.count(char)
    return unique_chars, freq_table
def sort_by_frequency(chars, freqs):
    sorted_chars = []
    sorted_freqs = []
    while freqs:
        max_freq = max(freqs)
        idx = freqs.index(max_freq)
        sorted_freqs.append(max_freq)
        sorted_chars.append(chars[idx])
        chars.pop(idx)
        freqs.pop(idx)
    return sorted_chars, sorted_freqs
def huffman_encoding(chars, freqs):
    encoder = ["null"] * len(chars)
    binary_tree = list(freqs)
    string_tree = list(chars)
    while len(binary_tree) > 1:
        right = min(binary_tree)
        right_idx = binary_tree.index(right)
        right_str = string_tree[right_idx]
        for char in right_str:
            char_idx = chars.index(char)
            if encoder[char_idx] == "null":
                encoder[char_idx] = "0"
            else:
                encoder[char_idx] = "0" + encoder[char_idx]
        binary_tree.pop(right_idx)
        string_tree.pop(right_idx)
        left = min(binary_tree)
        left_idx = binary_tree.index(left)
        left_str = string_tree[left_idx]
        for char in left_str:
            char_idx = chars.index(char)
            if encoder[char_idx] == "null":
                encoder[char_idx] = "1"
            else:
                encoder[char_idx] = "1" + encoder[char_idx]
        binary_tree.pop(left_idx)
        string_tree.pop(left_idx)
        binary_tree.insert(0, left + right)
        string_tree.insert(0, left_str + right_str)
    return encoder
def encode_string(s, chars, encoder):
    encoded_string = ""
    for char in s:
        idx = chars.index(char)
        encoded_string += encoder[idx]
    return encoded_string
def save_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
def main():
    with open("input.txt", "r") as f:
        s = f.readline().strip()
    chars, freqs = build_frequency_table(s)
    print("The String:", s)
    print("The char list:", chars)
    print("Frequency Table before sorting:", freqs)
    sorted_chars, sorted_freqs = sort_by_frequency(chars, freqs)
    print("Frequency Table after sorting:", sorted_freqs)
    print("Sorted char list:", sorted_chars)
    encoder = huffman_encoding(sorted_chars, sorted_freqs)
    print("Huffman Encoder:", encoder)
    encoded_string = encode_string(s, sorted_chars, encoder)
    print("Encoded string:", encoded_string)
    save_to_file("output.txt", encoded_string)
    dictionary_content = "\n".join(f"{char}={encoder[i]}" for i, char in enumerate(sorted_chars))
    save_to_file("dictionary.txt", dictionary_content)
    print("Encoding dictionary saved to dictionary.txt")
if __name__ == "__main__":
    main()