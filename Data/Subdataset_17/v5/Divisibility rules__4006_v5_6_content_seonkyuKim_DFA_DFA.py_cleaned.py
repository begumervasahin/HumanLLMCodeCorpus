
def dfa(input_string):
    transitions = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q3'},
        'q2': {'0': 'q4', '1': 'q0'},
        'q3': {'0': 'q1', '1': 'q2'},
        'q4': {'0': 'q3', '1': 'q4'}
    }
    initial_state = 'q0'
    final_state = 'q0'
    current_state = initial_state
    for char in input_string:
        if char in transitions[current_state]:
            current_state = transitions[current_state][char]
        else:
            return False
    return current_state == final_state
def is_binary(input_string):
    return set(input_string).issubset({'0', '1'})
def main():
    description = "Input a binary value (0 and 1). To exit the program, type 'exit'.\n"
    while True:
        user_input = input(description)
        if user_input.lower() == 'exit':
            break
        if not is_binary(user_input):
            print('Error: Input value is not binary.\n')
            continue
        if dfa(user_input):
            print('Accept\n')
        else:
            print('Not accept\n')
if __name__ == "__main__":
    main()