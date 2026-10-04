
import re
import timeit
from time import sleep
from BellmanFord import BFA
import msvcrt
def initialize_router():
    whichPort = {}
    adrToName = {}
    routerCount = 0
    routerName = input("Welcome to Emulated Bellman-Ford Algorithm\nWhich router am I?\n")
    with open("which_port.txt") as whichRouter:
        for line in whichRouter:
            router_id = line[0]
            port = int(line[2:6])
            whichPort[router_id] = port
            adrToName[port] = int(router_id)
            routerCount += 1
    return routerName, whichPort, adrToName, routerCount
def read_initial_cost(routerName):
    with open("adj_mat.txt") as adj_matrix_file:
        myLine = adj_matrix_file.readlines()[int(routerName) - 1].strip()
    initialCost = re.split(" ", myLine)
    print(f'Initial Cost is {initialCost}\n')
    return initialCost
def start_bellman_ford(routerCount, initialCost, routerName, whichPort, adrToName):
    myBf = BFA(routerCount, initialCost, routerName, whichPort, adrToName)
    myBf.who_to_send()
    while True:
        s = input("To start BellmanFord Algorithm, Enter 's'\n")
        if s == 's':
            break
        else:
            print("Wrong input! Please enter 's' to start.")
    myBf.send()
    return myBf
def emulate_bellman_ford(myBf):
    start = timeit.default_timer()
    while True:
        elapsedTime = timeit.default_timer() - start
        if elapsedTime > 0.1:
            myBf.send()
            start = timeit.default_timer()
        myBf.receive()
        sleep(0.1)
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if key == ord('u'):
                with open("adj_mat.txt") as adj_matrix_file:
                    myLine = adj_matrix_file.readlines()[int(routerName) - 1].strip()
                newCost = re.split(" ", myLine)
                print(f'New cost is {newCost}\n')
                myBf.check_cost(newCost)
if __name__ == "__main__":
    routerName, whichPort, adrToName, routerCount = initialize_router()
    initialCost = read_initial_cost(routerName)
    myBf = start_bellman_ford(routerCount, initialCost, routerName, whichPort, adrToName)
    emulate_bellman_ford(myBf)