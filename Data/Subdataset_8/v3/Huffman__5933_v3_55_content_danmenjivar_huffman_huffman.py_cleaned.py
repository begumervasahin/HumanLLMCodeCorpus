def main():
    print('Huffman Encoding Program')
    file_name = input('Enter the name of a text file to open: ') + '.txt'
    contents = read_file_contents(file_name)
    letters_with_frequency = count_letter_frequencies(contents)
    huffman_tree = build_huffman_tree(letters_with_frequency)
    huffman_table_sorted = build_huffman_table(huffman_tree)
    print_huffman_table(huffman_table_sorted)
    bitstring = encode_contents(contents, huffman_table_sorted)
    print_file_contents(contents)
    print_encoded_contents(bitstring)
def read_file_contents(file_name):
    with open(file_name, 'r') as file:
        return file.read()
def count_letter_frequencies(contents):
    frequency_dict = {}
    for letter in contents:
        frequency_dict[letter] = frequency_dict.get(letter, 0) + 1
    return sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
def build_huffman_tree(letters_with_frequency):
    nodes = [[(freq, letter)] for letter, freq in letters_with_frequency]
    while len(nodes) > 1:
        smallest_nodes = nodes[-2:]
        combined_node = (smallest_nodes[0][0][0] + smallest_nodes[1][0][0], smallest_nodes)
        nodes = nodes[:-2] + [combined_node]
        nodes.sort()
    return nodes
def build_huffman_table(huffman_tree):
    huffman_table = []
    encode_huffman_tree(huffman_tree, '', huffman_table)
    return sorted(huffman_table, key=lambda x: x[0], reverse=True)
def encode_huffman_tree(tree, code, huffman_table):
    if len(tree) == 1:
        huffman_table.append((tree[0][1], code))
    else:
        encode_huffman_tree(tree[0][1], code + '0', huffman_table)
        encode_huffman_tree(tree[1][1], code + '1', huffman_table)
def print_huffman_table(huffman_table_sorted):
    print('Binary codes are:')
    print('Character\tBinary Huffman\tBinary ASCII')
    for character, binary_code in huffman_table_sorted:
        ascii_code = bin(ord(character))[2:]
        print(f'\'{character}\'\t\t{binary_code}\t\t{ascii_code}')
def encode_contents(contents, huffman_table_sorted):
    bitstring = ''
    for character in contents:
        for item in huffman_table_sorted:
            if character in item:
                bitstring += item[1]
    return bitstring
def print_file_contents(contents):
    print(f"The contents of the file are: '{contents}'")
def print_encoded_contents(bitstring):
    print(f"The Huffman encoded contents are: '{bitstring}'")
if __name__ == '__main__':
    main()