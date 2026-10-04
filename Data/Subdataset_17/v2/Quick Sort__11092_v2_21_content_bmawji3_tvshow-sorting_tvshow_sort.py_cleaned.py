
input_file_path = "tvshow_list_unsorted.txt"
output_file_path = "tvshow_list_sorted.txt"
tv_shows = []
with open(input_file_path, "r") as input_file:
    for line in input_file:
        show_name, show_detail = line.strip().split('_')
        tv_shows.append((show_name, show_detail))
tv_shows.sort(key=lambda show: (show[1], show[0]))
with open(output_file_path, 'w') as output_file:
    for show in tv_shows:
        output_file.write(f"{show[0]}_{show[1]}\n")