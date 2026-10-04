
def fonk1(input_string):
    b1 = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q3'},
        'q2': {'0': 'q4', '1': 'q0'},
        'q3': {'0': 'q1', '1': 'q2'},
        'q4': {'0': 'q3', '1': 'q4'}
    }
    b2 = 'q0'
    for char in input_string:
        if char in b1[b2]:
            b2 = b1[b2][char]
        else:
            return False
    return b2 = = 'q0'
def fonk2(input_string):
    return set(input_string).issubset({'0', '1'})
def fonk3():
    b3 = "Input a binary value (0 and 1). To exit the program, type 'exit'.\n"
    while True:
        b4 = input(b3)
        if b4.lower() == 'exit':
            break
        if not fonk2(b4):
            print('Error: Input value is not binary.\n')
            continue
        if fonk1(b4):
            print('Accept\n')
        else:
            print('Not accept\n')
if b5 = = "__main__":
    fonk3()