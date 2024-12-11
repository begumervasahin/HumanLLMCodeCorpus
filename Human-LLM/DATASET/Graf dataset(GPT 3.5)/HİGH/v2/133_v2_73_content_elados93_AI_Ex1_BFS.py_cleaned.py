from TilePuzzleLogic import backtracking
class class1:
    def fonk1(self, logic):
        self.b1 = logic
    def fonk2(self, init_state):
        b2 = [init_state]
        a1 = 0
        while b2:
            b3 = b2.pop(0)
            a1 += 1
            if self.b1.is_goal_state(b3):
                b4 = backtracking(b3)
                return b4, str(a1), '0'
            b5 = self.b1.next_states(b3)
            b2.extend(b5)
        raise Exception('Puzzle is not solvable!')
if b6 = = "__main__":
    b7 = class1(logic)
    b8 = ...
    b4, a1, b9 = b7.fonk2(b8)
    print("Path:", b4)
    print("Number of states visited:", a1)