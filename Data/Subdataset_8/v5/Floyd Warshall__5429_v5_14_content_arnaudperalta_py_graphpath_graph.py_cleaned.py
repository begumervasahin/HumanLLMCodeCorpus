import numpy as np
class Graph:
    def __init__(self, data):
        self.size = data["nbNoeuds"]
        self.sommets_list = list(data["nomSommets"])
        self.rdv_list = list(data["nomRdv"])
        self.sommets_ini_list = list(data["nomSommetsInitiaux"])
        self.arcs = list(data["arcs"])
        self.error = self.validate_data(data)
        self.path = np.zeros(self.size ** 2)
        self.visited = np.zeros(self.size ** 2)
        self.target = 0
        self.min_depth = np.inf
        self.res = []
    def validate_data(self, data):
        if len(self.sommets_list) != self.size:
            return 1
        elif len(self.rdv_list) != data["nbLieuxRdv"]:
            return 2
        return 0
    def get_vertex_index(self, vertex):
        return self.sommets_list.index(vertex)
    def create_adjacency_matrix(self):
        adjacency_matrix = np.full((self.size, self.size), np.inf)
        for arc in self.arcs:
            start_index = self.get_vertex_index(arc["sommetInitial"])
            end_index = self.get_vertex_index(arc["sommetTerminal"])
            adjacency_matrix[start_index, end_index] = arc["duree"]
        return adjacency_matrix
    def transform_to_pair_matrix(self, matrix):
        pair_matrix = np.full((self.size ** 2, self.size ** 2), np.inf)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    for l in range(self.size):
                        if i == k and j == l:
                            pair_matrix[i * self.size + j, k * self.size + l] = np.inf
                        elif i == k:
                            pair_matrix[i * self.size + j, k * self.size + l] = matrix[j, l]
                        elif j == l:
                            pair_matrix[i * self.size + j, k * self.size + l] = matrix[i, k]
        return pair_matrix
    def find_optimal_rdv(self):
        shortest_path_matrix = self.calculate_shortest_path(self.transform_to_pair_matrix(self.create_adjacency_matrix()))
        initial_vertex = self.get_vertex_index(self.sommets_ini_list[0]) * self.size + self.get_vertex_index(self.sommets_ini_list[1])
        rdv_indices = [self.get_vertex_index(vertex) * self.size + self.get_vertex_index(vertex) for vertex in self.rdv_list]
        shortest_distance = np.inf
        final_rdv_index = np.inf
        for i in range(len(rdv_indices)):
            if shortest_path_matrix[initial_vertex, rdv_indices[i]] < shortest_distance:
                shortest_distance = shortest_path_matrix[initial_vertex, rdv_indices[i]]
                final_rdv_index = i
        if final_rdv_index != np.inf:
            return str(self.rdv_list[final_rdv_index])
        else:
            return ""
    def calculate_shortest_path(self, matrix):
        for i in range(self.size ** 2):
            matrix[i, i] = 0
        for k in range(self.size ** 2):
            for i in range(self.size ** 2):
                for j in range(self.size ** 2):
                    matrix[i, j] = min(matrix[i, j], matrix[i, k] + matrix[k, j])
        return matrix
    def explore_paths(self, matrix, position, depth):
        if depth > self.min_depth:
            return
        self.path[depth] = position
        if position == self.target:
            if self.min_depth == depth:
                self.res.append(np.copy(self.path[0:depth + 1]).astype(int).tolist())
            if self.min_depth > depth:
                self.min_depth = depth
                self.res = [np.copy(self.path[0:depth + 1]).astype(int).tolist()]
            return
        self.visited[position] = 1
        for i in range(self.size ** 2):
            if matrix[position][i] == np.inf or self.visited[i] == 1:
                continue
            self.explore_paths(matrix, i, depth + 1)
        self.visited[position] = 0
        return
    def find_optimal_rdv_alternate(self):
        pair_matrix = self.transform_to_pair_matrix(self.create_adjacency_matrix())
        initial_vertex = self.get_vertex_index(self.sommets_ini_list[0]) * self.size + self.get_vertex_index(self.sommets_ini_list[1])
        rdv_indices = [self.get_vertex_index(vertex) * self.size + self.get_vertex_index(vertex) for vertex in self.rdv_list]
        road_results = []
        min_path_length = np.inf
        for i in range(len(rdv_indices)):
            self.visited = np.zeros(self.size ** 2)
            self.path = np.zeros(self.size ** 2)
            self.min_depth = np.inf
            self.target = rdv_indices[i]
            self.explore_paths(pair_matrix, initial_vertex, 0)
            if len(self.res[0]) < min_path_length:
                min_path_length = len(self.res[0])
            road_results.append(self.res)
        candidate_paths = []
        for i in range(len(road_results)):
            if len(road_results[i][0]) == min_path_length:
                candidate_paths.append(road_results[i])
        min_distance = np.inf
        final_rdv_index = np.inf
        if len(candidate_paths) > 1:
            for i in range(len(candidate_paths)):
                total_distance = 0
                for u in range(len(candidate_paths[i])):
                    for j in range(min_path_length - 1):
                        total_distance += pair_matrix[candidate_paths[i][u][j]][candidate_paths[i][u][j + 1]]
                if total_distance < min_distance:
                    final_rdv_index = candidate_paths[i][0][min_path_length - 1]
                    min_distance = total_distance
        else:
            final_rdv_index = candidate_paths[0][0][min_path_length - 1]
        return str(self.sommets_list[(final_rdv_index