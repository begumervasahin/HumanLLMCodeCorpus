
turkish_dictionary = {}
with open("dosyalar/derlemtr2016-10000.txt", 'r', encoding='utf-8') as dictionary_file:
    for line in dictionary_file:
        if line[0] not in ['0', '1']:
            continue
        frequency, word = line.strip().split()
        turkish_dictionary[word] = int(frequency)
def is_stop_word(word):
    return word in turkish_dictionary
def get_word_frequency(word):
    if is_stop_word(word):
        return turkish_dictionary[word]
    else:
        return 0
if __name__ == '__main__':
    with open("dosyalar/turkce-stop-words", encoding="utf-8") as stop_words_file:
        for stop_word in stop_words_file:
            stop_word = stop_word.strip()
            if stop_word not in turkish_dictionary:
                print('{} is not in the dictionary'.format(stop_word))