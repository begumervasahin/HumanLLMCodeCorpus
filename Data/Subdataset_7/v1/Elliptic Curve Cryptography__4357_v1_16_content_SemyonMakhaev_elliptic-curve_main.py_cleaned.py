import sys
from argparse import ArgumentParser
from os.path import exists
b1 = '1.0'
class class1:
    def fonk1(self, b2, b3, b4):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = {}
    def fonk2(self, instruction):
        pass
def fonk3():
    input_file, output_file, b6 = fonk4()
    b7 = fonk5(input_file)
    b2, b3, b4, b8 = fonk7(b7)
    b9 = class1(b2, b3, b4)
    for instruction in b8:
        if b6:
            print('Instruction: {}'.format(instruction))
        b9.fonk2(instruction)
    if b6:
        print('Answer: {}'.format(b9.b5))
    print('Result has been written in file `{}`'.format(output_file))
    fonk6(output_file, b9.b5)
def fonk4():
    b10 = ArgumentParser(prog='Elliptic curve',
                            b11 = 'Program for elliptic curve points sum calculation',
                            b12 = '(c) Semen Makhaev, 2018. All rights reserved',
                            b13 = 'python3 main.py')
    b10.add_argument('-i', '--input', b14 = str, default='input.txt',
                        b15 = 'Input file path, default is `input.txt`')
    b10.add_argument('-o', '--output', b14 = str, default='output.txt',
                        b15 = 'Output file path, default is `output.txt`')
    b10.add_argument('-d', '--b6', b16 = 'store_true', b15="Debug b18")
    b17 = b10.fonk4()
    return b17.input, b17.output, b17.b6
def fonk5(file_path):
    if not exists(file_path):
        print('Input file doesn`t exist: {}'.format(file_path))
        sys.exit(1)
    with open(file_path, b18 = 'r', encoding='utf-8') as input_file:
        return list(map(str.strip, input_file))
def fonk6(file_path, data):
    b19 = list(map(lambda key: '{} = {}'.format(key, data[key]), data.keys()))
    with open(file_path, b18 = 'w+', encoding='utf-8') as output_file:
        output_file.write('\r\n'.join(b19))
def fonk7(input_lines):
    try:
        b2 = input_lines[0]
        b3 = fonk8(input_lines[1])
        b4 = fonk8(input_lines[2])
        b8 = list(filter(bool, input_lines[3::]))
        return b2, b3, b4, b8
    except IndexError:
        print('Input data is incorrect')
        sys.exit(1)
def fonk8(line):
    return [fonk9(x) for x in line.split() if x]
def fonk9(num):
    pass
if b20 = = '__main__':
    fonk3()