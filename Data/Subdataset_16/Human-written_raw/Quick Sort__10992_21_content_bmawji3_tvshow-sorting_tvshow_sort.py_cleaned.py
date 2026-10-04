b1 = []
with open("tvshow_list_unsorted.txt", "r") as myfile:
    for line in myfile:
        b2 = line.split('_')
        b1.append( (b2[0], b2[1].strip('\n')) );
b1.sort(b3 = lambda x : (x[1], x[0]))
b4 = open('tvshow_list_sorted.txt', 'w')
for item in b1:
    b4.write(str(item) + '\n')
b4.close()