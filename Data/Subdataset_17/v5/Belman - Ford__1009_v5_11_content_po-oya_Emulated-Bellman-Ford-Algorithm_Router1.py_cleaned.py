
import msvcrt
import re
import timeit
from BellmanFord import BFA
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
    print("Welcome to Emulated Bellman-Ford Algorithm")
    router_name = input("Which router am I?\n")
    port_mapping, address_to_name, router_count = load_port_mapping("which_port.txt")
    initial_cost = load_initial_cost("adj_mat.txt", router_name)
    print(f'Initial Cost is {initial_cost}\n')
    my_bf = BFA(router_count, initial_cost, router_name, port_mapping, address_to_name)
    my_bf.who_to_send()
    while True:
        s = input("To start Bellman-Ford Algorithm, Enter 's'\n")
        if s == 's':
            break
        else:
            print("Wrong input! Please enter 's' to start the Bellman-Ford Algorithm")
    my_bf.send()
    start_time = timeit.default_timer()
    while True:
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if key == ord('u'):
                new_cost = load_initial_cost("adj_mat.txt", router_name)
                print(f'New cost is {new_cost}\n')
                my_bf.check_cost(new_cost)
        elapsed_time = timeit.default_timer() - start_time
        if elapsed_time > 1:
            my_bf.send()
            start_time = timeit.default_timer()
        my_bf.receive()
if __name__ == "__main__":
    main()