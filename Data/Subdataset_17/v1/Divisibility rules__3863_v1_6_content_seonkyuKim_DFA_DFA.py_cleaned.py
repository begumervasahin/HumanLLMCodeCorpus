
def DFA(input_string):
    q0 = 'q0'
    q1 = 'q1'
    q2 = 'q2'
    q3 = 'q3'
    q4 = 'q4'
    curr_state = q0
    for element in input_string:
        if curr_state == q0:
            curr_state = q0 if element == '0' else q1
        elif curr_state == q1:
            curr_state = q2 if element == '0' else q3
        elif curr_state == q2:
            curr_state = q4 if element == '0' else q0
        elif curr_state == q3:
            curr_state = q1 if element == '0' else q2
        elif curr_state == q4:
            curr_state = q3 if element == '0' else q4
    return curr_state == q0
def check_binary(input_string):
    return set(input_string).issubset({'0', '1'})
def main():
    description = "Input a binary value (0 and 1). To exit the program, type 'exit'.\n"
    while True:
        user_input = input(description)
        if user_input.lower() == 'exit':
            break
        if not check_binary(user_input):
            print('Error: Input value is not binary.\n')
            continue
        is_accepted = DFA(user_input)
        if is_accepted:
            print('Accept\n')
        else:
            print('Not accept\n')
if __name__ == "__main__":
    main()