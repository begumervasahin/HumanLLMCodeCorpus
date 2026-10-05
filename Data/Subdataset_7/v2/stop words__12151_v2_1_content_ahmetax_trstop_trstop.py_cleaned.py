
b1 = {}
with open("dosyalar/derlemtr2016-10000.txt", 'r', b2 = 'utf-8') as dictionary_file:
    for line in dictionary_file:
        if line[0] not in ['0', '1']:
            continue
        frequency, b3 = line.strip().split()
        b1[b3] = int(frequency)
def fonk1(b3):
    return b3 in b1
def fonk2(b3):
    if fonk1(b3):
        return b1[b3]
    else:
        return 0
if b4 = = '__main__':
    with open("dosyalar/turkce-stop-words", b2 = "utf-8") as stop_words_file:
        for b5 in stop_words_file:
            b5 = b5.strip()
            if b5 not in b1:
                print('{} is not in the dictionary'.format(b5))