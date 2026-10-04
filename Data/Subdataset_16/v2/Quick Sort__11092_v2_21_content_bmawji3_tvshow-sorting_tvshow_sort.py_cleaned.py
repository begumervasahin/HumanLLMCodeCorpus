
b1 = "tvshow_list_unsorted.txt"
b2 = "tvshow_list_sorted.txt"
b3 = []
with open(b1, "r") as input_file:
    for line in input_file:
        show_name, b4 = line.strip().split('_')
        b3.append((show_name, b4))
b3.sort(b5 = lambda show: (show[1], show[0]))
with open(b2, 'w') as output_file:
    for show in b3:
        output_file.write(f"{show[0]}_{show[1]}\n")