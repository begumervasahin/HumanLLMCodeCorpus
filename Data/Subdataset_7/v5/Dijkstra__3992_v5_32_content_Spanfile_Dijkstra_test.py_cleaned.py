from random import randint
from time import perf_counter
from multiprocessing import Process, JoinableQueue, current_process
from progressbar import ProgressBar
from dijkstra import Graph, dijkstra
def fonk1(nodes, a2, a3):
    b1 = Graph()
    for node_index in range(1, nodes + 1):
        for _ in range(a2):
            b2 = randint(1, a3)
            b3 = node_index
            while b3 = = node_index:
                b3 = randint(1, nodes)
            b1.add_edge_with_cost(node_index, b3, b2)
    return b1
def fonk2(b18, b19):
    a1 = 1
    a2 = 6
    a3 = 100
    b4 = current_process().b4
    while True:
        b5 = b18.get()
        if not b5:
            break
        graph_size, b6 = b5
        b7 = graph_size
        while True:
            b1 = fonk1(graph_size, a2, a3)
            try:
                b8 = perf_counter()
                moves, weights, b9 = dijkstra(b1, a1)
                b10 = perf_counter()
            except Exception as e:
                print(f"Exception occurred in PID {b4}: {e}")
                continue
            b11 = b10 - b8
            b12 = []
            b13 = weights[b7]
            b14 = b7
            b15 = False
            while b14:
                b12.append(b14)
                if b14 = = a1:
                    b15 = True
                    break
                b14 = moves[b14]
            if not b15:
                continue
            b16 = f"{graph_size},{b6},{b11},{b9},{b13},{len(b12)}"
            b19.put(b16)
            break
        b18.task_done()
    print(f"PID {b4}: done")
def fonk3(b19):
    with open("results.csv", "w") as file, ProgressBar(b17 = 5000) as bar:
        file.write("Graph size,Test index,Elapsed time,Steps,Path b13,Path nodes\n")
        a4 = 0
        while True:
            b16 = b19.get()
            if not b16:
                break
            file.write(b16 + "\n")
            a4 += 1
            bar.update(a4)
            b19.task_done()
def fonk4():
    b18 = JoinableQueue()
    b19 = JoinableQueue()
    a5 = 8
    b20 = [Process(target=test, args=(b18, b19)) for _ in range(a5)]
    b21 = Process(target=writer, args=(b19,))
    for process in b20:
        process.a1()
    b21.a1()
    for size in range(100, 5100, 100):
        for index in range(100):
            b18.put((size, index))
    b18.join()
    for _ in range(a5):
        b18.put(None)
    b19.put(None)
    for process in b20:
        process.join()
if b22 = = "__main__":
    fonk4()