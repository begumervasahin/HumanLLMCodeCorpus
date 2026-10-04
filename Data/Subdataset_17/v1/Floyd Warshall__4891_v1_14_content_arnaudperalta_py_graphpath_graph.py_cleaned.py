import numpy as np
class Graph:
    def __init__(self, data):
        self.size = data["nbNoeuds"]
        self.sommetsList = list(data["nomSommets"])
        self.rdvList = list(data["nomRdv"])
        self.sommetsIniList = list(data["nomSommetsInitiaux"])
        self.arcs = list(data["arcs"])
        self.error = 0
        if len(self.sommetsList) != data["nbNoeuds"]:
            self.error = 1
        if len(self.rdvList) != data["nbLieuxRdv"]:
            self.error = 2
        self.path = np.zeros(self.size ** 2)
        self.bool = np.zeros(self.size ** 2)
        self.target = 0
        self.min = np.inf
        self.res = []
    def check_error(self):
        return self.error
    def mat_graph(self):
        mat = np.full((self.size, self.size), np.inf)
        for arc in self.arcs:
            mat[self.pos_sommet(arc["sommetInitial"]), self.pos_sommet(arc["sommetTerminal"])] = arc["duree"]
        return mat
    def pos_sommet(self, char):
        return self.sommetsList.index(char)
    def transform(self, mat):
        size_pair = self.size * self.size
        mat_pair = np.full((size_pair, size_pair), np.inf)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    for l in range(self.size):
                        if i == k and j == l:
                            mat_pair[i * self.size + j, k * self.size + l] = np.inf
                        elif i == k:
                            mat_pair[i * self.size + j, k * self.size + l] = mat[j, l]
                        elif j == l:
                            mat_pair[i * self.size + j, k * self.size + l] = mat[i, k]
        return mat_pair
    def rdv_optimal(self):
        mat_pcd = self.mat_pcd(self.transform(self.mat_graph()))
        init = self.pos_sommet(self.sommetsIniList[0]) * self.size + self.pos_sommet(self.sommetsIniList[1])
        rdv = [self.pos_sommet(c) * self.size + self.pos_sommet(c) for c in self.rdvList]
        res = np.inf
        fin = np.inf
        for i, rdv_point in enumerate(rdv):
            if mat_pcd[init, rdv_point] < res:
                res = mat_pcd[init, rdv_point]
                fin = i
        return str(self.rdvList[fin]) if fin != np.inf else ""
    def mat_pcd(self, mat):
        size_pair = self.size * self.size
        for i in range(size_pair):
            mat[i, i] = 0
        for k in range(size_pair):
            for i in range(size_pair):
                for j in range(size_pair):
                    mat[i, j] = min(mat[i, j], mat[i, k] + mat[k, j])
        return mat
    def explore(self, mat, position, depth):
        if depth > self.min:
            return
        self.path[depth] = position
        if position == self.target:
            if self.min == depth:
                self.res.append(np.copy(self.path[:depth + 1]).astype(int).tolist())
            if self.min > depth:
                self.min = depth
                self.res = [np.copy(self.path[:depth + 1]).astype(int).tolist()]
            return
        self.bool[position] = 1
        for i in range(self.size ** 2):
            if mat[position][i] == np.inf or self.bool[i] == 1:
                continue
            self.explore(mat, i, depth + 1)
        self.bool[position] = 0
    def rdv_optimal2(self):
        size_pair = self.size * self.size
        mat = self.transform(self.mat_graph())
        init = self.pos_sommet(self.sommetsIniList[0]) * self.size + self.pos_sommet(self.sommetsIniList[1])
        rdv = [self.pos_sommet(c) * self.size + self.pos_sommet(c) for c in self.rdvList]
        roadres = []
        sizemin = np.inf
        for target in rdv:
            self.bool = np.zeros(self.size ** 2)
            self.path = np.zeros(self.size ** 2)
            self.min = np.inf
            self.target = target
            self.explore(mat, init, 0)
            if len(self.res[0]) < sizemin:
                sizemin = len(self.res[0])
            roadres.append(self.res)
        candidat = [roads for roads in roadres if len(roads[0]) == sizemin]
        distmin = np.inf
        resfinal = np.inf
        if len(candidat) > 1:
            for roads in candidat:
                dist = sum(mat[roads[0][j]][roads[0][j + 1]] for j in range(sizemin - 1))
                if dist < distmin:
                    resfinal = roads[0][sizemin - 1]
                    distmin = dist
        else:
            resfinal = candidat[0][0][sizemin - 1]
        return str(self.sommetsList[resfinal