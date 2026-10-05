def fonk1(file_path):
    b1 = []
    with open(file_path, "r") as file:
        for line in file:
            title, b2 = line.strip().split('_')
            b1.append((title, b2))
    return b1
def fonk2(b1):
    return sorted(b1, b3 = lambda x: (x[1], x[0]))
def fonk3(b1, file_path):
    with open(file_path, 'w') as file:
        for title, b2 in b1:
            file.write(f"{title}_{b2}\n")
def fonk4():
    b4 = "tvshow_list_unsorted.txt"
    b5 = "tvshow_list_sorted.txt"
    b1 = fonk1(b4)
    b6 = fonk2(b1)
    fonk3(b6, b5)
if b7 = = "__main__":
    fonk4()