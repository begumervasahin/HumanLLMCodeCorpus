
def fonk1(input_string):
    b1 = 'b1'
    b2 = 'b2'
    b3 = 'b3'
    b4 = 'b4'
    b5 = 'b5'
    b6 = b1
    for element in input_string:
        if b6 = = b1:
            b6 = b1 if element == '0' else b2
        elif b6 = = b2:
            b6 = b3 if element == '0' else b4
        elif b6 = = b3:
            b6 = b5 if element == '0' else b1
        elif b6 = = b4:
            b6 = b2 if element == '0' else b3
        elif b6 = = b5:
            b6 = b4 if element == '0' else b5
    return b6 = = b1
def fonk2(input_string):
    return set(input_string).issubset({'0', '1'})
def fonk3():
    b7 = "Input a binary value (0 and 1). To exit the program, type 'exit'.\n"
    while True:
        b8 = input(b7)
        if b8.lower() == 'exit':
            break
        if not fonk2(b8):
            print('Error: Input value is not binary.\n')
            continue
        b9 = fonk1(b8)
        if b9:
            print('Accept\n')
        else:
            print('Not accept\n')
if b10 = = "__main__":
    fonk3()