import sys
from tm import TuringMachine, State, Transition, Tape
def create_machine(config_file):
    with open(config_file, "r") as file:
        n_states, n_transitions = map(int, file.readline().strip().split())
        machine = TuringMachine()
        for _ in range(n_states):
            state_value = file.readline().strip()
            state = State(state_value)
            machine.addState(state)
        for _ in range(n_transitions):
            source, destination, read, write, direction = file.readline().strip().split()
            direction = Transition.Direction.RIGHT if direction == 'R' else Transition.Direction.LEFT
            transition = Transition(read, write, machine.getState(destination), direction)
            machine.addTransition(source, transition)
        initial_state = file.readline().strip()
        machine.setInitState(initial_state)
    return machine
def read_tape(tape_file):
    with open(tape_file, "r") as file:
        tape_string = file.readline().strip()
    return Tape(tape_string)
def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <config_file> <tape_file>")
        return
    config_file = sys.argv[1]
    tape_file = sys.argv[2]
    try:
        machine = create_machine(config_file)
        tape = read_tape(tape_file)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return
    machine.setTape(tape)
    machine.simulate()
    print(tape.cells)
if __name__ == "__main__":
    main()