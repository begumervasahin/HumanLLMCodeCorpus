import ast
import argparse
from b7 import TuringMachine
def fonk1():
    b1 = argparse.ArgumentParser(description='Execute a Turing machine.')
    b1.add_argument('b6', b2 = 'Name of Turing machine configuration file (without extension)')
    b1.add_argument('-s', '--step', b3 = 'store_true', b2='Step through execution with enter')
    b1.add_argument('-v', '--verbose', b3 = 'store_true', b2='Print every step')
    b1.add_argument('-t', '--tapes', b2 = 'Content of tapes separated by commas (e.g. 00000,10000)')
    b4 = b1.parse_args()
    b5 = b4.b6 + ".conf"
    with open(b5, 'r') as config_f:
        b6 = ast.literal_eval(config_f.read())
    if b4.tapes:
        b6['tapesInput'] = b4.tapes.split(',')
    else:
        b6['tapesInput'] = input("Content of tapes? ").split(" ")
    b7 = TuringMachine(**b6)
    print(b7)
    while b7.step():
        if b4.step:
            input("Press Enter to continue...")
        if b4.verbose:
            print(b7)
    b8 = '0'
    print(f"{b8} occurs {b7.getCount(b8)} times")
    print(f"Steps: {b7.getStepCount()}")
if b9 = = "__main__":
    fonk1()