def DFA(input_string):
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
    initial_state = 'q0'
    final_state = 'q0'
    current_state = initial_state
    for char in input_string:
        current_state = transitions.get((current_state, char), 'invalid')
        if current_state == 'invalid':
            return False
    return current_state == final_state
def check_binary(input_string):
    return set(input_string).issubset({'0', '1'})
if __name__ == "__main__":
    description = "Input a binary string. Enter 'exit' to quit.\n"
    while True:
        input_string = input(description)
        if input_string.lower() == 'exit':
            break
        if not check_binary(input_string):
            print('Error: Input value is not binary.\n')
            continue
        is_accepted = DFA(input_string)
        if is_accepted:
            print('Accepted\n')
        else:
            print('Not Accepted\n')