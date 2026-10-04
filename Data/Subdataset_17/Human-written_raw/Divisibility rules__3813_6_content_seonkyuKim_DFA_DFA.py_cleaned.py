def DFA(input):
    q0 = 'q0'
    q1 = 'q1'
    q2 = 'q2'
    q3 = 'q3'
    q4 = 'q4'
    curr_state = q0
    iuput_list = [char for char in input]
    for element in iuput_list:
        if curr_state == q0:
            if element == '0':
                curr_state = q0
            elif element == '1':
                curr_state = q1
            continue
        if curr_state == q1:
            if element == '0':
                curr_state = q2
            elif element == '1':
                curr_state = q3
            continue
        if curr_state == q2:
            if element == '0':
                curr_state = q4
            elif element == '1':
                curr_state = q0
            continue
        if curr_state == q3:
            if element == '0':
                curr_state = q1
            elif element == '1':
                curr_state = q2
            continue
        if curr_state == q4:
            if element == '0':
                curr_state = q3
            elif element == '1':
                curr_state = q4
            continue
    if curr_state == q0:
        return True
    else:
        return False
def checkBinary(input):
    p = set(input)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        return True
    else :
        return False
description = \
if __name__ == "__main__" :
    while True:
        n = input(description)
        if n == 'exit':
            break
        if checkBinary(n) == False:
            print('Error: Input value is not binary.', end='\n')
            continue
        is_accept = DFA(n)
        if is_accept == True:
            print('Accept\n')
        else:
            print('Not accept\n')