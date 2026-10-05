
dictionary = {}
with open("dosyalar/derlemtr2016-10000.txt", 'r', encoding='utf-8') as fdict:
    for line in fdict:
        if line[0] not in ['0', '1']:
            continue
        freq, word = line.strip().split()
        dictionary[word] = int(freq)
def is_stop_word(word):
    return word in dictionary
def get_word_freq(word):
    if is_stop_word(word):
        return dictionary[word]
    else:
        return 0
if __name__ == '__main__':
    with open("dosyalar/turkce-stop-words", encoding="utf-8") as ftest:
        for word in ftest:
            word = word.strip()
            if word not in dictionary:
                print('{} is not in the dictionary'.format(word))