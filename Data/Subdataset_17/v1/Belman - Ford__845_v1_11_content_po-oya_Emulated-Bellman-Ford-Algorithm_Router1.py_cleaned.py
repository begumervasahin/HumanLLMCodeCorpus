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
        print("Router", self.router_name, "will send data to routers:", self.port_mapping)
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
def main():
    port_mapping = {}
    address_to_name = {}
    router_count = 0
    router_name = input("Welcome to Emulated Bellman-Ford Algorithm\nWhich router am I?\n")
    with open("which_port.txt") as which_router_file:
        for line in which_router_file:
            port_mapping[line[0]] = int(line[2:6])
            address_to_name[int(line[2:6])] = int(line[0])
            router_count += 1
    with open("adj_mat.txt") as adj_mat_file:
        my_line = adj_mat_file.readlines()[int(router_name) - 1].strip()
        initial_cost = re.split(r"\s+", my_line)
    print('Initial Cost is {}\n'.format(initial_cost))
    my_bf = BellmanFordAlgorithm(router_count, initial_cost, router_name, port_mapping, address_to_name)
    my_bf.who_to_send()
    s = input("To start Bellman-Ford Algorithm, Enter 's'\n")
    while s != 's':
        s = input("Wrong input! To start Bellman-Ford Algorithm, Enter 's'\n")
    my_bf.send()
    start = time.time()
    def periodic_send():
        nonlocal start
        while True:
            time.sleep(1)
            elapsed_time = time.time() - start
            if elapsed_time > 1:
                my_bf.send()
                start = time.time()
    send_thread = threading.Thread(target=periodic_send)
    send_thread.daemon = True
    send_thread.start()
    while True:
        my_bf.receive()
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if key == ord('u'):
                with open("adj_mat.txt") as adj_mat_file:
                    my_line = adj_mat_file.readlines()[int(router_name) - 1].strip()
                    new_cost = re.split(r"\s+", my_line)
                    print('New cost is {}\n'.format(new_cost))
                    my_bf.check_cost(new_cost)
if __name__ == "__main__":
    main()