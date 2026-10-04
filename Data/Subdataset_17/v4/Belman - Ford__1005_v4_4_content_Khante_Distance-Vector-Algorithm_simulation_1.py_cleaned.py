import network_1
import link_1
import threading
from time import sleep
ROUTER_QUEUE_SIZE = 0
SIMULATION_TIME = 2
def create_hosts():
    host_1 = network_1.Host('H1')
    host_2 = network_1.Host('H2')
    return [host_1, host_2]
def create_routers():
    cost_dict_a = {'H1': {0: 1}, 'RB': {1: 1}}
    router_a = network_1.Router(name='RA', cost_D=cost_dict_a, max_queue_size=ROUTER_QUEUE_SIZE)
    cost_dict_b = {'H2': {1: 3}, 'RA': {0: 1}}
    router_b = network_1.Router(name='RB', cost_D=cost_dict_b, max_queue_size=ROUTER_QUEUE_SIZE)
    return [router_a, router_b]
def create_link_layer():
    return link_1.LinkLayer()
def add_links(link_layer, host_1, router_a, router_b, host_2):
    link_layer.add_link(link_1.Link(host_1, 0, router_a, 0))
    link_layer.add_link(link_1.Link(router_a, 1, router_b, 0))
    link_layer.add_link(link_1.Link(router_b, 1, host_2, 0))
def start_threads(objects):
    threads = [threading.Thread(name=str(obj), target=obj.run) for obj in objects]
    for thread in threads:
        thread.start()
    return threads
def main():
    hosts = create_hosts()
    routers = create_routers()
    link_layer = create_link_layer()
    network_objects = hosts + routers + [link_layer]
    add_links(link_layer, hosts[0], routers[0], routers[1], hosts[1])
    threads = start_threads(network_objects)
    routers[0].send_routes(1)
    sleep(SIMULATION_TIME)
    print("Converged routing tables:")
    for obj in routers:
        obj.print_routes()
    hosts[0].udt_send('H2', 'MESSAGE_FROM_H1')
    sleep(SIMULATION_TIME)
    for obj in network_objects:
        obj.stop = True
    for thread in threads:
        thread.join()
    print("All simulation threads joined")
if __name__ == '__main__':
    main()