def deterministic_finite_automaton(input_string):
    q0 = 'q0'
    q1 = 'q1'
    q2 = 'q2'
    q3 = 'q3'
    q4 = 'q4'
    current_state = q0
    for char in input_string:
        if current_state == q0:
            if char == '0':
                current_state = q0
            elif char == '1':
                current_state = q1
        elif current_state == q1:
            if char == '0':
                current_state = q2
            elif char == '1':
                current_state = q3
        elif current_state == q2:
            if char == '0':
                current_state = q4
            elif char == '1':
                current_state = q0
        elif current_state == q3:
            if char == '0':
                current_state = q1
            elif char == '1':
                current_state = q2
        elif current_state == q4:
            if char == '0':
                current_state = q3
            elif char == '1':
                current_state = q4
    return current_state == q0
def is_binary(input_string):
    valid_characters = {'0', '1'}
    input_set = set(input_string)
    return input_set == valid_characters or input_set == {'0'} or input_set == {'1'}
if __name__ == "__main__":
    description = (
        "Input a binary value consisting of '0' and '1'.\n"
        "To exit the program, input 'exit'.\n"
    )
    while True:
        user_input = input(description)
        if user_input.lower() == 'exit':
            break
        if not is_binary(user_input):
            print('Error: Input value is not binary.\n')
            continue
        if deterministic_finite_automaton(user_input):
            print('Accepted\n')
        else:
            print('Not accepted\n')