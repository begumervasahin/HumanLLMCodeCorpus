import network_2
import link_2
import threading
from time import sleep
a1 = 0
a2 = 2
def fonk1():
    b1 = network_2.Host('H1')
    b2 = network_2.Host('H2')
    return [b1, b2]
def fonk2():
    b3 = {'H1': {0: 1}, 'RB': {1: 1}}
    b4 = network_2.Router(name='RA', cost_D=b3, max_queue_size=a1)
    b5 = {'H2': {1: 3}, 'RA': {0: 1}}
    b6 = network_2.Router(name='RB', cost_D=b5, max_queue_size=a1)
    return [b4, b6]
def fonk3():
    return link_2.LinkLayer()
def fonk4(b11, b9, b10):
    b11.add_link(link_2.Link(b9[0], 0, b10[0], 0))
    b11.add_link(link_2.Link(b10[0], 1, b10[1], 0))
    b11.add_link(link_2.Link(b10[1], 1, b9[1], 0))
def fonk5(objects):
    b7 = [threading.Thread(name=str(obj), target=obj.run) for obj in objects]
    for thread in b7:
        thread.start()
    return b7
def fonk6(b10):
    print("Converged routing tables:")
    for router in b10:
        router.print_routes()
def fonk7(objects, b7):
    for obj in objects:
        obj.b8 = True
    for thread in b7:
        thread.join()
    print("All simulation b7 joined")
def fonk8():
    b9 = fonk1()
    b10 = fonk2()
    b11 = fonk3()
    b12 = b9 + b10 + [b11]
    fonk4(b11, b9, b10)
    b7 = fonk5(b12)
    b10[0].send_routes(1)
    sleep(a2)
    fonk6(b10)
    b9[0].udt_send('H2', 'MESSAGE_FROM_H1')
    b9[1].udt_send('H1', 'reply for MESSAGE_FROM_H1')
    sleep(a2)
    fonk7(b12, b7)
if b13 = = '__main__':
    fonk8()