import glob
def fonk1(words_list):
    return [word.lower() for word in words_list]
def fonk2(phrase):
    return sum(len(word) for word in phrase)
def fonk3():
    b1 = glob.glob('./*.txt')
    print("There are", len(b1), ".txt b9 in this directory.")
    return b1
def fonk4(b7, b6):
    while True:
        b2 = input("Enter the phrase to search: ").split()
        if any(char.isdigit() for word in b2 for char in word):
            print("The query cannot contain stand-alone digits. Please try again.")
            continue
        b2 = fonk9(b2, b6)
        b2 = fonk10(b2, b7)
        if fonk2(b2) >= 1:
            break
        print("The query must contain at least one alphabetic character. Please try again.")
    return b2
def fonk5():
    with open("StopWords.csv", "r") as stop_words_file:
        return [line.strip() for line in stop_words_file]
def fonk6(all_files, b8, b6, b7):
    for b5 in all_files:
        with open(b5, "r") as current_file:
            fonk7(b5, current_file, b8, b6, b7)
def fonk7(b5, file_object, b8, b6, b7):
    a1 = 0
    for line in file_object:
        b3 = line.split()
        b3 = fonk9(b3, b6)
        b3 = fonk10(b3, b7)
        b3 = fonk1(b3)
        a2 = 0
        for word in b3:
            if b8[a2] == word:
                a2 += 1
                if a2 = = len(b8):
                    a1 += 1
                    a2 = 0
    print(f"File {b5} has {a1} a1 of the phrase {b8}")
def fonk8(all_files, b8, b6, b7):
    while True:
        b4 = int(input(f"How many b9 do you want to search in? (0 to {len(all_files)}) "))
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
            fonk7(b5, current_file, b8, b6, b7)
def fonk9(words_list, b6):
    return [word.rstrip("".join(b6)) for word in words_list]
def fonk10(words_list, b7):
    return [word for word in words_list if word not in b7]
def fonk11():
    print(__doc__)
    b6 = [".", ",", ":", ";", "!", "?"]
    b7 = fonk5()
    b7 = fonk1(b7)
    while True:
        b8 = fonk4(b7, b6)
        b8 = fonk1(b8)
        b9 = fonk3()
        b10 = input("Do you want to search all .txt b9 in the current folder? (Yes/No): ")
        if b10.lower() == "yes":
            fonk6(b9, b8, b6, b7)
        else:
            fonk8(b9, b8, b6, b7)
        b10 = input("Do you want to search again? (Yes/No): ")
        if b10.lower() != "yes":
            break
if b11 = = "__main__":
    fonk11()