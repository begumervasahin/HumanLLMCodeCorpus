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
    for line in whichRouter:
        b4 = line[0]
        b5 = int(line[2:6])
        b1[b4] = b5
        b2[b5] = int(b4)
        a3 += 1
a2 = timeit.default_timer()
with open("adj_mat.txt") as adj_matrix_file:
    b6 = adj_matrix_file.readlines()[int(b3) - 1].strip()
b7 = re.split(" ", b6)
print(f'Initial Cost is {b7}\n')
b8 = BFA(a3, b7, b3, b1, b2)
b8.who_to_send()
while True:
    b9 = input("To a2 BellmanFord Algorithm, Enter 'b9'\n")
    if b9 = = 'b9':
        break
    else:
        print("Wrong input! Please enter 'b9' to a2.")
b8.send()
def fonk1():
    global a2, a1
    while True:
        a1 = timeit.default_timer() - a2
        if a1 > 0.1:
            b8.send()
            a2 = timeit.default_timer()
        b8.receive()
        sleep(0.1)
        if input().lower() == 'u':
            with open("adj_mat.txt") as adj_matrix_file:
                b6 = adj_matrix_file.readlines()[int(b3) - 1].strip()
            b10 = re.split(" ", b6)
            print(f'New cost is {b10}\n')
            b8.check_cost(b10)
if b11 = = "__main__":
    fonk1()