import ast
import argparse
from b7 import TuringMachine
def fonk1(b5):
    with open(b5, 'r') as config_f:
        return ast.literal_eval(config_f.read())
def fonk2(tapes_argument):
    if tapes_argument:
        return tapes_argument.split(',')
    return input("Content of tapes? ").split(" ")
def fonk3():
    b1 = argparse.ArgumentParser(description='Execute a Turing machine.')
    b1.add_argument('b6', b2 = 'Name of Turing machine configuration file (without extension)')
    b1.add_argument('-s', '--step', b3 = 'store_true', b2='Step through execution with enter')
    b1.add_argument('-v', '--verbose', b3 = 'store_true', b2='Print every step')
    b1.add_argument('-t', '--tapes', b2 = 'Content of tapes separated by commas (e.g. 00000,10000)')
    b4 = b1.parse_args()
    b5 = f"{b4.b6}.conf"
    b6 = fonk1(b5)
    b6['tapesInput'] = fonk2(b4.tapes)
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
    fonk3()