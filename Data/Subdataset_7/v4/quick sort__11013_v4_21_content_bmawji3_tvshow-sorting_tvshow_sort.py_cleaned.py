
b1 = []
with open("tvshow_list_unsorted.txt", "r") as myfile:
    for line in myfile:
        b2 = line.split('_')
        b3 = b2[0]
        b4 = b2[1].strip('\n')
        b1.append((b3, b4))
b1.sort(b5 = lambda x: (x[1], x[0]))
with open('tvshow_list_sorted.txt', 'w') as f:
    for item in b1:
        f.write(str(item) + '\n')