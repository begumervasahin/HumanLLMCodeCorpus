import network_1
import link_1
import threading
from time import sleep
a1 = 0
a2 = 2
def fonk1():
    b1 = network_1.Host('H1')
    b2 = network_1.Host('H2')
    return [b1, b2]
def fonk2():
    b3 = {'H1': {0: 1}, 'RB': {1: 1}}
    b4 = network_1.Router(name='RA', cost_D=b3, max_queue_size=a1)
    b5 = {'H2': {1: 3}, 'RA': {0: 1}}
    b6 = network_1.Router(name='RB', cost_D=b5, max_queue_size=a1)
    return [b4, b6]
def fonk3():
    return link_1.LinkLayer()
def fonk4(b10, b1, b4, b6, b2):
    b10.add_link(link_1.Link(b1, 0, b4, 0))
    b10.add_link(link_1.Link(b4, 1, b6, 0))
    b10.add_link(link_1.Link(b6, 1, b2, 0))
def fonk5(objects):
    b7 = [threading.Thread(name=str(obj), target=obj.run) for obj in objects]
    for thread in b7:
        thread.start()
    return b7
def fonk6():
    b8 = fonk1()
    b9 = fonk2()
    b10 = fonk3()
    b11 = b8 + b9 + [b10]
    fonk4(b10, b8[0], b9[0], b9[1], b8[1])
    b7 = fonk5(b11)
    b9[0].send_routes(1)
    sleep(a2)
    print("Converged routing tables:")
    for obj in b9:
        obj.print_routes()
    b8[0].udt_send('H2', 'MESSAGE_FROM_H1')
    sleep(a2)
    for obj in b11:
        obj.b12 = True
    for thread in b7:
        thread.join()
    print("All simulation b7 joined")
if b13 = = '__main__':
    fonk6()