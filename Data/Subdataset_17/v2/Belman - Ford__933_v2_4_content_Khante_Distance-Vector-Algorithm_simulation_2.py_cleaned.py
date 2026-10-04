import network_2
import link_2
import threading
from time import sleep
ROUTER_QUEUE_SIZE = 0
SIMULATION_TIME = 2
def create_hosts():
    return [network_2.Host('H1'), network_2.Host('H2')]
def create_routers():
    cost_dict_a = {'H1': {0: 1}, 'RB': {1: 1}}
    cost_dict_b = {'H2': {1: 3}, 'RA': {0: 1}}
    router_a = network_2.Router(name='RA', cost_D=cost_dict_a, max_queue_size=ROUTER_QUEUE_SIZE)
    router_b = network_2.Router(name='RB', cost_D=cost_dict_b, max_queue_size=ROUTER_QUEUE_SIZE)
    return [router_a, router_b]
def create_link_layer():
    return link_2.LinkLayer()
def add_links(link_layer, hosts, routers):
    link_layer.add_link(link_2.Link(hosts[0], 0, routers[0], 0))
    link_layer.add_link(link_2.Link(routers[0], 1, routers[1], 0))
    link_layer.add_link(link_2.Link(routers[1], 1, hosts[1], 0))
def start_threads(objects):
    threads = [threading.Thread(name=str(obj), target=obj.run) for obj in objects]
    for thread in threads:
        thread.start()
    return threads
def print_routing_tables(routers):
    print("Converged routing tables:")
    for router in routers:
        router.print_routes()
def stop_simulation(objects, threads):
    for obj in objects:
        obj.stop = True
    for thread in threads:
        thread.join()
    print("All simulation threads joined")
def main():
    hosts = create_hosts()
    routers = create_routers()
    link_layer = create_link_layer()
    network_objects = hosts + routers + [link_layer]
    add_links(link_layer, hosts, routers)
    threads = start_threads(network_objects)
    routers[0].send_routes(1)
    sleep(SIMULATION_TIME)
    print_routing_tables(routers)
    hosts[0].udt_send('H2', 'MESSAGE_FROM_H1')
    hosts[1].udt_send('H1', 'reply for MESSAGE_FROM_H1')
    sleep(SIMULATION_TIME)
    stop_simulation(network_objects, threads)
if __name__ == '__main__':
    main()