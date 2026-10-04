
INPUT_FILE_PATH = "tvshow_list_unsorted.txt"
OUTPUT_FILE_PATH = "tvshow_list_sorted.txt"
def read_tv_shows(file_path):
    tv_shows = []
    with open(file_path, "r") as file:
        for line in file:
            show_name, show_detail = line.strip().split('_')
            tv_shows.append((show_name, show_detail))
    return tv_shows
def write_tv_shows(file_path, tv_shows):
    with open(file_path, 'w') as file:
        for show in tv_shows:
            file.write(f"{show[0]}_{show[1]}\n")
def main():
    tv_shows = read_tv_shows(INPUT_FILE_PATH)
    tv_shows.sort(key=lambda show: (show[1], show[0]))
    write_tv_shows(OUTPUT_FILE_PATH, tv_shows)
if __name__ == "__main__":
    main()