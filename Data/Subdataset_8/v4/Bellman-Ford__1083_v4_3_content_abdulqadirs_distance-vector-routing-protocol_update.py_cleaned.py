import socket
import pickle
def client(routers, new_cost):
    server_ip = "127.0.0.1"
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print("Error creating socket:", e)
        return
    port1 = ports[routers[0]]
    port2 = ports[routers[1]]
    for i, port in enumerate([port2, port1]):
        message = {'updated': {routers[i]: new_cost}}
        print("Sending message:", message)
        client_socket.sendto(pickle.dumps(message), (server_ip, int(port)))
def read_routers_from_file(file_path):
    with open(file_path, 'r') as file:
        num_routers = int(file.readline())
        ports_info = {}
        for _ in range(num_routers):
            router_line = file.readline().split()
            router_name, cost, port = router_line[0], float(router_line[1]), int(router_line[2])
            ports_info[router_name] = {'cost': cost, 'port': port}
        return ports_info
config_files = ['topology/configA.txt', 'topology/configB.txt', 'topology/configC.txt',
                'topology/configD.txt', 'topology/configE.txt', 'topology/configF.txt']
ports = {}
for file_path in config_files:
    ports.update(read_routers_from_file(file_path))
print("Enter routers to edit their connection")
print("Format: Router1 Router2 NewCost")
print()
routers_input = input(">")
routers = routers_input.split()
client(routers[:2], float(routers[2]))
while True:
    routers_input = input(">")
    routers = routers_input.split()
    client(routers[:2], float(routers[2]))