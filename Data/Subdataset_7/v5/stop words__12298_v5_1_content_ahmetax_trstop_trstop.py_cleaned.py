
def fonk1(file_path):
    b1 = {}
    with open(file_path, 'r', b2 = 'utf-8') as file:
        for line in file:
            if line.startswith(('0', '1')):
                frequency, b3 = line.strip().split()
                b1[b3] = int(frequency)
    return b1
def fonk2(b3, dictionary):
    return b3 in dictionary
def fonk3(b3, dictionary):
    if fonk2(b3, dictionary):
        return dictionary[b3]
    else:
        return 0
if b4 = = '__main__':
    b1 = fonk1("dosyalar/derlemtr2016-10000.txt")
    with open("dosyalar/turkce-stop-words", b2 = "utf-8") as stop_words_file:
        for b3 in stop_words_file:
            b3 = b3.strip()
            if b3 not in b1:
                print(f"'{b3}' is not in the dictionary")