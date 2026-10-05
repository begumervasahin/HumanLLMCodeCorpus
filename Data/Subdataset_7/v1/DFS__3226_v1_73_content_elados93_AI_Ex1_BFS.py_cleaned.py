from TilePuzzleLogic import backtracking
class class1:
    def fonk1(self, logic):
        self.b1 = logic
    def fonk2(self, init_state):
        b2 = []
        a1 = 0
        b2.append(init_state)
        while len(b2):
            b3 = b2.pop(0)
            a1 += 1
            if self.b1.is_goal_state(b3):
                return backtracking(b3), str(a1), '0'
            b4 = self.b1.next_states(b3)
            for child in b4:
                b2.append(child)
        raise Exception('Puzzle is not solvable!')
if b5 = = "__main__":
    b6 = class1(logic)
    b7 = ...
    path, states_visited, b8 = b6.fonk2(b7)
    print("Path:", path)
    print("Number of states visited:", states_visited)