import sys
def matriz(arquivo):
	conteudo = open(arquivo, 'r').readlines()
	matriz = []
	linha = []
	for i in range(len(conteudo)):
		for j in range(len(conteudo)):
			linha.append((conteudo[i].split(" ")[j]).replace('\n', ''))
		matriz.append(linha)
		linha = []
	return matriz
def nosAdjacentes(matriz):
	nosAdjacentes = []
	linha = []
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			if(matriz[i][j] != "1024"):
				linha.append(str(j) + " "+ matriz[i][j])
		nosAdjacentes.append(linha)
		linha = []
	return nosAdjacentes
def dijkstra(nosAdjacentes, inicio, fim):
	visitouNos = [0] * len(nosAdjacentes)
	solucao = []
	linha = []
	local = [0] * len(nosAdjacentes)
	linha.append ('- ' + inicio + ' 0')
	solucao.append(linha)
	visitouNos[int(inicio)] = 1
	noAtual = int(inicio)
	distanciaNoAtual = 0
	noAnterior = ""
	distanciaNoAnterior = 0
	menorAdj = ""
        distanciaAdj = ""
	while visitouNos[int(fim)] != 1:
		menorAdj = (nosAdjacentes[noAtual][0]).split(" ")[0]
		distanciaAdj = int((nosAdjacentes[noAtual][0]).split(" ")[1]) + int(distanciaNoAtual)
		for i in range(1,len(nosAdjacentes[noAtual])):
			if(visitouNos[int(menorAdj)] != 1):
				if(int(menorAdj) == int(fim) ):
					noAnterior = noAtual
				else:
					adj2 = 	(nosAdjacentes[noAtual][i]).split(" ")[0]
					if(visitouNos[int(adj2)] != 1):
						distanciaAdj2 = int((nosAdjacentes[noAtual][i]).split(" ")[1]) + int(distanciaNoAtual)
						if(distanciaAdj2 < distanciaAdj) :
							menorAdj = adj2
				                	distanciaAdj = distanciaAdj2
							noAnterior = noAtual
			elif(noAnterior == int(inicio) or visitouNos[int(menorAdj )] == 1):
				menorAdj = (nosAdjacentes[noAtual][i]).split(" ")[0]
				distanciaAdj = int((nosAdjacentes[noAtual][i]).split(" ")[1]) + int(distanciaNoAtual)
		if(noAnterior == ""):
			noAnterior = noAtual
		distanciaNoAnterior = (solucao[local[int(noAnterior)]][0]).split(" ")[2]
		if(len(solucao) > 2 and noAnterior != int(inicio) and int(menorAdj) != int(fim)):
			for i in range(len(nosAdjacentes[int(noAnterior)])):
				adj2 = 	(nosAdjacentes[noAnterior][i]).split(" ")[0]
				if(visitouNos[int(adj2)] != 1):
					distanciaAdj2 = int((nosAdjacentes[noAnterior][i]).split(" ")[1]) + int(distanciaNoAnterior)
					if(distanciaAdj2 < distanciaAdj):
						menorAdj = (nosAdjacentes[noAnterior][i]).split(" ")[0]
				                distanciaAdj = distanciaAdj2
		linha = []
		linha.append(str(noAnterior) + ' ' + str(menorAdj) + ' ' + str(distanciaAdj))
		solucao.append(linha)
		visitouNos[int(menorAdj)] = 1
		local[int(menorAdj)] = len(solucao) -1
		noAtual = int(menorAdj)
		distanciaNoAtual = int(distanciaAdj)
	return solucao
def exibirSolucao(solucao,inicio, fim):
	if(inicio == fim):
		print(inicio)
	else:
		sol=""
		sol += (solucao[(len(solucao)-1)][0]).split(" ")[1]
		sol += " "
		depois = (solucao[(len(solucao)-1)][0]).split(" ")[0]
		while int(depois) != int(inicio):
			for i in range(1,len(solucao)-1):
				if((solucao[i][0]).split(" ")[1] == depois):
					sol += (solucao[i][0]).split(" ")[1]
					sol += " "
					depois = (solucao[i][0]).split(" ")[0]
		sol += (solucao[0][0]).split(" ")[1]
		print(sol[::-1])
param = sys.argv[1:]
arquivo = param[0]
inicio = param[1]
fim = param[2]
nosAdjacentes = nosAdjacentes(matriz(arquivo))
exibirSolucao(dijkstra(nosAdjacentes,inicio,fim),inicio,fim)