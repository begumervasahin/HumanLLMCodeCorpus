import socket
import pickle
def fonk1(routers, new_cost):
    b1 = "127.0.0.1"
    b2 = b10[routers[0]]['b8']
    b3 = b10[routers[1]]['b8']
    try:
        b4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print("Error creating socket:", e)
        return
    for router, b8 in [(routers[0], b3), (routers[1], b2)]:
        b5 = {'updated': {router: new_cost}}
        print("Sending b5:", b5)
        b4.sendto(pickle.dumps(b5), (b1, b8))
def fonk2(filename):
    with open(filename, 'r') as file:
        b6 = int(file.readline())
        b7 = {}
        for _ in range(b6):
            router_name, cost, b8 = file.readline().split()
            b7[router_name] = {'cost': float(cost), 'b8': int(b8)}
        return b7
b9 = ['topology/configA.txt', 'topology/configB.txt', 'topology/configC.txt',
                'topology/configD.txt', 'topology/configE.txt', 'topology/configF.txt']
b10 = {}
for file_path in b9:
    b10.update(fonk2(file_path))
print("Enter routers to edit their connection")
print("Format: Router1 Router2 NewCost")
print()
while True:
    b11 = input(">")
    b12 = b11.split()
    if len(b12) != 3:
        print("Invalid input format. Please enter Router1 Router2 NewCost.")
        continue
    fonk1(b12[:2], float(b12[2]))