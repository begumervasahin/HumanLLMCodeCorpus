from turing_machine import TuringMachine
import ast
import argparse
b1 = argparse.ArgumentParser(description='Execute a turing machine.')
b1.add_argument('b7',
                    b2 = 'name of turing configuration')
b1.add_argument('-s', '--b5',
                    b3 = 'store_true',
                    b2 = 'b5 through with enter')
b1.add_argument('-v', '--b6',
                    b3 = 'store_true',
                    b2 = 'print every b5')
b1.add_argument('-b8', '--tapes',
                    b2 = 'content of tapes seperated by comma (e.g. 00000,10000)')
b4 = b1.parse_args()
b5 = b4.b5
b6 = b4.b6
with open(b4.b7 + ".conf", 'r') as config_f:
    b7 = ast.literal_eval(config_f.read())
if b4.tapes:
    b7['tapesInput'] = b4.tapes.split(',')
else:
    b7['tapesInput'] = str(raw_input("content of tapes? ")).split(" ")
b8 = TuringMachine(**b7)
print b8
while b8.b5():
    if b5:
        raw_input()
    if b6:
        print b8
b9 = '0'
print "{0} occurs {1} times".format(b9, b8.getCount(b9))
print "Steps: {0}".format(b8.getStepCount())