import argparse
import socket
import pickle
import time
import threading
parser = argparse.ArgumentParser(description='Simulate routing between routers')
parser.add_argument('router_id', metavar='<router_id>', help='Identifier of the router')
parser.add_argument('port_number', metavar='<port_number>', type=int, help='Port number for communication')
parser.add_argument('config_file', metavar='<config_file>', help='Configuration file containing router information')
args = parser.parse_args()
def bellman_ford(router_id, graph, distance, predecessor):
    while True:
        for node in graph:
            distance[node], predecessor[node] = float('inf'), None
        distance[router_id] = 0
        time.sleep(3)
        if time.clock() - start_time < 20:
            for key in graph:
                graph[key] = distance_vector_graph[key]
                for neighbor in distance_vector_graph[key]:
                    graph[key][neighbor] = distance_vector_graph[key][neighbor]
                    graph[neighbor][key] = distance_vector_graph[key][neighbor]
        for _ in range(len(graph) - 1):
            for u in graph:
                for v in graph[u]:
                    if distance[v] >= distance[u] + graph[u][v]:
                        distance[v], predecessor[v] = distance[u] + graph[u][v], u
        for key, value in distance.items():
            print("Distance to {}: {}".format(key, value))
        print('\n')
def client(router_id, port_numbers, distance_vector_graph):
    server_name = "127.0.0.1"
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except:
            print("Socket cannot be bound")
        i = 0
        while i < len(port_numbers):
            time.sleep(4)
            message = {router_id: graph[router_id]}
            client_socket.sendto(pickle.dumps(message), (server_name, int(port_numbers[i])))
            i += 1
def server(router_id, port_number):
    server_ip = "127.0.0.1"
    server_port = port_number
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))
    print("Server setup")
    timer_dict = {neighbor: time.clock() for neighbor in neighbor_list}
    while True:
        server_socket.settimeout(20)
        try:
            message, client_address = server_socket.recvfrom(2048)
            message = pickle.loads(message)
        except:
            print("Message not received from all neighbors")
            for neighbor in neighbor_list:
                graph[router_id][neighbor] = float('inf')
            continue
        if 'updated' in message:
            main_key = 'updated'
            new_data = message[main_key]
            key_1 = list(new_data.keys())[0]
            distance_vector_graph[router_id][key_1] = new_data[key_1]
        else:
            key = list(message.keys())[0]
            received_data = message[key]
            for neighbor, value in received_data.items():
                graph[neighbor][key] = value
                graph[key][neighbor] = value
            timer_dict[key] = time.clock()
        for neighbor in neighbor_list:
            if time.clock() - timer_dict[neighbor] > 15:
                change = neighbor
                graph[router_id][change] = float('inf')
                graph[change][router_id] = float('inf')
if __name__ == '__main__':
    script, router_id, port_number, config_file = args.router_id, args.port_number, args.config_file
    print("I am Router " + router_id)
    print("My port number is " + str(port_number))
    with open(config_file) as f:
        num_routers = int(f.readline().strip())
        print("Number of routers connected: " + str(num_routers))
        distance_vector_graph = {router_id: {}}
        router_port_list = []
        neighbor_list = []
        for _ in range(num_routers):
            router_info_str = f.readline().strip()
            router_info_list = router_info_str.split()
            neighbor_list.append(router_info_list[0])
            router_port_list.append(router_info_list[2])
            distance_vector_graph[router_id][router_info_list[0]] = float(router_info_list[1])
        print(neighbor_list)
    threading.Thread(target=server, args=(router_id, port_number)).start()
    time.sleep(4)
    threading.Thread(target=client, args=(router_id, router_port_list, distance_vector_graph)).start()
    threading.Thread(target=bellman_ford, args=(router_id, graph, distance, predecessor)).start()
    while True:
        pass