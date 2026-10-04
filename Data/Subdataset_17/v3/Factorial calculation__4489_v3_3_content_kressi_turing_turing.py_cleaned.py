import ast
import argparse
from turing_machine import TuringMachine
def read_config(config_file):
    with open(config_file, 'r') as config_f:
        return ast.literal_eval(config_f.read())
def get_tapes_input(tapes_argument):
    if tapes_argument:
        return tapes_argument.split(',')
    return input("Content of tapes? ").split(" ")
def main():
    parser = argparse.ArgumentParser(description='Execute a Turing machine.')
    parser.add_argument('config', help='Name of Turing machine configuration file (without extension)')
    parser.add_argument('-s', '--step', action='store_true', help='Step through execution with enter')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print every step')
    parser.add_argument('-t', '--tapes', help='Content of tapes separated by commas (e.g. 00000,10000)')
    args = parser.parse_args()
    config_file = f"{args.config}.conf"
    config = read_config(config_file)
    config['tapesInput'] = get_tapes_input(args.tapes)
    turing_machine = TuringMachine(**config)
    print(turing_machine)
    while turing_machine.step():
        if args.step:
            input("Press Enter to continue...")
        if args.verbose:
            print(turing_machine)
    char = '0'
    print(f"{char} occurs {turing_machine.getCount(char)} times")
    print(f"Steps: {turing_machine.getStepCount()}")
if __name__ == "__main__":
    main()