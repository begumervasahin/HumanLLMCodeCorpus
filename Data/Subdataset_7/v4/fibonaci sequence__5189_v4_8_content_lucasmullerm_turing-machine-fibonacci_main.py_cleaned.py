from tm import TuringMachine, State, Tape, Transition
import sys
def fonk1():
    with open(sys.argv[1], "r") as file:
        n_states, b1 = map(int, file.readline().strip().split())
        b2 = TuringMachine()
        for _ in range(n_states):
            b3 = file.readline().strip().split()
            b4 = b3[0]
            b5 = State(b4)
            b2.add_state(b5)
        for _ in range(b1):
            b3 = file.readline().strip().split()
            source, b6 = b3[0], b3[1]
            read_symbol, b7 = b3[2], b3[3]
            b8 = Transition.Direction.RIGHT if b3[4] == 'R' else Transition.Direction.LEFT
            b9 = Transition(read_symbol, b7, b2.get_state(b6), b8)
            b2.add_transition(source, b9)
        b10 = file.readline().strip()
        b2.set_init_state(b10)
    return b2
def fonk2():
    with open(sys.argv[2], "r") as file:
        b11 = file.readline().strip()
        b12 = Tape(b11)
    return b12
if b13 = = "__main__":
    b2 = fonk1()
    b12 = fonk2()
    b2.set_tape(b12)
    b2.simulate()
    print(b12.cells)