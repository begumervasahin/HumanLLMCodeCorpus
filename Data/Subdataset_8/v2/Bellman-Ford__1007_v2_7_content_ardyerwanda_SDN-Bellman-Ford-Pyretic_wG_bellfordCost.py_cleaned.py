def abilene_cost_list():
    huge = 1e30000
    route_table = {}
    route = {}
    for rt in range(1, 12):
        route_table[rt] = {}
        route[rt] = {}
        for u in range(1, 12):
            route_table[rt][u] = {}
            route[u] = {}
            for v in range(1, 12):
                if u == rt:
                    route[u][v] = huge
                    route[u][u] = 0
                elif u == v and v == rt:
                    route[u][v] = 0
                else:
                    route[u][v] = huge
                route_table[rt][u][v] = route[u][v]
    route_table[1][1][2] = 1
    route_table[1][1][4] = 1
    route_table[2][2][1] = route_table[1][1][2]
    route_table[2][2][3] = 1
    route_table[2][2][4] = 1
    route_table[3][3][2] = route_table[2][2][3]
    route_table[3][3][6] = 1
    route_table[4][4][1] = route_table[1][1][4]
    route_table[4][4][2] = route_table[2][2][4]
    route_table[4][4][5] = 1
    route_table[5][5][4] = route_table[4][4][5]
    route_table[5][5][6] = 1
    route_table[5][5][7] = 1
    route_table[6][6][3] = route_table[3][3][6]
    route_table[6][6][5] = route_table[5][5][6]
    route_table[6][6][11] = 1
    route_table[7][7][5] = route_table[5][5][7]
    route_table[7][7][8] = 1
    route_table[7][7][11] = 1
    route_table[8][8][7] = route_table[7][7][8]
    route_table[8][8][9] = 1
    route_table[9][9][8] = route_table[8][8][9]
    route_table[9][9][10] = 1
    route_table[10][10][9] = route_table[9][9][10]
    route_table[10][10][11] = 1
    route_table[11][11][6] = route_table[6][6][11]
    route_table[11][11][7] = route_table[7][7][11]
    route_table[11][11][10] = route_table[10][10][11]
    return route_table
result = abilene_cost_list()
print(result)