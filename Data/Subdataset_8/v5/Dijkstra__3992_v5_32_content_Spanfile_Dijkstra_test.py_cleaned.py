from random import randint
from time import perf_counter
from multiprocessing import Process, JoinableQueue, current_process
from progressbar import ProgressBar
from dijkstra import Graph, dijkstra
def generate_random_graph(nodes, edges_per_node, max_weight):
    graph = Graph()
    for node_index in range(1, nodes + 1):
        for _ in range(edges_per_node):
            weight = randint(1, max_weight)
            neighbour = node_index
            while neighbour == node_index:
                neighbour = randint(1, nodes)
            graph.add_edge_with_cost(node_index, neighbour, weight)
    return graph
def test(queue, output):
    start = 1
    edges_per_node = 6
    max_weight = 100
    pid = current_process().pid
    while True:
        task = queue.get()
        if not task:
            break
        graph_size, graph_index = task
        end = graph_size
        while True:
            graph = generate_random_graph(graph_size, edges_per_node, max_weight)
            try:
                start_time = perf_counter()
                moves, weights, steps = dijkstra(graph, start)
                end_time = perf_counter()
            except Exception as e:
                print(f"Exception occurred in PID {pid}: {e}")
                continue
            elapsed = end_time - start_time
            path = []
            length = weights[end]
            current = end
            complete = False
            while current:
                path.append(current)
                if current == start:
                    complete = True
                    break
                current = moves[current]
            if not complete:
                continue
            result = f"{graph_size},{graph_index},{elapsed},{steps},{length},{len(path)}"
            output.put(result)
            break
        queue.task_done()
    print(f"PID {pid}: done")
def writer(output):
    with open("results.csv", "w") as file, ProgressBar(max_value=5000) as bar:
        file.write("Graph size,Test index,Elapsed time,Steps,Path length,Path nodes\n")
        tasks_completed = 0
        while True:
            result = output.get()
            if not result:
                break
            file.write(result + "\n")
            tasks_completed += 1
            bar.update(tasks_completed)
            output.task_done()
def main():
    queue = JoinableQueue()
    output = JoinableQueue()
    num_processes = 8
    test_processes = [Process(target=test, args=(queue, output)) for _ in range(num_processes)]
    write_process = Process(target=writer, args=(output,))
    for process in test_processes:
        process.start()
    write_process.start()
    for size in range(100, 5100, 100):
        for index in range(100):
            queue.put((size, index))
    queue.join()
    for _ in range(num_processes):
        queue.put(None)
    output.put(None)
    for process in test_processes:
        process.join()
if __name__ == "__main__":
    main()