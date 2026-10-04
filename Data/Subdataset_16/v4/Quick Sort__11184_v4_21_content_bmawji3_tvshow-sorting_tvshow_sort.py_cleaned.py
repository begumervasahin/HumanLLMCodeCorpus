
b1 = []
with open("tvshow_list_unsorted.txt", "r") as myfile:
    for line in myfile:
        b2 = line.split('_')
        b1.append((b2[0], b2[1].strip('\n')))
b1.sort(b3 = lambda x: (x[1], x[0]))
with open('tvshow_list_sorted.txt', 'w') as sorted_file:
    for item in b1:
        sorted_file.write(f"{item[0]}_{item[1]}\n")