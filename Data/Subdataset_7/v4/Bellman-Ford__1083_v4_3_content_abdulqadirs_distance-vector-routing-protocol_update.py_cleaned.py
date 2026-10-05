import socket
import pickle
def fonk1(b13, new_cost):
    b1 = "127.0.0.1"
    try:
        b2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print("Error creating socket:", e)
        return
    b3 = b11[b13[0]]
    b4 = b11[b13[1]]
    for i, b9 in enumerate([b4, b3]):
        b5 = {'updated': {b13[i]: new_cost}}
        print("Sending b5:", b5)
        b2.sendto(pickle.dumps(b5), (b1, int(b9)))
def fonk2(file_path):
    with open(file_path, 'r') as file:
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
print("Enter b13 to edit their connection")
print("Format: Router1 Router2 NewCost")
print()
b12 = input(">")
b13 = b12.split()
fonk1(b13[:2], float(b13[2]))
while True:
    b12 = input(">")
    b13 = b12.split()
    fonk1(b13[:2], float(b13[2]))