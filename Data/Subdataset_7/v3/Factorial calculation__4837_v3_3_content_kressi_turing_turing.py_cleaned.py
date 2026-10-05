from b5 import TuringMachine
import ast
import argparse
def fonk1(config_name, b1 = False, verbose=False, tapes=None):
    b2 = fonk2()
    b3 = fonk3(b2.b3)
    b4 = b2.tapes.split(',') if b2.tapes else fonk4()
    b5 = fonk5(b3, b4)
    fonk6(b5, b2.b1, b2.verbose)
    fonk7(b5)
def fonk2():
    b6 = argparse.ArgumentParser(description='Execute a Turing machine.')
    b6.add_argument('b3', b7 = 'name of Turing configuration')
    b6.add_argument('-s', '--b1', b8 = 'store_true', b7='b1 through with Enter')
    b6.add_argument('-v', '--verbose', b8 = 'store_true', b7='print every b1')
    b6.add_argument('-t', '--tapes', b7 = 'content of tapes separated by comma (e.g. 00000,10000)')
    return b6.parse_args()
def fonk3(config_name):
    b9 = config_name + ".conf"
    with open(b9, 'r') as config_file:
        return ast.literal_eval(config_file.read())
def fonk4():
    return str(input("Content of tapes? ")).split()
def fonk5(b3, b4):
    return TuringMachine(b10 = b4, **b3)
def fonk6(b5, b1, verbose):
    while b5.b1():
        if b1:
            input("Press Enter to continue...")
        if verbose:
            print(b5)
def fonk7(b5):
    b11 = '0'
    print("{0} occurs {1} times".format(b11, b5.getCount(b11)))
    print("Steps: {0}".format(b5.getStepCount()))
if b12 = = "__main__":
    fonk1()