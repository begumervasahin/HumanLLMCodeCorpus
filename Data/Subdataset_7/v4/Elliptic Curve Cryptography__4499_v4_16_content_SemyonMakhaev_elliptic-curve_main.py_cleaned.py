import sys
from argparse import ArgumentParser
from os.path import exists
from lib import Computer, parse_number
b1 = '1.0'
def fonk1():
    input_file, output_file, b2 = fonk2()
    b3 = fonk3(input_file)
    b16, b17, b18, b4 = fonk5(b3)
    b5 = Computer(b16, b17, b18)
    for instruction in b4:
        if b2:
            print('Instruction:', instruction)
        b5.calculate(instruction)
    if b2:
        print('Answer:', b5.cache)
    print('The result has been written in file `{}`'.format(output_file))
    fonk4(output_file, b5.cache)
def fonk2():
    b6 = ArgumentParser(prog='Elliptic curve',
                            b7 = 'Program for elliptic curve points sum calculation',
                            b8 = '(c) Semen Makhaev, 2018. All rights reserved',
                            b9 = 'python3 main.py')
    b6.add_argument('-i', '--input', b10 = str, default='input.txt',
                        b11 = 'Input file path, default is `input.txt`')
    b6.add_argument('-o', '--output', b10 = str, default='output.txt',
                        b11 = 'Output file path, default is `output.txt`')
    b6.add_argument('-d', '--b2', b12 = 'store_true', b11="Debug b14")
    b13 = b6.fonk2()
    return b13.input, b13.output, b13.b2
def fonk3(file_path):
    if not exists(file_path):
        print('Input file doesn\'t exist:', file_path)
        sys.exit(1)
    with open(file_path, b14 = 'r', encoding='utf-8') as input_file:
        return list(map(str.strip, input_file))
def fonk4(file_path, data):
    b15 = ['{} = {}'.format(key, data[key]) for key in data]
    with open(file_path, b14 = 'w+', encoding='utf-8') as output_file:
        output_file.write('\n'.join(b15))
def fonk5(input_lines):
    try:
        b16 = input_lines[0]
        b17 = fonk6(input_lines[1])
        b18 = fonk6(input_lines[2])
        b4 = [line for line in input_lines[3:] if line.strip()]
        return b16, b17, b18, b4
    except IndexError:
        print('Input data is incorrect')
        sys.exit(1)
def fonk6(line):
    return [parse_number(x) for x in line.split() if x]
if b19 = = '__main__':
    fonk1()