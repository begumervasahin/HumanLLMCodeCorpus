
b1 = {}
with open("dosyalar/derlemtr2016-10000.txt", 'r', b2 = 'utf-8') as fdict:
    for line in fdict:
        if line[0] not in ['0', '1']:
            continue
        freq, b3 = line.strip().split()
        b1[b3] = int(freq)
def fonk1(b3):
    return b3 in b1
def fonk2(b3):
    if fonk1(b3):
        return b1[b3]
    else:
        return 0
if b4 = = '__main__':
    with open("dosyalar/turkce-stop-words", b2 = "utf-8") as ftest:
        for b3 in ftest:
            b3 = b3.strip()
            if b3 not in b1:
                print('{} is not in the b1'.format(b3))