import network_1
import link_1
import threading
from time import sleep
import sys
router_queue_size = 0
simulation_time = 2
if __name__ == '__main__':
    object_L = []
    host_1 = network_1.Host('H1')
    object_L.append(host_1)
    host_2 = network_1.Host('H2')
    object_L.append(host_2)
    cost_D = {'H1': {0: 1}, 'RB': {1: 1}}
    router_a = network_1.Router(name='RA',
                              cost_D = cost_D,
                              max_queue_size=router_queue_size)
    object_L.append(router_a)
    cost_D = {'H2': {1: 3}, 'RA': {0: 1}}
    router_b = network_1.Router(name='RB',
                              cost_D = cost_D,
                              max_queue_size=router_queue_size)
    object_L.append(router_b)
    link_layer = link_1.LinkLayer()
    object_L.append(link_layer)
    link_layer.add_link(link_1.Link(host_1, 0, router_a, 0))
    link_layer.add_link(link_1.Link(router_a, 1, router_b, 0))
    link_layer.add_link(link_1.Link(router_b, 1, host_2, 0))
    thread_L = []
    for obj in object_L:
        thread_L.append(threading.Thread(name=obj.__str__(), target=obj.run))
    for t in thread_L:
        t.start()
    router_a.send_routes(1)
    sleep(simulation_time)
    print("Converged routing tables")
    for obj in object_L:
        if str(type(obj)) == "<class 'network_1.Router'>":
            obj.print_routes()
    host_1.udt_send('H2', 'MESSAGE_FROM_H1')
    sleep(simulation_time)
    for o in object_L:
        o.stop = True
    for t in thread_L:
        t.join()
    print("All simulation threads joined")