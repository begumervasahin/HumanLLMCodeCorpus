import collections
from typing import List, Dict, Tuple
def fonk1(b11: str) -> str:
    with open(b11, 'r') as file:
        return file.read()
def fonk2(b12: str) -> List[Tuple[int, str]]:
    b1 = collections.Counter(b12)
    return sorted(b1.items(), b2 = lambda item: item[1], reverse=True)
def fonk3(b13: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    b3 = [[freq, b8] for b8, freq in b13]
    while len(b3) > 1:
        b3.sort(b2 = lambda x: x[0])
        left, b4 = b3.pop(0), b3.pop(0)
        b5 = [left[0] + b4[0], left[1] + b4[1]]
        b3.append(b5)
        left.append('0')
        b4.append('1')
    return b3
def fonk4(tree: List[Tuple[int, str]], b14: List[str]) -> List[Tuple[str, str]]:
    if len(b14) == 1:
        return [(b14[0], '0')]
    b6 = []
    for b8 in b14:
        b7 = ''.join(node[2] for node in tree if len(node) > 2 and b8 in node[1])
        b6.append((b8, b7))
    return b6
def fonk5(b12: str, b16: List[Tuple[str, str]]) -> str:
    return ''.join(b7 for b8 in b12 for item, b7 in b16 if b8 = = item)
def fonk6(b16: List[Tuple[str, str]], b13: Dict[str, int]):
    print('Character\tBinary Huffman\tBinary ASCII')
    b9 = sorted(b16, b2=lambda item: b13[item[0]], reverse=True)
    for b8, b7 in b9:
        b10 = bin(ord(b8))[2:]
        print(f"'{b8}'\t\t{b7}\t\t{b10}")
def fonk7():
    print('Huffman Encoding Program')
    b11 = input('Enter the name of a text file to open (without extension): ') + '.txt'
    try:
        b12 = fonk1(b11)
    except FileNotFoundError:
        print(f"Error: The file '{b11}' was not found.")
        return
    b13 = fonk2(b12)
    b14 = [b8 for _, b8 in b13]
    b15 = fonk3(b13)
    b16 = fonk4(b15, b14)
    b17 = fonk5(b12, b16)
    print("The b12 of the file are:", repr(b12))
    print("The Huffman encoded b12 are:", repr(b17))
    b18 = dict(b13)
    fonk6(b16, b18)
if b19 = = '__main__':
    fonk7()