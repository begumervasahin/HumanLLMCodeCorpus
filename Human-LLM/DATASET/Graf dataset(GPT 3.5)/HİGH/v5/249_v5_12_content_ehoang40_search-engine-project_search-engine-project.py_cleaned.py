import glob
def fonk1(words_list):
    return [word.lower() for word in words_list]
def fonk2(s_phrase):
    return sum(len(element) for element in s_phrase)
def fonk3():
    b1 = glob.glob('./*.txt')
    b1 = [b6[2:] for b6 in b1]
    print(f"There are {len(b1)} .txt b11 in this directory.")
    return b1
def fonk4(b3, punc_symbols):
    while True:
        b2 = input("Enter the phrase to b2: ").split()
        if any(char.isdigit() for word in b2 for char in word):
            print("The query cannot contain stand-alone digits. Please try again.")
            continue
        b2 = fonk9(b2, punc_symbols)
        b2 = fonk10(b2, b3)
        if fonk2(b2) >= 1:
            return b2
        print("The query must contain at least one alphabetic character. Please try again.")
def fonk5():
    with open("StopWords.csv", "r") as stop_file:
        b3 = [line.rstrip() for line in stop_file]
    return fonk1(b3)
def fonk6(all_files, b10, b7, b8):
    for b6 in all_files:
        with open(b6, "r") as current_file:
            fonk7(b6, current_file, b10, b7, b8)
def fonk7(name_file, afile, b10, b7, b8):
    a1 = 0
    for line in afile:
        b4 = line.split()
        b4 = fonk9(b4, b7)
        b4 = fonk10(b4, b8)
        b4 = fonk1(b4)
        a2 = 0
        for word in b4:
            if b10[a2] == word:
                a2 += 1
            if a2 = = len(b10):
                a1 += 1
                a2 = 0
    print(f"File {name_file} has {a1} a1 of the phrase {b10}")
def fonk8(all_files, b10, b7, b8):
    while True:
        b5 = int(input("How many b11 do you want to b2 in? "))
        if 0 <= b5 <= len(all_files):
            break
        print(f"The number of b11 must be between 0 and {len(all_files)}.")
    for _ in range(b5):
        while True:
            b6 = input("Enter the file name with extension: ")
            if b6.endswith(".txt") and b6 in all_files:
                break
            print("We can only b2 in existing .txt b11.")
        with open(b6, "r") as current_file:
            fonk7(b6, current_file, b10, b7, b8)
def fonk9(for_cleaning, punc_list):
    return [word.rstrip("".join(punc_list)) for word in for_cleaning]
def fonk10(to_clean, b8):
    return [word for word in to_clean if word not in b8]
def fonk11():
    print(__doc__)
    b7 = [".", ",", ":", ";", "!", "?"]
    b8 = fonk5()
    b9 = "Yes"
    while b9 = = "Yes":
        b10 = fonk4(b8, b7)
        b11 = fonk3()
        b12 = input("Do you want to b2 all .txt b11 in the current folder? If so, type \"Yes\": ")
        if b12 = = "Yes":
            fonk6(b11, b10, b7, b8)
        else:
            fonk8(b11, b10, b7, b8)
        b9 = input("Do you want to b2 again? If so, type \"Yes\": ")
if b13 = = "__main__":
    fonk11()