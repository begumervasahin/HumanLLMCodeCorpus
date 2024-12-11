from b7 import TuringMachine
import ast
import argparse
def fonk1(config_name, b1 = False, verbose=False, tapes=None):
    b2 = argparse.ArgumentParser(description='Execute a Turing machine.')
    b2.add_argument('b6', b3 = 'name of Turing configuration')
    b2.add_argument('-s', '--b1', b4 = 'store_true', b3='b1 through with Enter')
    b2.add_argument('-v', '--verbose', b4 = 'store_true', b3='print every b1')
    b2.add_argument('-t', '--tapes', b3 = 'content of tapes separated by comma (e.g. 00000,10000)')
    b5 = b2.parse_args()
    with open(b5.b6 + ".conf", 'r') as config_f:
        b6 = ast.literal_eval(config_f.read())
    if b5.tapes:
        b6['tapesInput'] = b5.tapes.split(',')
    else:
        b6['tapesInput'] = str(raw_input("Content of tapes? ")).split(" ")
    b7 = TuringMachine(**b6)
    print(b7)
    while b7.b1():
        if b1:
            raw_input("Press Enter to continue...")
        if verbose:
            print(b7)
    b8 = '0'
    print("{0} occurs {1} times".format(b8, b7.getCount(b8)))
    print("Steps: {0}".format(b7.getStepCount()))
if b9 = = "__main__":
    fonk1()