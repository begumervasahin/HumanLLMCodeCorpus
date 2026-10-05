import csv
from math import sqrt
with open('movie-b4.csv', 'r') as file1:
    b1 = csv.reader(file1)
    b2 = list(b1)
b3 = b2[0][1:]
b2.pop(0)
b4 = []
b5 = []
for item in b2:
    b5.append(item[0])
    b4.append({b3[i]: float(item[i + 1]) for i in range(len(b3))})
with open('user_preference.csv', 'r') as file2:
    b6 = csv.reader(file2)
    b7 = list(b6)
b8 = {b7[0][i]: float(b7[1][i]) for i in range(len(b7[0]))}
b9 = []
for critic in b4:
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    b14 = []
    for movie_name in b8.keys():
        if critic.get(movie_name) is not None and b8[movie_name] != -1:
            b10.append(critic[movie_name] * b8[movie_name])
            b11.append(critic[movie_name])
            b12.append(b8[movie_name])
            b13.append(critic[movie_name] ** 2)
            b14.append(b8[movie_name] ** 2)
    b15 = len(b10)
    if b15 * sum(b13) - sum(b11) * sum(b11) != 0 and b15 * sum(b14) - sum(b12) * sum(b12) != 0:
        b9.append((b15 * sum(b10) - sum(b11) * sum(b12)) / (sqrt(b15 * sum(b13) - sum(b11) * sum(b11)) * sqrt(b15 * sum(b14) - sum(b12) * sum(b12))))
    else:
        b9.append(0)
b16 = sorted(zip(b5, b9), key=lambda b11: b11[1], reverse=True)
b17 = {}
for movie_name in b3:
    b18 = []
    b19 = []
    for i in range(len(b9)):
        if b4[i].get(movie_name) is not None:
            b18.append(b9[i] * b4[i][movie_name])
            b19.append(abs(b9[i]))
    b17[movie_name] = sum(b18) / sum(b19)
b20 = sorted(b17, key=b17.get, reverse=True)
a1 = 0
for movie_name in b20:
    if b8[movie_name] == -1 and a1 < 3:
        print(movie_name)
        a1 += 1