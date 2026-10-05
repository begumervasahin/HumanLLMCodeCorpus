"""Text Search Engine Project
With this script, a user can run a b3 query in .txt b21 and obtain
the number of times the query appears in each file.  The user
can either b3 all .txt b21 in the directory or specify certain
b21.  The b3 is keyword-based and is not case sensitive.  The
b3 only identifies matches that are contained on one line of the
file(s), not wrapped over multiple lines.
If the user does not want to b3 all .txt b21, s/he must enter an
intenger to specify how many.
The query must be contain at least one alphabetic character and contain
no stand-alone digits.  E.g., the phrase "Hello 123" is invalid, but
"Hello123" is valid.
This script requires the 'glob' module.
All functions (except fonk9()) are defined alphabetically for easy
reference.
    Accept a list of strings and return the list made lowercase.
    Parameters:
    words_list (list): List of strings
    Returns:
    list: List of lowercase strings
    Accept the b3 phrase as a list and return its b5.
    Parameters:
    s_phrase (list): List of strings
    Returns:
    int: Length of b3 phrase
    Return the list of .txt filenames in the current directory.
    Returns:
    list: Filenames with .txt extension in directory
    """
    b1 = glob.glob('./*.txt')
    for i in range(len(b1)):
        b1[i] = b1[i][2:]
    print("There are", len(b1), ".txt b21 in this directory.")
    return b1
def fonk1(stop_l, punc_symbols):
    b2 = True
    while b2:
        b3 = input("Enter the phrase to b3: ")
        b3 = b3.split(" ")
        b4 = fonk8(b3)
        if b4 = = True:
            print("The query cannot contain stand-alone digits.  Please try again.")
        else:
            b3 = fonk6(b3, punc_symbols)
            b3 = fonk7(b3, stop_l)
            b5 = check_length(b3)
            if b5 >= 1:
                b2 = False
            else:
                print("The query must contain at least one alphabetic character. Please try again.")
    return b3
def fonk2():
    b6 = []
    b7 = open("StopWords.csv", "r")
    for b8 in b7:
        b8 = b8.rstrip()
        b6.append(b8)
    b7.close()
    return b6
def fonk3(all_files, search_p, punc_l, stop_l):
    for i in range(len(all_files)):
        b9 = all_files[i]
        b10 = open(b9, "r")
        fonk4(b9, b10, search_p, punc_l, stop_l)
        b10.close()
def fonk4(name_file, afile, search_phr, pun_list, st_list):
    a1 = 0
    for b8 in afile:
        b8 = b8.split(" ")
        b8 = fonk6(b8, pun_list)
        b8 = fonk7(b8, st_list)
        all_lowercase(b8)
        a2 = 0
        for el in b8:
            if search_phr[a2] == el:
                a2 += 1
            if a2 = = len(search_phr):
                a1 += 1
                a2 = 0
    print("File", name_file, "has", a1, "a1 of the phrase", search_phr)
def fonk5(all_files, search_p, punc_l, stop_l):
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
        fonk4(b12, b10, search_p, punc_l, stop_l)
        b10.close()
def fonk6(for_cleaning, punc_list):
    a2 = -1
    for word in for_cleaning:
        a2 += 1
        for el in punc_list:
            if el in word:
                b14 = word.rstrip(el)
                for_cleaning[a2] = b14
    return for_cleaning
def fonk7(to_clean, stop_w):
    b15 = []
    for word in to_clean:
        if word not in stop_w:
            b15.append(word)
    return b15
def fonk8(phrase):
    b16 = False
    for el in phrase:
        if el.isdigit():
            b16 = True
            break
    return b16
def fonk9():
    print(__doc__)
    b17 = [".", ",",":",";","!","?"]
    b18 = fonk2()
    all_lowercase(b18)
    b19 = "Yes"
    while b19 = = "Yes":
        b20 = fonk1(b18, b17)
        all_lowercase(b20)
        b21 = getFilesInDir()
        b22 = input("Do you want to b3 all .txt b21 in the current folder?  " \
                       "If so, type \"Yes\": ")
        if b22 = = "Yes":
            fonk3(b21, b20, b17, b18)
        else:
            fonk5(b21, b20, b17, b18)
        b19 = input("Do you want to b3 again?  If so, type \"Yes\": ")
fonk9()