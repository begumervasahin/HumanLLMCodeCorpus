def calculate_frequencies(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
def huffman_encoding(frequency):
    chars = list(frequency.keys())
    counts = list(frequency.values())
    huffman_codes = {char: "" for char in chars}
    while len(counts) > 1:
        combined = sorted(zip(counts, chars))
        counts, chars = zip(*combined)
        left, right = counts[:2], chars[:2]
        counts = counts[2:]
        chars = chars[2:]
        merged_freq = sum(left)
        merged_chars = "".join(sorted(right))
        for i, char in enumerate(right):
            huffman_codes[char] = ("0" if i == 0 else "1") + huffman_codes[char]
        counts = [merged_freq] + list(counts)
        chars = [merged_chars] + list(chars)
    return huffman_codes
def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
def main():
    with open("input.txt", "r") as file:
        text = file.readline().strip().lower()
    print("Input Text:", text)
    frequency = calculate_frequencies(text)
    print("Frequency Table:", frequency)
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