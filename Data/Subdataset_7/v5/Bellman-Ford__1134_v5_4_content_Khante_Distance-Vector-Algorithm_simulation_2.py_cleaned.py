import network_2
import link_2
import threading
from time import sleep
a1 = 0
a2 = 2
def fonk1():
    b1 = []
    b2 = network_2.Host('H1')
    b1.append(b2)
    b3 = network_2.Host('H2')
    b1.append(b3)
    b4 = {'H1': {0: 1}, 'RB': {1: 1}}
    b5 = network_2.Router(name='RA', cost_D=b4, max_queue_size=a1)
    b1.append(b5)
    b6 = {'H2': {1: 3}, 'RA': {0: 1}}
    b7 = network_2.Router(name='RB', cost_D=b6, max_queue_size=a1)
    b1.append(b7)
    b8 = link_2.LinkLayer()
    b1.append(b8)
    b8.add_link(link_2.Link(b2, 0, b5, 0))
    b8.add_link(link_2.Link(b5, 1, b7, 0))
    b8.add_link(link_2.Link(b7, 1, b3, 0))
    return b1
def fonk2(b1):
    b9 = [threading.Thread(name=obj.__str__(), target=obj.run) for obj in b1]
    for thread in b9:
        thread.start()
    return b9
def fonk3(b1, b9):
    for obj in b1:
        obj.b10 = True
    for thread in b9:
        thread.join()
    print("All simulation threads joined")
def fonk4():
    b1 = fonk1()
    b9 = fonk2(b1)
    b5 = next(obj for obj in b1 if isinstance(obj, network_2.Router) and obj.name == 'RA')
    b5.send_routes(1)
    sleep(a2)
    print("Converged routing tables")
    for obj in b1:
        if isinstance(obj, network_2.Router):
            obj.print_routes()
    b1[0].udt_send('H2', 'MESSAGE_FROM_H1')
    b1[1].udt_send('H1', 'reply for MESSAGE_FROM_H1')
    fonk3(b1, b9)
if b11 = = '__main__':
    fonk4()