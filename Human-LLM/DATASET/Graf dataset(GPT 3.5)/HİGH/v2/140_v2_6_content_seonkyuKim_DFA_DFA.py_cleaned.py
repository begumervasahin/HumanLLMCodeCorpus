def fonk1(b8):
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
    b4 = 'q0'
    b5 = b3
    for char in b8:
        b5 = b2.get((b5, char), 'invalid')
        if b5 = = 'invalid':
            return False
    return b5 = = b4
def fonk2(b8):
    return set(b8).issubset({'0', '1'})
if b6 = = "__main__":
    b7 = "Input a binary string. Enter 'exit' to quit.\n"
    while True:
        b8 = input(b7)
        if b8.lower() == 'exit':
            break
        if not fonk2(b8):
            print('Error: Input value is not binary.\n')
            continue
        b9 = fonk1(b8)
        if b9:
            print('Accepted\n')
        else:
            print('Not Accepted\n')