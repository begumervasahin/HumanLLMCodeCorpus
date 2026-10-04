import numpy as np
class Graph:
    def __init__(self, data):
        self.size = data["nbNoeuds"]
        self.sommetsList = data["nomSommets"]
        self.rdvList = data["nomRdv"]
        self.sommetsIniList = data["nomSommetsInitiaux"]
        self.arcs = data["arcs"]
        self.error_code = self._check_data_consistency(data)
        self.path = np.zeros(self.size ** 2, dtype=int)
        self.visited = np.zeros(self.size ** 2, dtype=bool)
        self.target = 0
        self.min_depth = np.inf
        self.results = []
    def _check_data_consistency(self, data):
        if len(self.sommetsList) != data["nbNoeuds"]:
            return 1
        if len(self.rdvList) != data["nbLieuxRdv"]:
            return 2
        return 0
    def check_error(self):
        return self.error_code
    def mat_graph(self):
        mat = np.full((self.size, self.size), np.inf)
        for arc in self.arcs:
            i = self.pos_sommet(arc["sommetInitial"])
            j = self.pos_sommet(arc["sommetTerminal"])
            mat[i, j] = arc["duree"]
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
        rdv_indices = [self.pos_sommet(c) * self.size + self.pos_sommet(c) for c in self.rdvList]
        min_distance = np.inf
        optimal_rdv_index = None
        for idx, rdv_point in enumerate(rdv_indices):
            if mat_pcd[init, rdv_point] < min_distance:
                min_distance = mat_pcd[init, rdv_point]
                optimal_rdv_index = idx
        return self.rdvList[optimal_rdv_index] if optimal_rdv_index is not None else ""
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
        if depth > self.min_depth:
            return
        self.path[depth] = position
        if position == self.target:
            if self.min_depth == depth:
                self.results.append(np.copy(self.path[:depth + 1]).tolist())
            if self.min_depth > depth:
                self.min_depth = depth
                self.results = [np.copy(self.path[:depth + 1]).tolist()]
            return
        self.visited[position] = True
        for i in range(self.size ** 2):
            if mat[position][i] != np.inf and not self.visited[i]:
                self.explore(mat, i, depth + 1)
        self.visited[position] = False
    def rdv_optimal2(self):
        mat = self.transform(self.mat_graph())
        init = self.pos_sommet(self.sommetsIniList[0]) * self.size + self.pos_sommet(self.sommetsIniList[1])
        rdv_indices = [self.pos_sommet(c) * self.size + self.pos_sommet(c) for c in self.rdvList]
        roadres = []
        min_size = np.inf
        for target in rdv_indices:
            self.visited.fill(False)
            self.path.fill(0)
            self.min_depth = np.inf
            self.target = target
            self.explore(mat, init, 0)
            if len(self.results[0]) < min_size:
                min_size = len(self.results[0])
            roadres.append(self.results)
        candidates = [roads for roads in roadres if len(roads[0]) == min_size]
        min_distance = np.inf
        final_result = None
        if len(candidates) > 1:
            for roads in candidates:
                distance = sum(mat[roads[0][j]][roads[0][j + 1]] for j in range(min_size - 1))
                if distance < min_distance:
                    final_result = roads[0][min_size - 1]
                    min_distance = distance
        else:
            final_result = candidates[0][0][min_size - 1]
        return self.sommetsList[final_result