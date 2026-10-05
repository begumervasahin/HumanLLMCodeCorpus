ï»¿import sys
def fonk1(g,s):
	for v in g.get_vertices():
		v.set_distancia(sys.maxint)
	g.get_vertice(s).set_distancia(0)
def fonk2(Q):
	b1 = Q[0]
	for v in Q:
		if v.get_distancia() <b1.get_distancia():
			b1 = v
	Q.remove(b1)
	return b1
def fonk3(u,v):
	if v.get_distancia() > u.get_distancia() + u.get_peso(v):
		v.set_distancia(u.get_distancia() + u.get_peso(v))
		v.set_anterior(u)
def fonk4(v, caminho):
    if v._anterior:
        caminho.append(v.get_anterior().get_id())
        fonk4(v.get_anterior(), caminho)
    return