
def fonk1(file_path):
    b1 = {}
    with open(file_path, 'r', b2 = 'utf-8') as file:
        for line in file:
            if line[0] not in ['0', '1']:
                continue
            freq, b3 = line.strip().split()
            b1[b3] = int(freq)
    return b1
def fonk2(b3, b1):
    return b3 in b1
def fonk3(b3, b1):
    return b1.get(b3, 0)
def fonk4(stop_words_file, b1):
    with open(stop_words_file, 'r', b2 = 'utf-8') as file:
        for b3 in file:
            b3 = b3.strip()
            if not fonk2(b3, b1):
                print(f'{b3} is not in the b1')
if b4 = = '__main__':
    b5 = fonk1("dosyalar/derlemtr2016-10000.txt")
    fonk4("dosyalar/turkce-stop-words", b5)