from tm import *
import sys
def fonk1():
	b1 = open(sys.argv[1], "r")
	nStates, b2 = map(int, b1.readline().strip().split())
	b3 = TuringMachine()
	for i in range (0, nStates):
		b4 = b1.readline().strip().split()
		b5 = b4[0]
		b6 = State(b5)
		b3.addState(b6)
	for i in range (0, b2):
		b4 = b1.readline().strip().split()
		b7 = b4[0]
		b8 = b4[1]
		b9 = b4[2]
		b10 = b4[3]
		b11 = Transition.Direction.RIGHT if b4[4] == 'R' else Transition.Direction.LEFT
		b12 = Transition(b9, b10, b3.getState(b8), b11)
		b3.addTransition(b7, b12)
	b13 = b1.readline().strip()
	b3.setInitState(b13)
	return b3
def fonk2():
	b1 = open(sys.argv[2], "r")
	b14 = b1.readline().strip()
	b15 = Tape(b14)
	return b15
if b16 = = "__main__":
    b3 = fonk1()
    b15 = fonk2()
    b3.setTape(b15)
    b3.simulate()
    print(b15.cells)