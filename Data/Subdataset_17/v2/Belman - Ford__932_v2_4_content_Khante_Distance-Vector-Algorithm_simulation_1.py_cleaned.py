import network_1
import link_1
import threading
from time import sleep
ROUTER_QUEUE_SIZE = 0
SIMULATION_TIME = 2
def main():
    network_objects = []
    host_1 = network_1.Host('H1')
    host_2 = network_1.Host('H2')
    network_objects.extend([host_1, host_2])
    cost_dict_a = {'H1': {0: 1}, 'RB': {1: 1}}
    router_a = network_1.Router(name='RA', cost_D=cost_dict_a, max_queue_size=ROUTER_QUEUE_SIZE)
    network_objects.append(router_a)
    cost_dict_b = {'H2': {1: 3}, 'RA': {0: 1}}
    router_b = network_1.Router(name='RB', cost_D=cost_dict_b, max_queue_size=ROUTER_QUEUE_SIZE)
    network_objects.append(router_b)
    link_layer = link_1.LinkLayer()
    network_objects.append(link_layer)
    link_layer.add_link(link_1.Link(host_1, 0, router_a, 0))
    link_layer.add_link(link_1.Link(router_a, 1, router_b, 0))
    link_layer.add_link(link_1.Link(router_b, 1, host_2, 0))
    threads = [threading.Thread(name=str(obj), target=obj.run) for obj in network_objects]
    for thread in threads:
        thread.start()
    router_a.send_routes(1)
    sleep(SIMULATION_TIME)
    print("Converged routing tables:")
    for obj in network_objects:
        if isinstance(obj, network_1.Router):
            obj.print_routes()
    host_1.udt_send('H2', 'MESSAGE_FROM_H1')
    sleep(SIMULATION_TIME)
    for obj in network_objects:
        obj.stop = True
    for thread in threads:
        thread.join()
    print("All simulation threads joined")
if __name__ == '__main__':
    main()