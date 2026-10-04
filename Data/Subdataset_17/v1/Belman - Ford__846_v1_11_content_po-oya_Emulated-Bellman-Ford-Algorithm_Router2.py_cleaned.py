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
    for lines in whichRouter:
        whichPort[lines[0]] = int(lines[2:6])
        adrToName[int(lines[2:6])] = int(lines[0])
        routerCount += 1
start = timeit.default_timer()
myLine = open("adj_mat.txt").readlines()[int(routerName) - 1]
myLine = myLine.rstrip('\n')
initialCost = re.split(" ", myLine)
print('Initial Cost is {}\n'.format(initialCost))
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
            myLine = open("adj_mat.txt").readlines()[int(routerName) - 1]
            myLine = myLine.rstrip('\n')
            newCost = re.split(" ", myLine)
            print('New cost is {}\n'.format(newCost))
            myBf.check_cost(newCost)
if __name__ == "__main__":
    emulate_bellman_ford()