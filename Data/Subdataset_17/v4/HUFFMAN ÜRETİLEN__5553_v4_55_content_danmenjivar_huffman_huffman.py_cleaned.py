
print('Huffman Encoding Program')
file_name = input('Enter the name of a text file to open: ') + '.txt'
with open(file_name, 'r') as file:
    contents = file.read()
letters = {}
for letter in contents:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1
nodes = [[frequency, letter] for letter, frequency in letters.items()]
nodes.sort()
def build_huffman_tree(nodes):
    while len(nodes) > 1:
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = [left[0] + right[0], left, right]
        left.append('0')
        right.append('1')
        nodes.append(new_node)
        nodes.sort(key=lambda x: x[0])
    return nodes[0]
huffman_tree = build_huffman_tree(nodes)
def generate_codes(tree, prefix=''):
    if len(tree) == 2:
        return {tree[1]: prefix}
    else:
        codes = {}
        codes.update(generate_codes(tree[1], prefix + tree[1][-1]))
        codes.update(generate_codes(tree[2], prefix + tree[2][-1]))
        return codes
huffman_codes = generate_codes(huffman_tree)
print('Binary codes are:')
print('Character\tBinary Huffman\tBinary ASCII')
for char, code in sorted(huffman_codes.items(), key=lambda item: letters[item[0]], reverse=True):
    print(f"'{char}'\t\t{code}\t\t{bin(ord(char))[2:]}")
encoded_string = ''.join(huffman_codes[char] for char in contents)
print(f"The contents of the file are: '{contents}'")
print(f"The Huffman encoded contents are: '{encoded_string}'")