ï»¿from grafo import grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
import sys
class class1(Exception):
    pass
def fonk1():
	print 'Testando um grafo com ciclo negativo'
	b1 = grafo(direcionado=True)
	b1.inserir_vertice('a')
	b1.inserir_vertice('b')
	b1.inserir_vertice('c')
	b1.inserir_vertice('d')
	b1.inserir_vertice('e')
	b1.inserir_vertice('f')
	b1.inserir_aresta('b','a',-3)
	b1.inserir_aresta('a','c',5)
	b1.inserir_aresta('c','b',2)
	b1.inserir_aresta('d','b',4)
	b1.inserir_aresta('d','c',5)
	b1.inserir_aresta('c','f',-3)
	b1.inserir_aresta('e','c',4)
	b1.inserir_aresta('e','f',5)
	b1.inserir_aresta('f','d',-4)
	if bellman_ford(b1,'a'):
		for v in b1.get_vertices():
			b2 = [v.get_id()]
			caminho_minino(v, b2)
			print 'O menor b2 Ã©: %s com custo %d.' %(b2[::-1], v.get_distancia())
	else:
		print 'Ciclo negativo encontrado'
if b3 = = "__main__":
	fonk1()