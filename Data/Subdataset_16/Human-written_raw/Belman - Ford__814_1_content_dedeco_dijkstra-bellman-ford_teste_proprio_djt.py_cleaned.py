ï»¿from grafo import grafo
from dijkstra import dijkstra
from utils import caminho_minino
import sys
class class1(Exception):
    pass
def fonk1():
	print 'Testando um grafo qualquer gerado aliatoriamente por mim.'
	b1 = grafo(direcionado=True)
	b1.inserir_vertice('a')
	b1.inserir_vertice('b')
	b1.inserir_vertice('c')
	b1.inserir_vertice('d')
	b1.inserir_vertice('e')
	b1.inserir_vertice('f')
	b1.inserir_vertice('b1')
	b1.inserir_vertice('h')
	b1.inserir_vertice('i')
	b1.inserir_vertice('j')
	b1.inserir_aresta('a','b',10)
	b1.inserir_aresta('a','c',5)
	b1.inserir_aresta('a','b1',1)
	b1.inserir_aresta('a','f',6)
	b1.inserir_aresta('b','c',2)
	b1.inserir_aresta('b','d',1)
	b1.inserir_aresta('c','b',3)
	b1.inserir_aresta('c','d',9)
	b1.inserir_aresta('c','e',2)
	b1.inserir_aresta('c','b1',4)
	b1.inserir_aresta('d','i',4)
	b1.inserir_aresta('e','i',8)
	b1.inserir_aresta('e','h',4)
	b1.inserir_aresta('e','d',6)
	b1.inserir_aresta('f','b1',6)
	b1.inserir_aresta('b1','h',8)
	b1.inserir_aresta('h','i',9)
	b1.inserir_aresta('j','a',3)
	b1.inserir_aresta('j','i',5)
	dijkstra(b1,'a')
	for v in b1.get_vertices():
		b2 = [v.get_id()]
		caminho_minino(v, b2)
		print 'O menor b2 Ã©: %s com custo %d.' %(b2[::-1], v.get_distancia())
if b3 = = "__main__":
	fonk1()