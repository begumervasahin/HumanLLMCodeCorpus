def fonk1(b16, b1):
    return b1 = = len(b16)
def fonk2(b11, b15, b16, b1, b6):
    if fonk1(b16, b1):
        return True
    for b4 in range(len(b11)):
        if b11[b4]:
            b2 = False
            b3 = b11[b4][0]
            for j in range(b6):
                if all(b3[0] != pot[0] for pot in b15[j]) and \
                   (all(b3[-1] != conf[-1] for conf in b15[j]) or \
                   (sum(p[-1] == 'f' for p in b15[j]) < 2 and b3[-1] == 'f')):
                    b15[j].append(b3)
                    b11[b4].remove(b3)
                    b16.add(b3)
                    b2 = True
                    if fonk2(b11, b15, b16, b1, b6):
                        return True
                    if b4 = = 0:
                        return False
                    b15[j].remove(b3)
                    b11[b4].insert(0, b3)
                    b16.remove(b3)
                    b2 = False
            if not b2:
                return False
if b5 = = '__main__':
    with open("input.txt", "r") as file_input, open("output.txt", "w") as file_output:
        if not file_input:
            file_output.write('No')
            exit()
        b6 = int(file_input.readline().strip())
        b7 = int(file_input.readline().strip())
        b8 = []
        for b4 in range(b7):
            b9 = file_input.readline().strip().split(',')
            b9 = [str(b4) + x for x in b9]
            b8.append(b9)
        b10 = True
        b11 = [[] for _ in range(len(b8))]
        b12 = {'AFC': [], 'CAF': [], 'CONCACAF': [], 'CONMEBOL': [], 'OFC': [], 'UEFA': []}
        for b4 in range(6):
            b9 = file_input.readline().strip().replace(':', ',').split(',')
            b12[b9[0]] = b9[1:] if b9[1] != 'None' else []
        for b4 in range(len(b8)):
            for j in range(len(b8[b4])):
                for confederation, teams in b12.items():
                    if b8[b4][j][1:] in teams:
                        b11[b4].append(b8[b4][j] + confederation[0])
        b13 = list(map(len, b8))
        b14 = list(map(len, b12.values()))
        if any(b6 < x for x in b13) or \
           any(b6 < x for x in b14[:-1]) or \
           (2 * b6 < b14[-1]):
            b10 = False
        b15 = []
        b1 = sum(b13)
        if b10:
            b15 = [[] for _ in range(b6)]
            b16 = set()
            fonk2(b11, b15, b16, b1, b6)
            file_output.write('Yes' + '\n')
            b17 = [[b3[1:-1] for b3 in group] if group else ['None'] for group in b15]
            for b9 in b17:
                file_output.write(','.join(b9) + '\n')
        else:
            file_output.write('No')