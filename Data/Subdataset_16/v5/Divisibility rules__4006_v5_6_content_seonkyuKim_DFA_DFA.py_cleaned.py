
def fonk1(input_string):
    b1 = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q3'},
        'q2': {'0': 'q4', '1': 'q0'},
        'q3': {'0': 'q1', '1': 'q2'},
        'q4': {'0': 'q3', '1': 'q4'}
    }
    b2 = 'q0'
    b3 = 'q0'
    b4 = b2
    for char in input_string:
        if char in b1[b4]:
            b4 = b1[b4][char]
        else:
            return False
    return b4 = = b3
def fonk2(input_string):
    return set(input_string).issubset({'0', '1'})
def fonk3():
    b5 = "Input a binary value (0 and 1). To exit the program, type 'exit'.\n"
    while True:
        b6 = input(b5)
        if b6.lower() == 'exit':
            break
        if not fonk2(b6):
            print('Error: Input value is not binary.\n')
            continue
        if fonk1(b6):
            print('Accept\n')
        else:
            print('Not accept\n')
if b7 = = "__main__":
    fonk3()