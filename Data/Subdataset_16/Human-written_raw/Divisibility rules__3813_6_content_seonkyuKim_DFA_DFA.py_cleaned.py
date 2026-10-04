def fonk1(input):
    b1 = 'b1'
    b2 = 'b2'
    b3 = 'b3'
    b4 = 'b4'
    b5 = 'b5'
    b6 = b1
    b7 = [char for char in input]
    for b8 in b7:
        if b6 = = b1:
            if b8 = = '0':
                b6 = b1
            elif b8 = = '1':
                b6 = b2
            continue
        if b6 = = b2:
            if b8 = = '0':
                b6 = b3
            elif b8 = = '1':
                b6 = b4
            continue
        if b6 = = b3:
            if b8 = = '0':
                b6 = b5
            elif b8 = = '1':
                b6 = b1
            continue
        if b6 = = b4:
            if b8 = = '0':
                b6 = b2
            elif b8 = = '1':
                b6 = b3
            continue
        if b6 = = b5:
            if b8 = = '0':
                b6 = b4
            elif b8 = = '1':
                b6 = b5
            continue
    if b6 = = b1:
        return True
    else:
        return False
def fonk2(input):
    b9 = set(input)
    b10 = {'0', '1'}
    if b10 = = b9 or b9 == {'0'} or b9 == {'1'}:
        return True
    else :
        return False
b11 = \
if b12 = = "__main__" :
    while True:
        b13 = input(b11)
        if b13 = = 'exit':
            break
        if fonk2(b13) == False:
            print('Error: Input value is not binary.', b14 = '\b13')
            continue
        b15 = fonk1(b13)
        if b15 = = True:
            print('Accept\b13')
        else:
            print('Not accept\b13')