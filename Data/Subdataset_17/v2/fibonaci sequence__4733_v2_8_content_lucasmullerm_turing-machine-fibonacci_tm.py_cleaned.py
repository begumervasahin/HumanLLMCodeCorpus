import enum
class State:
    def __init__(self, value):
        self.value = value
        self.transitions = {}
    def add_transition(self, transition):
        self.transitions[transition.read] = transition
    def step(self, symbol):
        try:
            transition = self.transitions[symbol]
            return transition.next_state, transition.write, transition.direction
        except KeyError:
            return self, None, None
class Transition:
    class Direction(enum.Enum):
        RIGHT = 1
        LEFT = 2
    def __init__(self, read, write, next_state, direction):
        self.read = read
        self.write = write
        self.next_state = next_state
        self.direction = direction
class Tape:
    def __init__(self, cells):
        self.cells = cells
        self.position = 0
    def reach_end(self):
        return self.position < 0 or self.position >= len(self.cells)
    def head(self):
        if self.reach_end():
            return -1
        return self.cells[self.position]
    def reset(self):
        self.position = 0
    def head_position(self):
        return self.position
    def write_on_position(self, symbol):
        pos = self.position
        self.cells = self.cells[:pos] + symbol + self.cells[pos + 1:]
    def update(self, to_write, direction):
        if self.reach_end():
            raise Exception('End of computation.')
        self.write_on_position(to_write)
        if direction == Transition.Direction.RIGHT:
            self.position += 1
        elif direction == Transition.Direction.LEFT:
            self.position -= 1
class TuringMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.tape = None
        self.visited = set()
        self.simulating = True
        self.initial_state = None
    def add_state(self, state):
        self.states[state.value] = state
    def add_transition(self, source_state, transition):
        self.states[source_state].add_transition(transition)
    def set_initial_state(self, state):
        self.current_state = self.states[state]
        self.initial_state = self.states[state]
    def set_tape(self, tape):
        self.tape = tape
    def start_over(self):
        self.current_state = self.initial_state
        self.tape.reset()
        self.simulating = True
        self.visited = {(self.current_state.value, self.tape.head_position())}
        log = "State: (%3s) " % (self.current_state.value)
        log += self.tape.cells + "\n" + " " * 12 + " " * self.tape.head_position() + "^\n"
        return log
    def get_state(self, state_value):
        return self.states[state_value]
    def simulate_step(self):
        if not self.simulating:
            return "Computation has stopped.\n"
        self.current_state, to_write, direction = self.current_state.step(self.tape.head())
        if to_write:
            self.tape.update(to_write, direction)
        if to_write is None or self.tape.reach_end():
            self.simulating = False
            return "\nEnd of computation\n"
        else:
            log = "State: (%3s) " % (self.current_state.value)
            log += self.tape.cells + "\n" + " " * 12 + " " * self.tape.head_position() + "^\n"
            return log
    def simulate(self):
        with open("log.txt", "a") as f:
            f.write("Beginning computation\n\n")
            f.write(self.start_over())
            while self.simulating:
                log_entry = self.simulate_step()
                f.write(log_entry)
            f.write("--------------------------------------\n")
if __name__ == "__main__":
    pass