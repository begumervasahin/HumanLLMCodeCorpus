from turing_machine import TuringMachine
import ast
import argparse
parser = argparse.ArgumentParser(description='Execute a Turing machine.')
parser.add_argument('config', help='Name of the Turing configuration')
parser.add_argument('-s', '--step', action='store_true', help='Step through with Enter')
parser.add_argument('-v', '--verbose', action='store_true', help='Print every step')
parser.add_argument('-t', '--tapes', help='Content of tapes separated by comma (e.g. 00000,10000)')
args = parser.parse_args()
step = args.step
verbose = args.verbose
config_file_name = args.config + ".conf"
with open(config_file_name, 'r') as config_file:
    config = ast.literal_eval(config_file.read())
if args.tapes:
    config['tapesInput'] = args.tapes.split(',')
else:
    config['tapesInput'] = str(input("Content of tapes? ")).split(" ")
turing_machine = TuringMachine(**config)
print(turing_machine)
while turing_machine.step():
    if step:
        input("Press Enter to continue...")
    if verbose:
        print(turing_machine)
char = '0'
print("{0} occurs {1} times".format(char, turing_machine.getCount(char)))
print("Steps: {0}".format(turing_machine.getStepCount()))