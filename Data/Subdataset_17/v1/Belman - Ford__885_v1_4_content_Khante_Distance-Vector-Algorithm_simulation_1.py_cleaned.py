import network_1
import link_1
import threading
from time import sleep
import sys
router_queue_size = 0
simulation_time = 2
def main():
    object_list = []
    host_1 = network_1.Host('H1')
    object_list.append(host_1)
    host_2 = network_1.Host('H2')
    object_list.append(host_2)
    cost_dict_a = {'H1': {0: 1}, 'RB': {1: 1}}
    router_a = network_1.Router(name='RA', cost_D=cost_dict_a, max_queue_size=router_queue_size)
    object_list.append(router_a)
    cost_dict_b = {'H2': {1: 3}, 'RA': {0: 1}}
    router_b = network_1.Router(name='RB', cost_D=cost_dict_b, max_queue_size=router_queue_size)
    object_list.append(router_b)
    link_layer = link_1.LinkLayer()
    object_list.append(link_layer)
    link_layer.add_link(link_1.Link(host_1, 0, router_a, 0))
    link_layer.add_link(link_1.Link(router_a, 1, router_b, 0))
    link_layer.add_link(link_1.Link(router_b, 1, host_2, 0))
    thread_list = [threading.Thread(name=str(obj), target=obj.run) for obj in object_list]
    for thread in thread_list:
        thread.start()
    router_a.send_routes(1)
    sleep(simulation_time)
    print("Converged routing tables:")
    for obj in object_list:
        if isinstance(obj, network_1.Router):
            obj.print_routes()
    host_1.udt_send('H2', 'MESSAGE_FROM_H1')
    sleep(simulation_time)
    for obj in object_list:
        obj.stop = True
    for thread in thread_list:
        thread.join()
    print("All simulation threads joined")
if __name__ == '__main__':
    main()