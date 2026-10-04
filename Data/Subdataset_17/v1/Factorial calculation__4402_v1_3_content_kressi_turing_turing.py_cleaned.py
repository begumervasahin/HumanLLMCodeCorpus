import ast
import argparse
from turing_machine import TuringMachine
def main():
    parser = argparse.ArgumentParser(description='Execute a Turing machine.')
    parser.add_argument('config', help='Name of Turing machine configuration file (without extension)')
    parser.add_argument('-s', '--step', action='store_true', help='Step through execution with enter')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print every step')
    parser.add_argument('-t', '--tapes', help='Content of tapes separated by commas (e.g. 00000,10000)')
    args = parser.parse_args()
    config_file = args.config + ".conf"
    with open(config_file, 'r') as config_f:
        config = ast.literal_eval(config_f.read())
    if args.tapes:
        config['tapesInput'] = args.tapes.split(',')
    else:
        config['tapesInput'] = input("Content of tapes? ").split(" ")
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