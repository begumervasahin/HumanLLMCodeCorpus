
tv_list = []
with open("tvshow_list_unsorted.txt", "r") as myfile:
    for line in myfile:
        temp_split = line.split('_')
        show_title = temp_split[0]
        show_genre = temp_split[1].strip('\n')
        tv_list.append((show_title, show_genre))
tv_list.sort(key=lambda x: (x[1], x[0]))
with open('tvshow_list_sorted.txt', 'w') as f:
    for item in tv_list:
        f.write(str(item) + '\n')