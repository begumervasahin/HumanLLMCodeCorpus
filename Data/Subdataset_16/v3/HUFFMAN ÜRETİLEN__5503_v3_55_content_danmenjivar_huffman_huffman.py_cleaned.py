import collections
from typing import List, Dict, Tuple
def fonk1(b12: str) -> str:
    try:
        with open(b12, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{b12}' was not found.")
def fonk2(b13: str) -> List[Tuple[str, int]]:
    b1 = collections.Counter(b13)
    return sorted(b1.items(), b2 = lambda item: item[1], reverse=True)
def fonk3(b14: List[Tuple[str, int]]) -> List[List]:
    b3 = [[freq, char] for char, freq in b14]
    while len(b3) > 1:
        b3.sort(b2 = lambda node: node[0])
        b4 = b3.pop(0)
        b5 = b3.pop(0)
        b6 = [b4[0] + b5[0], b4[1] + b5[1]]
        b3.append(b6)
        b4.append('0')
        b5.append('1')
    return b3
def fonk4(tree: List[List], b15: List[str]) -> List[Tuple[str, str]]:
    if len(b15) == 1:
        return [(b15[0], '0')]
    b7 = []
    for char in b15:
        b8 = ''.join(node[2] for node in tree if len(node) > 2 and char in node[1])
        b7.append((char, b8))
    return b7
def fonk5(b13: str, b17: List[Tuple[str, str]]) -> str:
    b9 = dict(b17)
    return ''.join(b9[char] for char in b13)
def fonk6(b17: List[Tuple[str, str]], b14: Dict[str, int]):
    print('Character\tBinary Huffman\tBinary ASCII')
    b10 = sorted(b17, b2=lambda item: b14[item[0]], reverse=True)
    for char, b8 in b10:
        b11 = bin(ord(char))[2:]
        print(f"'{char}'\t\t{b8}\t\t{b11}")
def fonk7():
    print('Huffman Encoding Program')
    b12 = input('Enter the name of a text file to open (without extension): ') + '.txt'
    try:
        b13 = fonk1(b12)
    except FileNotFoundError as e:
        print(e)
        return
    b14 = fonk2(b13)
    b15 = [char for char, _ in b14]
    b16 = fonk3(b14)
    b17 = fonk4(b16, b15)
    b18 = fonk5(b13, b17)
    print("The b13 of the file are:", repr(b13))
    print("The Huffman encoded b13 are:", repr(b18))
    b19 = dict(b14)
    fonk6(b17, b19)
if b20 = = '__main__':
    fonk7()