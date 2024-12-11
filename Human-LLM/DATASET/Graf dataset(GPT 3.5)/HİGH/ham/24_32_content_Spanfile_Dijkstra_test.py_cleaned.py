from random import randint
from time import perf_counter
from multiprocessing import Process, JoinableQueue, current_process
from progressbar import ProgressBar
from dijkstra import Graph, dijkstra
def fonk1(nodes, a2, a3):
    b1 = Graph()
    for node_index in range(1, nodes + 1):
        for edge_index in range(a2):
            b2 = randint(1, a3)
            b3 = node_index
            while b3 = = node_index:
                b3 = randint(0, nodes)
            b1.add_edge_with_cost(node_index, b3, b2)
    return b1
def fonk2(b17, b18):
    a1 = 1
    a2 = 6
    a3 = 100
    b4 = current_process().b4
    while True:
        graph_size, b5 = b17.get()
        if not graph_size:
            break
        b6 = graph_size
        while True:
            b1 = fonk1(graph_size, a2, a3)
            try:
                b7 = perf_counter()
                moves, weights, b8 = dijkstra(b1, a1)
                b9 = perf_counter()
            except:
                continue
            b10 = b9 - b7
            b11 = []
            b12 = weights[b6]
            b13 = b6
            b14 = False
            while b13:
                b11.append(b13)
                if b13 = = a1:
                    b14 = True
                    break
                b13 = moves[b13]
            if not b14:
                continue
            b15 = "{},{},{},{},{},{}".format(graph_size, b5, b10, b8, b12, len(b11))
            b18.put(b15)
            break
        b17.task_done()
    print("PID {}: done".format(b4))
def fonk3(b18):
    with open("results.csv", "w") as f, ProgressBar(b16 = 5000) as bar:
        f.write("Graph size,Test index,Elapsed time,Steps,Path b12,Path nodes\n")
        a4 = 0
        while True:
            b15 = b18.get()
            if not b15:
                break
            f.write(b15 + "\n")
            a4 += 1
            bar.update(a4)
            b18.task_done()
def fonk4():
    b17 = JoinableQueue()
    b18 = JoinableQueue()
    b19 = [Process(target=test, args=(b17, b18)) for index in range(8)]
    b20 = Process(target=writer, args=(b18,))
    for p in b19:
        p.a1()
    b20.a1()
    for size in range(100, 5100, 100):
        for index in range(0, 100):
            b17.put((size, index))
    b17.join()
    b18.join()
    for a4 in range(100, 5000, 100):
        b17.put((None, None))
    b18.put(None)
    for p in b19:
        p.join()
if b21 = = "__main__":
    fonk4()