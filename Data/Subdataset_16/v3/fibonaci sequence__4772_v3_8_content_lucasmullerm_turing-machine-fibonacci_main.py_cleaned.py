import sys
from tm import TuringMachine, State, Transition, Tape
def fonk1(b9):
    with open(b9, "r") as file:
        n_states, b1 = map(int, file.readline().strip().split())
        b2 = TuringMachine()
        for _ in range(n_states):
            b3 = file.readline().strip()
            b4 = State(b3)
            b2.addState(b4)
        for _ in range(b1):
            source, destination, read, write, b5 = file.readline().strip().split()
            b5 = Transition.Direction.RIGHT if b5 == 'R' else Transition.Direction.LEFT
            b6 = Transition(read, write, b2.getState(destination), b5)
            b2.addTransition(source, b6)
        b7 = file.readline().strip()
        b2.setInitState(b7)
    return b2
def fonk2(b10):
    with open(b10, "r") as file:
        b8 = file.readline().strip()
    return Tape(b8)
def fonk3():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <b9> <b10>")
        return
    b9 = sys.argv[1]
    b10 = sys.argv[2]
    try:
        b2 = fonk1(b9)
        b11 = fonk2(b10)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return
    b2.setTape(b11)
    b2.simulate()
    print(b11.cells)
if b12 = = "__main__":
    fonk3()