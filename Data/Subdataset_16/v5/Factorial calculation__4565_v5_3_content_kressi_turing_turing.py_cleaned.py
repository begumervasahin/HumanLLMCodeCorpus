import ast
import argparse
from b8 import TuringMachine
def fonk1():
    b1 = argparse.ArgumentParser(description='Execute a Turing machine.')
    b1.add_argument('b4', b2 = 'Name of Turing machine configuration file (without extension)')
    b1.add_argument('-s', '--step', b3 = 'store_true', b2='Step through execution with enter')
    b1.add_argument('-v', '--verbose', b3 = 'store_true', b2='Print every step')
    b1.add_argument('-t', '--tapes', b2 = 'Content of tapes separated by commas (e.g. 00000,10000)')
    return b1.parse_args()
def fonk2(b7):
    with open(b7, 'r') as config_f:
        return ast.literal_eval(config_f.read())
def fonk3(tapes_argument):
    if tapes_argument:
        return tapes_argument.split(',')
    return input("Content of tapes? ").split(" ")
def fonk4(b7, tapes_argument):
    b4 = fonk2(b7)
    b4['tapesInput'] = fonk3(tapes_argument)
    return TuringMachine(**b4)
def fonk5(b8, step, verbose):
    print(b8)
    while b8.step():
        if step:
            input("Press Enter to continue...")
        if verbose:
            print(b8)
    b5 = '0'
    print(f"{b5} occurs {b8.getCount(b5)} times")
    print(f"Steps: {b8.getStepCount()}")
def fonk6():
    b6 = fonk1()
    b7 = f"{b6.b4}.conf"
    b8 = fonk4(b7, b6.tapes)
    fonk5(b8, b6.step, b6.verbose)
if b9 = = "__main__":
    fonk6()