
from BellmanFord import BFA
import msvcrt
import re
import timeit
from time import sleep
a1 = 0
a2 = 0
b1 = {}
b2 = {}
a3 = 0
b3 = None
b4 = input("Welcome to Emulated Bellman-Ford Algorithm\n"
                   "Which router am I?\n")
with open("which_port.txt") as whichRouter:
    for lines in whichRouter:
        b1[lines[0]] = int(lines[2:6])
        b2[int(lines[2:6])] = int(lines[0])
        a3 += 1
a2 = timeit.default_timer()
b5 = open("adj_mat.txt").readlines()[int(b4) - 1]
b5 = b5.rstrip('\n')
b6 = re.split(" ", b5)
print('Initial Cost is {}\n'.format(b6))
b7 = BFA(a3, b6, b4, b1, b2)
b7.who_to_send()
try:
    b8 = input("To a2 BellmanFord Algorithm, Enter 'b8'\n")
    assert b8 = = 'b8'
except AssertionError:
    b8 = input("Wrong input! To a2 BellmanFord Algorithm, Enter 'b8'\n")
b7.send()
while True:
    b3 = msvcrt.kbhit()
    a1 = timeit.default_timer() - a2
    if a1 > 0.1:
        b7.send()
        a2 = a1
    b7.receive()
    if b3:
        b9 = ord(msvcrt.getch())
        if b9 = = ord('u'):
            b5 = open("adj_mat.txt").readlines()[int(b4) - 1]
            b5 = b5.rstrip('\n')
            b10 = re.split(" ", b5)
            print('New cost is {}\n'.format(b10))
            b7.check_cost(b10)