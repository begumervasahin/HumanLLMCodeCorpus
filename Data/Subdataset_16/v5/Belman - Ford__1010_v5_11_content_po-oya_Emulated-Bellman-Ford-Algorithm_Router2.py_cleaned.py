
import re
import timeit
from time import sleep
from BellmanFord import BFA
import msvcrt
def fonk1():
    b1 = {}
    b2 = {}
    a1 = 0
    b3 = input("Welcome to Emulated Bellman-Ford Algorithm\nWhich router am I?\n")
    with open("which_port.txt") as whichRouter:
        for line in whichRouter:
            b4 = line[0]
            b5 = int(line[2:6])
            b1[b4] = b5
            b2[b5] = int(b4)
            a1 += 1
    return b3, b1, b2, a1
def fonk2(b3):
    with open("adj_mat.txt") as adj_matrix_file:
        b6 = adj_matrix_file.readlines()[int(b3) - 1].strip()
    b7 = re.split(" ", b6)
    print(f'Initial Cost is {b7}\n')
    return b7
def fonk3(a1, b7, b3, b1, b2):
    b8 = BFA(a1, b7, b3, b1, b2)
    b8.who_to_send()
    while True:
        b9 = input("To b12 BellmanFord Algorithm, Enter 'b9'\n")
        if b9 = = 'b9':
            break
        else:
            print("Wrong input! Please enter 'b9' to b12.")
    b8.send()
    return b8
def fonk4(b3, b8):
    if msvcrt.kbhit():
        b10 = ord(msvcrt.getch())
        if b10 = = ord('u'):
            with open("adj_mat.txt") as adj_matrix_file:
                b6 = adj_matrix_file.readlines()[int(b3) - 1].strip()
            b11 = re.split(" ", b6)
            print(f'New cost is {b11}\n')
            b8.check_cost(b11)
def fonk5(b8):
    b12 = timeit.default_timer()
    while True:
        b13 = timeit.default_timer() - b12
        if b13 > 0.1:
            b8.send()
            b12 = timeit.default_timer()
        b8.receive()
        sleep(0.1)
        fonk4(b3, b8)
if b14 = = "__main__":
    b3, b1, b2, a1 = fonk1()
    b7 = fonk2(b3)
    b8 = fonk3(a1, b7, b3, b1, b2)
    fonk5(b8)