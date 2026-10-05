import random
import pickle
array = []
two_matches = []
three_matches = []
four_matches = []
five_matches = []
six_matches = []
seven_matches = []
win = []
limit = 15
loops = 100
dupes = 0
def end():
    print("One (may contain duplicates):")
    print(len(array))
    print("Two:")
    print(len(two_matches))
    print("Three:")
    print(len(three_matches))
    print("Four:")
    print(len(four_matches))
    print("Five:")
    print(len(five_matches))
    print(five_matches)
    print("Six:")
    print(len(six_matches))
    print(six_matches)
    print("Seven:")
    print(len(seven_matches))
    print(seven_matches)
    print("Win:")
    print(len(win))
    print(win)
    print(dupes, "/", loops, "Duplicates Removed")
    with open("Win.txt", 'wb') as f:
        pickle.dump(win, f)
    with open("Two.txt", 'wb') as f:
        pickle.dump(two_matches, f)
    with open("Three.txt", 'wb') as f:
        pickle.dump(three_matches, f)
    with open("Four.txt", 'wb') as f:
        pickle.dump(four_matches, f)
    with open("Five.txt", 'wb') as f:
        pickle.dump(five_matches, f)
    with open("Six.txt", 'wb') as f:
        pickle.dump(six_matches, f)
    with open("Seven.txt", 'wb') as f:
        pickle.dump(seven_matches, f)
    with open("Fail.txt", 'wb') as f:
        pickle.dump(array, f)
def most_common(lst, lstt):
    occurrences = 0
    most_common_num = max(set(lst), key=lst.count)
    for i in lst:
        if i == most_common_num:
            occurrences += 1
    if occurrences == 1:
        array.append(lstt)
    elif occurrences == 2:
        two_matches.append(lstt)
    elif occurrences == 3:
        three_matches.append(lstt)
    elif occurrences == 4:
        four_matches.append(lstt)
    elif occurrences == 5:
        five_matches.append(lstt)
    elif occurrences == 6:
        six_matches.append(lstt)
    elif occurrences == 7:
        seven_matches.append(lstt)
    elif occurrences == 8:
        win.append(lstt)
    print((len(array)) + (len(two_matches)) + (len(three_matches)) + (len(four_matches)) + (len(five_matches)) + (len(six_matches)) + (len(seven_matches)) + (len(win)))
for _ in range(loops):
    tmp = False
    N = []
    for x in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
        while not tmp:
            globals()[x] = random.randint((limit * -1), limit)
            if ((globals()[x] in N) == False) and ((globals()[x]) < limit):
                N.append(globals()[x])
                tmp = True
        tmp = False
    if ((([a, b, c, d, e, f, g, h, i] in two_matches) == False) and (([a, b, c, d, e, f, g, h, i] in three_matches) == False) and (
            ([a, b, c, d, e, f, g, h, i] in four_matches) == False) and (([a, b, c, d, e, f, g, h, i] in five_matches) == False) and (
            ([a, b, c, d, e, f, g, h, i] in six_matches) == False) and (([a, b, c, d, e, f, g, h, i] in seven_matches) == False) and (
            ([a, b, c, d, e, f, g, h, i] in win) == False)):
        aa = a * a
        bb = b * b
        cc = c * c
        dd = d * d
        ee = e * e
        ff = f * f
        gg = g * g
        hh = h * h
        ii = i * i
        h1 = aa + bb + cc
        h2 = dd + ee + ff
        h3 = gg + hh + ii
        v1 = aa + dd + gg
        v2 = bb + ee + hh
        v3 = cc + ff + ii
        d1 = aa + ee + ii
        d2 = gg + ee + cc
        sq_numbers = [a, b, c, d, e, f, g, h, i]
        answers = [h1, h2, h3, v1, v2, v3, d1, d2]
        most_common(answers, sq_numbers)
    else:
        print("Duplicate Found")
        dupes += 1
end()