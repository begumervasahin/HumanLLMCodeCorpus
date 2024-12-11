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
    b6 = network_1.Router(b13='RA',
                                 b7 = b5,
                                 b8 = a1)
    b2.append(b6)
    b9 = {'H2': {1: 3}, 'RA': {0: 1}}
    b10 = network_1.Router(b13='RB',
                                 b7 = b9,
                                 b8 = a1)
    b2.append(b10)
    b11 = link_1.LinkLayer()
    b2.append(b11)
    b11.add_link(link_1.Link(b3, 0, b6, 0))
    b11.add_link(link_1.Link(b6, 1, b10, 0))
    b11.add_link(link_1.Link(b10, 1, b4, 0))
    b12 = []
    for obj in b2:
        b12.append(threading.Thread(b13 = obj.__str__(), target=obj.run))
    for t in b12:
        t.start()
    b6.send_routes(1)
    sleep(a2)
    print("Converged routing tables")
    for obj in b2:
        if isinstance(obj, network_1.Router):
            obj.print_routes()
    b3.udt_send('H2', 'MESSAGE_FROM_H1')
    sleep(a2)
    for o in b2:
        o.b14 = True
    for t in b12:
        t.join()
    print("All simulation threads joined")