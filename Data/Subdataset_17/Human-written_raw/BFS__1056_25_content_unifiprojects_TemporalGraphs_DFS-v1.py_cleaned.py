25. Repository: unifiprojects/TemporalGraphs
   File: DFS-v1.py
   URL: https:
   Code Content:
'''
Il seguente codice necessita della libreria graphviz: https:
usare uno dei seguenti comandi (a scelta) per installare su ambiente Linux
apt-get install graphviz
pip install graphviz
-------------------------------------------------------------------------------------------
Pseudocodice della DFS_v1 temporale
Grafo temporale:                G(V,E)
Source vertex:                  s
Tempo di inizio:                Ts
Vettore dei tempi di visita:    delta
Algoritmo DFS-v1:
1) Inizializzo i 'delta(v) = inf', per ogni vertice 'v' in V
2) Visito il primo vertice 's' e metto 'delta(s) = Ts'
    a) Dopo la visita di ogni vertice 'u':
        Definisco 'E(u, v)' come gli insiemi di archi '(u, v, t)', vicini di u e diretti verso v,
        che non sono stati ancora attraversati e per cui 'delta(v) <= t'.
        Se esiste un vertice 'v' tale che E(u, v) non Ã© vuoto:
            Attraverso l'arco 'e = (u, v, t)' dove 't = min{t : (u, v, t) appartiene ad E(u,v)}'
            (attraverso l'arco con tempo minore)
            (in questo caso andiamo al passo b)
        Se non esiste un vertice 'v' tale che E(u, v) non Ã© vuoto:
            Se 'u' Ã© il source vertex terminiamo la DFS,
            altrimenti, consideriamo l'arco (up, u, t) che ci ha permesso di visitare 'u' e
                        effettuiamo il backtrack visitando il predecessore 'up' di 'u'
                        (in questo caso andiamo al passo a)
            (torno al vertice precedente)
    b) Dopo la visita di ogni arco (u, v, t):
        Se 'delta(v) > t' impostiamo 'delta(v) = t' e visitiamo 'v'
        altrimenti nulla
        (in entrambi i casi vado al passo a)
        (Il controllo 'delta(v) > t' Ã© necessario per visitare solo nodi 'v' che hanno delta(v) = inf)
- La DFS-v1 puÃ³ essere fatta anche utilizzando il max come la DFS-v2
- ComplessitÃ¡:
    O ( |E| + |V| + X)
    X = Per ogni nodo u, (numero di volte che u Ã© visitato) * (grado in uscita di u)
'''
def find_edge_with_min_time(E):
    edge_min = E[0]
    for i in range(1, len(E)):
        if E[i].time < edge_min.time:
            edge_min = E[i]
    return edge_min
def dfs_v1(current_node):
    global current_tree_node
    for v in graph.get_neighbors(current_node):
        if v is predecessor[current_tree_node.name]:
            continue
        filter_function = lambda edge: not edge.is_traversed and sigma[current_node] <= edge.time
        E = list(filter(filter_function, graph.get_edge_neighbor(current_node, v)))
        if len(E) != 0:
            edge_min = find_edge_with_min_time(E)
            edge_min.is_traversed = True
            if sigma[edge_min.destination] > edge_min.time:
                next_tree_node = TreeNode(edge_min.destination, edge_min.time)
                predecessor[next_tree_node.name] = current_tree_node
                current_tree_node.add_node(next_tree_node)
                current_tree_node = next_tree_node
                sigma[edge_min.destination] = edge_min.time
                dfs_v1(edge_min.destination)
    current_tree_node = predecessor[current_tree_node.name]
from temporal_graph import TemporalGraph
from math import inf
from TreeNode import TreeNode
from draw_tree import draw_tree
graph = TemporalGraph()
edges = [["a", "b", 1],
         ["a", "b", 6],
         ["b", "a", 8],
         ["b", "c", 4],
         ["b", "c", 7],
         ["c", "b", 6],
         ["a", "f", 3],
         ["a", "f", 7],
         ["f", "c", 5],
         ["f", "h", 2],
         ["f", "g", 8],
         ["g", "a", 9]]
for e in edges:
    graph.add_edge(e[0], e[1], e[2])
starting_time = 2
V = graph.get_nodes()
sigma = {key: inf for key in V}
source = V[0]
sigma[source] = starting_time
tree_node_root = TreeNode(source, starting_time)
predecessor = {node: None for node in V}
current_tree_node = tree_node_root
dfs_v1(source)
draw_tree(tree_node_root, 'DFS_v1')
   README Content:
TemporalGraphs
La repository contiene l'implementazione di 3 algoritmi di attraversamento di grafi temporali: BFS, DFS_v1, DFS_v2
Gli algoritmi vengono trattati nel paper
**"Temporal Graph Traversals: Definitions, Algorithms, and Applications**
**Authors: Silu Huang, James Cheng, Huanhuan Wu"**
I grafi prodotti dagli algoritmi possono essere visualizzati sfruttano la seguente libreria graphviz: https:
Usare uno dei seguenti comandi (a scelta) per installare su ambiente Linux
- apt-get install graphviz
- pip install graphviz
I PDF generati sono comunque disponibili in questa repo per i grafi forniti come esempio
