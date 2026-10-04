def read_tv_show_list(filename):
    tv_list = []
    with open(filename, "r") as file:
        for line in file:
            show_name, show_year = line.strip().split('_')
            tv_list.append((show_name, show_year))
    return tv_list
def write_sorted_tv_show_list(filename, tv_list):
    with open(filename, "w") as file:
        for show_name, show_year in tv_list:
            file.write(f"{show_name}_{show_year}\n")
def main():
    input_filename = "tvshow_list_unsorted.txt"
    output_filename = "tvshow_list_sorted.txt"
    tv_list = read_tv_show_list(input_filename)
    tv_list.sort(key=lambda show: (show[1], show[0]))
    write_sorted_tv_show_list(output_filename, tv_list)
if __name__ == "__main__":
    main()