import sys
from argparse import ArgumentParser
from os.path import exists
from lib import Computer, parse_number
__version__ = '1.0'
def main():
    input_file, output_file, debug = parse_args()
    input_data = read_input(input_file)
    curve_type, payload, coefficients, instructions = parse_input(input_data)
    computer = Computer(curve_type, payload, coefficients)
    for instruction in instructions:
        if debug:
            print(f'Instruction: {instruction}')
        computer.calc(instruction)
    if debug:
        print(f'Answer: {computer.cache}')
    print(f'Result has been written in file `{output_file}`')
    write_output(output_file, computer.cache)
def parse_args():
    parser = ArgumentParser(prog='Elliptic Curve',
                            description='Program for elliptic curve points sum calculation',
                            epilog='(c) Semen Makhaev, 2018. All rights reserved',
                            usage='python3 main.py')
    parser.add_argument('-i', '--input', type=str, default='input.txt',
                        help='Input file path, default is `input.txt`')
    parser.add_argument('-o', '--output', type=str, default='output.txt',
                        help='Output file path, default is `output.txt`')
    parser.add_argument('-d', '--debug', action='store_true', help="Enable debug mode")
    args = parser.parse_args()
    return args.input, args.output, args.debug
def read_input(file_path):
    if not exists(file_path):
        print(f'Input file doesn`t exist: {file_path}')
        sys.exit(1)
    with open(file_path, mode='r', encoding='utf-8') as input_file:
        return list(map(str.strip, input_file))
def write_output(file_path, data):
    lines = [f'{key} = {data[key]}' for key in data.keys()]
    with open(file_path, mode='w+', encoding='utf-8') as output_file:
        output_file.write('\r\n'.join(lines))
def parse_input(input_lines):
    try:
        curve_type = input_lines[0]
        payload = parse_numbers(input_lines[1])
        coefficients = parse_numbers(input_lines[2])
        instructions = list(filter(bool, input_lines[3:]))
        return curve_type, payload, coefficients, instructions
    except IndexError:
        print('Input data is incorrect')
        sys.exit(1)
def parse_numbers(line):
    return [parse_number(x) for x in line.split() if x]
if __name__ == '__main__':
    main()