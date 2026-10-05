import math
def is_full(visited):
    return pots_num_sum == len(visited)
def dfs(current, result, visited):
    if is_full(visited):
        return True
    for i in range(len(current)):
        if current[i]:
            flag = False
            team = current[i][0]
            for j in range(group_num):
                if all(team[0] != p[0] for p in result[j]) and \
                   (all(team[-1] != q[-1] for q in result[j]) or \
                   (sum(w[-1] == 'f' for w in result[j]) < 2 and team[-1] =='f')):
                    result[j].append(team)
                    current[i].remove(team)
                    visited.add(team)
                    flag = True
                    if dfs(current, result, visited):
                        return True
                    if i == 0:
                        return False
                    result[j].remove(team)
                    current[i].insert(0, team)
                    visited.remove(team)
                    flag = False
            if not flag:
                return False
if __name__ == '__main__':
    file_input = open("input.txt", "r")
    file_output = open("output.txt", "w")
    if not file_input:
        file_output.write('No')
    group_num = int(file_input.readline().strip())
    pot_num = int(file_input.readline().strip())
    pots = []
    for i in range(pot_num):
        line = file_input.readline().strip().split(',')
        line = [str(i) + x for x in line]
        pots.append(line)
    if_solution = True
    current = [[] for _ in range(len(pots))]
    confederations = []
    afc, caf, concacaf, conmebol, ofc, uefa = [], [], [], [], [], []
    for i in range(6):
        line = file_input.readline().strip().replace(':', ',').split(',')
        if line[0] == 'AFC':
            afc = line[1:]
        elif line[0] == 'CAF':
            caf = line[1:]
        elif line[0] == 'CONCACAF':
            concacaf = line[1:]
        elif line[0] == 'CONMEBOL':
            conmebol = line[1:]
        elif line[0] == 'OFC':
            ofc = line[1:]
        elif line[0] == 'UEFA':
            uefa = line[1:]
    for i in range(len(pots)):
        for j in range(len(pots[i])):
            if pots[i][j][1:] in afc:
                current[i].append(pots[i][j] + 'a')
            elif pots[i][j][1:] in caf:
                current[i].append(pots[i][j] + 'b')
            elif pots[i][j][1:] in concacaf:
                current[i].append(pots[i][j] + 'c')
            elif pots[i][j][1:] in conmebol:
                current[i].append(pots[i][j] + 'd')
            elif pots[i][j][1:] in ofc:
                current[i].append(pots[i][j] + 'e')
            elif pots[i][j][1:] in uefa:
                current[i].append(pots[i][j] + 'f')
    confederations.extend([afc, caf, concacaf, conmebol, ofc, uefa])
    pots_num = list(map(len, pots))
    confederations_num = list(map(len, confederations))
    if any(group_num < x for x in pots_num) or \
       any(group_num < x for x in confederations_num[:-1]) or \
       (2 * group_num < confederations_num[-1]):
        if_solution = False
    result = []
    pots_num_sum = sum(pots_num)
    if if_solution:
        result = [[] for _ in range(group_num)]
        visited = set()
        dfs(current, result, visited)
        file_output.write('Yes' + '\n')
        answer = [[y[1:-1] for y in x ] for x in result]
        for line in answer:
            if line:
                file_output.write(','.join(line) + '\n')
            else:
                file_output.write('None'+ '\n')
    else:
        file_output.write('No')
    file_input.close()
    file_output.close()