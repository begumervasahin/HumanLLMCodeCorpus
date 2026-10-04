def calculate_frequencies(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
def huffman_encoding(frequency):
    chars = list(frequency.keys())
    counts = list(frequency.values())
    huffman_tree = []
    huffman_codes = {char: "" for char in chars}
    while len(counts) > 1:
        combined = sorted(zip(counts, chars))
        counts, chars = zip(*combined)
        left = counts[0]
        right = counts[1]
        counts = counts[2:]
        chars = chars[2:]
        merged_freq = left + right
        merged_chars = "".join(sorted(chars[:2]))
        for char in merged_chars:
            if char in huffman_codes:
                huffman_codes[char] = ("0" if char in chars[0] else "1") + huffman_codes[char]
        counts = [merged_freq] + list(counts)
        chars = [merged_chars] + list(chars)
    return huffman_codes
def encode_text(text, huffman_codes):
    encoded_text = ''.join(huffman_codes[char] for char in text)
    return encoded_text
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
def main():
    with open("input.txt", "r") as f:
        text = f.readline().strip().lower()
    print("The String:", text)
    frequency = calculate_frequencies(text)
    print("Frequency Table before sorting:", frequency)
    huffman_codes = huffman_encoding(frequency)
    print("Huffman Codes:", huffman_codes)
    encoded_text = encode_text(text, huffman_codes)
    print("Encoded Text:", encoded_text)
    write_to_file("output.txt", encoded_text)
    huffman_dict_content = "\n".join(f"{char}={code}" for char, code in huffman_codes.items())
    write_to_file("dictionary.txt", huffman_dict_content)
    print("Huffman Encoding Complete.")
if __name__ == "__main__":
    main()