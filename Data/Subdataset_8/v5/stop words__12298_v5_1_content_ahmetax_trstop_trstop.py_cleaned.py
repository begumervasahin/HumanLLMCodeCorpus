
def read_word_frequencies(file_path):
    word_frequencies = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith(('0', '1')):
                frequency, word = line.strip().split()
                word_frequencies[word] = int(frequency)
    return word_frequencies
def is_stop_word(word, dictionary):
    return word in dictionary
def get_word_freq(word, dictionary):
    if is_stop_word(word, dictionary):
        return dictionary[word]
    else:
        return 0
if __name__ == '__main__':
    word_frequencies = read_word_frequencies("dosyalar/derlemtr2016-10000.txt")
    with open("dosyalar/turkce-stop-words", encoding="utf-8") as stop_words_file:
        for word in stop_words_file:
            word = word.strip()
            if word not in word_frequencies:
                print(f"'{word}' is not in the dictionary")