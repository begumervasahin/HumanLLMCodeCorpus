
input_file = "tvshow_list_unsorted.txt"
output_file = "tvshow_list_sorted.txt"
tv_list = []
with open(input_file, "r") as myfile:
    for line in myfile:
        temp_split = line.strip().split('_')
        tv_list.append((temp_split[0], temp_split[1]))
tv_list.sort(key=lambda x: (x[1], x[0]))
with open(output_file, 'w') as f:
    for item in tv_list:
        f.write(f"{item[0]}_{item[1]}\n")