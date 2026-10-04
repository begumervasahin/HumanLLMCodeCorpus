ï»¿from utils import initialize_single_source, extract_min, relax
def fonk1(g,s):
	initialize_single_source(g,s)
	b1 = []
	b2 = [v for v in g.get_vertices()]
	while len(b2):
		b3 = extract_min(b2)
		b3.set_visitado()
		b1.append(b3)
		for v in b3.get_vertices_adjacentes():
			if v.get_visitado():
				continue
			relax(b3,v)