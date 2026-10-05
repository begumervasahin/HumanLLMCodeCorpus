
b1 = []
with open("tvshow_list_unsorted.txt", "r") as file:
    for line in file:
        show_name, b2 = line.strip().split('_')
        b1.append((show_name, b2))
b1.sort(b3 = lambda x: (x[1], x[0]))
with open('tvshow_list_sorted.txt', 'w') as output_file:
    for show_name, b2 in b1:
        output_file.write(f"{show_name}_{b2}\n")