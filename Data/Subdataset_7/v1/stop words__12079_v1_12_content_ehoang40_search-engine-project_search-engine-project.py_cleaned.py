import glob
def fonk1(words_list):
    return [word.lower() for word in words_list]
def fonk2(s_phrase):
    return sum(len(word) for word in s_phrase)
def fonk3():
    b1 = glob.glob('./*.txt')
    print("There are", len(b1), ".txt b9 in this directory.")
    return b1
def fonk4(stop_l, punc_symbols):
    while True:
        b2 = input("Enter the phrase to b2: ").split()
        if any(char.isdigit() for word in b2 for char in word):
            print("The query cannot contain stand-alone digits. Please try again.")
            continue
        b2 = fonk9(b2, punc_symbols)
        b2 = fonk10(b2, stop_l)
        if fonk2(b2) >= 1:
            break
        print("The query must contain at least one alphabetic character. Please try again.")
    return b2
def fonk5():
    with open("StopWords.csv", "r") as stop_file:
        return [line.strip() for line in stop_file]
def fonk6(all_files, search_p, punc_l, stop_l):
    for b5 in all_files:
        with open(b5, "r") as current_file:
            fonk7(b5, current_file, search_p, punc_l, stop_l)
def fonk7(name_file, afile, search_phr, pun_list, st_list):
    a1 = 0
    for line in afile:
        b3 = line.split()
        b3 = fonk9(b3, pun_list)
        b3 = fonk10(b3, st_list)
        b3 = fonk1(b3)
        a2 = 0
        for word in b3:
            if search_phr[a2] == word:
                a2 += 1
                if a2 = = len(search_phr):
                    a1 += 1
                    a2 = 0
    print(f"File {name_file} has {a1} a1 of the phrase {search_phr}")
def fonk8(all_files, search_p, punc_l, stop_l):
    while True:
        b4 = int(input(f"How many b9 do you want to b2 in? (0 to {len(all_files)}) "))
        if 0 <= b4 <= len(all_files):
            break
        print("Invalid input. Please enter a number between 0 and", len(all_files))
    for _ in range(b4):
        while True:
            b5 = input("Enter the file name with extension: ")
            if b5.endswith(".txt") and b5 in all_files:
                break
            print("Invalid file name. Please enter a valid .txt file in the directory.")
        with open(b5, "r") as current_file:
            fonk7(b5, current_file, search_p, punc_l, stop_l)
def fonk9(for_cleaning, punc_list):
    return [word.rstrip("".join(punc_list)) for word in for_cleaning]
def fonk10(to_clean, stop_w):
    return [word for word in to_clean if word not in stop_w]
def fonk11():
    print(__doc__)
    b6 = [".", ",", ":", ";", "!", "?"]
    b7 = fonk5()
    b7 = fonk1(b7)
    while True:
        b8 = fonk4(b7, b6)
        b8 = fonk1(b8)
        b9 = fonk3()
        b10 = input("Do you want to b2 all .txt b9 in the current folder? (Yes/No): ")
        if b10.lower() == "yes":
            fonk6(b9, b8, b6, b7)
        else:
            fonk8(b9, b8, b6, b7)
        b10 = input("Do you want to b2 again? (Yes/No): ")
        if b10.lower() != "yes":
            break
if b11 = = "__main__":
    fonk11()