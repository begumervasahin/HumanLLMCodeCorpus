from tm import TuringMachine, State, Tape, Transition
import sys
def create_machine(file_path):
    with open(file_path, "r") as f:
        n_states, n_transitions = map(int, f.readline().strip().split())
        machine = TuringMachine()
        for _ in range(n_states):
            line = f.readline().strip().split()
            value = line[0]
            state = State(value)
            machine.add_state(state)
        for _ in range(n_transitions):
            line = f.readline().strip().split()
            source, destination = line[0], line[1]
            read, write = line[2], line[3]
            direction = Transition.Direction.RIGHT if line[4] == 'R' else Transition.Direction.LEFT
            transition = Transition(read, write, machine.get_state(destination), direction)
            machine.add_transition(source, transition)
        initial_state = f.readline().strip()
        machine.set_init_state(initial_state)
    return machine
def read_tape(file_path):
    with open(file_path, "r") as f:
        string = f.readline().strip()
        tape = Tape(string)
    return tape
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <machine_file> <tape_file>")
        sys.exit(1)
    machine_file = sys.argv[1]
    tape_file = sys.argv[2]
    machine = create_machine(machine_file)
    tape = read_tape(tape_file)
    machine.set_tape(tape)
    machine.simulate()
    print(tape.cells)