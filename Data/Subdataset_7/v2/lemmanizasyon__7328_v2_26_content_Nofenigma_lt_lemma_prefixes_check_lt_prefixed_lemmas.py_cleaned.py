import sys
def fonk1(filename):
    b1 = set()
    with open(filename, 'r', b2 = 'utf-8') as file:
        for line in file:
            b3 = line.strip().split('\t')[0]
            b1.add(b3)
    return b1
def fonk2(b11, b12, b1):
    with open(b11, 'r', b2 = 'utf-8') as b11:
        with open(b12, 'w', b2 = 'utf-8') as b12:
            for line in b11:
                b4 = line.strip().split('\t')
                if len(b4) == 10:
                    b5 = b4[2]
                    b6 = b4[3]
                    b7 = b4[5]
                    if b6 = = 'VERB':
                        if b5.startswith('nebe'):
                            if b5.startswith('nebesi'):
                                if 'b8 = Yes' in b7:
                                    if b5[6:] + 's' in b1:
                                        b4[2] = b5[6:] + 's'
                            elif b5[4:] in b1:
                                b4[2] = b5[4:]
                            elif b5[2:] in b1:
                                b4[2] = b5[2:]
                        elif b5.startswith('ne'):
                            if 'b8 = Yes' in b7:
                                b4[2] = b5[4:] + 's'
                            elif b5[2:] in b1:
                                b4[2] = b5[2:]
                        elif b5.startswith('tebe'):
                            if 'b8 = Yes' in b7:
                                b4[2] = b5[6:] + 's'
                            elif b5[2:] in b1:
                                b4[2] = b5[2:]
                            else:
                                b4[2] = b5[4:]
                        elif b5.startswith('be'):
                            if 'b8 = Yes' in b7:
                                b4[2] = b5[4:] + 's'
                            elif b5[2:] in b1:
                                b4[2] = b5[2:]
                    b9 = '\t'.join(b4)
                    b12.write(b9 + '\n')
                else:
                    b12.write(line)
if b10 = = "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py b11 b12 b13")
        sys.exit(1)
    b11 = sys.argv[1]
    b12 = sys.argv[2]
    b13 = sys.argv[3]
    b1 = fonk1(b13)
    fonk2(b11, b12, b1)