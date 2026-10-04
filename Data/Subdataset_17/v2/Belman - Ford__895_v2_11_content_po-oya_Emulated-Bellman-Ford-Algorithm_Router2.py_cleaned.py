import re
import timeit
from time import sleep
from BellmanFord import BFA
elapsedTime = 0
start = 0
whichPort = {}
adrToName = {}
routerCount = 0
routerName = input("Welcome to Emulated Bellman-Ford Algorithm\n"
                   "Which router am I?\n")
with open("which_port.txt") as whichRouter:
    for line in whichRouter:
        router_id = line[0]
        port = int(line[2:6])
        whichPort[router_id] = port
        adrToName[port] = int(router_id)
        routerCount += 1
start = timeit.default_timer()
with open("adj_mat.txt") as adj_matrix_file:
    myLine = adj_matrix_file.readlines()[int(routerName) - 1].strip()
initialCost = re.split(" ", myLine)
print(f'Initial Cost is {initialCost}\n')
myBf = BFA(routerCount, initialCost, routerName, whichPort, adrToName)
myBf.who_to_send()
while True:
    s = input("To start BellmanFord Algorithm, Enter 's'\n")
    if s == 's':
        break
    else:
        print("Wrong input! Please enter 's' to start.")
myBf.send()
def emulate_bellman_ford():
    global start, elapsedTime
    while True:
        elapsedTime = timeit.default_timer() - start
        if elapsedTime > 0.1:
            myBf.send()
            start = timeit.default_timer()
        myBf.receive()
        sleep(0.1)
        if input().lower() == 'u':
            with open("adj_mat.txt") as adj_matrix_file:
                myLine = adj_matrix_file.readlines()[int(routerName) - 1].strip()
            newCost = re.split(" ", myLine)
            print(f'New cost is {newCost}\n')
            myBf.check_cost(newCost)
if __name__ == "__main__":
    emulate_bellman_ford()