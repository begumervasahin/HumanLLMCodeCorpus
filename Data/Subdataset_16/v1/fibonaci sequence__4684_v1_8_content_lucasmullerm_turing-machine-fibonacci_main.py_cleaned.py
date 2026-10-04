import sys
from tm import TuringMachine, State, Transition, Tape
def fonk1(b10):
    with open(b10, "r") as f:
        n_states, b1 = map(int, f.readline().strip().split())
        b2 = TuringMachine()
        for _ in range(n_states):
            b3 = f.readline().strip()
            b4 = State(b3)
            b2.addState(b4)
        for _ in range(b1):
            b5 = f.readline().strip().split()
            source, destination, read, write, b6 = b5
            b6 = Transition.Direction.RIGHT if b6 == 'R' else Transition.Direction.LEFT
            b7 = Transition(read, write, b2.getState(destination), b6)
            b2.addTransition(source, b7)
        b8 = f.readline().strip()
        b2.setInitState(b8)
    return b2
def fonk2(b11):
    with open(b11, "r") as f:
        b9 = f.readline().strip()
    return Tape(b9)
def fonk3():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <b10> <b11>")
        return
    b10 = sys.argv[1]
    b11 = sys.argv[2]
    try:
        b2 = fonk1(b10)
        b12 = fonk2(b11)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    b2.setTape(b12)
    b2.simulate()
    print(b12.cells)
if b13 = = "__main__":
    fonk3()