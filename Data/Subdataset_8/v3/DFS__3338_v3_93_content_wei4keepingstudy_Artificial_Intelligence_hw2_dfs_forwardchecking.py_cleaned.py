def is_full(visited):
    return pots_num_sum == len(visited)
def dfs(current, result, visited):
    if is_full(visited):
        return True
    for i, cur in enumerate(current):
        if cur:
            flag = False
            team = cur[0]
            for j in range(group_num):
                if all(team[0] != p[0] for p in result[j]) and \
                   (all(team[-1] != q[-1] for q in result[j]) or \
                   (sum(w[-1] == 'f' for w in result[j]) < 2 and team[-1] == 'f')):
                    result[j].append(team)
                    cur.remove(team)
                    visited.add(team)
                    flag = True
                    if dfs(current, result, visited):
                        return True
                    if i == 0:
                        return False
                    result[j].remove(team)
                    cur.insert(0, team)
                    visited.remove(team)
                    flag = False
            if not flag:
                return False
if __name__ == '__main__':
    with open("input.txt", "r") as file_input:
        file_output = open("output.txt", "w")
        if not file_input:
            file_output.write('No')
        group_num = int(file_input.readline().strip())
        pot_num = int(file_input.readline().strip())
        pots = [file_input.readline().strip().split(',') for _ in range(pot_num)]
        if_solution = True
        current = [[] for _ in range(len(pots))]
        confederations = []
        afc, caf, concacaf, conmebol, ofc, uefa = [], [], [], [], [], []
        for _ in range(6):
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
        for i, pot in enumerate(pots):
            for j, team in enumerate(pot):
                conf = [afc, caf, concacaf, conmebol, ofc, uefa]
                for k, confed in enumerate(conf):
                    if team[1:] in confed:
                        current[i].append(team + chr(97 + k))
                        break
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
            answer = [[y[1:-1] for y in x] for x in result]
            for line in answer:
                file_output.write(','.join(line) + '\n' if line else 'None\n')
        else:
            file_output.write('No')
        file_output.close()