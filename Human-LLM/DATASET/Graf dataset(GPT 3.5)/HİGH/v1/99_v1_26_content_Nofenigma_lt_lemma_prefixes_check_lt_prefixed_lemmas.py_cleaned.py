import sys
def fonk1(filename):
    b1 = set()
    with open(filename, 'r', b2 = 'utf-8') as f:
        for line in f:
            b3 = line.strip().split('\t')[0]
            b1.add(b3)
    return b1
def fonk2(b9, b10, b1):
    with open(b9, 'r', b2 = 'utf-8') as f:
        with open(b10, 'w', b2 = 'utf-8') as doc:
            for line in f:
                b4 = line.strip().split('\t')
                if len(b4) == 10:
                    b5 = b4[2]
                    if b4[3] == 'VERB':
                        if b5.startswith('nebe'):
                            if b5.startswith('nebesi'):
                                if 'b6 = Yes' in b4[5]:
                                    if b5[6:] + 's' in b1:
                                        b4[2] = b5[6:] + 's'
                            elif b5[4:] in b1:
                                b4[2] = b5[4:]
                            elif b5[2:] in b1:
                                b4[2] = b5[2:]
                        elif b5.startswith('ne'):
                            if 'b6 = Yes' in b4[5]:
                                b4[2] = b5[4:] + 's'
                            elif b5[2:] in b1:
                                b4[2] = b5[2:]
                        elif b5.startswith('tebe'):
                            if 'b6 = Yes' in b4[5]:
                                b4[2] = b5[6:] + 's'
                            elif b5[2:] in b1:
                                b4[2] = b5[2:]
                            else:
                                b4[2] = b5[4:]
                        elif b5.startswith('be'):
                            if 'b6 = Yes' in b4[5]:
                                b4[2] = b5[4:] + 's'
                            elif b5[2:] in b1:
                                b4[2] = b5[2:]
                    b7 = '\t'.join(b4)
                    doc.write(b7 + '\n')
                else:
                    doc.write(line)
if b8 = = "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py b9 b10 b11")
        sys.exit(1)
    b9 = sys.argv[1]
    b10 = sys.argv[2]
    b11 = sys.argv[3]
    b1 = fonk1(b11)
    fonk2(b9, b10, b1)