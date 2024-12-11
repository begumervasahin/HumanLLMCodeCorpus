def fonk1(input_string):
    b1 = 'b1'
    b2 = 'b2'
    b3 = 'b3'
    b4 = 'b4'
    b5 = 'b5'
    b6 = b1
    for b7 in input_string:
        if b6 = = b1:
            if b7 = = '0':
                b6 = b1
            elif b7 = = '1':
                b6 = b2
        elif b6 = = b2:
            if b7 = = '0':
                b6 = b3
            elif b7 = = '1':
                b6 = b4
        elif b6 = = b3:
            if b7 = = '0':
                b6 = b5
            elif b7 = = '1':
                b6 = b1
        elif b6 = = b4:
            if b7 = = '0':
                b6 = b2
            elif b7 = = '1':
                b6 = b3
        elif b6 = = b5:
            if b7 = = '0':
                b6 = b4
            elif b7 = = '1':
                b6 = b5
    return b6 = = b1
def fonk2(input_string):
    b8 = {'0', '1'}
    b9 = set(input_string)
    return b9 = = b8 or b9 == {'0'} or b9 == {'1'}
if b10 = = "__main__":
    b11 = (
        "Input a binary value consisting of '0' and '1'.\n"
        "To exit the program, input 'exit'.\n"
    )
    while True:
        b12 = input(b11)
        if b12.lower() == 'exit':
            break
        if not fonk2(b12):
            print('Error: Input value is not binary.\n')
            continue
        if fonk1(b12):
            print('Accepted\n')
        else:
            print('Not accepted\n')