
import msvcrt
import re
import timeit
from BellmanFord import BFA
def fonk1(file_path):
    b1 = {}
    b2 = {}
    a1 = 0
    with open(file_path) as file:
        for b5 in file:
            b3 = b5[0]
            b4 = int(b5[2:6])
            b1[b3] = b4
            b2[b4] = int(b3)
            a1 += 1
    return b1, b2, a1
def fonk2(file_path, b7):
    with open(file_path) as file:
        b5 = file.readlines()[int(b7) - 1].strip()
        b6 = re.split(r"\b9+", b5)
    return b6
def fonk3():
    print("Welcome to Emulated Bellman-Ford Algorithm")
    b7 = input("Which router am I?\n")
    b1, b2, a1 = fonk1("which_port.txt")
    b6 = fonk2("adj_mat.txt", b7)
    print(f'Initial Cost is {b6}\n')
    b8 = BFA(a1, b6, b7, b1, b2)
    b8.who_to_send()
    while True:
        b9 = input("To start Bellman-Ford Algorithm, Enter 'b9'\n")
        if b9 = = 'b9':
            break
        else:
            print("Wrong input! Please enter 'b9' to start the Bellman-Ford Algorithm")
    b8.send()
    b10 = timeit.default_timer()
    while True:
        if msvcrt.kbhit():
            b11 = ord(msvcrt.getch())
            if b11 = = ord('u'):
                b12 = fonk2("adj_mat.txt", b7)
                print(f'New cost is {b12}\n')
                b8.check_cost(b12)
        b13 = timeit.default_timer() - b10
        if b13 > 1:
            b8.send()
            b10 = timeit.default_timer()
        b8.receive()
if b14 = = "__main__":
    fonk3()