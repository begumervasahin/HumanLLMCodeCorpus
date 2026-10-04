import network_2
import link_2
import threading
from time import sleep
import sys
a1 = 0
a2 = 2
if b1 = = '__main__':
    b2 = []
    b3 = network_2.Host('H1')
    b2.append(b3)
    b4 = network_2.Host('H2')
    b2.append(b4)
    b5 = {'H1': {0: 1}, 'RB': {1: 1}}
    b6 = network_2.Router(b11='RA',
                              b5 = b5,
                              b7 = a1)
    b2.append(b6)
    b5 = {'H2': {1: 3}, 'RA': {0: 1}}
    b8 = network_2.Router(b11='RB',
                              b5 = b5,
                              b7 = a1)
    b2.append(b8)
    b9 = link_2.LinkLayer()
    b2.append(b9)
    b9.add_link(link_2.Link(b3, 0, b6, 0))
    b9.add_link(link_2.Link(b6, 1, b8, 0))
    b9.add_link(link_2.Link(b8, 1, b4, 0))
    b10 = []
    for obj in b2:
        b10.append(threading.Thread(b11 = obj.__str__(), target=obj.run))
    for t in b10:
        t.start()
    b6.send_routes(1)
    sleep(a2)
    print("Converged routing tables")
    for obj in b2:
        if str(type(obj)) == "<class 'network_2.Router'>":
            obj.print_routes()
    b3.udt_send('H2', 'MESSAGE_FROM_H1')
    b4.udt_send('H1', 'reply for MESSAGE_FROM_H1')
    sleep(a2)
    for o in b2:
        o.b12 = True
    for t in b10:
        t.join()
    print("All simulation threads joined")