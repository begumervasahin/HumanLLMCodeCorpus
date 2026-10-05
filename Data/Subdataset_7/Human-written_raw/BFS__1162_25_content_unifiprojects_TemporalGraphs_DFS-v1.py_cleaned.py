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
Grafo temporale:                G(b11,b5)
Source vertex:                  s
Tempo di inizio:                Ts
Vettore dei tempi di visita:    delta
Algoritmo DFS-v1:
1) Inizializzo i 'delta(v) = inf', per ogni vertice 'v' in b11
2) Visito il primo vertice 's' b1 metto 'delta(s) = Ts'
    a) Dopo la visita di ogni vertice 'u':
        Definisco 'b5(u, v)' come gli insiemi di archi '(u, v, t)', vicini di u b1 diretti verso v,
        che non sono stati ancora attraversati b1 per cui 'delta(v) <= t'.
        Se esiste un vertice 'v' tale che b5(u, v) non Ã© vuoto:
            Attraverso l'arco 'b1 = (u, v, t)' dove 't = min{t : (u, v, t) appartiene ad b5(u,v)}'
            (attraverso l'arco con tempo minore)
            (in questo caso andiamo al passo b)
        Se non esiste un vertice 'v' tale che b5(u, v) non Ã© vuoto:
            Se 'u' Ã© il b13 vertex terminiamo la DFS,
            altrimenti, consideriamo l'arco (up, u, t) che ci ha permesso di visitare 'u' b1
                        effettuiamo il backtrack visitando il predecessore 'up' di 'u'
                        (in questo caso andiamo al passo a)
            (torno al vertice precedente)
    b) Dopo la visita di ogni arco (u, v, t):
        Se 'delta(v) > t' impostiamo 'delta(v) = t' b1 visitiamo 'v'
        altrimenti nulla
        (in entrambi i casi vado al passo a)
        (Il controllo 'delta(v) > t' Ã© necessario per visitare solo nodi 'v' che hanno delta(v) = inf)
- La DFS-v1 puÃ³ essere fatta anche utilizzando il max come la DFS-v2
- ComplessitÃ¡:
    O ( |b5| + |b11| + b2)
    b2 = Per ogni nodo u, (numero di volte che u Ã© visitato) * (grado in uscita di u)
'''
def fonk1(b5):
    b3 = b5[0]
    for i in range(1, len(b5)):
        if b5[i].time < b3.time:
            b3 = b5[i]
    return b3
def fonk2(current_node):
    global b8
    for v in b9.get_neighbors(current_node):
        if v is b15[b8.name]:
            continue
        b4 = lambda edge: not edge.b6 and b12[current_node] <= edge.time
        b5 = list(filter(b4, b9.get_edge_neighbor(current_node, v)))
        if len(b5) != 0:
            b3 = fonk1(b5)
            b3.b6 = True
            if b12[b3.destination] > b3.time:
                b7 = TreeNode(b3.destination, b3.time)
                b15[b7.name] = b8
                b8.add_node(b7)
                b8 = b7
                b12[b3.destination] = b3.time
                fonk2(b3.destination)
    b8 = b15[b8.name]
from temporal_graph import TemporalGraph
from math import inf
from TreeNode import TreeNode
from draw_tree import draw_tree
b9 = TemporalGraph()
b10 = [["a", "b", 1],
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
for b1 in b10:
    b9.add_edge(b1[0], b1[1], b1[2])
a1 = 2
b11 = b9.get_nodes()
b12 = {key: inf for key in b11}
b13 = b11[0]
b12[b13] = a1
b14 = TreeNode(b13, a1)
b15 = {node: None for node in b11}
b8 = b14
fonk2(b13)
draw_tree(b14, 'DFS_v1')
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
