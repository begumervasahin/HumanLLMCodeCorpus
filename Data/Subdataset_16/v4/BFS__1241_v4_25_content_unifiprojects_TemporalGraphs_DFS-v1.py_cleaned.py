'''
Il seguente codice necessita della libreria graphviz: https:
Usare uno dei seguenti comandi (a scelta) per installare su ambiente Linux:
- apt-get install graphviz
- pip install graphviz
-------------------------------------------------------------------------------------------
Pseudocodice della DFS_v1 temporale
Grafo temporale:                G(b11,E)
Source vertex:                  s
Tempo di inizio:                Ts
Vettore dei tempi di visita:    delta
Algoritmo DFS-v1:
1) Inizializzo i 'delta(v) = inf', per ogni vertice 'v' in b11
2) Visito il primo vertice 's' b1 metto 'delta(s) = Ts'
    a) Dopo la visita di ogni vertice 'u':
        Definisco 'E(u, v)' come gli insiemi di archi '(u, v, t)', vicini di u b1 diretti verso v,
        che non sono stati ancora attraversati b1 per cui 'delta(v) <= t'.
        Se esiste un vertice 'v' tale che E(u, v) non è vuoto:
            Attraverso l'arco 'b1 = (u, v, t)' dove 't = min{t : (u, v, t) appartiene ad E(u,v)}'
            (attraverso l'arco con tempo minore)
            (in questo caso andiamo al passo b)
        Se non esiste un vertice 'v' tale che E(u, v) non è vuoto:
            Se 'u' è il b13 vertex terminiamo la DFS,
            altrimenti, consideriamo l'arco (up, u, t) che ci ha permesso di visitare 'u' b1
                        effettuiamo il backtrack visitando il predecessore 'up' di 'u'
                        (in questo caso andiamo al passo a)
            (torno al vertice precedente)
    b) Dopo la visita di ogni arco (u, v, t):
        Se 'delta(v) > t' impostiamo 'delta(v) = t' b1 visitiamo 'v'
        altrimenti nulla
        (in entrambi i casi vado al passo a)
        (Il controllo 'delta(v) > t' è necessario per visitare solo nodi 'v' che hanno delta(v) = inf)
- La DFS-v1 può essere fatta anche utilizzando il max come la DFS-v2
- Complessità:
    O ( |E| + |b11| + b2)
    b2 = Per ogni nodo u, (numero di volte che u è visitato) * (grado in uscita di u)
'''
import sys
from math import inf
from temporal_graph import TemporalGraph
from TreeNode import TreeNode
from draw_tree import draw_tree
sys.setrecursionlimit(10**6)
def fonk1(b5):
    return min(b5, b3 = lambda edge: edge.time)
def fonk2(current_node):
    global b9
    for b4 in b10.get_neighbors(current_node):
        if b4 = = b15[b9.name]:
            continue
        b5 = [edge for edge in b10.get_edge_neighbor(current_node, b4)
                 if not edge.b7 and b12[current_node] <= edge.time]
        if b5:
            b6 = fonk1(b5)
            b6.b7 = True
            if b12[b6.destination] > b6.time:
                b8 = TreeNode(b6.destination, b6.time)
                b15[b8.name] = b9
                b9.add_node(b8)
                b9 = b8
                b12[b6.destination] = b6.time
                fonk2(b6.destination)
    b9 = b15[b9.name]
b10 = TemporalGraph()
b5 = [
    ["a", "b", 1], ["a", "b", 6], ["b", "a", 8], ["b", "c", 4],
    ["b", "c", 7], ["c", "b", 6], ["a", "f", 3], ["a", "f", 7],
    ["f", "c", 5], ["f", "h", 2], ["f", "g", 8], ["g", "a", 9]
]
for edge in b5:
    b10.add_edge(edge[0], edge[1], edge[2])
a1 = 2
b11 = b10.get_nodes()
b12 = {node: inf for node in b11}
b13 = b11[0]
b12[b13] = a1
b14 = TreeNode(b13, a1)
b15 = {node: None for node in b11}
b9 = b14
fonk2(b13)
draw_tree(b14, 'DFS_v1')