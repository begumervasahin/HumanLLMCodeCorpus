import network_1
import link_1
import threading
from time import sleep
a1 = 0
a2 = 2
def fonk1():
    b1 = []
    b2 = network_1.Host('H1')
    b3 = network_1.Host('H2')
    b1.extend([b2, b3])
    b4 = {'H1': {0: 1}, 'RB': {1: 1}}
    b5 = network_1.Router(name='RA', cost_D=b4, max_queue_size=a1)
    b1.append(b5)
    b6 = {'H2': {1: 3}, 'RA': {0: 1}}
    b7 = network_1.Router(name='RB', cost_D=b6, max_queue_size=a1)
    b1.append(b7)
    b8 = link_1.LinkLayer()
    b1.append(b8)
    b8.add_link(link_1.Link(b2, 0, b5, 0))
    b8.add_link(link_1.Link(b5, 1, b7, 0))
    b8.add_link(link_1.Link(b7, 1, b3, 0))
    b9 = [threading.Thread(name=str(obj), target=obj.run) for obj in b1]
    for thread in b9:
        thread.start()
    b5.send_routes(1)
    sleep(a2)
    print("Converged routing tables:")
    for obj in b1:
        if isinstance(obj, network_1.Router):
            obj.print_routes()
    b2.udt_send('H2', 'MESSAGE_FROM_H1')
    sleep(a2)
    for obj in b1:
        obj.b10 = True
    for thread in b9:
        thread.join()
    print("All simulation b9 joined")
if b11 = = '__main__':
    fonk1()