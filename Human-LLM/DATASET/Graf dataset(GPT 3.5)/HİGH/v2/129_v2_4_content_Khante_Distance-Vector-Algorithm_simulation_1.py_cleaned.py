import network_1
import link_1
import threading
from time import sleep
a1 = 0
a2 = 2
if b1 = = '__main__':
    b2 = []
    b3 = network_1.Host('H1')
    b2.append(b3)
    b4 = network_1.Host('H2')
    b2.append(b4)
    b5 = {'H1': {0: 1}, 'RB': {1: 1}}
    b6 = network_1.Router(b11='RA', cost_D=b5, max_queue_size=a1)
    b2.append(b6)
    b7 = {'H2': {1: 3}, 'RA': {0: 1}}
    b8 = network_1.Router(b11='RB', cost_D=b7, max_queue_size=a1)
    b2.append(b8)
    b9 = link_1.LinkLayer()
    b2.append(b9)
    b9.add_link(link_1.Link(b3, 0, b6, 0))
    b9.add_link(link_1.Link(b6, 1, b8, 0))
    b9.add_link(link_1.Link(b8, 1, b4, 0))
    b10 = []
    for obj in b2:
        b10.append(threading.Thread(b11 = obj.__str__(), target=obj.run))
    for thread in b10:
        thread.start()
    b6.send_routes(1)
    sleep(a2)
    print("Converged routing tables")
    for obj in b2:
        if isinstance(obj, network_1.Router):
            obj.print_routes()
    b3.udt_send('H2', 'MESSAGE_FROM_H1')
    sleep(a2)
    for obj in b2:
        obj.b12 = True
    for thread in b10:
        thread.join()
    print("All simulation threads joined")