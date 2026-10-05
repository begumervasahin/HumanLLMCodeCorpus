def read_tv_show_list(file_path):
    tv_list = []
    with open(file_path, "r") as file:
        for line in file:
            title, genre = line.strip().split('_')
            tv_list.append((title, genre))
    return tv_list
def sort_tv_show_list(tv_list):
    return sorted(tv_list, key=lambda x: (x[1], x[0]))
def write_tv_show_list(tv_list, file_path):
    with open(file_path, 'w') as file:
        for title, genre in tv_list:
            file.write(f"{title}_{genre}\n")
def main():
    unsorted_file_path = "tvshow_list_unsorted.txt"
    sorted_file_path = "tvshow_list_sorted.txt"
    tv_list = read_tv_show_list(unsorted_file_path)
    sorted_tv_list = sort_tv_show_list(tv_list)
    write_tv_show_list(sorted_tv_list, sorted_file_path)
if __name__ == "__main__":
    main()