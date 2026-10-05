import glob
def convert_to_lowercase(words_list):
    return [word.lower() for word in words_list]
def calculate_phrase_length(phrase):
    return sum(len(word) for word in phrase)
def get_text_files_in_directory():
    file_names = glob.glob('./*.txt')
    print(f"There are {len(file_names)} .txt files in this directory.")
    return file_names
def get_search_phrase(stop_words, punctuation_symbols):
    while True:
        search_query = input("Enter the phrase to search: ").split()
        if any(char.isdigit() for word in search_query for char in word):
            print("The query cannot contain stand-alone digits. Please try again.")
            continue
        search_query = remove_punctuation(search_query, punctuation_symbols)
        search_query = remove_stopwords(search_query, stop_words)
        if calculate_phrase_length(search_query) >= 1:
            break
        print("The query must contain at least one alphabetic character. Please try again.")
    return search_query
def get_stopwords():
    with open("StopWords.csv", "r") as stop_words_file:
        return [line.strip() for line in stop_words_file]
def search_all_text_files(all_files, search_phrase, punctuation_symbols, stop_words):
    for file_name in all_files:
        with open(file_name, "r") as current_file:
            search_file_for_phrase(file_name, current_file, search_phrase, punctuation_symbols, stop_words)
def search_file_for_phrase(file_name, file_object, search_phrase, punctuation_symbols, stop_words):
    occurrences = 0
    for line in file_object:
        words = line.split()
        words = remove_punctuation(words, punctuation_symbols)
        words = remove_stopwords(words, stop_words)
        words = convert_to_lowercase(words)
        index = 0
        for word in words:
            if search_phrase[index] == word:
                index += 1
                if index == len(search_phrase):
                    occurrences += 1
                    index = 0
    print(f"File {file_name} has {occurrences} occurrences of the phrase {search_phrase}")
def search_specific_text_files(all_files, search_phrase, punctuation_symbols, stop_words):
    while True:
        number_of_files = int(input(f"How many files do you want to search in? (0 to {len(all_files)}) "))
        if 0 <= number_of_files <= len(all_files):
            break
        print("Invalid input. Please enter a number between 0 and", len(all_files))
    for _ in range(number_of_files):
        while True:
            file_name = input("Enter the file name with extension: ")
            if file_name.endswith(".txt") and file_name in all_files:
                break
            print("Invalid file name. Please enter a valid .txt file in the directory.")
        with open(file_name, "r") as current_file:
            search_file_for_phrase(file_name, current_file, search_phrase, punctuation_symbols, stop_words)
def remove_punctuation(words_list, punctuation_symbols):
    return [word.rstrip("".join(punctuation_symbols)) for word in words_list]
def remove_stopwords(words_list, stop_words):
    return [word for word in words_list if word not in stop_words]
def main():
    print(__doc__)
    punctuation_symbols = [".", ",", ":", ";", "!", "?"]
    stop_words = get_stopwords()
    stop_words = convert_to_lowercase(stop_words)
    while True:
        search_phrase = get_search_phrase(stop_words, punctuation_symbols)
        search_phrase = convert_to_lowercase(search_phrase)
        files = get_text_files_in_directory()
        choice = input("Do you want to search all .txt files in the current folder? (Yes/No): ")
        if choice.lower() == "yes":
            search_all_text_files(files, search_phrase, punctuation_symbols, stop_words)
        else:
            search_specific_text_files(files, search_phrase, punctuation_symbols, stop_words)
        choice = input("Do you want to search again? (Yes/No): ")
        if choice.lower() != "yes":
            break
if __name__ == "__main__":
    main()