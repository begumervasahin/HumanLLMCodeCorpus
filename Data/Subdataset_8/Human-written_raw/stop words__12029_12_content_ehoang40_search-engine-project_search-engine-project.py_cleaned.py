"""Text Search Engine Project
With this script, a user can run a search query in .txt files and obtain
the number of times the query appears in each file.  The user
can either search all .txt files in the directory or specify certain
files.  The search is keyword-based and is not case sensitive.  The
search only identifies matches that are contained on one line of the
file(s), not wrapped over multiple lines.
If the user does not want to search all .txt files, s/he must enter an
intenger to specify how many.
The query must be contain at least one alphabetic character and contain
no stand-alone digits.  E.g., the phrase "Hello 123" is invalid, but
"Hello123" is valid.
This script requires the 'glob' module.
All functions (except main()) are defined alphabetically for easy
reference.
    Accept a list of strings and return the list made lowercase.
    Parameters:
    words_list (list): List of strings
    Returns:
    list: List of lowercase strings
    Accept the search phrase as a list and return its length.
    Parameters:
    s_phrase (list): List of strings
    Returns:
    int: Length of search phrase
    Return the list of .txt filenames in the current directory.
    Returns:
    list: Filenames with .txt extension in directory
    """
    file_names = glob.glob('./*.txt')
    for i in range(len(file_names)):
        file_names[i] = file_names[i][2:]
    print("There are", len(file_names), ".txt files in this directory.")
    return file_names
def get_phrase(stop_l, punc_symbols):
    invalid_input = True
    while invalid_input:
        search = input("Enter the phrase to search: ")
        search = search.split(" ")
        contains_digit = test_for_digits(search)
        if contains_digit == True:
            print("The query cannot contain stand-alone digits.  Please try again.")
        else:
            search = remove_punctuation(search, punc_symbols)
            search = remove_stopwords(search, stop_l)
            length = check_length(search)
            if length >= 1:
                invalid_input = False
            else:
                print("The query must contain at least one alphabetic character. Please try again.")
    return search
def get_stop_words():
    stop_list = []
    stop_file = open("StopWords.csv", "r")
    for l in stop_file:
        l = l.rstrip()
        stop_list.append(l)
    stop_file.close()
    return stop_list
def process_all(all_files, search_p, punc_l, stop_l):
    for i in range(len(all_files)):
        infile = all_files[i]
        current_file = open(infile, "r")
        process_file(infile, current_file, search_p, punc_l, stop_l)
        current_file.close()
def process_file(name_file, afile, search_phr, pun_list, st_list):
    occurrences = 0
    for l in afile:
        l = l.split(" ")
        l = remove_punctuation(l, pun_list)
        l = remove_stopwords(l, st_list)
        all_lowercase(l)
        index = 0
        for el in l:
            if search_phr[index] == el:
                index += 1
            if index == len(search_phr):
                occurrences += 1
                index = 0
    print("File", name_file, "has", occurrences, "occurrences of the phrase", search_phr)
def process_some(all_files, search_p, punc_l, stop_l):
    while True:
        number_files = int(input("How many files do you want to search in? "))
        if number_files < 0 or number_files > len(all_files):
            print("The number of files must be between 0 and", len(all_files), ".")
        else:
            break
    for i in range(number_files):
        invalid_input = True
        while invalid_input:
            file_name = input("Enter the file name with extension: ")
            file_name_list = list(file_name)
            if file_name_list[len(file_name_list)-1]=="t" and \
               file_name_list[len(file_name_list)-2]=="x" and \
               file_name_list[len(file_name_list)-3]=="t" and \
               file_name_list[len(file_name_list)-4]=="." and \
               file_name in all_files:
                break
            else:
                print("We can only search in existing .txt files.")
        current_file = open(file_name, "r")
        process_file(file_name, current_file, search_p, punc_l, stop_l)
        current_file.close()
def remove_punctuation(for_cleaning, punc_list):
    index = -1
    for word in for_cleaning:
        index += 1
        for el in punc_list:
            if el in word:
                no_punc_word = word.rstrip(el)
                for_cleaning[index] = no_punc_word
    return for_cleaning
def remove_stopwords(to_clean, stop_w):
    clean = []
    for word in to_clean:
        if word not in stop_w:
            clean.append(word)
    return clean
def test_for_digits(phrase):
    digit = False
    for el in phrase:
        if el.isdigit():
            digit = True
            break
    return digit
def main():
    print(__doc__)
    punctuation = [".", ",",":",";","!","?"]
    stop_words = get_stop_words()
    all_lowercase(stop_words)
    choice1 = "Yes"
    while choice1 == "Yes":
        search_phrase = get_phrase(stop_words, punctuation)
        all_lowercase(search_phrase)
        files = getFilesInDir()
        choice2 = input("Do you want to search all .txt files in the current folder?  " \
                       "If so, type \"Yes\": ")
        if choice2 == "Yes":
            process_all(files, search_phrase, punctuation, stop_words)
        else:
            process_some(files, search_phrase, punctuation, stop_words)
        choice1 = input("Do you want to search again?  If so, type \"Yes\": ")
main()