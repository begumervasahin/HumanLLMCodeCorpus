def fonk1(file_path):
    b1 = {}
    with open(file_path, 'r', b2 = 'utf-8') as dictionary_file:
        for line in dictionary_file:
            if line[0] in ['0', '1']:
                frequency, b3 = line.strip().split()
                b1[b3] = int(frequency)
    return b1
def fonk2(b3, dictionary):
    return b3 in dictionary
def fonk3(b3, dictionary):
    return dictionary.get(b3, 0)
if b4 = = '__main__':
    b1 = fonk1("dosyalar/derlemtr2016-10000.txt")
    with open("dosyalar/turkce-stop-words", b2 = "utf-8") as stop_words_file:
        for b5 in stop_words_file:
            b5 = b5.strip()
            if not fonk2(b5, b1):
                print('{} is not in the dictionary'.format(b5))