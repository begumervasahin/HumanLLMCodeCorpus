import collections
def get_file_contents(file_name: str) -> str:
    with open(file_name, 'r') as file:
        return file.read()
def calculate_frequencies(contents: str) -> list:
    frequency = collections.Counter(contents)
    return sorted([[freq, char] for char, freq in frequency.items()], key=lambda x: x[0], reverse=True)
def build_huffman_tree(frequencies: list) -> list:
    nodes = [[freq, char] for freq, char in frequencies]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x[0])
        left = nodes.pop(0)
        right = nodes.pop(0)
        combined_node = [left[0] + right[0], left[1] + right[1]]
        left.append('0')
        right.append('1')
        nodes.append(combined_node)
        nodes.sort(key=lambda x: x[0])
    return nodes
def generate_huffman_codes(tree: list, original_chars: list) -> list:
    checklist = []
    for node in tree:
        if node not in checklist:
            checklist.append(node)
    if len(original_chars) == 1:
        return [[original_chars[0], '0']]
    letter_binary = []
    for char in original_chars:
        code = ''.join([node[2] for node in checklist if len(node) > 2 and char in node[1]])
        letter_binary.append([char, code])
    return letter_binary
def encode_contents(contents: str, huffman_codes: list) -> str:
    bitstring = ''.join([code for char in contents for item, code in huffman_codes if char == item])
    return bitstring
def display_huffman_table(huffman_codes: list, frequencies: dict):
    print('Character\tBinary Huffman\tBinary ASCII')
    huffman_codes_sorted = sorted(huffman_codes, key=lambda x: frequencies[x[0]], reverse=True)
    for char, code in huffman_codes_sorted:
        print(f"'{char}'\t\t{code}\t\t{bin(ord(char))[2:]}")
def main():
    print('Huffman Encoding Program')
    file_name = input('Enter the name of a text file to open: ') + '.txt'
    contents = get_file_contents(file_name)
    frequencies = calculate_frequencies(contents)
    original_chars = [char for _, char in frequencies]
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree, original_chars)
    bitstring = encode_contents(contents, huffman_codes)
    print("The contents of the file are:", repr(contents))
    print("The Huffman encoded contents are:", repr(bitstring))
    frequencies_dict = {char: freq for freq, char in frequencies}
    display_huffman_table(huffman_codes, frequencies_dict)
if __name__ == '__main__':
    main()