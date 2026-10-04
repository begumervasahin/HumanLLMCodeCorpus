
b1 = "tvshow_list_unsorted.txt"
b2 = "tvshow_list_sorted.txt"
def fonk1(file_path):
    b3 = []
    with open(file_path, "r") as file:
        for line in file:
            show_name, b4 = line.strip().split('_')
            b3.append((show_name, b4))
    return b3
def fonk2(file_path, b3):
    with open(file_path, 'w') as file:
        for show in b3:
            file.write(f"{show[0]}_{show[1]}\n")
def fonk3():
    b3 = fonk1(b1)
    b3.sort(b5 = lambda show: (show[1], show[0]))
    fonk2(b2, b3)
if b6 = = "__main__":
    fonk3()