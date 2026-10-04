import network_2
import link_2
import threading
from time import sleep
a1 = 0
a2 = 2
def fonk1():
    return [network_2.Host('H1'), network_2.Host('H2')]
def fonk2():
    b1 = {'H1': {0: 1}, 'RB': {1: 1}}
    b2 = network_2.Router(name='RA', cost_D=b1, max_queue_size=a1)
    b3 = {'H2': {1: 3}, 'RA': {0: 1}}
    b4 = network_2.Router(name='RB', cost_D=b3, max_queue_size=a1)
    return [b2, b4]
def fonk3():
    return link_2.LinkLayer()
def fonk4(b9, b7, b8):
    b9.add_link(link_2.Link(b7[0], 0, b8[0], 0))
    b9.add_link(link_2.Link(b8[0], 1, b8[1], 0))
    b9.add_link(link_2.Link(b8[1], 1, b7[1], 0))
def fonk5(objects):
    b5 = [threading.Thread(name=str(obj), target=obj.run) for obj in objects]
    for thread in b5:
        thread.start()
    return b5
def fonk6(b8):
    print("Converged routing tables:")
    for router in b8:
        router.print_routes()
def fonk7(objects, b5):
    for obj in objects:
        obj.b6 = True
    for thread in b5:
        thread.join()
    print("All simulation b5 joined")
def fonk8():
    b7 = fonk1()
    b8 = fonk2()
    b9 = fonk3()
    b10 = b7 + b8 + [b9]
    fonk4(b9, b7, b8)
    b5 = fonk5(b10)
    b8[0].send_routes(1)
    sleep(a2)
    fonk6(b8)
    b7[0].udt_send('H2', 'MESSAGE_FROM_H1')
    b7[1].udt_send('H1', 'reply for MESSAGE_FROM_H1')
    sleep(a2)
    fonk7(b10, b5)
if b11 = = '__main__':
    fonk8()