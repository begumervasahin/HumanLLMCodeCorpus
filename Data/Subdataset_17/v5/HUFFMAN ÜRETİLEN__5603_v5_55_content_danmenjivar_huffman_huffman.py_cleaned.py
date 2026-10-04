def main():
    print("Huffman Encoding Program")
    file_name = input("Enter the name of a text file to open: ") + ".txt"
    contents = read_file(file_name)
    frequency_dict = calculate_frequencies(contents)
    huffman_tree = build_huffman_tree(frequency_dict)
    huffman_codes = generate_codes(huffman_tree)
    display_huffman_codes(huffman_codes, frequency_dict)
    encoded_string = encode_contents(contents, huffman_codes)
    print(f"The contents of the file are: '{contents}'")
    print(f"The Huffman encoded contents are: '{encoded_string}'")
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
def calculate_frequencies(contents):
    frequency_dict = {}
    for char in contents:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict
def build_huffman_tree(frequency_dict):
    nodes = [[freq, char] for char, freq in frequency_dict.items()]
    nodes.sort(key=lambda x: x[0])
    while len(nodes) > 1:
        left = nodes.pop(0)
        right = nodes.pop(0)
        combined_node = [left[0] + right[0], left, right]
        nodes.append(combined_node)
        nodes.sort(key=lambda x: x[0])
    return nodes[0]
def generate_codes(tree, prefix=''):
    if len(tree) == 2:
        return {tree[1]: prefix}
    codes = {}
    codes.update(generate_codes(tree[1], prefix + '0'))
    codes.update(generate_codes(tree[2], prefix + '1'))
    return codes
def display_huffman_codes(huffman_codes, frequency_dict):
    print('Binary codes are:')
    print('Character\tBinary Huffman\tBinary ASCII')
    for char, code in sorted(huffman_codes.items(), key=lambda item: frequency_dict[item[0]], reverse=True):
        print(f"'{char}'\t\t{code}\t\t{bin(ord(char))[2:]}")
def encode_contents(contents, huffman_codes):
    return ''.join(huffman_codes[char] for char in contents)
if __name__ == "__main__":
    main()