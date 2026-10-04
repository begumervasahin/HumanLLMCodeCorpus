
word_frequencies = {}
def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line[0] not in ['0', '1']:
                continue
            freq, word = line.strip().split()
            word_frequencies[word] = int(freq)
def is_stop_word(word):
    return word in word_frequencies
def get_word_freq(word):
    return word_frequencies.get(word, 0)
def check_stop_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for word in file:
            word = word.strip()
            if not is_stop_word(word):
                print(f'{word} sÃ¶zlÃ¼kte yok')
if __name__ == '__main__':
    load_dictionary("dosyalar/derlemtr2016-10000.txt")
    check_stop_words("dosyalar/turkce-stop-words")