
print('Huffman Encoding Program')
file_name = input('Enter the name of a text file to open: ') + '.txt'
with open(file_name, 'r') as file:
    contents = file.read()
letters = []
only_letters = []
for letter in contents:
    if letter not in letters:
        freq = contents.count(letter)
        letters.append(freq)
        letters.append(letter)
        only_letters.append(letter)
temp_letters_with_frequency = list.copy(letters)
letters_with_frequency = []
for i in range(0, len(temp_letters_with_frequency), 2):
    new_element_for_letters_freq = [temp_letters_with_frequency[i], temp_letters_with_frequency[i + 1]]
    letters_with_frequency.append(new_element_for_letters_freq)
letters_with_frequency.sort(key=lambda x: x[0], reverse=True)
nodes = []
while len(letters) > 0:
    nodes.append(letters[0:2])
    letters = letters[2:]
nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)
def combine(nodes):
    pos = 0
    newnode = []
    if len(nodes) > 1:
        nodes.sort(key=lambda x: int(x[0]))
        nodes[pos].append('0')
        nodes[pos + 1].append('1')
        combined_node1 = str(nodes[pos][0]) + str(nodes[pos + 1][0])
        combined_node2 = str(nodes[pos][1]) + str(nodes[pos + 1][1])
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes = []
        newnodes.append(newnode)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        huffman_tree.append(nodes)
        combine(nodes)
    return huffman_tree
newnodes = combine(nodes)
huffman_tree.sort(key=lambda x: str(x[0]), reverse=True)
checklist = []
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)
letter_binary = []
if len(only_letters) == 1:
    letter_code = [only_letters[0], '0']
    letter_binary.append(letter_code * len(contents))
else:
    for letter in only_letters:
        lettercode = ''
        for node in checklist:
            if len(node) > 2 and letter in node[1]:
                lettercode = lettercode + node[2]
        letter_code = [letter, lettercode]
        letter_binary.append(letter_code)
lookup = {y: x for x, y in letters_with_frequency}
huffman_table_sorted = sorted(letter_binary, key=lambda x: lookup[x[0]], reverse=True)
print('Binary codes are: ')
print('Character\tBinary Huffman\tBinary ASCII')
for i in range(len(huffman_table_sorted)):
    print('\'%s\'\t\t%s\t\t%s' % (huffman_table_sorted[i][0], huffman_table_sorted[i][1], bin(ord(huffman_table_sorted[i][0][0]))[2:]))
bitstring = ''
for character in contents:
    for item in letter_binary:
        if character in item:
            bitstring = bitstring + item[1]
print("The contents of the file are: \'%s\'" % contents)
print('The Huffman encoded contents are: \'%s\'' % bitstring)