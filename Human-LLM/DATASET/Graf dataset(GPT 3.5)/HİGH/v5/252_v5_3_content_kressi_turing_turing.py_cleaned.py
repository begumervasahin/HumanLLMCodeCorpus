from b9 import TuringMachine
import ast
import argparse
def fonk1(config_name, b1 = False, verbose=False, tapes=None):
    b2 = argparse.ArgumentParser(description='Execute a Turing machine.')
    b2.add_argument('b7', b3 = 'Name of the Turing configuration')
    b2.add_argument('-s', '--b1', b4 = 'store_true', b3='Step through with Enter')
    b2.add_argument('-v', '--verbose', b4 = 'store_true', b3='Print every b1')
    b2.add_argument('-t', '--tapes', b3 = 'Content of tapes separated by comma (e.g. 00000,10000)')
    b5 = b2.parse_args()
    b6 = b5.b7 + ".conf"
    with open(b6, 'r') as config_file:
        b7 = ast.literal_eval(config_file.read())
    b8 = b5.tapes.split(',') if b5.tapes else str(input("Content of tapes? ")).split()
    b9 = TuringMachine(tapesInput=b8, **b7)
    print(b9)
    while b9.b1():
        if b1:
            input("Press Enter to continue...")
        if verbose:
            print(b9)
    b10 = '0'
    print("{0} occurs {1} times".format(b10, b9.getCount(b10)))
    print("Steps: {0}".format(b9.getStepCount()))
if b11 = = "__main__":
    fonk1()