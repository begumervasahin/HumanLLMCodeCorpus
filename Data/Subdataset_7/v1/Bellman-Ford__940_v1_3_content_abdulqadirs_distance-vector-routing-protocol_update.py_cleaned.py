import socket
import pickle
def fonk1(b13, new_cost):
    b1 = "127.0.0.1"
    b2 = b11[b13[0]]
    b3 = b11[b13[1]]
    try:
        b4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print("Socket cannot be bound:", e)
    a1 = 0
    while a1 < 2:
        if a1 = = 0:
            b5 = {'updated': {b13[a1]: new_cost}}
            print(b5)
            b4.sendto(pickle.dumps(b5), (b1, int(b3)))
        else:
            b5 = {'updated': {b13[a1]: new_cost}}
            b4.sendto(pickle.dumps(b5), (b1, int(b2)))
            print(b5)
        a1 += 1
def fonk2(filename):
    with open(filename, 'r') as file:
        b6 = int(file.readline())
        b7 = {}
        for _ in range(b6):
            b8 = file.readline()
            b9 = b8.split()
            b9[1] = float(b9[1])
            b7[b9[0]] = int(b9[2])
        return b7
b10 = ['topology/configA.txt', 'topology/configB.txt', 'topology/configC.txt',
         'topology/configD.txt', 'topology/configE.txt', 'topology/configF.txt']
b11 = {}
for file_path in b10:
    b11.update(fonk2(file_path))
print("Enter b13 to edit their connection")
print("Router1 Router2 NewCost")
print()
while True:
    b12 = input(">")
    b13 = b12.split()
    if len(b13) != 3:
        print("Invalid input format. Please enter Router1 Router2 NewCost.")
        continue
    fonk1(b13[:2], float(b13[2]))