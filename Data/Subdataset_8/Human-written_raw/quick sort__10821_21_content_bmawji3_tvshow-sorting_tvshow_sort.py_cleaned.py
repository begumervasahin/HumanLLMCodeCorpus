tv_list = []
with open("tvshow_list_unsorted.txt", "r") as myfile:
    for line in myfile:
        temp_split = line.split('_')
        tv_list.append( (temp_split[0], temp_split[1].strip('\n')) );
tv_list.sort(key=lambda x : (x[1], x[0]))
f = open('tvshow_list_sorted.txt', 'w')
for item in tv_list:
    f.write(str(item) + '\n')
f.close()