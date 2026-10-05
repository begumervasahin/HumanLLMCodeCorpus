from b9 import TuringMachine
import ast
import argparse
b1 = argparse.ArgumentParser(description='Execute a Turing machine.')
b1.add_argument('b8', b2 = 'Name of the Turing configuration')
b1.add_argument('-s', '--b5', b3 = 'store_true', b2='Step through with Enter')
b1.add_argument('-v', '--b6', b3 = 'store_true', b2='Print every b5')
b1.add_argument('-t', '--tapes', b2 = 'Content of tapes separated by comma (e.g. 00000,10000)')
b4 = b1.parse_args()
b5 = b4.b5
b6 = b4.b6
b7 = b4.b8 + ".conf"
with open(b7, 'r') as config_file:
    b8 = ast.literal_eval(config_file.read())
if b4.tapes:
    b8['tapesInput'] = b4.tapes.split(',')
else:
    b8['tapesInput'] = str(input("Content of tapes? ")).split(" ")
b9 = TuringMachine(**b8)
print(b9)
while b9.b5():
    if b5:
        input("Press Enter to continue...")
    if b6:
        print(b9)
b10 = '0'
print("{0} occurs {1} times".format(b10, b9.getCount(b10)))
print("Steps: {0}".format(b9.getStepCount()))