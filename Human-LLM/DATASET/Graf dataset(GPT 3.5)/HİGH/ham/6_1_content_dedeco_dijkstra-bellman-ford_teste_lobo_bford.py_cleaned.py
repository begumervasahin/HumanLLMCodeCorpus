ï»¿from grafo import grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
import sys
class class1(Exception):
    pass
def fonk1():
	print 'Testando grafo de exemplo das aulas do prof. Fernando Lobo da universidade Algarve in Portugal.'
	b1 = grafo(direcionado=True)
	b1.inserir_vertice('a')
	b1.inserir_vertice('b')
	b1.inserir_vertice('c')
	b1.inserir_vertice('d')
	b1.inserir_vertice('e')
	b1.inserir_aresta('a','b',10)
	b1.inserir_aresta('a','c',3)
	b1.inserir_aresta('b','c',1)
	b1.inserir_aresta('b','d',2)
	b1.inserir_aresta('c','b',4)
	b1.inserir_aresta('c','d',8)
	b1.inserir_aresta('c','e',2)
	b1.inserir_aresta('d','e',7)
	b1.inserir_aresta('e','d',9)
	if bellman_ford(b1,'a'):
		for v in b1.get_vertices():
			b2 = [v.get_id()]
			caminho_minino(v, b2)
			print 'O menor b2 Ã©: %s com custo %d.' %(b2[::-1], v.get_distancia())
	else:
		print 'Ciclo negativo encontrado'
if b3 = = "__main__":
	fonk1()