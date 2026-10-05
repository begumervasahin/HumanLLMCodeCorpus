def load_turkish_dictionary(file_path):
    turkish_dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as dictionary_file:
        for line in dictionary_file:
            if line[0] in ['0', '1']:
                frequency, word = line.strip().split()
                turkish_dictionary[word] = int(frequency)
    return turkish_dictionary
def is_stop_word(word, dictionary):
    return word in dictionary
def get_word_frequency(word, dictionary):
    return dictionary.get(word, 0)
if __name__ == '__main__':
    turkish_dictionary = load_turkish_dictionary("dosyalar/derlemtr2016-10000.txt")
    with open("dosyalar/turkce-stop-words", encoding="utf-8") as stop_words_file:
        for stop_word in stop_words_file:
            stop_word = stop_word.strip()
            if not is_stop_word(stop_word, turkish_dictionary):
                print('{} is not in the dictionary'.format(stop_word))