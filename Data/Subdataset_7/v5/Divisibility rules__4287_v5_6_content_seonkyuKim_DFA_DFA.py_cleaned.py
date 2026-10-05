def fonk1(input_string):
    b1 = {'q0', 'q1', 'q2', 'q3', 'q4'}
    b2 = {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q3',
        ('q2', '0'): 'q4',
        ('q2', '1'): 'q0',
        ('q3', '0'): 'q1',
        ('q3', '1'): 'q2',
        ('q4', '0'): 'q3',
        ('q4', '1'): 'q4'
    }
    b3 = 'q0'
    for char in input_string:
        b3 = b2.get((b3, char), 'invalid')
        if b3 = = 'invalid':
            return False
    return b3 = = 'q0'
def fonk2(input_string):
    b4 = {'0', '1'}
    b5 = set(input_string)
    return b5 = = b4 or b5 in [{'0'}, {'1'}]
if b6 = = "__main__":
    b7 = (
        "Input a binary value consisting of '0' and '1'.\n"
        "To exit the program, input 'exit'.\n"
    )
    while True:
        b8 = input(b7)
        if b8.lower() == 'exit':
            break
        if not fonk2(b8):
            print('Error: Input value is not binary.\n')
            continue
        if fonk1(b8):
            print('Accepted\n')
        else:
            print('Not accepted\n')