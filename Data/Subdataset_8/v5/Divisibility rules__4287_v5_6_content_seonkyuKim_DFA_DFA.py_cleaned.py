def deterministic_finite_automaton(input_string):
    states = {'q0', 'q1', 'q2', 'q3', 'q4'}
    transitions = {
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
    current_state = 'q0'
    for char in input_string:
        current_state = transitions.get((current_state, char), 'invalid')
        if current_state == 'invalid':
            return False
    return current_state == 'q0'
def is_binary(input_string):
    valid_characters = {'0', '1'}
    input_set = set(input_string)
    return input_set == valid_characters or input_set in [{'0'}, {'1'}]
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