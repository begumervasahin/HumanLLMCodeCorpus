
def load_frequency_dictionary(file_path):
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line[0] not in ['0', '1']:
                continue
            freq, word = line.strip().split()
            dictionary[word] = int(freq)
    return dictionary
def is_stop_word(word, dictionary):
    return word in dictionary
def get_word_freq(word, dictionary):
    return dictionary.get(word, 0)
def check_stop_words(stop_words_file, dictionary):
    with open(stop_words_file, 'r', encoding='utf-8') as file:
        for word in file:
            word = word.strip()
            if not is_stop_word(word, dictionary):
                print(f'{word} is not in the dictionary')
if __name__ == '__main__':
    frequency_dict = load_frequency_dictionary("dosyalar/derlemtr2016-10000.txt")
    check_stop_words("dosyalar/turkce-stop-words", frequency_dict)