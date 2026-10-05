from turing_machine import TuringMachine
import ast
import argparse
def execute_turing_machine(config_name, step=False, verbose=False, tapes=None):
    parser = argparse.ArgumentParser(description='Execute a Turing machine.')
    parser.add_argument('config', help='name of Turing configuration')
    parser.add_argument('-s', '--step', action='store_true', help='step through with Enter')
    parser.add_argument('-v', '--verbose', action='store_true', help='print every step')
    parser.add_argument('-t', '--tapes', help='content of tapes separated by comma (e.g. 00000,10000)')
    args = parser.parse_args()
    config_file_name = args.config + ".conf"
    with open(config_file_name, 'r') as config_file:
        config = ast.literal_eval(config_file.read())
    tapes_input = args.tapes.split(',') if args.tapes else str(input("Content of tapes? ")).split()
    turing_machine = TuringMachine(tapesInput=tapes_input, **config)
    print(turing_machine)
    while turing_machine.step():
        if step:
            input("Press Enter to continue...")
        if verbose:
            print(turing_machine)
    char = '0'
    print("{0} occurs {1} times".format(char, turing_machine.getCount(char)))
    print("Steps: {0}".format(turing_machine.getStepCount()))
if __name__ == "__main__":
    execute_turing_machine()