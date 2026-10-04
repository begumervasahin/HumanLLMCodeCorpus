import re
import timeit
from time import sleep
from BellmanFord import BFA
a1 = 0
a2 = 0
b1 = {}
b2 = {}
a3 = 0
b3 = input("Welcome to Emulated Bellman-Ford Algorithm\n"
                   "Which router am I?\n")
with open("which_port.txt") as whichRouter:
    for lines in whichRouter:
        b1[lines[0]] = int(lines[2:6])
        b2[int(lines[2:6])] = int(lines[0])
        a3 += 1
a2 = timeit.default_timer()
b4 = open("adj_mat.txt").readlines()[int(b3) - 1]
b4 = b4.rstrip('\n')
b5 = re.split(" ", b4)
print('Initial Cost is {}\n'.format(b5))
b6 = BFA(a3, b5, b3, b1, b2)
b6.who_to_send()
while True:
    b7 = input("To a2 BellmanFord Algorithm, Enter 'b7'\n")
    if b7 = = 'b7':
        break
    else:
        print("Wrong input! Please enter 'b7' to a2.")
b6.send()
def fonk1():
    global a2, a1
    while True:
        a1 = timeit.default_timer() - a2
        if a1 > 0.1:
            b6.send()
            a2 = timeit.default_timer()
        b6.receive()
        sleep(0.1)
        if input().lower() == 'u':
            b4 = open("adj_mat.txt").readlines()[int(b3) - 1]
            b4 = b4.rstrip('\n')
            b8 = re.split(" ", b4)
            print('New cost is {}\n'.format(b8))
            b6.check_cost(b8)
if b9 = = "__main__":
    fonk1()