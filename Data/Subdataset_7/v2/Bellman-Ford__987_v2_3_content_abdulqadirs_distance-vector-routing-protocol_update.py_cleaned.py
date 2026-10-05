import socket
import pickle
def fonk1(routers, new_cost):
    b1 = "127.0.0.1"
    b2 = b11[routers[0]]
    b3 = b11[routers[1]]
    try:
        b4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print("Error creating socket:", e)
        return
    for router, b9 in [(routers[0], b3), (routers[1], b2)]:
        b5 = {'updated': {router: new_cost}}
        print("Sending b5:", b5)
        b4.sendto(pickle.dumps(b5), (b1, int(b9)))
def fonk2(filename):
    with open(filename, 'r') as file:
        b6 = int(file.readline())
        b7 = {}
        for _ in range(b6):
            b8 = file.readline().split()
            router_name, cost, b9 = b8[0], float(b8[1]), int(b8[2])
            b7[router_name] = {'cost': cost, 'b9': b9}
        return b7
b10 = ['topology/configA.txt', 'topology/configB.txt', 'topology/configC.txt',
                'topology/configD.txt', 'topology/configE.txt', 'topology/configF.txt']
b11 = {}
for file_path in b10:
    b11.update(fonk2(file_path))
print("Enter routers to edit their connection")
print("Format: Router1 Router2 NewCost")
print()
while True:
    b12 = input(">")
    b13 = b12.split()
    if len(b13) != 3:
        print("Invalid input format. Please enter Router1 Router2 NewCost.")
        continue
    fonk1(b13[:2], float(b13[2]))