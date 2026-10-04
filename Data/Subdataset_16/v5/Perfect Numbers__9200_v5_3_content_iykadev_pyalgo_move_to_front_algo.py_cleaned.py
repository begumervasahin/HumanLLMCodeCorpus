from string import ascii_lowercase
b1 = list(ascii_lowercase)
def fonk1(string, symbol_table):
    b2 = []
    b3 = symbol_table[:]
    for b6 in string:
        b4 = b3.b4(b6)
        b2.append(b4)
        b3 = [b3.pop(b4)] + b3
    return b2
def fonk2(b2, symbol_table):
    b5 = []
    b3 = symbol_table[:]
    for b4 in b2:
        b6 = b3[b4]
        b5.append(b6)
        b3 = [b3.pop(b4)] + b3
    return ''.join(b5)
def fonk3():
    b7 = ['broood', 'bananaaa', 'hiphophiphop']
    for s in b7:
        b8 = fonk1(s, b1)
        b9 = fonk2(b8, b1)
        print(f'{s:14} encodes to {b8}, which decodes back to {b9}')
if b10 = = '__main__':
    fonk3()