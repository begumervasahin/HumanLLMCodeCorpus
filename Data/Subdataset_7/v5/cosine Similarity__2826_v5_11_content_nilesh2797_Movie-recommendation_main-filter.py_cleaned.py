import csv
from math import sqrt
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = csv.b1(file)
        return list(b1)
b2 = fonk1('movie-b4.csv')
b3 = b2[0][1:]
b2.pop(0)
b4 = [{b3[i]: float(row[i + 1]) for i in range(len(b3))} for row in b2]
b5 = [row[0] for row in b2]
b6 = fonk1('user_preference.csv')
b7 = {b6[0][i]: float(b6[1][i]) for i in range(len(b6[0]))}
b8 = []
for critic in b4:
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    for movie_name, user_rating in b7.items():
        b14 = critic.get(movie_name)
        if b14 is not None and user_rating != -1:
            b9.append(b14 * user_rating)
            b10.append(b14)
            b11.append(user_rating)
            b12.append(b14 ** 2)
            b13.append(user_rating ** 2)
    b15 = len(b9)
    if b15 * sum(b12) - sum(b10) * sum(b10) != 0 and b15 * sum(b13) - sum(b11) * sum(b11) != 0:
        b8.append((b15 * sum(b9) - sum(b10) * sum(b11)) / (sqrt(b15 * sum(b12) - sum(b10) * sum(b10)) * sqrt(b15 * sum(b13) - sum(b11) * sum(b11))))
    else:
        b8.append(0)
b16 = sorted(zip(b5, b8), key=lambda b10: b10[1], reverse=True)
b17 = {}
for movie_name in b3:
    b18 = []
    b19 = []
    for i, b14 in enumerate(b4):
        if movie_name in b14:
            b18.append(b8[i] * b14[movie_name])
            b19.append(abs(b8[i]))
    if b19:
        b17[movie_name] = sum(b18) / sum(b19)
    else:
        b17[movie_name] = 0
b20 = sorted(b17, key=b17.get, reverse=True)
a1 = 0
for movie_name in b20:
    if b7[movie_name] == -1 and a1 < 3:
        print(movie_name)
        a1 += 1