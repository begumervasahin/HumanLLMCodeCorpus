import ast
import argparse
from turing_machine import TuringMachine
def parse_arguments():
    parser = argparse.ArgumentParser(description='Execute a Turing machine.')
    parser.add_argument('config', help='Name of Turing machine configuration file (without extension)')
    parser.add_argument('-s', '--step', action='store_true', help='Step through execution with enter')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print every step')
    parser.add_argument('-t', '--tapes', help='Content of tapes separated by commas (e.g. 00000,10000)')
    return parser.parse_args()
def read_config(config_file):
    with open(config_file, 'r') as config_f:
        return ast.literal_eval(config_f.read())
def get_tapes_input(tapes_argument):
    if tapes_argument:
        return tapes_argument.split(',')
    return input("Content of tapes? ").split(" ")
def initialize_turing_machine(config_file, tapes_argument):
    config = read_config(config_file)
    config['tapesInput'] = get_tapes_input(tapes_argument)
    return TuringMachine(**config)
def execute_turing_machine(turing_machine, step, verbose):
    print(turing_machine)
    while turing_machine.step():
        if step:
            input("Press Enter to continue...")
        if verbose:
            print(turing_machine)
    char = '0'
    print(f"{char} occurs {turing_machine.getCount(char)} times")
    print(f"Steps: {turing_machine.getStepCount()}")
def main():
    args = parse_arguments()
    config_file = f"{args.config}.conf"
    turing_machine = initialize_turing_machine(config_file, args.tapes)
    execute_turing_machine(turing_machine, args.step, args.verbose)
if __name__ == "__main__":
    main()