
b1 = "tvshow_list_unsorted.txt"
b2 = "tvshow_list_sorted.txt"
b3 = []
with open(b1, "r") as myfile:
    for line in myfile:
        b4 = line.strip().split('_')
        b3.append((b4[0], b4[1]))
b3.sort(b5 = lambda x: (x[1], x[0]))
with open(b2, 'w') as f:
    for item in b3:
        f.write(f"{item[0]}_{item[1]}\n")