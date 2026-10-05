
tv_shows = []
with open("tvshow_list_unsorted.txt", "r") as file:
    for line in file:
        show_name, season_number = line.strip().split('_')
        tv_shows.append((show_name, season_number))
tv_shows.sort(key=lambda x: (x[1], x[0]))
with open('tvshow_list_sorted.txt', 'w') as output_file:
    for show in tv_shows:
        output_file.write(f"{show}\n")