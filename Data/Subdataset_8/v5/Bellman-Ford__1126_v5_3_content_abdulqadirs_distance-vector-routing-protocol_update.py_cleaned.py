import socket
import pickle
def send_updated_cost(routers, new_cost):
    server_ip = "127.0.0.1"
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print("Error creating socket:", e)
        return
    port1 = router_ports[routers[0]]
    port2 = router_ports[routers[1]]
    for i, port in enumerate([port2, port1]):
        message = {'updated': {routers[i]: new_cost}}
        print("Sending message:", message)
        client_socket.sendto(pickle.dumps(message), (server_ip, port))
def read_router_ports(file_path):
    with open(file_path, 'r') as file:
        num_routers = int(file.readline())
        router_ports = {}
        for _ in range(num_routers):
            name, cost, port = file.readline().split()
            router_ports[name] = {'cost': float(cost), 'port': int(port)}
        return router_ports
config_files = [
    'topology/configA.txt', 'topology/configB.txt', 'topology/configC.txt',
    'topology/configD.txt', 'topology/configE.txt', 'topology/configF.txt'
]
router_ports = {}
for file_path in config_files:
    router_ports.update(read_router_ports(file_path))
print("Enter routers to edit their connection")
print("Format: Router1 Router2 NewCost")
print()
routers_input = input(">")
routers = routers_input.split()
send_updated_cost(routers[:2], float(routers[2]))
while True:
    routers_input = input(">")
    routers = routers_input.split()
    send_updated_cost(routers[:2], float(routers[2]))