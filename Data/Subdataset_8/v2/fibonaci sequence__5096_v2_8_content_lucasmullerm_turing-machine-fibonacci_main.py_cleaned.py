from tm import TuringMachine, State, Tape, Transition
import sys
def create_machine_from_file(file_path):
    with open(file_path, "r") as file:
        n_states, n_transitions = map(int, file.readline().strip().split())
        machine = TuringMachine()
        for _ in range(n_states):
            line = file.readline().strip().split()
            state_value = line[0]
            state = State(state_value)
            machine.add_state(state)
        for _ in range(n_transitions):
            line = file.readline().strip().split()
            source, destination = line[0], line[1]
            read_symbol, write_symbol = line[2], line[3]
            direction = Transition.Direction.RIGHT if line[4] == 'R' else Transition.Direction.LEFT
            transition = Transition(read_symbol, write_symbol, machine.get_state(destination), direction)
            machine.add_transition(source, transition)
        initial_state = file.readline().strip()
        machine.set_init_state(initial_state)
    return machine
def read_tape_from_file(file_path):
    with open(file_path, "r") as file:
        tape_contents = file.readline().strip()
        tape = Tape(tape_contents)
    return tape
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <machine_file> <tape_file>")
        sys.exit(1)
    machine_file = sys.argv[1]
    tape_file = sys.argv[2]
    machine = create_machine_from_file(machine_file)
    tape = read_tape_from_file(tape_file)
    machine.set_tape(tape)
    machine.simulate()
    print("Final tape contents:", tape.cells)