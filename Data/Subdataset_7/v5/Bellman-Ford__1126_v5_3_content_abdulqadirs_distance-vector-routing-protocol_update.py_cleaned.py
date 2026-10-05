import socket
import pickle
def fonk1(b11, new_cost):
    b1 = "127.0.0.1"
    try:
        b2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print("Error creating socket:", e)
        return
    b3 = b7[b11[0]]
    b4 = b7[b11[1]]
    for i, b8 in enumerate([b4, b3]):
        b5 = {'updated': {b11[i]: new_cost}}
        print("Sending b5:", b5)
        b2.sendto(pickle.dumps(b5), (b1, b8))
def fonk2(file_path):
    with open(file_path, 'r') as file:
        b6 = int(file.readline())
        b7 = {}
        for _ in range(b6):
            name, cost, b8 = file.readline().split()
            b7[name] = {'cost': float(cost), 'b8': int(b8)}
        return b7
b9 = [
    'topology/configA.txt', 'topology/configB.txt', 'topology/configC.txt',
    'topology/configD.txt', 'topology/configE.txt', 'topology/configF.txt'
]
b7 = {}
for file_path in b9:
    b7.update(fonk2(file_path))
print("Enter b11 to edit their connection")
print("Format: Router1 Router2 NewCost")
print()
b10 = input(">")
b11 = b10.split()
fonk1(b11[:2], float(b11[2]))
while True:
    b10 = input(">")
    b11 = b10.split()
    fonk1(b11[:2], float(b11[2]))