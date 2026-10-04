import re
import time
import threading
class BellmanFordAlgorithm:
    def __init__(self, router_count, initial_cost, router_name, port_mapping, address_to_name):
        self.router_count = router_count
        self.cost = list(map(int, initial_cost))
        self.router_name = router_name
        self.port_mapping = port_mapping
        self.address_to_name = address_to_name
        self.distances = [float('inf')] * router_count
        self.distances[int(router_name) - 1] = 0
        self.previous_nodes = [None] * router_count
    def who_to_send(self):
        print(f"Router {self.router_name} will send data to routers: {self.port_mapping}")
    def send(self):
        print("Sending data...")
    def receive(self):
        print("Receiving data...")
    def check_cost(self, new_cost):
        new_cost = list(map(int, new_cost))
        for i in range(self.router_count):
            if new_cost[i] < self.cost[i]:
                self.cost[i] = new_cost[i]
                self.distances[i] = self.cost[i]
                self.previous_nodes[i] = int(self.router_name)
        print("Updated costs:", self.cost)
def load_port_mapping(file_path):
    port_mapping = {}
    address_to_name = {}
    router_count = 0
    with open(file_path) as file:
        for line in file:
            router_id = line[0]
            port = int(line[2:6])
            port_mapping[router_id] = port
            address_to_name[port] = int(router_id)
            router_count += 1
    return port_mapping, address_to_name, router_count
def load_initial_cost(file_path, router_name):
    with open(file_path) as file:
        line = file.readlines()[int(router_name) - 1].strip()
        initial_cost = re.split(r"\s+", line)
    return initial_cost
def main():
    router_name = input("Welcome to Emulated Bellman-Ford Algorithm\nWhich router am I?\n")
    port_mapping, address_to_name, router_count = load_port_mapping("which_port.txt")
    initial_cost = load_initial_cost("adj_mat.txt", router_name)
    print(f'Initial Cost is {initial_cost}\n')
    my_bf = BellmanFordAlgorithm(router_count, initial_cost, router_name, port_mapping, address_to_name)
    my_bf.who_to_send()
    s = input("To start Bellman-Ford Algorithm, Enter 's'\n")
    while s != 's':
        s = input("Wrong input! To start Bellman-Ford Algorithm, Enter 's'\n")
    my_bf.send()
    start_time = time.time()
    def periodic_send():
        nonlocal start_time
        while True:
            time.sleep(1)
            elapsed_time = time.time() - start_time
            if elapsed_time > 1:
                my_bf.send()
                start_time = time.time()
    send_thread = threading.Thread(target=periodic_send, daemon=True)
    send_thread.start()
    while True:
        my_bf.receive()
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if key == ord('u'):
                new_cost = load_initial_cost("adj_mat.txt", router_name)
                print(f'New cost is {new_cost}\n')
                my_bf.check_cost(new_cost)
if __name__ == "__main__":
    main()