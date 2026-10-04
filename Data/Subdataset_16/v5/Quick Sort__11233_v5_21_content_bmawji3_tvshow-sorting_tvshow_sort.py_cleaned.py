def fonk1(filename):
    b1 = []
    with open(filename, "r") as file:
        for line in file:
            show_name, b2 = line.strip().split('_')
            b1.append((show_name, b2))
    return b1
def fonk2(filename, b1):
    with open(filename, "w") as file:
        for show_name, b2 in b1:
            file.write(f"{show_name}_{b2}\n")
def fonk3():
    b3 = "tvshow_list_unsorted.txt"
    b4 = "tvshow_list_sorted.txt"
    b1 = fonk1(b3)
    b1.sort(b5 = lambda show: (show[1], show[0]))
    fonk2(b4, b1)
if b6 = = "__main__":
    fonk3()