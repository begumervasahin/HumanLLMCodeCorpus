import glob
def fonk1(words_list):
    for i in range(len(words_list)):
        words_list[i] = words_list[i].lower()
    return words_list
def fonk2(s_phrase):
    a1 = 0
    for element in s_phrase:
        for char in element:
            a1 += 1
    return a1
def fonk3():
    b1 = glob.glob('./*.txt')
    for i in range(len(b1)):
        b1[i] = b1[i][2:]
    print("There are", len(b1), ".txt b21 in this directory.")
    return b1
def fonk4(stop_l, punc_symbols):
    b2 = True
    while b2:
        b3 = input("Enter the phrase to b3: ")
        b3 = b3.split(" ")
        b4 = fonk11(b3)
        if b4 = = True:
            print("The query cannot contain stand-alone digits. Please try again.")
        else:
            b3 = fonk9(b3, punc_symbols)
            b3 = fonk10(b3, stop_l)
            b5 = fonk2(b3)
            if b5 >= 1:
                b2 = False
            else:
                print("The query must contain at least one alphabetic character. Please try again.")
    return b3
def fonk5():
    b6 = []
    b7 = open("StopWords.csv", "r")
    for b8 in b7:
        b8 = b8.rstrip()
        b6.append(b8)
    b7.close()
    return b6
def fonk6(all_files, search_p, punc_l, stop_l):
    for i in range(len(all_files)):
        b9 = all_files[i]
        b10 = open(b9, "r")
        fonk7(b9, b10, search_p, punc_l, stop_l)
        b10.close()
def fonk7(name_file, afile, search_phr, pun_list, st_list):
    a2 = 0
    for b8 in afile:
        b8 = b8.split(" ")
        b8 = fonk9(b8, pun_list)
        b8 = fonk10(b8, st_list)
        fonk1(b8)
        a3 = 0
        for el in b8:
            if search_phr[a3] == el:
                a3 += 1
            if a3 = = len(search_phr):
                a2 += 1
                a3 = 0
    print("File", name_file, "has", a2, "a2 of the phrase", search_phr)
def fonk8(all_files, search_p, punc_l, stop_l):
    while True:
        b11 = int(input("How many b21 do you want to b3 in? "))
        if b11 < 0 or b11 > len(all_files):
            print("The number of b21 must be between 0 and", len(all_files), ".")
        else:
            break
    for i in range(b11):
        b2 = True
        while b2:
            b12 = input("Enter the file name with extension: ")
            b13 = list(b12)
            if b13[len(b13)-1]=="t" and \
               b13[len(b13)-2]=="x" and \
               b13[len(b13)-3]=="t" and \
               b13[len(b13)-4]=="." and \
               b12 in all_files:
                break
            else:
                print("We can only b3 in existing .txt b21.")
        b10 = open(b12, "r")
        fonk7(b12, b10, search_p, punc_l, stop_l)
        b10.close()
def fonk9(for_cleaning, punc_list):
    a3 = -1
    for word in for_cleaning:
        a3 += 1
        for el in punc_list:
            if el in word:
                b14 = word.rstrip(el)
                for_cleaning[a3] = b14
    return for_cleaning
def fonk10(to_clean, stop_w):
    b15 = []
    for word in to_clean:
        if word not in stop_w:
            b15.append(word)
    return b15
def fonk11(phrase):
    b16 = False
    for el in phrase:
        if el.isdigit():
            b16 = True
            break
    return b16
def fonk12():
    print(__doc__)
    b17 = [".", ",", ":", ";", "!", "?"]
    b18 = fonk5()
    fonk1(b18)
    b19 = "Yes"
    while b19 = = "Yes":
        b20 = fonk4(b18, b17)
        fonk1(b20)
        b21 = fonk3()
        b22 = input("Do you want to b3 all .txt b21 in the current folder?  " \
                       "If so, type \"Yes\": ")
        if b22 = = "Yes":
            fonk6(b21, b20, b17, b18)
        else:
            fonk8(b21, b20, b17, b18)
        b19 = input("Do you want to b3 again?  If so, type \"Yes\": ")
fonk12()