import glob
def all_lowercase(words_list):
    return [word.lower() for word in words_list]
def check_length(s_phrase):
    return sum(len(word) for word in s_phrase)
def get_files_in_dir():
    file_names = glob.glob('./*.txt')
    print("There are", len(file_names), ".txt files in this directory.")
    return file_names
def get_phrase(stop_l, punc_symbols):
    while True:
        search = input("Enter the phrase to search: ").split()
        if any(char.isdigit() for word in search for char in word):
            print("The query cannot contain stand-alone digits. Please try again.")
            continue
        search = remove_punctuation(search, punc_symbols)
        search = remove_stopwords(search, stop_l)
        if check_length(search) >= 1:
            break
        print("The query must contain at least one alphabetic character. Please try again.")
    return search
def get_stop_words():
    with open("StopWords.csv", "r") as stop_file:
        return [line.strip() for line in stop_file]
def process_all(all_files, search_p, punc_l, stop_l):
    for file_name in all_files:
        with open(file_name, "r") as current_file:
            process_file(file_name, current_file, search_p, punc_l, stop_l)
def process_file(name_file, afile, search_phr, pun_list, st_list):
    occurrences = 0
    for line in afile:
        words = line.split()
        words = remove_punctuation(words, pun_list)
        words = remove_stopwords(words, st_list)
        words = all_lowercase(words)
        index = 0
        for word in words:
            if search_phr[index] == word:
                index += 1
                if index == len(search_phr):
                    occurrences += 1
                    index = 0
    print(f"File {name_file} has {occurrences} occurrences of the phrase {search_phr}")
def process_some(all_files, search_p, punc_l, stop_l):
    while True:
        number_files = int(input(f"How many files do you want to search in? (0 to {len(all_files)}) "))
        if 0 <= number_files <= len(all_files):
            break
        print("Invalid input. Please enter a number between 0 and", len(all_files))
    for _ in range(number_files):
        while True:
            file_name = input("Enter the file name with extension: ")
            if file_name.endswith(".txt") and file_name in all_files:
                break
            print("Invalid file name. Please enter a valid .txt file in the directory.")
        with open(file_name, "r") as current_file:
            process_file(file_name, current_file, search_p, punc_l, stop_l)
def remove_punctuation(for_cleaning, punc_list):
    return [word.rstrip("".join(punc_list)) for word in for_cleaning]
def remove_stopwords(to_clean, stop_w):
    return [word for word in to_clean if word not in stop_w]
def main():
    print(__doc__)
    punctuation = [".", ",", ":", ";", "!", "?"]
    stop_words = get_stop_words()
    stop_words = all_lowercase(stop_words)
    while True:
        search_phrase = get_phrase(stop_words, punctuation)
        search_phrase = all_lowercase(search_phrase)
        files = get_files_in_dir()
        choice = input("Do you want to search all .txt files in the current folder? (Yes/No): ")
        if choice.lower() == "yes":
            process_all(files, search_phrase, punctuation, stop_words)
        else:
            process_some(files, search_phrase, punctuation, stop_words)
        choice = input("Do you want to search again? (Yes/No): ")
        if choice.lower() != "yes":
            break
if __name__ == "__main__":
    main()